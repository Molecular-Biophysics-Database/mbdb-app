from invenio_records_resources.services import SearchOptions as InvenioSearchOptions

from . import facets


class MbdbBliSearchOptions(InvenioSearchOptions):
    """MbdbBliRecord search options."""

    facets = {
        "_schema": facets._schema,
        "created": facets.created,
        "_id": facets._id,
        "metadata_general_parameters_associated_publications_additional_authors_affiliations": (
            facets.metadata_general_parameters_associated_publications_additional_authors_affiliations
        ),
        "metadata_general_parameters_associated_publications_additional_authors_family_name": (
            facets.metadata_general_parameters_associated_publications_additional_authors_family_name
        ),
        "metadata_general_parameters_associated_publications_additional_authors_given_name": (
            facets.metadata_general_parameters_associated_publications_additional_authors_given_name
        ),
        "metadata_general_parameters_associated_publications_additional_authors_identifiers": (
            facets.metadata_general_parameters_associated_publications_additional_authors_identifiers
        ),
        "metadata_general_parameters_associated_publications_additional_pid": (
            facets.metadata_general_parameters_associated_publications_additional_pid
        ),
        "metadata_general_parameters_associated_publications_additional_publication_year": (
            facets.metadata_general_parameters_associated_publications_additional_publication_year
        ),
        "metadata_general_parameters_associated_publications_additional_publisher": (
            facets.metadata_general_parameters_associated_publications_additional_publisher
        ),
        "metadata_general_parameters_associated_publications_additional_resource_type": (
            facets.metadata_general_parameters_associated_publications_additional_resource_type
        ),
        "metadata_general_parameters_associated_publications_additional_title": (
            facets.metadata_general_parameters_associated_publications_additional_title
        ),
        "metadata_general_parameters_associated_publications_main_authors_affiliations": (
            facets.metadata_general_parameters_associated_publications_main_authors_affiliations
        ),
        "metadata_general_parameters_associated_publications_main_authors_family_name": (
            facets.metadata_general_parameters_associated_publications_main_authors_family_name
        ),
        "metadata_general_parameters_associated_publications_main_authors_given_name": (
            facets.metadata_general_parameters_associated_publications_main_authors_given_name
        ),
        "metadata_general_parameters_associated_publications_main_authors_identifiers": (
            facets.metadata_general_parameters_associated_publications_main_authors_identifiers
        ),
        "metadata_general_parameters_associated_publications_main_pid": (
            facets.metadata_general_parameters_associated_publications_main_pid
        ),
        "metadata_general_parameters_associated_publications_main_publication_year": (
            facets.metadata_general_parameters_associated_publications_main_publication_year
        ),
        "metadata_general_parameters_associated_publications_main_publisher": (
            facets.metadata_general_parameters_associated_publications_main_publisher
        ),
        "metadata_general_parameters_associated_publications_main_resource_type": (
            facets.metadata_general_parameters_associated_publications_main_resource_type
        ),
        "metadata_general_parameters_associated_publications_main_title": (
            facets.metadata_general_parameters_associated_publications_main_title
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_expression_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_expression_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_expression_source_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_expression_source_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_external_databases": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_external_databases
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_biological_postprocessing_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_biological_postprocessing_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_chemical_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_chemical_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_chemical_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_chemical_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_synthesis_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_synthesis_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_synthesis_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_synthesis_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_polymer_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_polymer_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_report": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_report
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_sequence": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_sequence
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_variant": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_variant
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_inchikey": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_inchikey
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_chemical_modifications_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_chemical_modifications_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_chemical_modifications_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_chemical_modifications_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_chemical_modifications_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_chemical_modifications_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_chemical_modifications_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_chemical_modifications_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_copy_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_copy_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_expression_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_expression_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_expression_source_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_expression_source_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_external_databases": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_external_databases
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_biological_postprocessing_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_biological_postprocessing_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_chemical_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_chemical_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_chemical_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_chemical_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_synthesis_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_synthesis_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_synthesis_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_synthesis_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_polymer_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_polymer_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_report": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_report
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_sequence": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_sequence
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_variant": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_variant
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_inchikey": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_inchikey
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_components_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_components_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_derived_from": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_derived_from
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_fluid": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_fluid
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_health_status": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_health_status
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_cell_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_cell_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_fraction": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_fraction
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_organ": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_organ
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_tissue": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_tissue
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Genetic_material": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Genetic_material
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_capsid_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_capsid_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_envelope_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_envelope_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_host_cell_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_host_cell_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_host_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_host_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_location_S_N_latitude_": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_location_S_N_latitude_
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_location_W_E_longitude_": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_location_W_E_longitude_
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_source": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_source
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_class": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_class
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_additional_specifications_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_additional_specifications_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_additional_specifications_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_additional_specifications_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_copy_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_copy_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_expression_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_expression_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_expression_source_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_expression_source_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_external_databases": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_external_databases
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_biological_postprocessing_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_biological_postprocessing_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_chemical_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_chemical_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_chemical_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_chemical_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_synthesis_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_synthesis_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_synthesis_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_synthesis_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_polymer_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_polymer_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_report": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_report
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_sequence": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_sequence
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_variant": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_variant
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_inchikey": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_inchikey
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_number_of_mono_layers": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_number_of_mono_layers
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_distribution_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_distribution_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_lower": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_lower
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_mean": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_mean
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_median": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_median
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_upper": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_upper
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_details_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_details_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_product": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_product
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_degassing_method": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_degassing_method
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_id": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_id
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_ionic_strength_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_ionic_strength_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_ionic_strength_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_ionic_strength_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_pH_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_pH_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_pH_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_pH_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_pH_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_pH_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_pH_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_pH_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_pH_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_pH_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_pH_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_pH_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_inchikey": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_inchikey
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_report": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_report
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_ultrafiltration_method_filter_material": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_ultrafiltration_method_filter_material
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_ultrafiltration_method_pore_size": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_ultrafiltration_method_pore_size
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_expression_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_expression_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_expression_source_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_expression_source_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_external_databases": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_external_databases
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_id": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_id
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_modifications_biological_postprocessing_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_modifications_biological_postprocessing_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_modifications_chemical_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_modifications_chemical_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_modifications_chemical_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_modifications_chemical_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_modifications_synthesis_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_modifications_synthesis_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_modifications_synthesis_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_modifications_synthesis_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_polymer_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_polymer_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_report": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_report
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_sequence": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_sequence
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_supplier_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_supplier_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_variant": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_variant
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_inchikey": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_inchikey
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_chemical_modifications_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_chemical_modifications_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_chemical_modifications_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_chemical_modifications_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_chemical_modifications_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_chemical_modifications_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_chemical_modifications_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_chemical_modifications_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_copy_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_copy_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_expression_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_expression_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_expression_source_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_expression_source_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_external_databases": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_external_databases
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_biological_postprocessing_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_biological_postprocessing_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_chemical_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_chemical_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_chemical_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_chemical_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_synthesis_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_synthesis_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_synthesis_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_synthesis_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_polymer_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_polymer_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_report": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_report
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_sequence": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_sequence
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_supplier_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_supplier_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_variant": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_variant
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_inchikey": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_inchikey
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_components_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_components_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_derived_from": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_derived_from
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_fluid": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_fluid
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_health_status": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_health_status
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_cell_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_cell_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_fraction": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_fraction
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_organ": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_organ
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_tissue": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_tissue
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Genetic_material": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Genetic_material
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_capsid_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_capsid_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_envelope_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_envelope_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_host_cell_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_host_cell_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_host_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_host_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_location_S_N_latitude_": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_location_S_N_latitude_
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_location_W_E_longitude_": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_location_W_E_longitude_
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_source": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_source
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_class": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_class
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_additional_specifications_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_additional_specifications_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_additional_specifications_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_additional_specifications_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_copy_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_copy_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_expression_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_expression_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_expression_source_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_expression_source_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_external_databases": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_external_databases
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_biological_postprocessing_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_biological_postprocessing_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_chemical_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_chemical_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_chemical_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_chemical_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_synthesis_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_synthesis_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_synthesis_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_synthesis_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_polymer_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_polymer_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_report": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_report
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_sequence": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_sequence
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_supplier_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_supplier_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_variant": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_variant
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_inchikey": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_inchikey
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_components_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_components_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_number_of_mono_layers": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_number_of_mono_layers
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_size_distribution_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_size_distribution_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_size_lower": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_size_lower
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_size_mean": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_size_mean
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_size_median": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_size_median
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_size_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_size_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_size_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_size_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_size_upper": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_size_upper
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_details_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_details_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_product": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_product
        ),
        "metadata_general_parameters_collection_start_time": (
            facets.metadata_general_parameters_collection_start_time
        ),
        "metadata_general_parameters_depositors_contributors_affiliations": (
            facets.metadata_general_parameters_depositors_contributors_affiliations
        ),
        "metadata_general_parameters_depositors_contributors_family_name": (
            facets.metadata_general_parameters_depositors_contributors_family_name
        ),
        "metadata_general_parameters_depositors_contributors_given_name": (
            facets.metadata_general_parameters_depositors_contributors_given_name
        ),
        "metadata_general_parameters_depositors_contributors_identifiers": (
            facets.metadata_general_parameters_depositors_contributors_identifiers
        ),
        "metadata_general_parameters_depositors_depositor_affiliations": (
            facets.metadata_general_parameters_depositors_depositor_affiliations
        ),
        "metadata_general_parameters_depositors_depositor_family_name": (
            facets.metadata_general_parameters_depositors_depositor_family_name
        ),
        "metadata_general_parameters_depositors_depositor_given_name": (
            facets.metadata_general_parameters_depositors_depositor_given_name
        ),
        "metadata_general_parameters_depositors_depositor_identifiers": (
            facets.metadata_general_parameters_depositors_depositor_identifiers
        ),
        "metadata_general_parameters_depositors_principal_contact_affiliations": (
            facets.metadata_general_parameters_depositors_principal_contact_affiliations
        ),
        "metadata_general_parameters_depositors_principal_contact_family_name": (
            facets.metadata_general_parameters_depositors_principal_contact_family_name
        ),
        "metadata_general_parameters_depositors_principal_contact_given_name": (
            facets.metadata_general_parameters_depositors_principal_contact_given_name
        ),
        "metadata_general_parameters_depositors_principal_contact_identifiers": (
            facets.metadata_general_parameters_depositors_principal_contact_identifiers
        ),
        "metadata_general_parameters_derived_parameters_entities_involved_copy_number": (
            facets.metadata_general_parameters_derived_parameters_entities_involved_copy_number
        ),
        "metadata_general_parameters_derived_parameters_entities_involved_entity__version": (
            facets.metadata_general_parameters_derived_parameters_entities_involved_entity__version
        ),
        "metadata_general_parameters_derived_parameters_id": (
            facets.metadata_general_parameters_derived_parameters_id
        ),
        "metadata_general_parameters_derived_parameters_name": (
            facets.metadata_general_parameters_derived_parameters_name
        ),
        "metadata_general_parameters_derived_parameters_type": (
            facets.metadata_general_parameters_derived_parameters_type
        ),
        "metadata_general_parameters_derived_parameters_unit": (
            facets.metadata_general_parameters_derived_parameters_unit
        ),
        "metadata_general_parameters_derived_parameters_value": (
            facets.metadata_general_parameters_derived_parameters_value
        ),
        "metadata_general_parameters_derived_parameters_value_error_error_level": (
            facets.metadata_general_parameters_derived_parameters_value_error_error_level
        ),
        "metadata_general_parameters_derived_parameters_value_error_errors_are_relative": (
            facets.metadata_general_parameters_derived_parameters_value_error_errors_are_relative
        ),
        "metadata_general_parameters_derived_parameters_value_error_lower_error": (
            facets.metadata_general_parameters_derived_parameters_value_error_lower_error
        ),
        "metadata_general_parameters_derived_parameters_value_error_upper_error": (
            facets.metadata_general_parameters_derived_parameters_value_error_upper_error
        ),
        "metadata_general_parameters_funding_reference": (
            facets.metadata_general_parameters_funding_reference
        ),
        "metadata_general_parameters_instrument_manufacturer": (
            facets.metadata_general_parameters_instrument_manufacturer
        ),
        "metadata_general_parameters_instrument_model": (
            facets.metadata_general_parameters_instrument_model
        ),
        "metadata_general_parameters_instrument_name": (
            facets.metadata_general_parameters_instrument_name
        ),
        "metadata_general_parameters_instrument_performance_test_additional_information": (
            facets.metadata_general_parameters_instrument_performance_test_additional_information
        ),
        "metadata_general_parameters_instrument_performance_test_published_test_protocol_authors_affiliations": (
            facets.metadata_general_parameters_instrument_performance_test_published_test_protocol_authors_affiliations
        ),
        "metadata_general_parameters_instrument_performance_test_published_test_protocol_authors_family_name": (
            facets.metadata_general_parameters_instrument_performance_test_published_test_protocol_authors_family_name
        ),
        "metadata_general_parameters_instrument_performance_test_published_test_protocol_authors_given_name": (
            facets.metadata_general_parameters_instrument_performance_test_published_test_protocol_authors_given_name
        ),
        "metadata_general_parameters_instrument_performance_test_published_test_protocol_authors_identifiers": (
            facets.metadata_general_parameters_instrument_performance_test_published_test_protocol_authors_identifiers
        ),
        "metadata_general_parameters_instrument_performance_test_published_test_protocol_pid": (
            facets.metadata_general_parameters_instrument_performance_test_published_test_protocol_pid
        ),
        "metadata_general_parameters_instrument_performance_test_published_test_protocol_publication_year": (
            facets.metadata_general_parameters_instrument_performance_test_published_test_protocol_publication_year
        ),
        "metadata_general_parameters_instrument_performance_test_published_test_protocol_publisher": (
            facets.metadata_general_parameters_instrument_performance_test_published_test_protocol_publisher
        ),
        "metadata_general_parameters_instrument_performance_test_published_test_protocol_resource_type": (
            facets.metadata_general_parameters_instrument_performance_test_published_test_protocol_resource_type
        ),
        "metadata_general_parameters_instrument_performance_test_published_test_protocol_title": (
            facets.metadata_general_parameters_instrument_performance_test_published_test_protocol_title
        ),
        "metadata_general_parameters_instrument_performance_test_report": (
            facets.metadata_general_parameters_instrument_performance_test_report
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_concentration_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_concentration_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_concentration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_concentration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_expression_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_expression_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_expression_source_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_expression_source_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_external_databases": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_external_databases
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_modifications_biological_postprocessing_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_modifications_biological_postprocessing_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_modifications_chemical_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_modifications_chemical_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_modifications_chemical_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_modifications_chemical_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_modifications_synthesis_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_modifications_synthesis_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_modifications_synthesis_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_modifications_synthesis_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_polymer_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_polymer_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_parameter": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_parameter
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_report": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_report
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_technique": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_technique
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_sequence": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_sequence
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_supplier_catalog_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_supplier_catalog_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_supplier_further_information": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_supplier_further_information
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_supplier_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_supplier_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_variant": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_variant
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_additional_identifiers": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_additional_identifiers
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_inchikey": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_inchikey
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_isotopic_labeling": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_isotopic_labeling
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_chemical_modifications_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_chemical_modifications_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_chemical_modifications_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_chemical_modifications_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_chemical_modifications_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_chemical_modifications_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_chemical_modifications_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_chemical_modifications_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_copy_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_copy_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_expression_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_expression_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_expression_source_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_expression_source_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_external_databases": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_external_databases
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_biological_postprocessing_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_biological_postprocessing_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_chemical_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_chemical_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_chemical_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_chemical_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_synthesis_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_synthesis_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_synthesis_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_synthesis_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_polymer_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_polymer_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_parameter": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_parameter
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_report": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_report
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_technique": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_technique
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_sequence": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_sequence
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_supplier_catalog_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_supplier_catalog_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_supplier_further_information": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_supplier_further_information
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_supplier_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_supplier_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_variant": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_variant
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_additional_identifiers": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_additional_identifiers
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_inchikey": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_inchikey
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_components_isotopic_labeling": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_components_isotopic_labeling
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_preparation_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_preparation_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_preparation_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_preparation_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_derived_from": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_derived_from
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_fluid": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_fluid
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_health_status": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_health_status
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_cell_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_cell_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_fraction": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_fraction
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_organ": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_organ
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_tissue": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_tissue
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Genetic_material": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Genetic_material
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_capsid_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_capsid_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_envelope_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_envelope_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_host_cell_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_host_cell_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_host_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_host_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_location_S_N_latitude_": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_location_S_N_latitude_
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_location_W_E_longitude_": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_location_W_E_longitude_
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_source": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_source
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_class": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_class
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_additional_specifications_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_additional_specifications_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_additional_specifications_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_additional_specifications_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_copy_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_copy_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_expression_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_expression_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_expression_source_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_expression_source_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_external_databases": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_external_databases
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_biological_postprocessing_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_biological_postprocessing_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_chemical_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_chemical_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_chemical_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_chemical_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_synthesis_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_synthesis_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_synthesis_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_synthesis_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_polymer_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_polymer_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_parameter": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_parameter
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_report": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_report
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_technique": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_technique
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_sequence": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_sequence
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_supplier_catalog_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_supplier_catalog_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_supplier_further_information": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_supplier_further_information
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_supplier_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_supplier_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_variant": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_variant
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_additional_identifiers": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_additional_identifiers
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_inchikey": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_inchikey
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_components_isotopic_labeling": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_components_isotopic_labeling
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_number_of_mono_layers": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_number_of_mono_layers
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_size_distribution_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_size_distribution_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_size_lower": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_size_lower
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_size_mean": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_size_mean
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_size_median": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_size_median
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_size_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_size_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_size_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_size_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_size_upper": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_size_upper
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_details_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_details_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_product": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_product
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_additional_identifiers": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_additional_identifiers
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_additional_specifications": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_additional_specifications
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_obtained_by": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_obtained_by
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_unit": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_unit
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value_error_error_level": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value_error_error_level
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_inchikey": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_inchikey
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_isotopic_labeling": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_isotopic_labeling
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_unit": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_unit
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value_error_error_level": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value_error_error_level
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value_error_lower_error": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value_error_lower_error
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value_error_upper_error": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value_error_upper_error
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_name": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_name
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_parameter": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_parameter
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_report": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_report
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_unit": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_unit
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_controlled": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_controlled
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_unit": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_unit
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_technique": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_technique
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_supplier_catalog_number": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_supplier_catalog_number
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_supplier_further_information": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_supplier_further_information
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_supplier_name": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_supplier_name
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_type": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_type
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_humidity_controlled": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_humidity_controlled
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_humidity_obtained_by": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_humidity_obtained_by
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_humidity_unit": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_humidity_unit
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value_error_error_level": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value_error_error_level
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value_error_lower_error": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value_error_lower_error
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value_error_upper_error": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value_error_upper_error
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_pressure_controlled": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_pressure_controlled
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_pressure_obtained_by": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_pressure_obtained_by
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_pressure_unit": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_pressure_unit
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value_error_error_level": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value_error_error_level
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value_error_lower_error": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value_error_lower_error
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value_error_upper_error": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value_error_upper_error
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_temperature_controlled": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_temperature_controlled
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_temperature_obtained_by": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_temperature_obtained_by
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_temperature_operational_value": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_temperature_operational_value
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_temperature_unit": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_temperature_unit
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value_error_error_level": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value_error_error_level
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_raw_measurements": (
            facets.metadata_general_parameters_raw_measurements
        ),
        "metadata_general_parameters_record_information_access_rights": (
            facets.metadata_general_parameters_record_information_access_rights
        ),
        "metadata_general_parameters_record_information_date_available": (
            facets.metadata_general_parameters_record_information_date_available
        ),
        "metadata_general_parameters_record_information_deposition_date": (
            facets.metadata_general_parameters_record_information_deposition_date
        ),
        "metadata_general_parameters_record_information_identifier": (
            facets.metadata_general_parameters_record_information_identifier
        ),
        "metadata_general_parameters_record_information_internal_id": (
            facets.metadata_general_parameters_record_information_internal_id
        ),
        "metadata_general_parameters_record_information_keywords": (
            facets.metadata_general_parameters_record_information_keywords
        ),
        "metadata_general_parameters_record_information_measurement_group_id": (
            facets.metadata_general_parameters_record_information_measurement_group_id
        ),
        "metadata_general_parameters_record_information_metadata_access_rights": (
            facets.metadata_general_parameters_record_information_metadata_access_rights
        ),
        "metadata_general_parameters_record_information_project_description": (
            facets.metadata_general_parameters_record_information_project_description
        ),
        "metadata_general_parameters_record_information_project_id": (
            facets.metadata_general_parameters_record_information_project_id
        ),
        "metadata_general_parameters_record_information_project_owner_affiliations": (
            facets.metadata_general_parameters_record_information_project_owner_affiliations
        ),
        "metadata_general_parameters_record_information_project_owner_family_name": (
            facets.metadata_general_parameters_record_information_project_owner_family_name
        ),
        "metadata_general_parameters_record_information_project_owner_given_name": (
            facets.metadata_general_parameters_record_information_project_owner_given_name
        ),
        "metadata_general_parameters_record_information_project_owner_identifiers": (
            facets.metadata_general_parameters_record_information_project_owner_identifiers
        ),
        "metadata_general_parameters_record_information_project_title": (
            facets.metadata_general_parameters_record_information_project_title
        ),
        "metadata_general_parameters_record_information_publisher": (
            facets.metadata_general_parameters_record_information_publisher
        ),
        "metadata_general_parameters_record_information_resource_type": (
            facets.metadata_general_parameters_record_information_resource_type
        ),
        "metadata_general_parameters_record_information_resource_type_general": (
            facets.metadata_general_parameters_record_information_resource_type_general
        ),
        "metadata_general_parameters_record_information_subject_category": (
            facets.metadata_general_parameters_record_information_subject_category
        ),
        "metadata_general_parameters_record_information_title": (
            facets.metadata_general_parameters_record_information_title
        ),
        "metadata_general_parameters_schema_version": (
            facets.metadata_general_parameters_schema_version
        ),
        "metadata_general_parameters_technique": (
            facets.metadata_general_parameters_technique
        ),
        "metadata_method_specific_parameters_data_analysis_data_fitting_model": (
            facets.metadata_method_specific_parameters_data_analysis_data_fitting_model
        ),
        "metadata_method_specific_parameters_data_analysis_data_fitting_quality": (
            facets.metadata_method_specific_parameters_data_analysis_data_fitting_quality
        ),
        "metadata_method_specific_parameters_data_analysis_data_fitting_quality_type": (
            facets.metadata_method_specific_parameters_data_analysis_data_fitting_quality_type
        ),
        "metadata_method_specific_parameters_data_analysis_data_fitting_software_name": (
            facets.metadata_method_specific_parameters_data_analysis_data_fitting_software_name
        ),
        "metadata_method_specific_parameters_data_analysis_data_fitting_software_version": (
            facets.metadata_method_specific_parameters_data_analysis_data_fitting_software_version
        ),
        "metadata_method_specific_parameters_data_analysis_data_processing_steps_description": (
            facets.metadata_method_specific_parameters_data_analysis_data_processing_steps_description
        ),
        "metadata_method_specific_parameters_data_analysis_data_processing_steps_link_to_source_code": (
            facets.metadata_method_specific_parameters_data_analysis_data_processing_steps_link_to_source_code
        ),
        "metadata_method_specific_parameters_data_analysis_data_processing_steps_name": (
            facets.metadata_method_specific_parameters_data_analysis_data_processing_steps_name
        ),
        "metadata_method_specific_parameters_data_analysis_data_processing_steps_software_name": (
            facets.metadata_method_specific_parameters_data_analysis_data_processing_steps_software_name
        ),
        "metadata_method_specific_parameters_data_analysis_data_processing_steps_software_tool": (
            facets.metadata_method_specific_parameters_data_analysis_data_processing_steps_software_tool
        ),
        "metadata_method_specific_parameters_data_analysis_data_processing_steps_software_version": (
            facets.metadata_method_specific_parameters_data_analysis_data_processing_steps_software_version
        ),
        "metadata_method_specific_parameters_data_analysis_derived_parameter__version": (
            facets.metadata_method_specific_parameters_data_analysis_derived_parameter__version
        ),
        "metadata_method_specific_parameters_measurements_id": (
            facets.metadata_method_specific_parameters_measurements_id
        ),
        "metadata_method_specific_parameters_measurements_name": (
            facets.metadata_method_specific_parameters_measurements_name
        ),
        "metadata_method_specific_parameters_data_analysis_measurements__version": (
            facets.metadata_method_specific_parameters_data_analysis_measurements__version
        ),
        "metadata_method_specific_parameters_experiment_type": (
            facets.metadata_method_specific_parameters_experiment_type
        ),
        "metadata_method_specific_parameters_measurement_protocol_id": (
            facets.metadata_method_specific_parameters_measurement_protocol_id
        ),
        "metadata_method_specific_parameters_measurement_protocol_name": (
            facets.metadata_method_specific_parameters_measurement_protocol_name
        ),
        "metadata_method_specific_parameters_measurement_protocol_shaking_speed_unit": (
            facets.metadata_method_specific_parameters_measurement_protocol_shaking_speed_unit
        ),
        "metadata_method_specific_parameters_measurement_protocol_shaking_speed_value": (
            facets.metadata_method_specific_parameters_measurement_protocol_shaking_speed_value
        ),
        "metadata_method_specific_parameters_measurement_protocol_shaking_speed_value_error_error_level": (
            facets.metadata_method_specific_parameters_measurement_protocol_shaking_speed_value_error_error_level
        ),
        "metadata_method_specific_parameters_measurement_protocol_shaking_speed_value_error_errors_are_relative": (
            facets.metadata_method_specific_parameters_measurement_protocol_shaking_speed_value_error_errors_are_relative
        ),
        "metadata_method_specific_parameters_measurement_protocol_shaking_speed_value_error_lower_error": (
            facets.metadata_method_specific_parameters_measurement_protocol_shaking_speed_value_error_lower_error
        ),
        "metadata_method_specific_parameters_measurement_protocol_shaking_speed_value_error_upper_error": (
            facets.metadata_method_specific_parameters_measurement_protocol_shaking_speed_value_error_upper_error
        ),
        "metadata_method_specific_parameters_measurement_protocol_start_time_unit": (
            facets.metadata_method_specific_parameters_measurement_protocol_start_time_unit
        ),
        "metadata_method_specific_parameters_measurement_protocol_start_time_value": (
            facets.metadata_method_specific_parameters_measurement_protocol_start_time_value
        ),
        "metadata_method_specific_parameters_measurement_protocol_start_time_value_error_error_level": (
            facets.metadata_method_specific_parameters_measurement_protocol_start_time_value_error_error_level
        ),
        "metadata_method_specific_parameters_measurement_protocol_start_time_value_error_errors_are_relative": (
            facets.metadata_method_specific_parameters_measurement_protocol_start_time_value_error_errors_are_relative
        ),
        "metadata_method_specific_parameters_measurement_protocol_start_time_value_error_lower_error": (
            facets.metadata_method_specific_parameters_measurement_protocol_start_time_value_error_lower_error
        ),
        "metadata_method_specific_parameters_measurement_protocol_start_time_value_error_upper_error": (
            facets.metadata_method_specific_parameters_measurement_protocol_start_time_value_error_upper_error
        ),
        "metadata_method_specific_parameters_measurement_protocol_time_length_unit": (
            facets.metadata_method_specific_parameters_measurement_protocol_time_length_unit
        ),
        "metadata_method_specific_parameters_measurement_protocol_time_length_value": (
            facets.metadata_method_specific_parameters_measurement_protocol_time_length_value
        ),
        "metadata_method_specific_parameters_measurement_protocol_time_length_value_error_error_level": (
            facets.metadata_method_specific_parameters_measurement_protocol_time_length_value_error_error_level
        ),
        "metadata_method_specific_parameters_measurement_protocol_time_length_value_error_errors_are_relative": (
            facets.metadata_method_specific_parameters_measurement_protocol_time_length_value_error_errors_are_relative
        ),
        "metadata_method_specific_parameters_measurement_protocol_time_length_value_error_lower_error": (
            facets.metadata_method_specific_parameters_measurement_protocol_time_length_value_error_lower_error
        ),
        "metadata_method_specific_parameters_measurement_protocol_time_length_value_error_upper_error": (
            facets.metadata_method_specific_parameters_measurement_protocol_time_length_value_error_upper_error
        ),
        "metadata_method_specific_parameters_measurement_protocol_type": (
            facets.metadata_method_specific_parameters_measurement_protocol_type
        ),
        "metadata_method_specific_parameters_measurements_measured_data_response_name": (
            facets.metadata_method_specific_parameters_measurements_measured_data_response_name
        ),
        "metadata_method_specific_parameters_measurements_measured_data_response_unit": (
            facets.metadata_method_specific_parameters_measurements_measured_data_response_unit
        ),
        "metadata_method_specific_parameters_measurements_measured_data_response_values": (
            facets.metadata_method_specific_parameters_measurements_measured_data_response_values
        ),
        "metadata_method_specific_parameters_measurements_measured_data_time_name": (
            facets.metadata_method_specific_parameters_measurements_measured_data_time_name
        ),
        "metadata_method_specific_parameters_measurements_measured_data_time_unit": (
            facets.metadata_method_specific_parameters_measurements_measured_data_time_unit
        ),
        "metadata_method_specific_parameters_measurements_measured_data_time_values": (
            facets.metadata_method_specific_parameters_measurements_measured_data_time_values
        ),
        "metadata_method_specific_parameters_measurements_measurement_protocol_step__version": (
            facets.metadata_method_specific_parameters_measurements_measurement_protocol_step__version
        ),
        "metadata_method_specific_parameters_measurements_sample_analytes_concentration_obtained_by": (
            facets.metadata_method_specific_parameters_measurements_sample_analytes_concentration_obtained_by
        ),
        "metadata_method_specific_parameters_measurements_sample_analytes_concentration_obtained_protocol_description": (
            facets.metadata_method_specific_parameters_measurements_sample_analytes_concentration_obtained_protocol_description
        ),
        "metadata_method_specific_parameters_measurements_sample_analytes_concentration_obtained_protocol_name": (
            facets.metadata_method_specific_parameters_measurements_sample_analytes_concentration_obtained_protocol_name
        ),
        "metadata_method_specific_parameters_measurements_sample_analytes_concentration_unit": (
            facets.metadata_method_specific_parameters_measurements_sample_analytes_concentration_unit
        ),
        "metadata_method_specific_parameters_measurements_sample_analytes_concentration_value": (
            facets.metadata_method_specific_parameters_measurements_sample_analytes_concentration_value
        ),
        "metadata_method_specific_parameters_measurements_sample_analytes_concentration_value_error_error_level": (
            facets.metadata_method_specific_parameters_measurements_sample_analytes_concentration_value_error_error_level
        ),
        "metadata_method_specific_parameters_measurements_sample_analytes_concentration_value_error_errors_are_relative": (
            facets.metadata_method_specific_parameters_measurements_sample_analytes_concentration_value_error_errors_are_relative
        ),
        "metadata_method_specific_parameters_measurements_sample_analytes_concentration_value_error_lower_error": (
            facets.metadata_method_specific_parameters_measurements_sample_analytes_concentration_value_error_lower_error
        ),
        "metadata_method_specific_parameters_measurements_sample_analytes_concentration_value_error_upper_error": (
            facets.metadata_method_specific_parameters_measurements_sample_analytes_concentration_value_error_upper_error
        ),
        "metadata_method_specific_parameters_measurements_sample_analytes_entity__version": (
            facets.metadata_method_specific_parameters_measurements_sample_analytes_entity__version
        ),
        "metadata_method_specific_parameters_measurements_sample_chemical_environment__version": (
            facets.metadata_method_specific_parameters_measurements_sample_chemical_environment__version
        ),
        "metadata_method_specific_parameters_plates_id": (
            facets.metadata_method_specific_parameters_plates_id
        ),
        "metadata_method_specific_parameters_plates_name": (
            facets.metadata_method_specific_parameters_plates_name
        ),
        "metadata_method_specific_parameters_measurements_sample_plate__version": (
            facets.metadata_method_specific_parameters_measurements_sample_plate__version
        ),
        "metadata_method_specific_parameters_measurements_sample_preparation_protocol_description": (
            facets.metadata_method_specific_parameters_measurements_sample_preparation_protocol_description
        ),
        "metadata_method_specific_parameters_measurements_sample_preparation_protocol_name": (
            facets.metadata_method_specific_parameters_measurements_sample_preparation_protocol_name
        ),
        "metadata_method_specific_parameters_measurements_sample_temperature_controlled": (
            facets.metadata_method_specific_parameters_measurements_sample_temperature_controlled
        ),
        "metadata_method_specific_parameters_measurements_sample_temperature_obtained_by": (
            facets.metadata_method_specific_parameters_measurements_sample_temperature_obtained_by
        ),
        "metadata_method_specific_parameters_measurements_sample_temperature_operational_value": (
            facets.metadata_method_specific_parameters_measurements_sample_temperature_operational_value
        ),
        "metadata_method_specific_parameters_measurements_sample_temperature_unit": (
            facets.metadata_method_specific_parameters_measurements_sample_temperature_unit
        ),
        "metadata_method_specific_parameters_measurements_sample_temperature_value": (
            facets.metadata_method_specific_parameters_measurements_sample_temperature_value
        ),
        "metadata_method_specific_parameters_measurements_sample_temperature_value_error_error_level": (
            facets.metadata_method_specific_parameters_measurements_sample_temperature_value_error_error_level
        ),
        "metadata_method_specific_parameters_measurements_sample_temperature_value_error_errors_are_relative": (
            facets.metadata_method_specific_parameters_measurements_sample_temperature_value_error_errors_are_relative
        ),
        "metadata_method_specific_parameters_measurements_sample_temperature_value_error_lower_error": (
            facets.metadata_method_specific_parameters_measurements_sample_temperature_value_error_lower_error
        ),
        "metadata_method_specific_parameters_measurements_sample_temperature_value_error_upper_error": (
            facets.metadata_method_specific_parameters_measurements_sample_temperature_value_error_upper_error
        ),
        "metadata_method_specific_parameters_measurements_sample_well_position": (
            facets.metadata_method_specific_parameters_measurements_sample_well_position
        ),
        "metadata_method_specific_parameters_sensors_id": (
            facets.metadata_method_specific_parameters_sensors_id
        ),
        "metadata_method_specific_parameters_sensors_name": (
            facets.metadata_method_specific_parameters_sensors_name
        ),
        "metadata_method_specific_parameters_measurements_sensor__version": (
            facets.metadata_method_specific_parameters_measurements_sensor__version
        ),
        "metadata_method_specific_parameters_plates_sealing": (
            facets.metadata_method_specific_parameters_plates_sealing
        ),
        "metadata_method_specific_parameters_plates_supplier_catalog_number": (
            facets.metadata_method_specific_parameters_plates_supplier_catalog_number
        ),
        "metadata_method_specific_parameters_plates_supplier_further_information": (
            facets.metadata_method_specific_parameters_plates_supplier_further_information
        ),
        "metadata_method_specific_parameters_plates_supplier_name": (
            facets.metadata_method_specific_parameters_plates_supplier_name
        ),
        "metadata_method_specific_parameters_plates_surface_modification_protocol_description": (
            facets.metadata_method_specific_parameters_plates_surface_modification_protocol_description
        ),
        "metadata_method_specific_parameters_plates_surface_modification_protocol_name": (
            facets.metadata_method_specific_parameters_plates_surface_modification_protocol_name
        ),
        "metadata_method_specific_parameters_plates_surface_modification_type": (
            facets.metadata_method_specific_parameters_plates_surface_modification_type
        ),
        "metadata_method_specific_parameters_plates_type": (
            facets.metadata_method_specific_parameters_plates_type
        ),
        "metadata_method_specific_parameters_plates_wells": (
            facets.metadata_method_specific_parameters_plates_wells
        ),
        "metadata_method_specific_parameters_schema_version": (
            facets.metadata_method_specific_parameters_schema_version
        ),
        "metadata_method_specific_parameters_sensors_hydration_time_unit": (
            facets.metadata_method_specific_parameters_sensors_hydration_time_unit
        ),
        "metadata_method_specific_parameters_sensors_hydration_time_value": (
            facets.metadata_method_specific_parameters_sensors_hydration_time_value
        ),
        "metadata_method_specific_parameters_sensors_hydration_time_value_error_error_level": (
            facets.metadata_method_specific_parameters_sensors_hydration_time_value_error_error_level
        ),
        "metadata_method_specific_parameters_sensors_hydration_time_value_error_errors_are_relative": (
            facets.metadata_method_specific_parameters_sensors_hydration_time_value_error_errors_are_relative
        ),
        "metadata_method_specific_parameters_sensors_hydration_time_value_error_lower_error": (
            facets.metadata_method_specific_parameters_sensors_hydration_time_value_error_lower_error
        ),
        "metadata_method_specific_parameters_sensors_hydration_time_value_error_upper_error": (
            facets.metadata_method_specific_parameters_sensors_hydration_time_value_error_upper_error
        ),
        "metadata_method_specific_parameters_sensors_ligand_information_ligand__version": (
            facets.metadata_method_specific_parameters_sensors_ligand_information_ligand__version
        ),
        "metadata_method_specific_parameters_sensors_ligand_information_ligand_immobilization_chemistry": (
            facets.metadata_method_specific_parameters_sensors_ligand_information_ligand_immobilization_chemistry
        ),
        "metadata_method_specific_parameters_sensors_ligand_information_ligand_immobilization_protocol_description": (
            facets.metadata_method_specific_parameters_sensors_ligand_information_ligand_immobilization_protocol_description
        ),
        "metadata_method_specific_parameters_sensors_ligand_information_ligand_immobilization_protocol_name": (
            facets.metadata_method_specific_parameters_sensors_ligand_information_ligand_immobilization_protocol_name
        ),
        "metadata_method_specific_parameters_sensors_previously_used": (
            facets.metadata_method_specific_parameters_sensors_previously_used
        ),
        "metadata_method_specific_parameters_sensors_sensor_id": (
            facets.metadata_method_specific_parameters_sensors_sensor_id
        ),
        "metadata_method_specific_parameters_sensors_supplier_catalog_number": (
            facets.metadata_method_specific_parameters_sensors_supplier_catalog_number
        ),
        "metadata_method_specific_parameters_sensors_supplier_further_information": (
            facets.metadata_method_specific_parameters_sensors_supplier_further_information
        ),
        "metadata_method_specific_parameters_sensors_supplier_name": (
            facets.metadata_method_specific_parameters_sensors_supplier_name
        ),
        "metadata_method_specific_parameters_sensors_surface_properties": (
            facets.metadata_method_specific_parameters_sensors_surface_properties
        ),
        "updated": facets.updated,
        **getattr(InvenioSearchOptions, "facets", {}),
    }
    sort_options = {
        **InvenioSearchOptions.sort_options,
    }
