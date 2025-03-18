"""
Extracts the initial facet groups from the model json file.
"""

import json
import sys

import click
import yaml

ignored_keys = ["value", "unit", "id"]


def extract_facets(obj: dict, path: list[str]):
    if obj["type"] == "vocabulary":
        yield "vocabulary", path
    elif obj["type"] == "relation":
        yield "vocabulary", path
    elif "properties" in obj:
        for key, value in obj["properties"].items():
            if key in ignored_keys:
                continue
            yield from extract_facets(value, path + [key])
    elif "items" in obj:
        yield from extract_facets(obj["items"], path)
    else:
        yield obj["type"], path


def to_pythonic_name(name: str):
    return name.replace(" ", "_").replace("-", "_").replace("/", "_").lower()


@click.command()
@click.argument("model_json_file", type=click.Path(exists=True))
@click.argument("output_yaml_file", type=click.Path())
def main(model_json_file, output_yaml_file):
    """Extracts the initial facet groups from the model json file.

    Usage: python ./common/onetime_scripts/extract_facet_groups.py bli/models/records.json models/bli-facet-groups.yaml
    """
    with open(model_json_file) as f:
        model = json.load(f)
    metadata = model["model"]["properties"]["metadata"]
    out = {}
    for idx, (facet_type, facet) in enumerate(extract_facets(metadata, ["metadata"])):
        path = ".".join(part for part in facet)
        out[path] = idx + 1
    with open(output_yaml_file, "w") as f:
        yaml.safe_dump({"facets": {"facet-groups": {"default": out}}}, f)
    yaml.safe_dump({"facets": {"facet-groups": {"default": out}}}, sys.stdout)


if __name__ == "__main__":
    main()
