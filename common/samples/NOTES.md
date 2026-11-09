# Sample records

| File | What it is |
|---|---|
| `<id>-production.json` | **Production copy**: record exported as-is from the production MBDB API (old format, does not import). |
| `<id>-converted.json` | The production copy repaired for the RDM 14 model by `convert_production.py` (see below). Imports with 0 validation errors. |
| `6g5wd-zxy65-production.json`, `-converted.json` | MST record `6g5wd-zxy65`, complete (depositors, funding). |
| `gf2bm-df854-production.json`, `-converted.json` | MST record `gf2bm-df854`, complete (depositors, funding incl. ERDF). |
| `6g5wd-zxy65.json` | Older simplified variant of the same record: depositors and funding emptied, so the draft does not validate (missing `depositor`, `principal_contact`). |
| `orig_6g5wd-zxy65.json` | Unmodified older export of the same record (old MBDB format, does not import as-is). |
| `convert_production.py` | Production parser (first version): production copy -> importable record. |
| `upload_data.py` | Import script, see below. |

## Converting another production record

1. Download the record JSON from production MBDB (the record's API URL, e.g. `.../api/mst/<id>`).
2. Convert it (needs internet: funder ROR ids are looked up on api.ror.org):
   ```
   python3 common/samples/convert_production.py common/samples/<id>-production.json
   ```
   It writes `common/samples/<id>-converted.json` (or give an output path as a 2nd argument).
   Read the `WARNING:` lines. If a funder name has no exact ROR match, the script stops and says so:
   find the funder on https://ror.org and add the name to `KNOWN_FUNDERS` in `convert_production.py`.
3. Try the import (below). If it fails, the error says what else needs repairing; add that
   repair to `convert_production.py` and to the list below.

`convert_production.py` currently handles MST records (`metadata.general_parameters`); other models
may need more.

## Importing

```
.venv/bin/invenio shell common/samples/upload_data.py common/samples/<id>-converted.json user@demo.org
```

- The draft is created by the system user and then handed over to the given owner, so they can edit it in the UI
  (users can only create records through a community/workflow).
- Invenio never creates vocabulary items on its own. The script creates referenced items that are missing,
  from the data embedded in the record: affiliations, funders, awards, chemicals and organisms.
- Each run creates a new draft; vocabulary items are only created once.

## Production records need production parsers

The `-converted.json` files were repaired with `convert_production.py`, a first version of such a parser. Records exported from
production MBDB use the old data format and **do not import into the new version as-is**. Before migrating
production data we need to **write production parsers that repair the records automatically** for the new
version. The repairs done on these records are the list of what such a parser has to do (at least):

1. **Drop export-only fields.** Keep only `$schema`, `metadata`, `files`, `custom_fields`. Drop `id`,
   `pids` (the production DOI cannot be registered here: "No configuration defined for PIDs {'doi'}"),
   `parent` (ownership, `owned_by: {user: 76}`, workflow), `access`, `stats`, `versions`, `links`, `state`,
   `status`, `is_draft`, `is_published`, `revision_id`, `created`, `updated`, `expanded`, `media_files`, ...
   DOIs and ownership must be migrated separately.
2. **Normalize vocabulary ids.** E.g. `"inchikey: OQNWUUGFAWNUME-UHFFFAOYSA-N"` (stray space) ->
   `"inchikey:OQNWUUGFAWNUME-UHFFFAOYSA-N"`.
3. **Affiliations: old MBDB format -> Invenio affiliations.**
   `{"@v": ..., "id": "ror:00wzqmx94", "city", "country", "title": {"en": ...}}` ->
   `{"id": "00wzqmx94", "name": "Czech Academy of Sciences, Institute of Biotechnology"}` (plain ROR id).
4. **Funding: old OpenAIRE references -> Invenio funder/award.**
   `{"@v": ..., "id": "oa:ga0_________::312c...", "funder_name", "grant_id", "title"}` ->
   `{"funder": {"id": "<ROR>", "name"}, "award": {"id": "<ROR>::<grant id>", "number", "title"}}`.
   The old records have only funder **names**; their ROR ids must be looked up (ROR API, as in
   `app_data/vocabularies/convertors/grants/convert_grants.py`), and the funder gets its official ROR name.
   Names the ROR search does not find are mapped in `KNOWN_FUNDERS`. Found so far:
   Czech Science Foundation = `01pv73b02`; Ministry of Education, Youth and Sports (also written
   "... of Czech Republic (MEYS)") = `037n8p820`; European Regional Development Fund = `00k4n6c32`
   (European Commission: ERDF is an EU fund, not an organisation; ROR maps its Crossref funder id there).
5. **Instrument:** top-level `manufacturer` -> `props.manufacturer`.
6. **Drop old relation snapshots** (`"@v": "<uuid>::<revision>"`) everywhere in the record.
7. **Missing vocabulary items** (affiliations, funders, awards, chemicals, organisms) must exist before the
   record is created: either created from the embedded data (as `upload_data.py` does) or added to
   `app_data/vocabularies`.

Open points for the parsers:

- **Production funding data is inconsistent between records** and the parser does not fix it yet:
  - the same grant written differently: Czech Science Foundation `GA25-16037S` (6g5wd) vs `25-16037S` (gf2bm)
    -> two different awards for one grant;
  - the same project under different funders and numbers: "Innovation of Czech Infrastructure for Integrative
    Structural Biology" is MEYS `EH23_015/0008175` (6g5wd) but ERDF `CZ.02.01.01/00/23_015/0008175` (gf2bm).
  Decide the canonical form (e.g. GAČR numbers without "GA") and normalize in the parser before a bulk migration.
- Award ids contain the grant number as-is, e.g. `00k4n6c32::CZ.02.01.01/00/23_015/0008175`: the `/` may be a
  problem in URLs like `/api/awards/<id>`.
- Depositor identifiers stay as `orcid:...` strings (model field is a plain keyword array).
- Only two MST records have been checked; other models (SPR, ITC, BLI, MP) and other records may need more repairs.
