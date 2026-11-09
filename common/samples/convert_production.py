"""Convert a record exported from production MBDB to the RDM 14 model.

    python3 common/samples/convert_production.py <production export.json> [output.json]

Without an output path, writes <record id>-converted.json next to the export.

Then import the output with upload_data.py (see NOTES.md). This is a first version of the
"production parser": it does the repairs listed in NOTES.md. Check its warnings and the
import result for every new record, other records may need more repairs.

Needs internet access: funder ROR ids are looked up in the ROR registry (api.ror.org).
"""

import json
import re
import subprocess
from pathlib import Path
import sys
import urllib.parse

# what a client sends when creating a record; everything else is export-only
# (pids incl. the production DOI, parent/ownership, access, stats, versions, state, ...)
KEPT_TOP_LEVEL_KEYS = ("$schema", "custom_fields", "metadata")

# "inchikey: OQNW..." -> "inchikey:OQNW..."
SPACED_ID = re.compile(r"^(\w+):\s+")

# funder names (as written in production records) that the ROR name search does not find;
# add new ones here when the conversion stops with "No exact ROR match"
# (name -> (ROR id, official ROR name))
KNOWN_FUNDERS = {
    # an EU fund, not an organisation: ROR maps its Crossref funder id 501100008530 to the
    # European Commission, which administers it
    "European Regional Development Fund": ("00k4n6c32", "European Commission"),
    "Ministry of Education, Youth and Sports of Czech Republic (MEYS)": (
        "037n8p820",
        "Ministry of Education Youth and Sports",
    ),
}

_ror_cache = dict(KNOWN_FUNDERS)


def lookup_funder_ror(name):
    """(ROR id, official ROR name) of a funder: KNOWN_FUNDERS, else exact name match of the top ROR hits."""
    if name not in _ror_cache:
        url = "https://api.ror.org/v2/organizations?query=" + urllib.parse.quote(name)
        # curl instead of urllib: python.org Python on macOS has no root certificates by default
        items = json.loads(subprocess.check_output(["curl", "-sf", "--max-time", "30", url]))["items"]
        normalized = name.replace(",", "").lower()
        for item in items[:5]:
            names = [n["value"].replace(",", "").lower() for n in item["names"]]
            if normalized in names:
                display_name = next(n["value"] for n in item["names"] if "ror_display" in n["types"])
                _ror_cache[name] = (item["id"].rsplit("/", 1)[1], display_name)
                break
        else:
            raise RuntimeError(
                f"No exact ROR match for funder {name!r}: find it on https://ror.org "
                "and add it to KNOWN_FUNDERS in convert_production.py"
            )
    return _ror_cache[name]


def clean(data):
    """Drop old relation snapshots ("@v") and normalize spaced vocabulary ids, recursively."""
    if isinstance(data, dict):
        result = {}
        for key, value in data.items():
            if key == "@v":
                continue
            if key == "id" and isinstance(value, str):
                value = SPACED_ID.sub(r"\1:", value)
            result[key] = clean(value)
        return result
    if isinstance(data, list):
        return [clean(value) for value in data]
    return data


def convert_affiliations(data, warnings):
    """Old {"id": "ror:<id>", "title": {...}, city, country} -> Invenio {"id": "<id>", "name"}."""
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "affiliations" and isinstance(value, list):
                converted = []
                for affiliation in value:
                    affiliation_id = affiliation.get("id", "")
                    if not affiliation_id.startswith("ror:"):
                        warnings.append(f"affiliation without ROR id kept as-is: {affiliation}")
                        converted.append(affiliation)
                        continue
                    name = affiliation.get("name") or affiliation.get("title", {}).get("en")
                    converted.append({"id": affiliation_id.removeprefix("ror:"), "name": name})
                data[key] = converted
            else:
                convert_affiliations(value, warnings)
    elif isinstance(data, list):
        for value in data:
            convert_affiliations(value, warnings)


def convert_funding(funding_references):
    """Old OpenAIRE {"id": "oa:...", funder_name, grant_id, title} -> Invenio funder/award."""
    converted = []
    for reference in funding_references:
        funder_id, funder_name = lookup_funder_ror(reference["funder_name"])
        converted.append(
            {
                "funder": {"id": funder_id, "name": funder_name},
                "award": {
                    "id": f"{funder_id}::{reference['grant_id']}",
                    "number": reference["grant_id"],
                    "title": reference["title"],
                },
            }
        )
    return converted


def convert(record):
    warnings = []
    record = clean({key: record[key] for key in KEPT_TOP_LEVEL_KEYS if key in record})
    record["files"] = {"enabled": True}

    general_parameters = record["metadata"]["general_parameters"]
    convert_affiliations(record["metadata"], warnings)
    general_parameters["funding_references"] = convert_funding(general_parameters.get("funding_references", []))

    instrument = general_parameters.get("instrument")
    if instrument and "manufacturer" in instrument:
        instrument.setdefault("props", {})["manufacturer"] = instrument.pop("manufacturer")

    for award in (f["award"] for f in general_parameters["funding_references"]):
        if "/" in award["number"]:
            warnings.append(f"award id contains '/', may be a problem in URLs: {award['id']}")
    return record, warnings


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    source = Path(sys.argv[1])
    with open(source) as f:
        production_record = json.load(f)
    target = Path(sys.argv[2]) if len(sys.argv) == 3 else source.with_name(f"{production_record['id']}-converted.json")
    if target.resolve() == source.resolve():
        sys.exit(f"Output {target} would overwrite the input, give another output path.")
    converted, warnings = convert(production_record)
    with open(target, "w") as f:
        json.dump(converted, f, ensure_ascii=False, indent=2)
    for warning in warnings:
        print("WARNING:", warning)
    print("written", target)
