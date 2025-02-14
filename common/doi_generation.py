import datetime
from typing import List
from flask import current_app

# <Converting MBDB depositors to DataCite creators>
def add_optional_fields_creator(field: str, person: dict, creator: dict) -> None:
    options = {
        "affiliations": ("affiliation", to_affiliation),
        "identifiers": ("nameIdentifiers", to_name_identifiers),
    }

    if field not in options.keys():
        raise ValueError(f"'{field}' is not allowed, allowed values are {options.keys}")

    if field not in person.keys():
        return None

    field_name, func = options[field]
    creator.update({field_name: [func(element) for element in person[field]]})


def to_affiliation(affiliation) -> dict:
    aff_id = affiliation["id"][4:]  # remove ror: from id
    aff_name = affiliation["title"]["en"]
    return {
        "schemeUri": "https://ror.org/",
        "affiliationIdentifier": f"https://ror.org/{aff_id}",
        "affiliationIdentifierScheme": "ROR",
        "name": f"{aff_name}",
    }


def to_name_identifiers(orcid: str) -> dict:
    orcid = orcid[6:]  # removing orcid: from id
    return {
        "schemeUri": "https://orcid.org",
        "nameIdentifier": f"https://orcid.org/{orcid}",
        "nameIdentifierScheme": "ORCID",
    }


def to_creator(person: dict) -> dict:
    given_name = person["given_name"]
    family_name = person["family_name"]

    creator = {
        "name": f"{family_name}, {given_name}",
        "givenName": given_name,
        "familyName": family_name,
    }

    for field in ("affiliations", "identifiers"):
        add_optional_fields_creator(field, person, creator)

    return creator


def to_creators(depositors: dict) -> List[dict]:
    creators = [depositors["principal_contact"]]

    # prevent duplication of names
    if depositors["depositor"] != depositors["principal_contact"]:
        creators += [depositors["depositor"]]

    # only add contributors if there are any
    if "contributors" in depositors.keys():
        creators += depositors["contributors"]

    return [to_creator(creator) for creator in creators]

# </Converting MBDB depositors to DataCite creators>

def to_titles(title: str) -> List[dict]:
    return [{"title": title}]


def to_types(record_info: dict) -> dict:
    return {
        "resourceTypeGeneral": record_info["resource_type_general"],
        "resourceType": record_info["resource_type"],
    }


def to_publisher(record_info: dict) -> dict:
    return {"name": record_info["publisher"]}


def to_publication_year(date: datetime.date) -> int:
    return date.year


def to_subjects(record_info: dict) -> List[dict]:
    return [{"subject": record_info["subject_category"]}]


def to_url(record: dict) -> str:
    base_url = current_app.config.get("BASE_DOMAIN")
    record_type = record["metadata"]["general_parameters"]["record_information"][
        "resource_type"
    ].lower()
    record_id = record["id"]
    return f"{base_url}/{record_type}/{record_id}"


def to_rights(record_info: dict) -> List[dict]:
    has_license = record_info.get("license", None)
    rights_list = []
    if has_license:
        rights_list.append(
            {
                "rights": "Creative Commons Zero v1.0 Universal",
                "rightsUri": "https://creativecommons.org/publicdomain/zero/1.0/legalcode",
            }
        )
    return rights_list


def add_schema(datacite_version):
    return datacite_version


class DataCiteMappingMBDB:
    """Interface between DataCite and MBDB data models"""

    def __init__(self):
        # current_date is used both in creating the payload and updating
        # the record to ensures that they will be consistent
        self.current_date = datetime.date.today()

    @staticmethod
    def metadata_check(data, errors=None):
        """Ensure that the mandatory fields in DataCite's schema are present"""
        if errors is None:
            errors = []

        gp = data["metadata"]["general_parameters"]
        record_info = gp["record_information"]

        if "depositors" not in gp:
            errors.append("Creators are mandatory")
        if "title" not in record_info:
            errors.append("Title is mandatory")
        if "resource_type" not in record_info:
            errors.append("Resource type is mandatory")
        return errors

    def create_datacite_payload(self, data):
        """Extracted information to generate a DataCite compatible payload"""
        gp = data["metadata"]["general_parameters"]
        record_info = gp["record_information"]

        # The tuple fields correspond to
        # (
        #   DataCite schema field name,
        #   function that maps MBDB schema to DataCiteSchema,
        #   data that will be converted,
        # )
        fields = (
            ("creators", to_creators, gp["depositors"]),
            ("titles", to_titles, record_info["title"]),
            ("types", to_types, record_info),
            ("publisher", to_publisher, record_info),
            ("publicationYear", to_publication_year, self.current_date),
            ("subjects", to_subjects, record_info),
            ("rightsList", to_rights, record_info),
            ("url", to_url, data),
            ("schemaVersion", add_schema, "http://datacite.org/schema/kernel-4"),
        )

        return {field: func(data) for field, func, data in fields}

    @staticmethod
    def get_doi(record):
        """Extract DOI from record metadata"""
        return record["metadata"]["general_parameters"]["record_information"].get(
            "external_identifier", None
        )

    def add_doi(self, record, data, doi_value):
        """Add the DOI to the record metadata"""
        info = data["metadata"]["general_parameters"]["record_information"]
        info.update(
            {
                "external_identifier": doi_value,
                "date_available": self.current_date.isoformat(),
            }
        )
        record.update(data)
        record.commit()
