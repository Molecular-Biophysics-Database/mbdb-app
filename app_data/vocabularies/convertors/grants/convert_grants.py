import json
import subprocess
import urllib.parse

import yaml

with open("grants.yaml") as f:
    grants = yaml.safe_load(f)


def lookup_ror(name):
    print(name)
    url = "https://api.ror.org/organizations?query=" + urllib.parse.quote(name)
    items = json.loads(subprocess.check_output(["curl", "-s", url]))["items"]
    if not items:
        raise RuntimeError(f"No ROR match for funder: {name}")
    it = items[0]
    print(it)
    ror_id = it["id"].removeprefix("https://ror.org/")
    country = it["locations"][0]["geonames_details"]["country_code"]
    label = it["names"][0]["value"]
    print(label)
    return ror_id, label, country


funders = {}
for g in grants:
    funder_name = g["props"]["funder_name"]
    if funder_name not in funders:
        funders[funder_name] = lookup_ror(funder_name)

funders_output = []
awards_output = []
for g in grants:
    funder_name = g["props"]["funder_name"]
    funder_id, label, country = funders[funder_name]
    number = str(g["props"]["grant_id"])
    funders_output.append(
        {
            "id": funder_id,
            "country": country,
            "identifiers": [{"identifier": funder_id, "scheme": "ror"}],
            "name": label,
            "title": {"en": funder_name},
        }
    )
    awards_output.append(
        {
            "id": f"{funder_id}::{number}",
            "funder": {"id": funder_id, "name": label},
            "number": number,
            "title": {"en": g["title"]["en"]},
        }
    )

# deduplicate funders
seen = set()
funders_output = [
    f for f in funders_output if f["id"] not in seen and not seen.add(f["id"])
]

with open("funders.yaml", "w") as f:
    yaml.dump(funders_output, f, sort_keys=True, allow_unicode=True)
with open("awards.yaml", "w") as f:
    yaml.dump(awards_output, f, sort_keys=True, allow_unicode=True)

print(f"{len(awards_output)} awards, {len(funders_output)} funders")
