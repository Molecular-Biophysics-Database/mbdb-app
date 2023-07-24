from invenio_records_resources.services import SearchOptions as InvenioSearchOptions

from . import facets


class MbdbMstSearchOptions(InvenioSearchOptions):
    """MbdbMstRecord search options."""

    facets = {
        "_schema": facets._schema,
        "created": facets.created,
        "_id": facets._id,
        "metadata_general_parameters_associated_publications_additional_authors_affiliations": (
            facets.metadata_general_parameters_associated_publications_additional_authors_affiliations
        ),
        "metadata_general_parameters_associated_publications_additional_authors_full_name": (
            facets.metadata_general_parameters_associated_publications_additional_authors_full_name
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
        "metadata_general_parameters_associated_publications_main_authors_full_name": (
            facets.metadata_general_parameters_associated_publications_main_authors_full_name
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
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_expression_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_expression_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_expression_source_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_expression_source_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_external_databases": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_external_databases
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_biological_postprocessing_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_biological_postprocessing_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_chemical_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_chemical_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_chemical_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_chemical_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_synthesis_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_synthesis_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_synthesis_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_synthesis_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_polymer_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_polymer_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_sequence": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_sequence
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_variant": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Polymer_variant
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_inchikey": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_inchikey
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Chemical_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_chemical_modifications_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_chemical_modifications_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_chemical_modifications_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_chemical_modifications_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_chemical_modifications_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_chemical_modifications_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_chemical_modifications_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_chemical_modifications_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_copy_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_copy_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_expression_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_expression_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_expression_source_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_expression_source_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_external_databases": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_external_databases
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_chemical_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_chemical_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_chemical_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_chemical_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_synthesis_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_synthesis_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_synthesis_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_synthesis_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_polymer_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_polymer_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_sequence": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_sequence
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_variant": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Polymer_variant
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_copy_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_copy_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_inchikey": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_inchikey
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_components_Chemical_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_external_databases": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_external_databases
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Molecular_assembly_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_derived_from": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_derived_from
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_fluid": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_fluid
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_health_status": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_health_status
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_id": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_id
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Body_fluid_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_celltype": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_celltype
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_derived_from": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_derived_from
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_fraction": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_fraction
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_health_status": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_health_status
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_id": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_id
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_organ": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_organ
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_tissue": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_tissue
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Cell_fraction_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_Genetic_material": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_Genetic_material
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_capsid_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_capsid_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_derived_from": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_derived_from
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_envelope_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_envelope_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_host_cell_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_host_cell_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_host_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_host_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_id": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_id
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_biological_origin_Virion_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_location_S_N_latitude_": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_location_S_N_latitude_
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_location_W_E_longitude_": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_location_W_E_longitude_
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_source": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_source
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_environmental_origin_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_class": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_class
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_additional_specifications_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_additional_specifications_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_additional_specifications_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_additional_specifications_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_copy_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_copy_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_expression_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_expression_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_expression_source_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_expression_source_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_external_databases": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_external_databases
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_polymer_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_polymer_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_sequence": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_sequence
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_variant": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Polymer_variant
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_copy_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_copy_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_inchikey": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_inchikey
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_components_Chemical_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_number_of_mono_layers": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_number_of_mono_layers
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_size_distribution_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_size_distribution_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_size_lower": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_size_lower
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_size_mean": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_size_mean
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_size_median": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_size_median
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_size_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_size_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_size_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_size_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_size_upper": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_size_upper
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_details_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_chemical_origin_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_product": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_product
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_constituents_Complex_substance_of_industrial_production_origin_type
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
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_expression_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_expression_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_expression_source_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_expression_source_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_external_databases": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_external_databases
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_biological_postprocessing_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_biological_postprocessing_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_chemical_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_chemical_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_chemical_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_chemical_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_synthesis_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_synthesis_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_synthesis_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_synthesis_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_polymer_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_polymer_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_sequence": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_sequence
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_variant": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Polymer_variant
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_inchikey": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_inchikey
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Chemical_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_chemical_modifications_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_chemical_modifications_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_chemical_modifications_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_chemical_modifications_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_chemical_modifications_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_chemical_modifications_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_chemical_modifications_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_chemical_modifications_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_copy_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_copy_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_expression_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_expression_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_expression_source_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_expression_source_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_external_databases": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_external_databases
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_chemical_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_chemical_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_chemical_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_chemical_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_synthesis_modification": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_synthesis_modification
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_synthesis_monomer_position": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_synthesis_monomer_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_organism": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_organism
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_polymer_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_polymer_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_sequence": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_sequence
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_variant": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Polymer_variant
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_copy_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_copy_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_inchikey": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_inchikey
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_components_Chemical_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_external_databases": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_external_databases
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_supplier_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_supplier_name
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_type": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_solvent_Molecular_assembly_type
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_ultrafiltration_method_filter_material": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_ultrafiltration_method_filter_material
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_ultrafiltration_method_pore_size": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_ultrafiltration_method_pore_size
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_expression_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_expression_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_expression_source_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_expression_source_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_external_databases": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_external_databases
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_id": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_id
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_biological_postprocessing_monomer_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_biological_postprocessing_monomer_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_chemical_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_chemical_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_chemical_monomer_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_chemical_monomer_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_synthesis_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_synthesis_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_synthesis_monomer_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_synthesis_monomer_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_polymer_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_polymer_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_sequence": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_sequence
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_supplier_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_supplier_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Polymer_variant": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Polymer_variant
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_id": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_id
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_inchikey": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_inchikey
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_supplier_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_supplier_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Chemical_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Chemical_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_chemical_modifications_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_chemical_modifications_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_chemical_modifications_monomer_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_chemical_modifications_monomer_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_chemical_modifications_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_chemical_modifications_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_chemical_modifications_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_chemical_modifications_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_copy_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_copy_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_expression_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_expression_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_expression_source_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_expression_source_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_external_databases": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_external_databases
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_monomer_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_monomer_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_chemical_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_chemical_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_chemical_monomer_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_chemical_monomer_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_synthesis_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_synthesis_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_synthesis_monomer_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_synthesis_monomer_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_polymer_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_polymer_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_sequence": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_sequence
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_supplier_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_supplier_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_variant": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Polymer_variant
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_copy_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_copy_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_inchikey": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_inchikey
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_supplier_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_supplier_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_components_Chemical_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_external_databases": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_external_databases
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_id": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_id
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_supplier_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_supplier_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Molecular_assembly_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_derived_from": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_derived_from
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_fluid": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_fluid
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_health_status": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_health_status
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_id": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_id
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Body_fluid_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_celltype": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_celltype
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_derived_from": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_derived_from
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_fraction": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_fraction
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_health_status": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_health_status
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_id": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_id
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_organ": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_organ
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_tissue": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_tissue
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Cell_fraction_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_Genetic_material": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_Genetic_material
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_capsid_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_capsid_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_derived_from": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_derived_from
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_envelope_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_envelope_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_host_cell_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_host_cell_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_host_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_host_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_id": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_id
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_biological_origin_Virion_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_id": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_id
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_location_S_N_latitude_": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_location_S_N_latitude_
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_location_W_E_longitude_": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_location_W_E_longitude_
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_source": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_source
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_environmental_origin_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_class": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_class
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_additional_specifications_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_additional_specifications_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_additional_specifications_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_additional_specifications_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_copy_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_copy_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_expression_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_expression_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_expression_source_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_expression_source_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_external_databases": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_external_databases
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_monomer_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_monomer_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_monomer_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_monomer_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_modification": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_modification
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_monomer_position": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_monomer_position
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_organism": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_organism
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_polymer_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_polymer_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_sequence": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_sequence
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_variant": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Polymer_variant
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_additional_identifiers": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_additional_identifiers
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_copy_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_copy_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_inchikey": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_inchikey
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_isotopic_labeling": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_isotopic_labeling
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_parameter": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_parameter
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_size_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_size_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_source": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_source
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_technique": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_technique
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_catalog_number": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_catalog_number
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_further_information": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_further_information
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_components_Chemical_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_number_of_mono_layers": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_number_of_mono_layers
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_size_distribution_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_size_distribution_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_size_lower": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_size_lower
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_size_mean": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_size_mean
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_size_median": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_size_median
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_size_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_size_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_size_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_size_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_size_upper": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_size_upper
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_details_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_id": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_id
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_chemical_origin_type
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_additional_specifications": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_additional_specifications
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_id": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_id
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_preparation_protocol_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_preparation_protocol_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_preparation_protocol_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_preparation_protocol_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_product": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_product
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_duration_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_duration_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_duration_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_duration_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_storage_preparation_description": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_storage_preparation_description
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_storage_preparation_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_storage_preparation_name
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_controlled": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_controlled
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_operational_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_operational_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_unit": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_unit
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_value": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_value
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_type": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_type
        ),
        "metadata_general_parameters_depositors_contributors_affiliations": (
            facets.metadata_general_parameters_depositors_contributors_affiliations
        ),
        "metadata_general_parameters_depositors_contributors_full_name": (
            facets.metadata_general_parameters_depositors_contributors_full_name
        ),
        "metadata_general_parameters_depositors_contributors_identifiers": (
            facets.metadata_general_parameters_depositors_contributors_identifiers
        ),
        "metadata_general_parameters_depositors_depositor_affiliations": (
            facets.metadata_general_parameters_depositors_depositor_affiliations
        ),
        "metadata_general_parameters_depositors_depositor_full_name": (
            facets.metadata_general_parameters_depositors_depositor_full_name
        ),
        "metadata_general_parameters_depositors_depositor_identifiers": (
            facets.metadata_general_parameters_depositors_depositor_identifiers
        ),
        "metadata_general_parameters_depositors_principal_contact_affiliations": (
            facets.metadata_general_parameters_depositors_principal_contact_affiliations
        ),
        "metadata_general_parameters_depositors_principal_contact_full_name": (
            facets.metadata_general_parameters_depositors_principal_contact_full_name
        ),
        "metadata_general_parameters_depositors_principal_contact_identifiers": (
            facets.metadata_general_parameters_depositors_principal_contact_identifiers
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_id": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_id
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_name
        ),
        "metadata_general_parameters_derived_parameters_entities_involved_entity__version": (
            facets.metadata_general_parameters_derived_parameters_entities_involved_entity__version
        ),
        "metadata_general_parameters_derived_parameters_entities_involved_stoichiometry": (
            facets.metadata_general_parameters_derived_parameters_entities_involved_stoichiometry
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
        "metadata_general_parameters_instrument_performance_test_published_test_protocol_authors_full_name": (
            facets.metadata_general_parameters_instrument_performance_test_published_test_protocol_authors_full_name
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
        "metadata_general_parameters_instrument_performance_test_report_description": (
            facets.metadata_general_parameters_instrument_performance_test_report_description
        ),
        "metadata_general_parameters_instrument_performance_test_report_name": (
            facets.metadata_general_parameters_instrument_performance_test_report_name
        ),
        "metadata_general_parameters_instrument_performance_test_report_processing_steps_description": (
            facets.metadata_general_parameters_instrument_performance_test_report_processing_steps_description
        ),
        "metadata_general_parameters_instrument_performance_test_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_instrument_performance_test_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_instrument_performance_test_report_processing_steps_name": (
            facets.metadata_general_parameters_instrument_performance_test_report_processing_steps_name
        ),
        "metadata_general_parameters_instrument_performance_test_report_processing_steps_software_name": (
            facets.metadata_general_parameters_instrument_performance_test_report_processing_steps_software_name
        ),
        "metadata_general_parameters_instrument_performance_test_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_instrument_performance_test_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_instrument_performance_test_report_processing_steps_software_version": (
            facets.metadata_general_parameters_instrument_performance_test_report_processing_steps_software_version
        ),
        "metadata_general_parameters_instrument_performance_test_report_recommended_software": (
            facets.metadata_general_parameters_instrument_performance_test_report_recommended_software
        ),
        "metadata_general_parameters_instrument_performance_test_report_size_unit": (
            facets.metadata_general_parameters_instrument_performance_test_report_size_unit
        ),
        "metadata_general_parameters_instrument_performance_test_report_size_value": (
            facets.metadata_general_parameters_instrument_performance_test_report_size_value
        ),
        "metadata_general_parameters_instrument_performance_test_report_source": (
            facets.metadata_general_parameters_instrument_performance_test_report_source
        ),
        "metadata_general_parameters_instrument_performance_test_report_type": (
            facets.metadata_general_parameters_instrument_performance_test_report_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_expression_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_expression_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_expression_source_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_expression_source_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_external_databases": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_external_databases
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_biological_postprocessing_monomer_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_biological_postprocessing_monomer_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_chemical_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_chemical_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_chemical_monomer_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_chemical_monomer_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_synthesis_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_synthesis_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_synthesis_monomer_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_synthesis_monomer_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_polymer_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_polymer_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_parameter": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_parameter
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_size_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_size_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_source": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_source
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_report_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_technique": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_quality_controls_technique
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_sequence": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_sequence
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_supplier_catalog_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_supplier_catalog_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_supplier_further_information": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_supplier_further_information
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_supplier_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_supplier_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_variant": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Polymer_variant
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_additional_identifiers": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_additional_identifiers
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_inchikey": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_inchikey
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_isotopic_labeling": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_isotopic_labeling
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_parameter": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_parameter
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_size_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_size_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_source": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_source
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_report_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_technique": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_quality_controls_technique
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_supplier_catalog_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_supplier_catalog_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_supplier_further_information": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_supplier_further_information
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_supplier_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_supplier_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Chemical_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_chemical_modifications_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_chemical_modifications_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_chemical_modifications_monomer_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_chemical_modifications_monomer_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_chemical_modifications_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_chemical_modifications_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_chemical_modifications_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_chemical_modifications_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_copy_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_copy_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_expression_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_expression_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_expression_source_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_expression_source_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_external_databases": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_external_databases
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_monomer_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_monomer_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_chemical_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_chemical_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_chemical_monomer_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_chemical_monomer_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_synthesis_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_synthesis_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_synthesis_monomer_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_synthesis_monomer_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_polymer_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_polymer_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_parameter": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_parameter
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_size_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_size_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_source": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_source
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_report_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_technique": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_quality_controls_technique
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_sequence": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_sequence
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_supplier_catalog_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_supplier_catalog_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_supplier_further_information": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_supplier_further_information
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_supplier_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_supplier_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_variant": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Polymer_variant
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_additional_identifiers": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_additional_identifiers
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_copy_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_copy_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_inchikey": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_inchikey
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_isotopic_labeling": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_isotopic_labeling
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_parameter": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_parameter
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_size_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_size_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_source": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_source
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_report_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_technique": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_quality_controls_technique
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_supplier_catalog_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_supplier_catalog_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_supplier_further_information": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_supplier_further_information
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_supplier_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_supplier_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_components_Chemical_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_external_databases": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_external_databases
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_preparation_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_preparation_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_preparation_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_preparation_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_parameter": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_parameter
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_size_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_size_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_source": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_source
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_report_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_technique": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_quality_controls_technique
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_supplier_catalog_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_supplier_catalog_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_supplier_further_information": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_supplier_further_information
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_supplier_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_supplier_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Molecular_assembly_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_derived_from": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_derived_from
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_fluid": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_fluid
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_health_status": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_health_status
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_id": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_id
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_preparation_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_preparation_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_preparation_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_preparation_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Body_fluid_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_celltype": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_celltype
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_derived_from": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_derived_from
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_fraction": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_fraction
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_health_status": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_health_status
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_id": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_id
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_organ": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_organ
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_preparation_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_preparation_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_preparation_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_preparation_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_tissue": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_tissue
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Cell_fraction_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_Genetic_material": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_Genetic_material
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_capsid_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_capsid_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_derived_from": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_derived_from
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_envelope_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_envelope_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_host_cell_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_host_cell_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_host_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_host_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_id": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_id
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_preparation_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_preparation_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_preparation_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_preparation_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_biological_origin_Virion_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_location_S_N_latitude_": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_location_S_N_latitude_
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_location_W_E_longitude_": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_location_W_E_longitude_
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_preparation_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_preparation_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_preparation_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_preparation_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_source": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_source
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_environmental_origin_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_class": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_class
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_additional_specifications_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_additional_specifications_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_additional_specifications_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_additional_specifications_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_copy_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_copy_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_expression_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_expression_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_expression_source_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_expression_source_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_external_databases": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_external_databases
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_monomer_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_monomer_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_monomer_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_monomer_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_modification": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_modification
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_monomer_position": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_monomer_position
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_organism": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_organism
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_polymer_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_polymer_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_parameter": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_parameter
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_size_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_size_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_source": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_source
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_report_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_technique": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_quality_controls_technique
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_sequence": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_sequence
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_catalog_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_catalog_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_further_information": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_further_information
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_supplier_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_variant": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Polymer_variant
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_additional_identifiers": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_additional_identifiers
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_copy_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_copy_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_inchikey": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_inchikey
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_isotopic_labeling": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_isotopic_labeling
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_parameter": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_parameter
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_size_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_size_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_source": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_source
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_report_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_technique": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_quality_controls_technique
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_catalog_number": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_catalog_number
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_further_information": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_further_information
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_supplier_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_components_Chemical_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_number_of_mono_layers": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_number_of_mono_layers
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_size_distribution_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_size_distribution_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_size_lower": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_size_lower
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_size_mean": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_size_mean
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_size_median": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_size_median
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_size_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_size_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_size_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_size_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_size_upper": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_size_upper
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_details_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_preparation_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_preparation_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_preparation_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_preparation_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_chemical_origin_type
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_additional_specifications": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_additional_specifications
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_preparation_protocol_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_preparation_protocol_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_preparation_protocol_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_preparation_protocol_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_product": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_product
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_duration_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_duration_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_duration_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_duration_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_duration_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_duration_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_duration_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_duration_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_duration_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_duration_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_storage_preparation_description": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_storage_preparation_description
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_storage_preparation_name": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_storage_preparation_name
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_controlled": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_controlled
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_obtained_by": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_obtained_by
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_operational_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_operational_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_unit": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_unit
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_value": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_value
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_error_level": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_error_level
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_storage_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_type": (
            facets.metadata_general_parameters_instrument_performance_test_sample_composition_Complex_substance_of_industrial_production_origin_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_additional_specifications": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_additional_specifications
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_obtained_by": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_obtained_by
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_expression_organism": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_expression_organism
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_expression_source_type": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_expression_source_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_external_databases": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_external_databases
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_biological_postprocessing_monomer_position": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_biological_postprocessing_monomer_position
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_chemical_modification": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_chemical_modification
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_chemical_monomer_position": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_chemical_monomer_position
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_synthesis_modification": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_synthesis_modification
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_synthesis_monomer_position": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_synthesis_monomer_position
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_organism": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_organism
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_polymer_type": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_polymer_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_parameter": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_parameter
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_size_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_size_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_source": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_source
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_type": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_report_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_technique": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_quality_controls_technique
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_sequence": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_sequence
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_supplier_catalog_number": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_supplier_catalog_number
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_supplier_further_information": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_supplier_further_information
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_supplier_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_supplier_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_type": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_variant": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Polymer_variant
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_additional_identifiers": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_additional_identifiers
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_additional_specifications": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_additional_specifications
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_obtained_by": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_obtained_by
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_inchikey": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_inchikey
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_isotopic_labeling": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_isotopic_labeling
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_parameter": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_parameter
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_size_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_size_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_source": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_source
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_type": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_report_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_technique": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_quality_controls_technique
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_supplier_catalog_number": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_supplier_catalog_number
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_supplier_further_information": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_supplier_further_information
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_supplier_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_supplier_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_type": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Chemical_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_additional_specifications": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_additional_specifications
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_chemical_modifications_modification": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_chemical_modifications_modification
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_chemical_modifications_monomer_position": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_chemical_modifications_monomer_position
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_chemical_modifications_protocol_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_chemical_modifications_protocol_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_chemical_modifications_protocol_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_chemical_modifications_protocol_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_additional_specifications": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_additional_specifications
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_copy_number": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_copy_number
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_expression_organism": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_expression_organism
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_expression_source_type": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_expression_source_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_external_databases": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_external_databases
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_modification": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_modification
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_monomer_position": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_monomer_position
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_biological_postprocessing_protocol_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_chemical_modification": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_chemical_modification
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_chemical_monomer_position": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_chemical_monomer_position
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_chemical_protocol_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_chemical_protocol_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_chemical_protocol_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_chemical_protocol_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_synthesis_modification": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_synthesis_modification
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_synthesis_monomer_position": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_synthesis_monomer_position
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_modifications_synthesis_protocol_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_organism": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_organism
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_polymer_type": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_polymer_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_parameter": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_parameter
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_size_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_size_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_source": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_source
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_type": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_report_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_technique": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_quality_controls_technique
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_sequence": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_sequence
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_supplier_catalog_number": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_supplier_catalog_number
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_supplier_further_information": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_supplier_further_information
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_supplier_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_supplier_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_type": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_variant": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Polymer_variant
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_additional_identifiers": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_additional_identifiers
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_additional_specifications": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_additional_specifications
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_copy_number": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_copy_number
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_inchikey": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_inchikey
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_isotopic_labeling": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_isotopic_labeling
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_parameter": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_parameter
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_size_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_size_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_source": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_source
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_type": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_report_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_technique": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_quality_controls_technique
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_supplier_catalog_number": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_supplier_catalog_number
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_supplier_further_information": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_supplier_further_information
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_supplier_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_supplier_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_type": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_components_Chemical_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_obtained_by": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_obtained_by
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_obtained_protocol_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_obtained_protocol_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_obtained_protocol_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_obtained_protocol_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_external_databases": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_external_databases
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_preparation_protocol_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_preparation_protocol_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_preparation_protocol_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_preparation_protocol_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_parameter": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_parameter
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_processing_steps_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_processing_steps_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_processing_steps_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_processing_steps_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_processing_steps_software_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_processing_steps_software_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_processing_steps_software_tool": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_processing_steps_software_tool
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_processing_steps_software_version": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_processing_steps_software_version
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_recommended_software": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_recommended_software
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_size_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_size_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_size_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_size_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_source": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_source
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_type": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_report_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_duration_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_description": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_description
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_storage_preparation_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_controlled": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_controlled
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_obtained_by
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_operational_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_operational_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_storage_from_QC_to_measurement_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_technique": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_quality_controls_technique
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_supplier_catalog_number": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_supplier_catalog_number
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_supplier_further_information": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_supplier_further_information
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_supplier_name": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_supplier_name
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_type": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_atmosphere_composition_Molecular_assembly_type
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_humidity_controlled": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_humidity_controlled
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_humidity_obtained_by": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_humidity_obtained_by
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_humidity_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_humidity_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_humidity_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_humidity_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_humidity_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_humidity_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_humidity_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_humidity_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_humidity_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_humidity_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_humidity_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_humidity_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_pressure_controlled": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_pressure_controlled
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_pressure_obtained_by": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_pressure_obtained_by
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_pressure_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_pressure_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_pressure_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_pressure_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_pressure_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_pressure_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_pressure_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_pressure_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_pressure_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_pressure_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_pressure_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_pressure_value_error_upper_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_temperature_controlled": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_temperature_controlled
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_temperature_obtained_by": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_temperature_obtained_by
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_temperature_operational_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_temperature_operational_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_temperature_unit": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_temperature_unit
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_temperature_value": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_temperature_value
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_temperature_value_error_error_level": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_temperature_value_error_error_level
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_temperature_value_error_errors_are_relative": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_temperature_value_error_errors_are_relative
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_temperature_value_error_lower_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_temperature_value_error_lower_error
        ),
        "metadata_general_parameters_physical_environment_at_sample_handling_temperature_value_error_upper_error": (
            facets.metadata_general_parameters_physical_environment_at_sample_handling_temperature_value_error_upper_error
        ),
        "metadata_general_parameters_raw_data_information_collection_start_time": (
            facets.metadata_general_parameters_raw_data_information_collection_start_time
        ),
        "metadata_general_parameters_raw_data_information_file_information_description": (
            facets.metadata_general_parameters_raw_data_information_file_information_description
        ),
        "metadata_general_parameters_raw_data_information_file_information_name": (
            facets.metadata_general_parameters_raw_data_information_file_information_name
        ),
        "metadata_general_parameters_raw_data_information_file_information_processing_steps_description": (
            facets.metadata_general_parameters_raw_data_information_file_information_processing_steps_description
        ),
        "metadata_general_parameters_raw_data_information_file_information_processing_steps_link_to_source_code": (
            facets.metadata_general_parameters_raw_data_information_file_information_processing_steps_link_to_source_code
        ),
        "metadata_general_parameters_raw_data_information_file_information_processing_steps_name": (
            facets.metadata_general_parameters_raw_data_information_file_information_processing_steps_name
        ),
        "metadata_general_parameters_raw_data_information_file_information_processing_steps_software_name": (
            facets.metadata_general_parameters_raw_data_information_file_information_processing_steps_software_name
        ),
        "metadata_general_parameters_raw_data_information_file_information_processing_steps_software_tool": (
            facets.metadata_general_parameters_raw_data_information_file_information_processing_steps_software_tool
        ),
        "metadata_general_parameters_raw_data_information_file_information_processing_steps_software_version": (
            facets.metadata_general_parameters_raw_data_information_file_information_processing_steps_software_version
        ),
        "metadata_general_parameters_raw_data_information_file_information_recommended_software": (
            facets.metadata_general_parameters_raw_data_information_file_information_recommended_software
        ),
        "metadata_general_parameters_raw_data_information_file_information_size_unit": (
            facets.metadata_general_parameters_raw_data_information_file_information_size_unit
        ),
        "metadata_general_parameters_raw_data_information_file_information_size_value": (
            facets.metadata_general_parameters_raw_data_information_file_information_size_value
        ),
        "metadata_general_parameters_raw_data_information_file_information_source": (
            facets.metadata_general_parameters_raw_data_information_file_information_source
        ),
        "metadata_general_parameters_raw_data_information_file_information_type": (
            facets.metadata_general_parameters_raw_data_information_file_information_type
        ),
        "metadata_general_parameters_record_access_rights": (
            facets.metadata_general_parameters_record_access_rights
        ),
        "metadata_general_parameters_record_date_available": (
            facets.metadata_general_parameters_record_date_available
        ),
        "metadata_general_parameters_record_deposition_date": (
            facets.metadata_general_parameters_record_deposition_date
        ),
        "metadata_general_parameters_record_id": (
            facets.metadata_general_parameters_record_id
        ),
        "metadata_general_parameters_record_identifier": (
            facets.metadata_general_parameters_record_identifier
        ),
        "metadata_general_parameters_record_keywords": (
            facets.metadata_general_parameters_record_keywords
        ),
        "metadata_general_parameters_record_measurement_group_id": (
            facets.metadata_general_parameters_record_measurement_group_id
        ),
        "metadata_general_parameters_record_metadata_access_rights": (
            facets.metadata_general_parameters_record_metadata_access_rights
        ),
        "metadata_general_parameters_record_project_description": (
            facets.metadata_general_parameters_record_project_description
        ),
        "metadata_general_parameters_record_project_id": (
            facets.metadata_general_parameters_record_project_id
        ),
        "metadata_general_parameters_record_project_owner_affiliations": (
            facets.metadata_general_parameters_record_project_owner_affiliations
        ),
        "metadata_general_parameters_record_project_owner_full_name": (
            facets.metadata_general_parameters_record_project_owner_full_name
        ),
        "metadata_general_parameters_record_project_owner_identifiers": (
            facets.metadata_general_parameters_record_project_owner_identifiers
        ),
        "metadata_general_parameters_record_project_title": (
            facets.metadata_general_parameters_record_project_title
        ),
        "metadata_general_parameters_record_publisher": (
            facets.metadata_general_parameters_record_publisher
        ),
        "metadata_general_parameters_record_resource_type": (
            facets.metadata_general_parameters_record_resource_type
        ),
        "metadata_general_parameters_record_resource_type_general": (
            facets.metadata_general_parameters_record_resource_type_general
        ),
        "metadata_general_parameters_record_subject_category": (
            facets.metadata_general_parameters_record_subject_category
        ),
        "metadata_general_parameters_record_title": (
            facets.metadata_general_parameters_record_title
        ),
        "metadata_general_parameters_record_version": (
            facets.metadata_general_parameters_record_version
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
        "metadata_general_parameters_derived_parameters_id": (
            facets.metadata_general_parameters_derived_parameters_id
        ),
        "metadata_general_parameters_derived_parameters_name": (
            facets.metadata_general_parameters_derived_parameters_name
        ),
        "metadata_method_specific_parameters_data_analysis_derived_parameter__version": (
            facets.metadata_method_specific_parameters_data_analysis_derived_parameter__version
        ),
        "metadata_method_specific_parameters_data_analysis_f_cold_and_hot_f_cold_end": (
            facets.metadata_method_specific_parameters_data_analysis_f_cold_and_hot_f_cold_end
        ),
        "metadata_method_specific_parameters_data_analysis_f_cold_and_hot_f_cold_start": (
            facets.metadata_method_specific_parameters_data_analysis_f_cold_and_hot_f_cold_start
        ),
        "metadata_method_specific_parameters_data_analysis_f_cold_and_hot_f_hot_end": (
            facets.metadata_method_specific_parameters_data_analysis_f_cold_and_hot_f_hot_end
        ),
        "metadata_method_specific_parameters_data_analysis_f_cold_and_hot_f_hot_start": (
            facets.metadata_method_specific_parameters_data_analysis_f_cold_and_hot_f_hot_start
        ),
        "metadata_method_specific_parameters_data_analysis_f_cold_and_hot_time_unit": (
            facets.metadata_method_specific_parameters_data_analysis_f_cold_and_hot_time_unit
        ),
        "metadata_method_specific_parameters_excitation_led_color": (
            facets.metadata_method_specific_parameters_excitation_led_color
        ),
        "metadata_method_specific_parameters_excitation_led_power": (
            facets.metadata_method_specific_parameters_excitation_led_power
        ),
        "metadata_method_specific_parameters_experiment_type": (
            facets.metadata_method_specific_parameters_experiment_type
        ),
        "metadata_method_specific_parameters_ir_mst_laser_power": (
            facets.metadata_method_specific_parameters_ir_mst_laser_power
        ),
        "metadata_method_specific_parameters_measurements_measured_data_x_data_name": (
            facets.metadata_method_specific_parameters_measurements_measured_data_x_data_name
        ),
        "metadata_method_specific_parameters_measurements_measured_data_x_data_unit": (
            facets.metadata_method_specific_parameters_measurements_measured_data_x_data_unit
        ),
        "metadata_method_specific_parameters_measurements_measured_data_x_data_values": (
            facets.metadata_method_specific_parameters_measurements_measured_data_x_data_values
        ),
        "metadata_method_specific_parameters_measurements_measured_data_y_data_name": (
            facets.metadata_method_specific_parameters_measurements_measured_data_y_data_name
        ),
        "metadata_method_specific_parameters_measurements_measured_data_y_data_unit": (
            facets.metadata_method_specific_parameters_measurements_measured_data_y_data_unit
        ),
        "metadata_method_specific_parameters_measurements_measured_data_y_data_values": (
            facets.metadata_method_specific_parameters_measurements_measured_data_y_data_values
        ),
        "metadata_method_specific_parameters_measurements_name": (
            facets.metadata_method_specific_parameters_measurements_name
        ),
        "metadata_method_specific_parameters_measurements_position": (
            facets.metadata_method_specific_parameters_measurements_position
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_id": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_id
        ),
        "metadata_general_parameters_chemical_information_chemical_environments_name": (
            facets.metadata_general_parameters_chemical_information_chemical_environments_name
        ),
        "metadata_method_specific_parameters_measurements_sample_chemical_environment__version": (
            facets.metadata_method_specific_parameters_measurements_sample_chemical_environment__version
        ),
        "metadata_method_specific_parameters_measurements_sample_container": (
            facets.metadata_method_specific_parameters_measurements_sample_container
        ),
        "metadata_method_specific_parameters_measurements_sample_ligands_concentration_obtained_by": (
            facets.metadata_method_specific_parameters_measurements_sample_ligands_concentration_obtained_by
        ),
        "metadata_method_specific_parameters_measurements_sample_ligands_concentration_obtained_protocol_description": (
            facets.metadata_method_specific_parameters_measurements_sample_ligands_concentration_obtained_protocol_description
        ),
        "metadata_method_specific_parameters_measurements_sample_ligands_concentration_obtained_protocol_name": (
            facets.metadata_method_specific_parameters_measurements_sample_ligands_concentration_obtained_protocol_name
        ),
        "metadata_method_specific_parameters_measurements_sample_ligands_concentration_unit": (
            facets.metadata_method_specific_parameters_measurements_sample_ligands_concentration_unit
        ),
        "metadata_method_specific_parameters_measurements_sample_ligands_concentration_value": (
            facets.metadata_method_specific_parameters_measurements_sample_ligands_concentration_value
        ),
        "metadata_method_specific_parameters_measurements_sample_ligands_concentration_value_error_error_level": (
            facets.metadata_method_specific_parameters_measurements_sample_ligands_concentration_value_error_error_level
        ),
        "metadata_method_specific_parameters_measurements_sample_ligands_concentration_value_error_errors_are_relative": (
            facets.metadata_method_specific_parameters_measurements_sample_ligands_concentration_value_error_errors_are_relative
        ),
        "metadata_method_specific_parameters_measurements_sample_ligands_concentration_value_error_lower_error": (
            facets.metadata_method_specific_parameters_measurements_sample_ligands_concentration_value_error_lower_error
        ),
        "metadata_method_specific_parameters_measurements_sample_ligands_concentration_value_error_upper_error": (
            facets.metadata_method_specific_parameters_measurements_sample_ligands_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_id": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_id
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_name
        ),
        "metadata_method_specific_parameters_measurements_sample_ligands_entity__version": (
            facets.metadata_method_specific_parameters_measurements_sample_ligands_entity__version
        ),
        "metadata_method_specific_parameters_measurements_sample_preparation_description": (
            facets.metadata_method_specific_parameters_measurements_sample_preparation_description
        ),
        "metadata_method_specific_parameters_measurements_sample_preparation_name": (
            facets.metadata_method_specific_parameters_measurements_sample_preparation_name
        ),
        "metadata_method_specific_parameters_measurements_sample_targets_concentration_obtained_by": (
            facets.metadata_method_specific_parameters_measurements_sample_targets_concentration_obtained_by
        ),
        "metadata_method_specific_parameters_measurements_sample_targets_concentration_obtained_protocol_description": (
            facets.metadata_method_specific_parameters_measurements_sample_targets_concentration_obtained_protocol_description
        ),
        "metadata_method_specific_parameters_measurements_sample_targets_concentration_obtained_protocol_name": (
            facets.metadata_method_specific_parameters_measurements_sample_targets_concentration_obtained_protocol_name
        ),
        "metadata_method_specific_parameters_measurements_sample_targets_concentration_unit": (
            facets.metadata_method_specific_parameters_measurements_sample_targets_concentration_unit
        ),
        "metadata_method_specific_parameters_measurements_sample_targets_concentration_value": (
            facets.metadata_method_specific_parameters_measurements_sample_targets_concentration_value
        ),
        "metadata_method_specific_parameters_measurements_sample_targets_concentration_value_error_error_level": (
            facets.metadata_method_specific_parameters_measurements_sample_targets_concentration_value_error_error_level
        ),
        "metadata_method_specific_parameters_measurements_sample_targets_concentration_value_error_errors_are_relative": (
            facets.metadata_method_specific_parameters_measurements_sample_targets_concentration_value_error_errors_are_relative
        ),
        "metadata_method_specific_parameters_measurements_sample_targets_concentration_value_error_lower_error": (
            facets.metadata_method_specific_parameters_measurements_sample_targets_concentration_value_error_lower_error
        ),
        "metadata_method_specific_parameters_measurements_sample_targets_concentration_value_error_upper_error": (
            facets.metadata_method_specific_parameters_measurements_sample_targets_concentration_value_error_upper_error
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_id": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_id
        ),
        "metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_name": (
            facets.metadata_general_parameters_chemical_information_entities_of_interest_Complex_substance_of_industrial_production_origin_name
        ),
        "metadata_method_specific_parameters_measurements_sample_targets_entity__version": (
            facets.metadata_method_specific_parameters_measurements_sample_targets_entity__version
        ),
        "metadata_method_specific_parameters_schema_version": (
            facets.metadata_method_specific_parameters_schema_version
        ),
        "metadata_method_specific_parameters_signal_type": (
            facets.metadata_method_specific_parameters_signal_type
        ),
        "updated": facets.updated,
        **getattr(InvenioSearchOptions, "facets", {}),
    }
    sort_options = {
        **InvenioSearchOptions.sort_options,
    }
