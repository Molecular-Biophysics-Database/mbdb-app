import yaml

with open("affiliations-input.yaml") as f:
    items = yaml.safe_load(f)

output = []
for item in items:
    ror_id = item["id"].removeprefix("ror:")
    name = item["title"]["en"]
    output.append(
        {
            "id": ror_id,
            "name": name,
            "title": {"en": name},
            "country_name": item["props"]["country"],
            "location_name": item["props"]["city"],
            "identifiers": [{"identifier": ror_id, "scheme": "ror"}],
            "status": "active",

        }
    )

with open("affiliations-output.yaml", "w") as f:
    yaml.dump(output, f, sort_keys=True, allow_unicode=True)
