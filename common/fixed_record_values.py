from datetime import date
from copy import deepcopy
from pathlib import Path
import yaml


def schema_version(model: str) -> str:
    """
    Extracts the version from the model and returns it.
    Note that it assumes models can be located in ../models
    """
    model_path = Path(__file__).parent.parent / "models"
    models = ("General_parameters", "BLI", "ITC", "MST", "SPR", "MP")

    if model not in models:
        raise ValueError(f"model: '{model}' is not among the known models: {models}")

    with open(model_path / f"{model.lower()}-definitions.yaml", "r") as f:
        yml = yaml.safe_load(f)

    # Sets the name of the object that contains the schema version
    if model != "General_parameters":
        model = f"{model}_specific_parameters"

    return yml[model]["properties"]["schema_version"]["enum"][0]


def make_fixed_values(method: str, resource_type: str) -> dict:
    """
    Based on the technique, make_fixed_values constructs an initial
    metadata record with all the fixed values set
    """
    record = deepcopy(FIXED_RECORD_VALUES)
    metadata = record["metadata"]
    gp = metadata["general_parameters"]
    gp["method"] = method
    gp["record_information"]["resource_type"] = resource_type
    gp["record_information"]["deposition_date"] = date.today().isoformat()
    metadata["method_specific_parameters"] = {
        "schema_version": schema_version(resource_type)
    }
    return record

# These values are the fixed (general parameter) values that are added to all records
FIXED_RECORD_VALUES = {
    "metadata": {
        "general_parameters": {
            "schema_version": schema_version("General_parameters"),
            "record_information": {
                "access_rights": "open",
                "publisher": "MBDB",
                "resource_type_general": "Dataset",
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
