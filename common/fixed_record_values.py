from datetime import date
from copy import deepcopy
from pathlib import Path
import yaml


def schema_version(model: str) -> str:
    model_path = Path(__file__).parent.parent / "models"
    models = ("General_parameters", "BLI", "ITC", "MST", "SPR")

    if model not in models:
        raise ValueError(f"model: '{model}' is not among the known models: {models}")

    with open(model_path / f"{model.lower()}-definitions.yaml", "r") as f:
        yml = yaml.safe_load(f)

    # Name of the object that has the schema version
    if model != "General_parameters":
        model = f"{model}_specific_parameters"

    return yml[model]["properties"]["schema_version"]["enum"][0]


def make_fixed_values(technique: str, resource_type: str) -> dict:
    record = deepcopy(FIXED_RECORD_VALUES)
    metadata = record["metadata"]
    gp = metadata["general_parameters"]
    gp["technique"] = technique
    gp["record_information"]["resource_type"] = resource_type
    metadata["method_specific_parameters"] = {
        "schema_version": schema_version(resource_type)
    }
    return record


FIXED_RECORD_VALUES = {
    "metadata": {
        "general_parameters": {
            "schema_version": schema_version("General_parameters"),
            "record_information": {
                "access_rights": "open",
                "publisher": "MBDB",
                "resource_type_general": "Dataset",
                "deposition_date": date.today().isoformat(),
                "subject_category": "Biophysics",
                "copyright": "Anyone is free to distribute the data and metadata",
                "license": {
                    "name": "CC0 1.0 Universal",
                    "url": "https://creativecommons.org/publicdomain/zero/1.0/",
                },
            },
        },
    }
}
