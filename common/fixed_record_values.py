from datetime import date
from copy import deepcopy

FIXED_RECORD_VALUES = {
    "metadata": {
        "general_parameters": {
            "schema_version": "0.9.24",
            "record_information": {
                "access_rights": "open access",
                "metadata_access_rights": "open access",
                "publisher": "MBDB",
                "resource_type_general": "Dataset",
                "deposition_date": date.today().isoformat(),
                "date_available": date.today().isoformat(),
                "subject_category": "Biophysics",
            },
        },
    }
}


def make_fixed_values(technique: str, schema_version: str, resource_type: str) -> dict:
    record = deepcopy(FIXED_RECORD_VALUES)
    metadata = record["metadata"]
    gp = metadata["general_parameters"]
    gp["technique"] = technique
    gp["record_information"]["resource_type"] = resource_type
    metadata["method_specific_parameters"] = {"schema_version": schema_version}
    return record
