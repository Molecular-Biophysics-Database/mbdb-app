"""Fields offered by the advanced search.

Kinds: ``words`` is a keyword with a ``.words`` sub-field (copy_to in the model
files, see models/text_search.py), ``text`` is analyzed text (vocabulary titles).
"""

from __future__ import annotations

from oarepo_model.datatypes.registry import from_yaml

_TYPES = {
    **from_yaml("../../models/general_parameters-definitions-rdm.yaml", __file__),
    **from_yaml("../../models/mst/mst-definitions.yaml", __file__),
}
_GP = "metadata.general_parameters"
_INFO = f"{_GP}.record_information"
_ENTITY = f"{_GP}.entities_of_interest"
_RESULT = f"{_GP}.results"
_MSP = "metadata.method_specific_parameters"


def _field(group, label, path, kind, options=None):
    return {"group": group, "label": label, "path": path, "kind": kind, "options": options}


def _enum(type_name, prop):
    return _TYPES[type_name]["properties"][prop]["enum"]


def _variants(type_name):
    return [variant["discriminator"] for variant in _TYPES[type_name]["oneof"]]


FIELDS = [
    _field("Record", "Title", f"{_INFO}.title", "words"),
    _field("Record", "Method", f"{_GP}.method", "enum", _TYPES["SUPPORTED_METHODS"]["enum"]),
    _field("Record", "Access rights", f"{_INFO}.access_rights", "enum", _variants("Record_information")),
    _field("Record", "Deposition date", f"{_INFO}.deposition_date", "date"),
    _field("Record", "Date available", f"{_INFO}.date_available", "date"),
    _field("Record", "DOI", f"{_INFO}.external_identifier", "keyword"),
    _field("Record", "Instrument", f"{_GP}.instrument.title.en", "text"),
    _field("Record", "Principal contact family name", f"{_GP}.depositors.principal_contact.family_name", "words"),
    _field("Record", "Depositor family name", f"{_GP}.depositors.depositor.family_name", "words"),
    _field("Record", "Contributor family name", f"{_GP}.depositors.contributors.family_name", "words"),
    _field("Record", "Publication title", f"{_GP}.associated_publication.title", "words"),
    _field("Record", "Publication journal", f"{_GP}.associated_publication.journal", "words"),
    _field("Entity of interest", "Entity name", f"{_ENTITY}.name", "words"),
    _field("Entity of interest", "Entity type", f"{_ENTITY}.type", "enum", _variants("Entity")),
    _field("Entity of interest", "Polymer type", f"{_ENTITY}.polymer_type", "enum", _enum("Polymer", "polymer_type")),
    _field("Entity of interest", "Variant", f"{_ENTITY}.variant", "words"),
    _field("Entity of interest", "Source organism", f"{_ENTITY}.source_organism.title.en", "text"),
    _field("Entity of interest", "Chemical name", f"{_ENTITY}.basic_information.title.en", "text"),
    _field("Chemical environment", "Constituent name", f"{_GP}.chemical_environments.constituents.name", "words"),
    _field("Chemical environment", "pH", f"{_GP}.chemical_environments.ph", "number"),
    _field("Result", "Result name", f"{_RESULT}.name", "words"),
    _field("Result", "Result type", f"{_RESULT}.type", "enum", _variants("Result")),
    _field("Result", "Result value", f"{_RESULT}.value", "number"),
    _field("MST", "Experiment type", f"{_MSP}.experiment_type", "enum", _enum("MST_specific_parameters", "experiment_type")),
    _field("MST", "Signal type", f"{_MSP}.signal_type", "enum", _enum("MST_specific_parameters", "signal_type")),
    _field("MST", "Excitation LED color", f"{_MSP}.excitation_led_color", "enum", _enum("MST_specific_parameters", "excitation_led_color")),
    _field("MST", "Excitation LED power", f"{_MSP}.excitation_led_power", "number"),
    _field("MST", "IR MST laser power", f"{_MSP}.ir_mst_laser_power", "number"),
    _field("MST", "Temperature", f"{_MSP}.temperature.value", "number"),
]
