import yaml

with open("chemicals-input.yaml") as f:
    items = yaml.safe_load(f)

output = []
for item in items:
    output.append(
        {
            "id": item["id"],
            "title": {"en": item["title"]["en"]},
            "custom_fields": {
                "chemical_formula": item["chemical_formula"],
                "molecular_weight": item["molecular_weight"],
                "additional_identifiers": item["additional_identifiers"],
            },
        }
    )

with open("../chemicals-output.yaml", "w") as f:
    yaml.dump(output, f, sort_keys=False, allow_unicode=True)
