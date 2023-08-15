"""Facet definitions."""

from flask_babelex import lazy_gettext as _
from invenio_records_resources.services.records.facets import TermsFacet
from oarepo_runtime.facets.date import DateTimeFacet
from oarepo_runtime.facets.nested_facet import NestedLabeledFacet
from oarepo_vocabularies.services.facets import VocabularyFacet

_schema = TermsFacet(field="$schema", label=_("$schema.label"))

created = DateTimeFacet(field="created", label=_("created.label"))

_id = TermsFacet(field="id", label=_("id.label"))

metadata_general_parameters_associated_publications_additional_authors_affiliations = NestedLabeledFacet(
    path="metadata.general_parameters.associated_publications.additional",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.associated_publications.additional.authors",
        nested_facet=VocabularyFacet(
            field="metadata.general_parameters.associated_publications.additional.authors.affiliations",
            label=_(
                "metadata/general_parameters/associated_publications/additional/authors/affiliations.label"
            ),
            vocabulary="affiliations",
        ),
    ),
)

metadata_general_parameters_associated_publications_additional_authors_family_name = NestedLabeledFacet(
    path="metadata.general_parameters.associated_publications.additional",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.associated_publications.additional.authors",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.associated_publications.additional.authors.family_name",
            label=_(
                "metadata/general_parameters/associated_publications/additional/authors/family_name.label"
            ),
        ),
    ),
)

metadata_general_parameters_associated_publications_additional_authors_given_name = NestedLabeledFacet(
    path="metadata.general_parameters.associated_publications.additional",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.associated_publications.additional.authors",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.associated_publications.additional.authors.given_name",
            label=_(
                "metadata/general_parameters/associated_publications/additional/authors/given_name.label"
            ),
        ),
    ),
)

metadata_general_parameters_associated_publications_additional_authors_identifiers = NestedLabeledFacet(
    path="metadata.general_parameters.associated_publications.additional",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.associated_publications.additional.authors",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.associated_publications.additional.authors.identifiers",
            label=_(
                "metadata/general_parameters/associated_publications/additional/authors/identifiers.label"
            ),
        ),
    ),
)

metadata_general_parameters_associated_publications_additional_pid = NestedLabeledFacet(
    path="metadata.general_parameters.associated_publications.additional",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.associated_publications.additional.pid",
        label=_(
            "metadata/general_parameters/associated_publications/additional/pid.label"
        ),
    ),
)

metadata_general_parameters_associated_publications_additional_publication_year = NestedLabeledFacet(
    path="metadata.general_parameters.associated_publications.additional",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.associated_publications.additional.publication_year",
        label=_(
            "metadata/general_parameters/associated_publications/additional/publication_year.label"
        ),
    ),
)

metadata_general_parameters_associated_publications_additional_publisher = NestedLabeledFacet(
    path="metadata.general_parameters.associated_publications.additional",
    nested_facet=TermsFacet(
        field=(
            "metadata.general_parameters.associated_publications.additional.publisher"
        ),
        label=_(
            "metadata/general_parameters/associated_publications/additional/publisher.label"
        ),
    ),
)

metadata_general_parameters_associated_publications_additional_resource_type = NestedLabeledFacet(
    path="metadata.general_parameters.associated_publications.additional",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.associated_publications.additional.resource_type",
        label=_(
            "metadata/general_parameters/associated_publications/additional/resource_type.label"
        ),
    ),
)

metadata_general_parameters_associated_publications_additional_title = NestedLabeledFacet(
    path="metadata.general_parameters.associated_publications.additional",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.associated_publications.additional.title",
        label=_(
            "metadata/general_parameters/associated_publications/additional/title.label"
        ),
    ),
)

metadata_general_parameters_associated_publications_main_authors_affiliations = NestedLabeledFacet(
    path="metadata.general_parameters.associated_publications.main.authors",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.associated_publications.main.authors.affiliations",
        label=_(
            "metadata/general_parameters/associated_publications/main/authors/affiliations.label"
        ),
        vocabulary="affiliations",
    ),
)

metadata_general_parameters_associated_publications_main_authors_family_name = NestedLabeledFacet(
    path="metadata.general_parameters.associated_publications.main.authors",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.associated_publications.main.authors.family_name",
        label=_(
            "metadata/general_parameters/associated_publications/main/authors/family_name.label"
        ),
    ),
)

metadata_general_parameters_associated_publications_main_authors_given_name = NestedLabeledFacet(
    path="metadata.general_parameters.associated_publications.main.authors",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.associated_publications.main.authors.given_name",
        label=_(
            "metadata/general_parameters/associated_publications/main/authors/given_name.label"
        ),
    ),
)

metadata_general_parameters_associated_publications_main_authors_identifiers = NestedLabeledFacet(
    path="metadata.general_parameters.associated_publications.main.authors",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.associated_publications.main.authors.identifiers",
        label=_(
            "metadata/general_parameters/associated_publications/main/authors/identifiers.label"
        ),
    ),
)

metadata_general_parameters_associated_publications_main_pid = TermsFacet(
    field="metadata.general_parameters.associated_publications.main.pid",
    label=_("metadata/general_parameters/associated_publications/main/pid.label"),
)

metadata_general_parameters_associated_publications_main_publication_year = TermsFacet(
    field="metadata.general_parameters.associated_publications.main.publication_year",
    label=_(
        "metadata/general_parameters/associated_publications/main/publication_year.label"
    ),
)

metadata_general_parameters_associated_publications_main_publisher = TermsFacet(
    field="metadata.general_parameters.associated_publications.main.publisher",
    label=_("metadata/general_parameters/associated_publications/main/publisher.label"),
)

metadata_general_parameters_associated_publications_main_resource_type = TermsFacet(
    field="metadata.general_parameters.associated_publications.main.resource_type",
    label=_(
        "metadata/general_parameters/associated_publications/main/resource_type.label"
    ),
)

metadata_general_parameters_associated_publications_main_title = TermsFacet(
    field="metadata.general_parameters.associated_publications.main.title",
    label=_("metadata/general_parameters/associated_publications/main/title.label"),
)

metadata_general_parameters_chemical_information_chemical_environments_additional_specifications = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.additional_specifications",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/additional_specifications.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_additional_specifications = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.additional_specifications",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/additional_specifications.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.concentration.obtained_by",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/concentration/obtained_by.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_obtained_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.concentration.obtained_protocol.description",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/concentration/obtained_protocol/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_obtained_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.concentration.obtained_protocol.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/concentration/obtained_protocol/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.concentration.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/concentration/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.concentration.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/concentration/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.concentration.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/concentration/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.concentration.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/concentration/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.concentration.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/concentration/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_concentration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.concentration.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/concentration/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_expression_organism = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.expression_organism",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/expression_organism.label"
        ),
        vocabulary="organisms",
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_expression_source_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.expression_source_type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/expression_source_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_external_databases = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.external_databases",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/external_databases.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_biological_postprocessing_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.biological_postprocessing.modification",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/modifications/biological_postprocessing/modification.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_biological_postprocessing_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.biological_postprocessing.position",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/modifications/biological_postprocessing/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_biological_postprocessing_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.biological_postprocessing.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/modifications/biological_postprocessing/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_biological_postprocessing_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.biological_postprocessing.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/modifications/biological_postprocessing/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_chemical_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.chemical.modification",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/modifications/chemical/modification.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_chemical_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.chemical.position",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/modifications/chemical/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_chemical_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.chemical.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/modifications/chemical/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_chemical_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.chemical.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/modifications/chemical/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_synthesis_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.synthesis.modification",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/modifications/synthesis/modification.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_synthesis_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.synthesis.position",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/modifications/synthesis/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_synthesis_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.synthesis.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/modifications/synthesis/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_modifications_synthesis_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.modifications.synthesis.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/modifications/synthesis/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.molecular_weight.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/molecular_weight/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.molecular_weight.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/molecular_weight/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.molecular_weight.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/molecular_weight/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.molecular_weight.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/molecular_weight/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.molecular_weight.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/molecular_weight/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_molecular_weight_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.molecular_weight.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/molecular_weight/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_organism = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.organism",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/organism.label"
        ),
        vocabulary="organisms",
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_polymer_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.polymer_type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/polymer_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_parameter = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.parameter",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/parameter.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_report = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.report",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/report.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.duration.unit",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/duration/unit.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.duration.value",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/duration/value.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.duration.value_error.error_level",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/duration/value_error/error_level.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.duration.value_error.errors_are_relative",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/duration/value_error/errors_are_relative.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.duration.value_error.lower_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/duration/value_error/lower_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_duration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.duration.value_error.upper_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/duration/value_error/upper_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.storage_preparation.description",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/storage_preparation/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.storage_preparation.name",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/storage_preparation/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_controlled = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.temperature.controlled",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/temperature/controlled.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.temperature.obtained_by",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/temperature/obtained_by.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_operational_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.temperature.operational_value",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/temperature/operational_value.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.temperature.unit",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/temperature/unit.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.temperature.value",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/temperature/value.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.temperature.value_error.error_level",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/temperature/value_error/error_level.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.temperature.value_error.errors_are_relative",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/temperature/value_error/errors_are_relative.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.temperature.value_error.lower_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/temperature/value_error/lower_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_storage_until_measurement_temperature_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.storage_until_measurement.temperature.value_error.upper_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/storage_until_measurement/temperature/value_error/upper_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_quality_controls_technique = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.quality_controls.technique",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/quality_controls/technique.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_sequence = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.sequence",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/sequence.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.duration.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/duration/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.duration.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/duration/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.duration.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/duration/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.duration.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/duration/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.duration.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/duration/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_duration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.duration.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/duration/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.storage_preparation.description",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/storage_preparation/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.storage_preparation.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/storage_preparation/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_controlled = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.temperature.controlled",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/temperature/controlled.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.temperature.obtained_by",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/temperature/obtained_by.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_operational_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.temperature.operational_value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/temperature/operational_value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.temperature.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/temperature/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.temperature.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/temperature/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.temperature.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/temperature/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.temperature.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/temperature/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.temperature.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/temperature/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_storage_temperature_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.storage.temperature.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/storage/temperature/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_supplier_catalog_number = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.supplier.catalog_number",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/supplier/catalog_number.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_supplier_further_information = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.supplier.further_information",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/supplier/further_information.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_supplier_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.supplier.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/supplier/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_variant = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.variant",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/variant.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_additional_identifiers = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.additional_identifiers",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/additional_identifiers.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_inchikey = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.inchikey",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/inchikey.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_isotopic_labeling = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.isotopic_labeling",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/isotopic_labeling.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_chemical_modifications_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.chemical_modifications",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.chemical_modifications.modification",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/chemical_modifications/modification.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_chemical_modifications_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.chemical_modifications",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.chemical_modifications.position",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/chemical_modifications/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_chemical_modifications_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.chemical_modifications",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.chemical_modifications.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/chemical_modifications/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_chemical_modifications_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.chemical_modifications",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.chemical_modifications.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/chemical_modifications/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_additional_specifications = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.additional_specifications",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/additional_specifications.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_copy_number = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.copy_number",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/copy_number.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_expression_organism = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.expression_organism",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/expression_organism.label"
        ),
        vocabulary="organisms",
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_expression_source_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.expression_source_type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/expression_source_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_external_databases = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.external_databases",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/external_databases.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_biological_postprocessing_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.biological_postprocessing.modification",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/modifications/biological_postprocessing/modification.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_biological_postprocessing_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.biological_postprocessing.position",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/modifications/biological_postprocessing/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_biological_postprocessing_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.biological_postprocessing.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/modifications/biological_postprocessing/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_biological_postprocessing_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.biological_postprocessing.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/modifications/biological_postprocessing/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_chemical_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.chemical.modification",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/modifications/chemical/modification.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_chemical_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.chemical.position",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/modifications/chemical/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_chemical_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.chemical.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/modifications/chemical/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_chemical_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.chemical.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/modifications/chemical/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_synthesis_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.synthesis.modification",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/modifications/synthesis/modification.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_synthesis_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.synthesis.position",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/modifications/synthesis/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_synthesis_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.synthesis.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/modifications/synthesis/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_modifications_synthesis_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.modifications.synthesis.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/modifications/synthesis/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.molecular_weight.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/molecular_weight/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.molecular_weight.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/molecular_weight/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.molecular_weight.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/molecular_weight/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.molecular_weight.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/molecular_weight/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.molecular_weight.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/molecular_weight/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_molecular_weight_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.molecular_weight.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/molecular_weight/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_organism = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.organism",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/organism.label"
        ),
        vocabulary="organisms",
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_polymer_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.polymer_type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/polymer_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_parameter = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.parameter",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/parameter.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_report = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.report",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/report.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.duration.unit",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/duration/unit.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.duration.value",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/duration/value.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.duration.value_error.error_level",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/duration/value_error/error_level.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.duration.value_error.errors_are_relative",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/duration/value_error/errors_are_relative.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.duration.value_error.lower_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/duration/value_error/lower_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_duration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.duration.value_error.upper_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/duration/value_error/upper_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.storage_preparation.description",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/storage_preparation/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.storage_preparation.name",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/storage_preparation/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_controlled = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.temperature.controlled",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/temperature/controlled.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.temperature.obtained_by",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/temperature/obtained_by.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_operational_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.temperature.operational_value",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/temperature/operational_value.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.temperature.unit",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/temperature/unit.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.temperature.value",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/temperature/value.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.temperature.value_error.error_level",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/temperature/value_error/error_level.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.temperature.value_error.errors_are_relative",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/temperature/value_error/errors_are_relative.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.temperature.value_error.lower_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/temperature/value_error/lower_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.storage_until_measurement.temperature.value_error.upper_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/storage_until_measurement/temperature/value_error/upper_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_quality_controls_technique = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.quality_controls.technique",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/quality_controls/technique.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_sequence = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.sequence",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/sequence.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.duration.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/duration/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.duration.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/duration/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.duration.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/duration/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.duration.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/duration/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.duration.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/duration/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_duration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.duration.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/duration/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.storage_preparation.description",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/storage_preparation/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.storage_preparation.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/storage_preparation/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_controlled = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.temperature.controlled",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/temperature/controlled.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.temperature.obtained_by",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/temperature/obtained_by.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_operational_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.temperature.operational_value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/temperature/operational_value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.temperature.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/temperature/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.temperature.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/temperature/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.temperature.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/temperature/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.temperature.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/temperature/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.temperature.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/temperature/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_storage_temperature_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.storage.temperature.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/storage/temperature/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_supplier_catalog_number = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.supplier.catalog_number",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/supplier/catalog_number.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_supplier_further_information = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.supplier.further_information",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/supplier/further_information.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_supplier_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.supplier.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/supplier/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_variant = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.variant",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/variant.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_additional_identifiers = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.additional_identifiers",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/additional_identifiers.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_inchikey = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.inchikey",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/inchikey.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_components_isotopic_labeling = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.components.isotopic_labeling",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/components/isotopic_labeling.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_preparation_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.preparation_protocol.description",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/preparation_protocol/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_preparation_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.preparation_protocol.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/preparation_protocol/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_derived_from = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.derived_from",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/derived_from.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_fluid = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.fluid",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/fluid.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_health_status = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.health_status",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/health_status.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_cell_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.cell_type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/cell_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_fraction = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.fraction",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/fraction.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_organ = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.organ",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/organ.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_tissue = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.tissue",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/tissue.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_Genetic_material = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.Genetic_material",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/Genetic_material.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_capsid_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.capsid_type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/capsid_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_envelope_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.envelope_type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/envelope_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_host_cell_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.host_cell_type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/host_cell_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_host_organism = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.host_organism",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/host_organism.label"
        ),
        vocabulary="organisms",
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_location_S_N_latitude_ = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.location.S-N(latitude)",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/location/S-N(latitude).label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_location_W_E_longitude_ = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.location.W-E(longitude)",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/location/W-E(longitude).label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_source = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.source",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/source.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_class = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.class",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/class.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_additional_specifications_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.additional_specifications.description",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/additional_specifications/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_additional_specifications_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.additional_specifications.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/additional_specifications/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_additional_specifications = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.additional_specifications",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/additional_specifications.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_copy_number = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.copy_number",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/copy_number.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_expression_organism = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.expression_organism",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/expression_organism.label"
        ),
        vocabulary="organisms",
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_expression_source_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.expression_source_type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/expression_source_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_external_databases = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.external_databases",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/external_databases.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_biological_postprocessing_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.biological_postprocessing.modification",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/modifications/biological_postprocessing/modification.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_biological_postprocessing_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.biological_postprocessing.position",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/modifications/biological_postprocessing/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_biological_postprocessing_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.biological_postprocessing.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/modifications/biological_postprocessing/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_biological_postprocessing_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.biological_postprocessing.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/modifications/biological_postprocessing/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_chemical_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.chemical.modification",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/modifications/chemical/modification.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_chemical_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.chemical.position",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/modifications/chemical/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_chemical_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.chemical.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/modifications/chemical/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_chemical_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.chemical.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/modifications/chemical/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_synthesis_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.synthesis.modification",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/modifications/synthesis/modification.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_synthesis_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.synthesis.position",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/modifications/synthesis/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_synthesis_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.synthesis.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/modifications/synthesis/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_modifications_synthesis_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.modifications.synthesis.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/modifications/synthesis/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.molecular_weight.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/molecular_weight/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.molecular_weight.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/molecular_weight/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.molecular_weight.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/molecular_weight/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.molecular_weight.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/molecular_weight/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.molecular_weight.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/molecular_weight/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_molecular_weight_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.molecular_weight.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/molecular_weight/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_organism = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.organism",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/organism.label"
        ),
        vocabulary="organisms",
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_polymer_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.polymer_type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/polymer_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_parameter = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.parameter",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/parameter.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_report = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.report",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/report.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.duration.unit",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/duration/unit.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.duration.value",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/duration/value.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.duration.value_error.error_level",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/duration/value_error/error_level.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.duration.value_error.errors_are_relative",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/duration/value_error/errors_are_relative.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.duration.value_error.lower_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/duration/value_error/lower_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_duration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.duration.value_error.upper_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/duration/value_error/upper_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.storage_preparation.description",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/storage_preparation/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.storage_preparation.name",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/storage_preparation/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_controlled = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.temperature.controlled",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/temperature/controlled.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.temperature.obtained_by",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/temperature/obtained_by.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_operational_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.temperature.operational_value",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/temperature/operational_value.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.temperature.unit",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/temperature/unit.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.temperature.value",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/temperature/value.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.temperature.value_error.error_level",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/temperature/value_error/error_level.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.temperature.value_error.errors_are_relative",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/temperature/value_error/errors_are_relative.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.temperature.value_error.lower_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/temperature/value_error/lower_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.storage_until_measurement.temperature.value_error.upper_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/storage_until_measurement/temperature/value_error/upper_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_quality_controls_technique = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.quality_controls.technique",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/quality_controls/technique.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_sequence = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.sequence",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/sequence.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.duration.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/duration/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.duration.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/duration/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.duration.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/duration/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.duration.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/duration/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.duration.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/duration/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_duration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.duration.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/duration/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.storage_preparation.description",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/storage_preparation/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.storage_preparation.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/storage_preparation/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_controlled = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.temperature.controlled",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/temperature/controlled.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.temperature.obtained_by",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/temperature/obtained_by.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_operational_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.temperature.operational_value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/temperature/operational_value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.temperature.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/temperature/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.temperature.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/temperature/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.temperature.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/temperature/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.temperature.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/temperature/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.temperature.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/temperature/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_storage_temperature_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.storage.temperature.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/storage/temperature/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_supplier_catalog_number = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.supplier.catalog_number",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/supplier/catalog_number.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_supplier_further_information = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.supplier.further_information",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/supplier/further_information.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_supplier_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.supplier.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/supplier/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_variant = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.variant",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/variant.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_additional_identifiers = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.additional_identifiers",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/additional_identifiers.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_inchikey = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.inchikey",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/inchikey.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_components_isotopic_labeling = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.isotopic_labeling",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/components/isotopic_labeling.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_number_of_mono_layers = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.number_of_mono_layers",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/number_of_mono_layers.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_distribution_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.size.distribution_type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/size/distribution_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_lower = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.size.lower",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/size/lower.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_mean = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.size.mean",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/size/mean.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_median = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.size.median",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/size/median.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.size.type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/size/type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.size.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/size/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_size_upper = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.size.upper",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/size/upper.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_details_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.details.type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/details/type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_constituents_product = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.constituents.product",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/constituents/product.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_degassing_method = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.degassing_method",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/degassing_method.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.dynamic_viscosity.obtained_by",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/dynamic_viscosity/obtained_by.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.dynamic_viscosity.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/dynamic_viscosity/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.dynamic_viscosity.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/dynamic_viscosity/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.dynamic_viscosity.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/dynamic_viscosity/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.dynamic_viscosity.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/dynamic_viscosity/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.dynamic_viscosity.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/dynamic_viscosity/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_dynamic_viscosity_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.dynamic_viscosity.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/dynamic_viscosity/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_id = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field=(
            "metadata.general_parameters.chemical_information.chemical_environments.id"
        ),
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/id.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_ionic_strength_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.ionic_strength.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/ionic_strength/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_ionic_strength_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.ionic_strength.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/ionic_strength/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_pH_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.pH.obtained_by",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/pH/obtained_by.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_pH_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.pH.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/pH/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_pH_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.pH.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/pH/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_pH_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.pH.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/pH/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_pH_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.pH.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/pH/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_pH_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.pH.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/pH/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_additional_identifiers = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.additional_identifiers",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/additional_identifiers.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_additional_specifications = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.additional_specifications",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/additional_specifications.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.concentration.obtained_by",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/concentration/obtained_by.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_obtained_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.concentration.obtained_protocol.description",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/concentration/obtained_protocol/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_obtained_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.concentration.obtained_protocol.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/concentration/obtained_protocol/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.concentration.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/concentration/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.concentration.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/concentration/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.concentration.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/concentration/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.concentration.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/concentration/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.concentration.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/concentration/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_concentration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.concentration.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/concentration/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_inchikey = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.inchikey",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/inchikey.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_isotopic_labeling = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.isotopic_labeling",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/isotopic_labeling.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.molecular_weight.unit",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/molecular_weight/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.molecular_weight.value",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/molecular_weight/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.molecular_weight.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/molecular_weight/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.molecular_weight.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/molecular_weight/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.molecular_weight.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/molecular_weight/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_molecular_weight_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.molecular_weight.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/molecular_weight/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_parameter = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.parameter",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/parameter.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_report = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.report",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/report.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.duration.unit",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/duration/unit.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.duration.value",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/duration/value.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.duration.value_error.error_level",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/duration/value_error/error_level.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.duration.value_error.errors_are_relative",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/duration/value_error/errors_are_relative.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.duration.value_error.lower_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/duration/value_error/lower_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_duration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.duration.value_error.upper_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/duration/value_error/upper_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.storage_preparation.description",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/storage_preparation/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.storage_preparation.name",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/storage_preparation/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_controlled = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.temperature.controlled",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/temperature/controlled.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.temperature.obtained_by",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/temperature/obtained_by.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_operational_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.temperature.operational_value",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/temperature/operational_value.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.temperature.unit",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/temperature/unit.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.temperature.value",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/temperature/value.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.temperature.value_error.error_level",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/temperature/value_error/error_level.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.temperature.value_error.errors_are_relative",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/temperature/value_error/errors_are_relative.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.temperature.value_error.lower_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/temperature/value_error/lower_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_storage_until_measurement_temperature_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.storage_until_measurement.temperature.value_error.upper_error",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/storage_until_measurement/temperature/value_error/upper_error.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_quality_controls_technique = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_information.chemical_environments.solvent.quality_controls.technique",
            label=_(
                "metadata/general_parameters/chemical_information/chemical_environments/solvent/quality_controls/technique.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_supplier_catalog_number = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.supplier.catalog_number",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/supplier/catalog_number.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_supplier_further_information = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.supplier.further_information",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/supplier/further_information.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_supplier_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.supplier.name",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/supplier/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_solvent_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.solvent.type",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/solvent/type.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_ultrafiltration_method_filter_material = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.ultrafiltration_method.filter_material",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/ultrafiltration_method/filter_material.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_chemical_environments_ultrafiltration_method_pore_size = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.chemical_environments.ultrafiltration_method.pore_size",
        label=_(
            "metadata/general_parameters/chemical_information/chemical_environments/ultrafiltration_method/pore_size.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_additional_specifications = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.additional_specifications",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/additional_specifications.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_expression_organism = VocabularyFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.expression_organism",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/expression_organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_chemical_information_entities_of_interest_expression_source_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.expression_source_type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/expression_source_type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_external_databases = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.external_databases",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/external_databases.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_id = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.id",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/id.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_modifications_biological_postprocessing_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.modifications.biological_postprocessing.modification",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/modifications/biological_postprocessing/modification.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_modifications_biological_postprocessing_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.modifications.biological_postprocessing.position",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/modifications/biological_postprocessing/position.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_modifications_biological_postprocessing_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.modifications.biological_postprocessing.protocol.description",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/modifications/biological_postprocessing/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_modifications_biological_postprocessing_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.modifications.biological_postprocessing.protocol.name",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/modifications/biological_postprocessing/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_modifications_chemical_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.modifications.chemical.modification",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/modifications/chemical/modification.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_modifications_chemical_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.modifications.chemical.position",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/modifications/chemical/position.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_modifications_chemical_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.modifications.chemical.protocol.description",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/modifications/chemical/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_modifications_chemical_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.modifications.chemical.protocol.name",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/modifications/chemical/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_modifications_synthesis_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.modifications.synthesis.modification",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/modifications/synthesis/modification.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_modifications_synthesis_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.modifications.synthesis.position",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/modifications/synthesis/position.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_modifications_synthesis_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.modifications.synthesis.protocol.description",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/modifications/synthesis/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_modifications_synthesis_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.modifications.synthesis.protocol.name",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/modifications/synthesis/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_unit = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.molecular_weight.unit",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/molecular_weight/unit.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.molecular_weight.value",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/molecular_weight/value.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.molecular_weight.value_error.error_level",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/molecular_weight/value_error/error_level.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.molecular_weight.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/molecular_weight/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.molecular_weight.value_error.lower_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/molecular_weight/value_error/lower_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_molecular_weight_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.molecular_weight.value_error.upper_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/molecular_weight/value_error/upper_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_name = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.name",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/name.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_organism = VocabularyFacet(
    field=(
        "metadata.general_parameters.chemical_information.entities_of_interest.organism"
    ),
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_chemical_information_entities_of_interest_polymer_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.polymer_type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/polymer_type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_parameter = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.parameter",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/parameter.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_report = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.report",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/report.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.duration.unit",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/duration/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.duration.value",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/duration/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.duration.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/duration/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.duration.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/duration/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.duration.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/duration/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_duration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.duration.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/duration/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.storage_preparation.description",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/storage_preparation/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.storage_preparation.name",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/storage_preparation/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_controlled = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.temperature.controlled",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/temperature/controlled.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.temperature.obtained_by",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/temperature/obtained_by.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_operational_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.temperature.operational_value",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/temperature/operational_value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.temperature.unit",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/temperature/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.temperature.value",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/temperature/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.temperature.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/temperature/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.temperature.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/temperature/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.temperature.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/temperature/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_storage_until_measurement_temperature_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.storage_until_measurement.temperature.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/storage_until_measurement/temperature/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_quality_controls_technique = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.quality_controls.technique",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/quality_controls/technique.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_sequence = TermsFacet(
    field=(
        "metadata.general_parameters.chemical_information.entities_of_interest.sequence"
    ),
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/sequence.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_unit = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.duration.unit",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/duration/unit.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.duration.value",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/duration/value.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.duration.value_error.error_level",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/duration/value_error/error_level.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.duration.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/duration/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.duration.value_error.lower_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/duration/value_error/lower_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_duration_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.duration.value_error.upper_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/duration/value_error/upper_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_storage_preparation_description = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.storage_preparation.description",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/storage_preparation/description.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_storage_preparation_name = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.storage_preparation.name",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/storage_preparation/name.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_controlled = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.temperature.controlled",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/temperature/controlled.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_obtained_by = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.temperature.obtained_by",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/temperature/obtained_by.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_operational_value = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.temperature.operational_value",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/temperature/operational_value.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_unit = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.temperature.unit",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/temperature/unit.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.temperature.value",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/temperature/value.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.temperature.value_error.error_level",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/temperature/value_error/error_level.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.temperature.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/temperature/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.temperature.value_error.lower_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/temperature/value_error/lower_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_storage_temperature_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.storage.temperature.value_error.upper_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/storage/temperature/value_error/upper_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_supplier_catalog_number = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.supplier.catalog_number",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/supplier/catalog_number.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_supplier_further_information = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.supplier.further_information",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/supplier/further_information.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_supplier_name = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.supplier.name",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/supplier/name.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_variant = TermsFacet(
    field=(
        "metadata.general_parameters.chemical_information.entities_of_interest.variant"
    ),
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/variant.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_additional_identifiers = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.additional_identifiers",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/additional_identifiers.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_inchikey = TermsFacet(
    field=(
        "metadata.general_parameters.chemical_information.entities_of_interest.inchikey"
    ),
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/inchikey.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_isotopic_labeling = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.isotopic_labeling",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/isotopic_labeling.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_chemical_modifications_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.chemical_modifications",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.chemical_modifications.modification",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/chemical_modifications/modification.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_chemical_modifications_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.chemical_modifications",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.chemical_modifications.position",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/chemical_modifications/position.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_chemical_modifications_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.chemical_modifications",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.chemical_modifications.protocol.description",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/chemical_modifications/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_chemical_modifications_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.chemical_modifications",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.chemical_modifications.protocol.name",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/chemical_modifications/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_additional_specifications = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.additional_specifications",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/additional_specifications.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_copy_number = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.copy_number",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/copy_number.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_expression_organism = VocabularyFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.expression_organism",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/expression_organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_chemical_information_entities_of_interest_components_expression_source_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.expression_source_type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/expression_source_type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_external_databases = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.external_databases",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/external_databases.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_biological_postprocessing_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.biological_postprocessing.modification",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/modifications/biological_postprocessing/modification.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_biological_postprocessing_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.biological_postprocessing.position",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/modifications/biological_postprocessing/position.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_biological_postprocessing_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.biological_postprocessing.protocol.description",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/modifications/biological_postprocessing/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_biological_postprocessing_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.biological_postprocessing.protocol.name",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/modifications/biological_postprocessing/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_chemical_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.chemical.modification",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/modifications/chemical/modification.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_chemical_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.chemical.position",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/modifications/chemical/position.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_chemical_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.chemical.protocol.description",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/modifications/chemical/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_chemical_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.chemical.protocol.name",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/modifications/chemical/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_synthesis_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.synthesis.modification",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/modifications/synthesis/modification.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_synthesis_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.synthesis.position",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/modifications/synthesis/position.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_synthesis_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.synthesis.protocol.description",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/modifications/synthesis/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_modifications_synthesis_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.modifications.synthesis.protocol.name",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/modifications/synthesis/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_unit = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.molecular_weight.unit",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/molecular_weight/unit.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.molecular_weight.value",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/molecular_weight/value.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.molecular_weight.value_error.error_level",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/molecular_weight/value_error/error_level.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.molecular_weight.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/molecular_weight/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.molecular_weight.value_error.lower_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/molecular_weight/value_error/lower_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_molecular_weight_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.molecular_weight.value_error.upper_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/molecular_weight/value_error/upper_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_name = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.name",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/name.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_organism = VocabularyFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.organism",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_chemical_information_entities_of_interest_components_polymer_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.polymer_type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/polymer_type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_parameter = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.parameter",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/parameter.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_report = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.report",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/report.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.duration.unit",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/duration/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.duration.value",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/duration/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.duration.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/duration/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.duration.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/duration/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.duration.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/duration/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_duration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.duration.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/duration/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.storage_preparation.description",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/storage_preparation/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.storage_preparation.name",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/storage_preparation/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_controlled = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.temperature.controlled",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/temperature/controlled.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.temperature.obtained_by",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/temperature/obtained_by.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_operational_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.temperature.operational_value",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/temperature/operational_value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.temperature.unit",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/temperature/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.temperature.value",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/temperature/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.temperature.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/temperature/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.temperature.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/temperature/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.temperature.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/temperature/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.storage_until_measurement.temperature.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/storage_until_measurement/temperature/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_quality_controls_technique = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.components.quality_controls.technique",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/components/quality_controls/technique.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_sequence = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.sequence",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/sequence.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_unit = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.duration.unit",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/duration/unit.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.duration.value",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/duration/value.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.duration.value_error.error_level",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/duration/value_error/error_level.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.duration.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/duration/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.duration.value_error.lower_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/duration/value_error/lower_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_duration_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.duration.value_error.upper_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/duration/value_error/upper_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_storage_preparation_description = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.storage_preparation.description",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/storage_preparation/description.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_storage_preparation_name = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.storage_preparation.name",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/storage_preparation/name.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_controlled = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.temperature.controlled",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/temperature/controlled.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_obtained_by = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.temperature.obtained_by",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/temperature/obtained_by.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_operational_value = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.temperature.operational_value",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/temperature/operational_value.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_unit = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.temperature.unit",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/temperature/unit.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.temperature.value",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/temperature/value.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.temperature.value_error.error_level",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/temperature/value_error/error_level.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.temperature.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/temperature/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.temperature.value_error.lower_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/temperature/value_error/lower_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_storage_temperature_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.storage.temperature.value_error.upper_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/storage/temperature/value_error/upper_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_supplier_catalog_number = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.supplier.catalog_number",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/supplier/catalog_number.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_supplier_further_information = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.supplier.further_information",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/supplier/further_information.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_supplier_name = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.supplier.name",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/supplier/name.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_variant = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.variant",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/variant.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_additional_identifiers = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.additional_identifiers",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/additional_identifiers.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_inchikey = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.inchikey",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/inchikey.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_components_isotopic_labeling = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.components.isotopic_labeling",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/components/isotopic_labeling.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_preparation_protocol_description = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.preparation_protocol.description",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/preparation_protocol/description.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_preparation_protocol_name = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.preparation_protocol.name",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/preparation_protocol/name.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_derived_from = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.derived_from",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/derived_from.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_fluid = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.fluid",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/fluid.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_health_status = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.health_status",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/health_status.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_cell_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.cell_type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/cell_type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_fraction = TermsFacet(
    field=(
        "metadata.general_parameters.chemical_information.entities_of_interest.fraction"
    ),
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/fraction.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_organ = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.organ",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/organ.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_tissue = TermsFacet(
    field=(
        "metadata.general_parameters.chemical_information.entities_of_interest.tissue"
    ),
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/tissue.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_Genetic_material = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.Genetic_material",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/Genetic_material.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_capsid_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.capsid_type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/capsid_type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_envelope_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.envelope_type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/envelope_type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_host_cell_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.host_cell_type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/host_cell_type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_host_organism = VocabularyFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.host_organism",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/host_organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_chemical_information_entities_of_interest_location_S_N_latitude_ = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.location.S-N(latitude)",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/location/S-N(latitude).label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_location_W_E_longitude_ = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.location.W-E(longitude)",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/location/W-E(longitude).label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_source = TermsFacet(
    field=(
        "metadata.general_parameters.chemical_information.entities_of_interest.source"
    ),
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/source.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_class = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.class",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/class.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_additional_specifications_description = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.additional_specifications.description",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/additional_specifications/description.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_additional_specifications_name = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.additional_specifications.name",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/additional_specifications/name.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_additional_specifications = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.additional_specifications",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/additional_specifications.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_copy_number = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.copy_number",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/copy_number.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_expression_organism = VocabularyFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.expression_organism",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/expression_organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_expression_source_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.expression_source_type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/expression_source_type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_external_databases = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.external_databases",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/external_databases.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_biological_postprocessing_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.biological_postprocessing.modification",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/modifications/biological_postprocessing/modification.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_biological_postprocessing_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.biological_postprocessing.position",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/modifications/biological_postprocessing/position.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_biological_postprocessing_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.biological_postprocessing.protocol.description",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/modifications/biological_postprocessing/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_biological_postprocessing_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.biological_postprocessing.protocol.name",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/modifications/biological_postprocessing/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_chemical_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.chemical.modification",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/modifications/chemical/modification.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_chemical_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.chemical.position",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/modifications/chemical/position.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_chemical_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.chemical.protocol.description",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/modifications/chemical/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_chemical_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.chemical.protocol.name",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/modifications/chemical/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_synthesis_modification = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.synthesis.modification",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/modifications/synthesis/modification.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_synthesis_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.synthesis.position",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/modifications/synthesis/position.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_synthesis_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.synthesis.protocol.description",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/modifications/synthesis/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_modifications_synthesis_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.modifications.synthesis.protocol.name",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/modifications/synthesis/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_unit = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.molecular_weight.unit",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/molecular_weight/unit.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.molecular_weight.value",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/molecular_weight/value.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.molecular_weight.value_error.error_level",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/molecular_weight/value_error/error_level.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.molecular_weight.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/molecular_weight/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.molecular_weight.value_error.lower_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/molecular_weight/value_error/lower_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_molecular_weight_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.molecular_weight.value_error.upper_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/molecular_weight/value_error/upper_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_name = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.name",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/name.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_organism = VocabularyFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.organism",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_polymer_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.polymer_type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/polymer_type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_parameter = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.parameter",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/parameter.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_report = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.report",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/report.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.duration.unit",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/duration/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.duration.value",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/duration/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.duration.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/duration/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.duration.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/duration/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.duration.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/duration/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_duration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.duration.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/duration/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.storage_preparation.description",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/storage_preparation/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.storage_preparation.name",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/storage_preparation/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_controlled = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.temperature.controlled",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/temperature/controlled.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.temperature.obtained_by",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/temperature/obtained_by.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_operational_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.temperature.operational_value",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/temperature/operational_value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.temperature.unit",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/temperature/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.temperature.value",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/temperature/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.temperature.value_error.error_level",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/temperature/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.temperature.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/temperature/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.temperature.value_error.lower_error",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/temperature/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.storage_until_measurement.temperature.value_error.upper_error",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/storage_until_measurement/temperature/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_quality_controls_technique = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.quality_controls.technique",
        label=_(
            "metadata/general_parameters/chemical_information/entities_of_interest/details/components/quality_controls/technique.label"
        ),
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_sequence = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.sequence",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/sequence.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_unit = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.duration.unit",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/duration/unit.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.duration.value",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/duration/value.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.duration.value_error.error_level",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/duration/value_error/error_level.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.duration.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/duration/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.duration.value_error.lower_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/duration/value_error/lower_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_duration_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.duration.value_error.upper_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/duration/value_error/upper_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_storage_preparation_description = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.storage_preparation.description",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/storage_preparation/description.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_storage_preparation_name = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.storage_preparation.name",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/storage_preparation/name.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_controlled = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.temperature.controlled",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/temperature/controlled.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_obtained_by = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.temperature.obtained_by",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/temperature/obtained_by.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_operational_value = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.temperature.operational_value",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/temperature/operational_value.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_unit = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.temperature.unit",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/temperature/unit.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.temperature.value",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/temperature/value.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.temperature.value_error.error_level",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/temperature/value_error/error_level.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.temperature.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/temperature/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.temperature.value_error.lower_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/temperature/value_error/lower_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_storage_temperature_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.storage.temperature.value_error.upper_error",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/storage/temperature/value_error/upper_error.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_supplier_catalog_number = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.supplier.catalog_number",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/supplier/catalog_number.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_supplier_further_information = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.supplier.further_information",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/supplier/further_information.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_supplier_name = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.supplier.name",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/supplier/name.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_variant = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.variant",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/variant.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_additional_identifiers = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.additional_identifiers",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/additional_identifiers.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_inchikey = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.inchikey",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/inchikey.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_components_isotopic_labeling = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.components.isotopic_labeling",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/components/isotopic_labeling.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_number_of_mono_layers = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.number_of_mono_layers",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/number_of_mono_layers.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_size_distribution_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.size.distribution_type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/size/distribution_type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_size_lower = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.size.lower",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/size/lower.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_size_mean = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.size.mean",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/size/mean.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_size_median = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.size.median",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/size/median.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_size_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.size.type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/size/type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_size_unit = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.size.unit",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/size/unit.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_size_upper = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.size.upper",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/size/upper.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_details_type = TermsFacet(
    field="metadata.general_parameters.chemical_information.entities_of_interest.details.type",
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/details/type.label"
    ),
)

metadata_general_parameters_chemical_information_entities_of_interest_product = TermsFacet(
    field=(
        "metadata.general_parameters.chemical_information.entities_of_interest.product"
    ),
    label=_(
        "metadata/general_parameters/chemical_information/entities_of_interest/product.label"
    ),
)

metadata_general_parameters_collection_start_time = DateTimeFacet(
    field="metadata.general_parameters.collection_start_time",
    label=_("metadata/general_parameters/collection_start_time.label"),
)

metadata_general_parameters_depositors_contributors_affiliations = NestedLabeledFacet(
    path="metadata.general_parameters.depositors.contributors",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.depositors.contributors.affiliations",
        label=_(
            "metadata/general_parameters/depositors/contributors/affiliations.label"
        ),
        vocabulary="affiliations",
    ),
)

metadata_general_parameters_depositors_contributors_family_name = NestedLabeledFacet(
    path="metadata.general_parameters.depositors.contributors",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.depositors.contributors.family_name",
        label=_(
            "metadata/general_parameters/depositors/contributors/family_name.label"
        ),
    ),
)

metadata_general_parameters_depositors_contributors_given_name = NestedLabeledFacet(
    path="metadata.general_parameters.depositors.contributors",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.depositors.contributors.given_name",
        label=_("metadata/general_parameters/depositors/contributors/given_name.label"),
    ),
)

metadata_general_parameters_depositors_contributors_identifiers = NestedLabeledFacet(
    path="metadata.general_parameters.depositors.contributors",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.depositors.contributors.identifiers",
        label=_(
            "metadata/general_parameters/depositors/contributors/identifiers.label"
        ),
    ),
)

metadata_general_parameters_depositors_depositor_affiliations = VocabularyFacet(
    field="metadata.general_parameters.depositors.depositor.affiliations",
    label=_("metadata/general_parameters/depositors/depositor/affiliations.label"),
    vocabulary="affiliations",
)

metadata_general_parameters_depositors_depositor_family_name = TermsFacet(
    field="metadata.general_parameters.depositors.depositor.family_name",
    label=_("metadata/general_parameters/depositors/depositor/family_name.label"),
)

metadata_general_parameters_depositors_depositor_given_name = TermsFacet(
    field="metadata.general_parameters.depositors.depositor.given_name",
    label=_("metadata/general_parameters/depositors/depositor/given_name.label"),
)

metadata_general_parameters_depositors_depositor_identifiers = TermsFacet(
    field="metadata.general_parameters.depositors.depositor.identifiers",
    label=_("metadata/general_parameters/depositors/depositor/identifiers.label"),
)

metadata_general_parameters_depositors_principal_contact_affiliations = VocabularyFacet(
    field="metadata.general_parameters.depositors.principal_contact.affiliations",
    label=_(
        "metadata/general_parameters/depositors/principal_contact/affiliations.label"
    ),
    vocabulary="affiliations",
)

metadata_general_parameters_depositors_principal_contact_family_name = TermsFacet(
    field="metadata.general_parameters.depositors.principal_contact.family_name",
    label=_(
        "metadata/general_parameters/depositors/principal_contact/family_name.label"
    ),
)

metadata_general_parameters_depositors_principal_contact_given_name = TermsFacet(
    field="metadata.general_parameters.depositors.principal_contact.given_name",
    label=_(
        "metadata/general_parameters/depositors/principal_contact/given_name.label"
    ),
)

metadata_general_parameters_depositors_principal_contact_identifiers = TermsFacet(
    field="metadata.general_parameters.depositors.principal_contact.identifiers",
    label=_(
        "metadata/general_parameters/depositors/principal_contact/identifiers.label"
    ),
)

metadata_general_parameters_derived_parameters_entities_involved_copy_number = NestedLabeledFacet(
    path="metadata.general_parameters.derived_parameters",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.derived_parameters.entities_involved",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.derived_parameters.entities_involved.copy_number",
            label=_(
                "metadata/general_parameters/derived_parameters/entities_involved/copy_number.label"
            ),
        ),
    ),
)

metadata_general_parameters_derived_parameters_entities_involved_entity__version = NestedLabeledFacet(
    path="metadata.general_parameters.derived_parameters",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.derived_parameters.entities_involved",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.derived_parameters.entities_involved.entity.@v",
            label=_(
                "metadata/general_parameters/derived_parameters/entities_involved/entity/@v.label"
            ),
        ),
    ),
)

metadata_general_parameters_derived_parameters_id = NestedLabeledFacet(
    path="metadata.general_parameters.derived_parameters",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.derived_parameters.id",
        label=_("metadata/general_parameters/derived_parameters/id.label"),
    ),
)

metadata_general_parameters_derived_parameters_name = NestedLabeledFacet(
    path="metadata.general_parameters.derived_parameters",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.derived_parameters.name",
        label=_("metadata/general_parameters/derived_parameters/name.label"),
    ),
)

metadata_general_parameters_derived_parameters_type = NestedLabeledFacet(
    path="metadata.general_parameters.derived_parameters",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.derived_parameters.type",
        label=_("metadata/general_parameters/derived_parameters/type.label"),
    ),
)

metadata_general_parameters_derived_parameters_unit = NestedLabeledFacet(
    path="metadata.general_parameters.derived_parameters",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.derived_parameters.unit",
        label=_("metadata/general_parameters/derived_parameters/unit.label"),
    ),
)

metadata_general_parameters_derived_parameters_value = NestedLabeledFacet(
    path="metadata.general_parameters.derived_parameters",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.derived_parameters.value",
        label=_("metadata/general_parameters/derived_parameters/value.label"),
    ),
)

metadata_general_parameters_derived_parameters_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.derived_parameters",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.derived_parameters.value_error.error_level",
        label=_(
            "metadata/general_parameters/derived_parameters/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_derived_parameters_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.derived_parameters",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.derived_parameters.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/derived_parameters/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_derived_parameters_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.derived_parameters",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.derived_parameters.value_error.lower_error",
        label=_(
            "metadata/general_parameters/derived_parameters/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_derived_parameters_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.derived_parameters",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.derived_parameters.value_error.upper_error",
        label=_(
            "metadata/general_parameters/derived_parameters/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_funding_reference = VocabularyFacet(
    field="metadata.general_parameters.funding_reference",
    label=_("metadata/general_parameters/funding_reference.label"),
    vocabulary="grants",
)

metadata_general_parameters_instrument_manufacturer = TermsFacet(
    field="metadata.general_parameters.instrument.manufacturer",
    label=_("metadata/general_parameters/instrument/manufacturer.label"),
)

metadata_general_parameters_instrument_model = TermsFacet(
    field="metadata.general_parameters.instrument.model",
    label=_("metadata/general_parameters/instrument/model.label"),
)

metadata_general_parameters_instrument_name = TermsFacet(
    field="metadata.general_parameters.instrument.name",
    label=_("metadata/general_parameters/instrument/name.label"),
)

metadata_general_parameters_instrument_performance_test_additional_information = TermsFacet(
    field=(
        "metadata.general_parameters.instrument.performance_test.additional_information"
    ),
    label=_(
        "metadata/general_parameters/instrument/performance_test/additional_information.label"
    ),
)

metadata_general_parameters_instrument_performance_test_published_test_protocol_authors_affiliations = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.published_test_protocol.authors",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.instrument.performance_test.published_test_protocol.authors.affiliations",
        label=_(
            "metadata/general_parameters/instrument/performance_test/published_test_protocol/authors/affiliations.label"
        ),
        vocabulary="affiliations",
    ),
)

metadata_general_parameters_instrument_performance_test_published_test_protocol_authors_family_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.published_test_protocol.authors",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.published_test_protocol.authors.family_name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/published_test_protocol/authors/family_name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_published_test_protocol_authors_given_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.published_test_protocol.authors",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.published_test_protocol.authors.given_name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/published_test_protocol/authors/given_name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_published_test_protocol_authors_identifiers = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.published_test_protocol.authors",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.published_test_protocol.authors.identifiers",
        label=_(
            "metadata/general_parameters/instrument/performance_test/published_test_protocol/authors/identifiers.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_published_test_protocol_pid = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.published_test_protocol.pid",
    label=_(
        "metadata/general_parameters/instrument/performance_test/published_test_protocol/pid.label"
    ),
)

metadata_general_parameters_instrument_performance_test_published_test_protocol_publication_year = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.published_test_protocol.publication_year",
    label=_(
        "metadata/general_parameters/instrument/performance_test/published_test_protocol/publication_year.label"
    ),
)

metadata_general_parameters_instrument_performance_test_published_test_protocol_publisher = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.published_test_protocol.publisher",
    label=_(
        "metadata/general_parameters/instrument/performance_test/published_test_protocol/publisher.label"
    ),
)

metadata_general_parameters_instrument_performance_test_published_test_protocol_resource_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.published_test_protocol.resource_type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/published_test_protocol/resource_type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_published_test_protocol_title = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.published_test_protocol.title",
    label=_(
        "metadata/general_parameters/instrument/performance_test/published_test_protocol/title.label"
    ),
)

metadata_general_parameters_instrument_performance_test_report = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.report",
    label=_("metadata/general_parameters/instrument/performance_test/report.label"),
)

metadata_general_parameters_instrument_performance_test_sample_composition_additional_specifications = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.additional_specifications",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/additional_specifications.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_concentration_obtained_by = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.concentration.obtained_by",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/concentration/obtained_by.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_concentration_obtained_protocol_description = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.concentration.obtained_protocol.description",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/concentration/obtained_protocol/description.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_concentration_obtained_protocol_name = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.concentration.obtained_protocol.name",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/concentration/obtained_protocol/name.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_concentration_unit = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.concentration.unit",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/concentration/unit.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.concentration.value",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/concentration/value.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.concentration.value_error.error_level",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/concentration/value_error/error_level.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.concentration.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/concentration/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.concentration.value_error.lower_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/concentration/value_error/lower_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_concentration_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.concentration.value_error.upper_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/concentration/value_error/upper_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_expression_organism = VocabularyFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.expression_organism",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/expression_organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_instrument_performance_test_sample_composition_expression_source_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.expression_source_type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/expression_source_type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_external_databases = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.external_databases",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/external_databases.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_modifications_biological_postprocessing_modification = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.biological_postprocessing.modification",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/modifications/biological_postprocessing/modification.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_modifications_biological_postprocessing_position = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.biological_postprocessing.position",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/modifications/biological_postprocessing/position.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_modifications_biological_postprocessing_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.biological_postprocessing.protocol.description",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/modifications/biological_postprocessing/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_modifications_biological_postprocessing_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.biological_postprocessing.protocol.name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/modifications/biological_postprocessing/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_modifications_chemical_modification = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.chemical.modification",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/modifications/chemical/modification.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_modifications_chemical_position = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.chemical.position",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/modifications/chemical/position.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_modifications_chemical_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.chemical.protocol.description",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/modifications/chemical/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_modifications_chemical_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.chemical.protocol.name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/modifications/chemical/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_modifications_synthesis_modification = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.synthesis.modification",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/modifications/synthesis/modification.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_modifications_synthesis_position = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.synthesis.position",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/modifications/synthesis/position.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_modifications_synthesis_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.synthesis.protocol.description",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/modifications/synthesis/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_modifications_synthesis_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.modifications.synthesis.protocol.name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/modifications/synthesis/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_unit = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.molecular_weight.unit",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/molecular_weight/unit.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.molecular_weight.value",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/molecular_weight/value.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.molecular_weight.value_error.error_level",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/molecular_weight/value_error/error_level.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.molecular_weight.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/molecular_weight/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.molecular_weight.value_error.lower_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/molecular_weight/value_error/lower_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_molecular_weight_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.molecular_weight.value_error.upper_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/molecular_weight/value_error/upper_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_name = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.name",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/name.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_organism = VocabularyFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.organism",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_instrument_performance_test_sample_composition_polymer_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.polymer_type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/polymer_type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_parameter = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.parameter",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/parameter.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_report = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.report",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/report.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.duration.unit",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/duration/unit.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.duration.value",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/duration/value.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.duration.value_error.error_level",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/duration/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.duration.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/duration/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.duration.value_error.lower_error",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/duration/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_duration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.duration.value_error.upper_error",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/duration/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.storage_preparation.description",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/storage_preparation/description.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.storage_preparation.name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/storage_preparation/name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_controlled = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.temperature.controlled",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/temperature/controlled.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.temperature.obtained_by",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/temperature/obtained_by.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_operational_value = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.temperature.operational_value",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/temperature/operational_value.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.temperature.unit",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/temperature/unit.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.temperature.value",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/temperature/value.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.temperature.value_error.error_level",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/temperature/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.temperature.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/temperature/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.temperature.value_error.lower_error",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/temperature/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_storage_until_measurement_temperature_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.storage_until_measurement.temperature.value_error.upper_error",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/storage_until_measurement/temperature/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_quality_controls_technique = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.quality_controls.technique",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/quality_controls/technique.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_sequence = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.sequence",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/sequence.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_unit = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.duration.unit",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/duration/unit.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.duration.value",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/duration/value.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.duration.value_error.error_level",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/duration/value_error/error_level.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.duration.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/duration/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.duration.value_error.lower_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/duration/value_error/lower_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_duration_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.duration.value_error.upper_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/duration/value_error/upper_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_storage_preparation_description = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.storage_preparation.description",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/storage_preparation/description.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_storage_preparation_name = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.storage_preparation.name",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/storage_preparation/name.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_controlled = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.temperature.controlled",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/temperature/controlled.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_obtained_by = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.temperature.obtained_by",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/temperature/obtained_by.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_operational_value = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.temperature.operational_value",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/temperature/operational_value.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_unit = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.temperature.unit",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/temperature/unit.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.temperature.value",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/temperature/value.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.temperature.value_error.error_level",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/temperature/value_error/error_level.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.temperature.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/temperature/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.temperature.value_error.lower_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/temperature/value_error/lower_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_storage_temperature_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.storage.temperature.value_error.upper_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/storage/temperature/value_error/upper_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_supplier_catalog_number = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.supplier.catalog_number",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/supplier/catalog_number.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_supplier_further_information = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.supplier.further_information",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/supplier/further_information.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_supplier_name = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.supplier.name",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/supplier/name.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_variant = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.variant",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/variant.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_additional_identifiers = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.additional_identifiers",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/additional_identifiers.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_inchikey = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.inchikey",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/inchikey.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_isotopic_labeling = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.isotopic_labeling",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/isotopic_labeling.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_chemical_modifications_modification = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.chemical_modifications",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.chemical_modifications.modification",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/chemical_modifications/modification.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_chemical_modifications_position = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.chemical_modifications",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.chemical_modifications.position",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/chemical_modifications/position.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_chemical_modifications_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.chemical_modifications",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.chemical_modifications.protocol.description",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/chemical_modifications/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_chemical_modifications_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.chemical_modifications",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.chemical_modifications.protocol.name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/chemical_modifications/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_additional_specifications = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.additional_specifications",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/additional_specifications.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_copy_number = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.copy_number",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/copy_number.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_expression_organism = VocabularyFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.expression_organism",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/expression_organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_expression_source_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.expression_source_type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/expression_source_type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_external_databases = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.external_databases",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/external_databases.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_biological_postprocessing_modification = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.biological_postprocessing.modification",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/modifications/biological_postprocessing/modification.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_biological_postprocessing_position = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.biological_postprocessing.position",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/modifications/biological_postprocessing/position.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_biological_postprocessing_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.biological_postprocessing.protocol.description",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/modifications/biological_postprocessing/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_biological_postprocessing_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.biological_postprocessing.protocol.name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/modifications/biological_postprocessing/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_chemical_modification = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.chemical.modification",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/modifications/chemical/modification.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_chemical_position = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.chemical.position",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/modifications/chemical/position.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_chemical_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.chemical.protocol.description",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/modifications/chemical/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_chemical_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.chemical.protocol.name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/modifications/chemical/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_synthesis_modification = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.synthesis.modification",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/modifications/synthesis/modification.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_synthesis_position = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.synthesis.position",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/modifications/synthesis/position.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_synthesis_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.synthesis.protocol.description",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/modifications/synthesis/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_modifications_synthesis_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.modifications.synthesis.protocol.name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/modifications/synthesis/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_unit = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.molecular_weight.unit",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/molecular_weight/unit.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.molecular_weight.value",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/molecular_weight/value.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.molecular_weight.value_error.error_level",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/molecular_weight/value_error/error_level.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.molecular_weight.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/molecular_weight/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.molecular_weight.value_error.lower_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/molecular_weight/value_error/lower_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_molecular_weight_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.molecular_weight.value_error.upper_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/molecular_weight/value_error/upper_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_name = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.name",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/name.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_organism = VocabularyFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.organism",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_polymer_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.polymer_type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/polymer_type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_parameter = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.parameter",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/parameter.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_report = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.report",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/report.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.duration.unit",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/duration/unit.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.duration.value",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/duration/value.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.duration.value_error.error_level",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/duration/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.duration.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/duration/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.duration.value_error.lower_error",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/duration/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_duration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.duration.value_error.upper_error",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/duration/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.storage_preparation.description",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/storage_preparation/description.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.storage_preparation.name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/storage_preparation/name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_controlled = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.temperature.controlled",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/temperature/controlled.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.temperature.obtained_by",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/temperature/obtained_by.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_operational_value = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.temperature.operational_value",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/temperature/operational_value.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.temperature.unit",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/temperature/unit.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.temperature.value",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/temperature/value.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.temperature.value_error.error_level",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/temperature/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.temperature.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/temperature/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.temperature.value_error.lower_error",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/temperature/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.storage_until_measurement.temperature.value_error.upper_error",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/storage_until_measurement/temperature/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_quality_controls_technique = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.components.quality_controls.technique",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/components/quality_controls/technique.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_sequence = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.sequence",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/sequence.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_unit = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.duration.unit",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/duration/unit.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.duration.value",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/duration/value.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.duration.value_error.error_level",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/duration/value_error/error_level.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.duration.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/duration/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.duration.value_error.lower_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/duration/value_error/lower_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_duration_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.duration.value_error.upper_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/duration/value_error/upper_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_storage_preparation_description = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.storage_preparation.description",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/storage_preparation/description.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_storage_preparation_name = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.storage_preparation.name",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/storage_preparation/name.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_controlled = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.temperature.controlled",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/temperature/controlled.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_obtained_by = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.temperature.obtained_by",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/temperature/obtained_by.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_operational_value = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.temperature.operational_value",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/temperature/operational_value.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_unit = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.temperature.unit",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/temperature/unit.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.temperature.value",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/temperature/value.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.temperature.value_error.error_level",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/temperature/value_error/error_level.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.temperature.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/temperature/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.temperature.value_error.lower_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/temperature/value_error/lower_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_storage_temperature_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.storage.temperature.value_error.upper_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/storage/temperature/value_error/upper_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_supplier_catalog_number = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.supplier.catalog_number",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/supplier/catalog_number.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_supplier_further_information = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.supplier.further_information",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/supplier/further_information.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_supplier_name = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.supplier.name",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/supplier/name.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_variant = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.variant",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/variant.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_additional_identifiers = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.additional_identifiers",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/additional_identifiers.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_inchikey = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.inchikey",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/inchikey.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_components_isotopic_labeling = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.components.isotopic_labeling",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/components/isotopic_labeling.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_preparation_protocol_description = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.preparation_protocol.description",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/preparation_protocol/description.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_preparation_protocol_name = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.preparation_protocol.name",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/preparation_protocol/name.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_derived_from = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.derived_from",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/derived_from.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_fluid = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.fluid",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/fluid.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_health_status = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.health_status",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/health_status.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_cell_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.cell_type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/cell_type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_fraction = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.fraction",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/fraction.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_organ = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.organ",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/organ.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_tissue = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.tissue",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/tissue.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_Genetic_material = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.Genetic_material",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/Genetic_material.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_capsid_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.capsid_type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/capsid_type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_envelope_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.envelope_type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/envelope_type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_host_cell_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.host_cell_type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/host_cell_type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_host_organism = VocabularyFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.host_organism",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/host_organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_instrument_performance_test_sample_composition_location_S_N_latitude_ = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.location.S-N(latitude)",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/location/S-N(latitude).label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_location_W_E_longitude_ = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.location.W-E(longitude)",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/location/W-E(longitude).label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_source = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.source",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/source.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_class = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.class",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/class.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_additional_specifications_description = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.additional_specifications.description",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/additional_specifications/description.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_additional_specifications_name = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.additional_specifications.name",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/additional_specifications/name.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_additional_specifications = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.additional_specifications",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/additional_specifications.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_copy_number = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.copy_number",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/copy_number.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_expression_organism = VocabularyFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.expression_organism",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/expression_organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_expression_source_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.expression_source_type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/expression_source_type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_external_databases = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.external_databases",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/external_databases.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_biological_postprocessing_modification = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.biological_postprocessing.modification",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/modifications/biological_postprocessing/modification.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_biological_postprocessing_position = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.biological_postprocessing.position",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/modifications/biological_postprocessing/position.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_biological_postprocessing_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.biological_postprocessing.protocol.description",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/modifications/biological_postprocessing/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_biological_postprocessing_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.biological_postprocessing.protocol.name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/modifications/biological_postprocessing/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_chemical_modification = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.chemical.modification",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/modifications/chemical/modification.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_chemical_position = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.chemical.position",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/modifications/chemical/position.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_chemical_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.chemical.protocol.description",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/modifications/chemical/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_chemical_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.chemical.protocol.name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/modifications/chemical/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_synthesis_modification = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.synthesis.modification",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/modifications/synthesis/modification.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_synthesis_position = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.synthesis.position",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/modifications/synthesis/position.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_synthesis_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.synthesis.protocol.description",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/modifications/synthesis/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_modifications_synthesis_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.modifications.synthesis.protocol.name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/modifications/synthesis/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_unit = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.molecular_weight.unit",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/molecular_weight/unit.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.molecular_weight.value",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/molecular_weight/value.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.molecular_weight.value_error.error_level",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/molecular_weight/value_error/error_level.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.molecular_weight.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/molecular_weight/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.molecular_weight.value_error.lower_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/molecular_weight/value_error/lower_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_molecular_weight_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.molecular_weight.value_error.upper_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/molecular_weight/value_error/upper_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_name = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.name",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/name.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_organism = VocabularyFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.organism",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_polymer_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.polymer_type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/polymer_type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_parameter = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.parameter",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/parameter.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_report = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.report",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/report.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.duration.unit",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/duration/unit.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.duration.value",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/duration/value.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.duration.value_error.error_level",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/duration/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.duration.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/duration/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.duration.value_error.lower_error",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/duration/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_duration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.duration.value_error.upper_error",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/duration/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.storage_preparation.description",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/storage_preparation/description.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.storage_preparation.name",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/storage_preparation/name.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_controlled = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.temperature.controlled",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/temperature/controlled.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.temperature.obtained_by",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/temperature/obtained_by.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_operational_value = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.temperature.operational_value",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/temperature/operational_value.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.temperature.unit",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/temperature/unit.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.temperature.value",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/temperature/value.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.temperature.value_error.error_level",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/temperature/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.temperature.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/temperature/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.temperature.value_error.lower_error",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/temperature/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_storage_until_measurement_temperature_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.storage_until_measurement.temperature.value_error.upper_error",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/storage_until_measurement/temperature/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_quality_controls_technique = NestedLabeledFacet(
    path="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.quality_controls.technique",
        label=_(
            "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/quality_controls/technique.label"
        ),
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_sequence = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.sequence",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/sequence.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_unit = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.duration.unit",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/duration/unit.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.duration.value",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/duration/value.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.duration.value_error.error_level",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/duration/value_error/error_level.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.duration.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/duration/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.duration.value_error.lower_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/duration/value_error/lower_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_duration_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.duration.value_error.upper_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/duration/value_error/upper_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_storage_preparation_description = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.storage_preparation.description",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/storage_preparation/description.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_storage_preparation_name = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.storage_preparation.name",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/storage_preparation/name.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_controlled = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.temperature.controlled",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/temperature/controlled.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_obtained_by = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.temperature.obtained_by",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/temperature/obtained_by.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_operational_value = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.temperature.operational_value",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/temperature/operational_value.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_unit = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.temperature.unit",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/temperature/unit.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.temperature.value",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/temperature/value.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.temperature.value_error.error_level",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/temperature/value_error/error_level.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.temperature.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/temperature/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.temperature.value_error.lower_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/temperature/value_error/lower_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_storage_temperature_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.storage.temperature.value_error.upper_error",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/storage/temperature/value_error/upper_error.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_supplier_catalog_number = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.supplier.catalog_number",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/supplier/catalog_number.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_supplier_further_information = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.supplier.further_information",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/supplier/further_information.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_supplier_name = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.supplier.name",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/supplier/name.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_variant = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.variant",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/variant.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_additional_identifiers = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.additional_identifiers",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/additional_identifiers.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_inchikey = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.inchikey",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/inchikey.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_components_isotopic_labeling = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.components.isotopic_labeling",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/components/isotopic_labeling.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_number_of_mono_layers = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.number_of_mono_layers",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/number_of_mono_layers.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_size_distribution_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.size.distribution_type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/size/distribution_type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_size_lower = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.size.lower",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/size/lower.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_size_mean = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.size.mean",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/size/mean.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_size_median = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.size.median",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/size/median.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_size_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.size.type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/size/type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_size_unit = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.size.unit",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/size/unit.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_size_upper = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.size.upper",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/size/upper.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_details_type = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.details.type",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/details/type.label"
    ),
)

metadata_general_parameters_instrument_performance_test_sample_composition_product = TermsFacet(
    field="metadata.general_parameters.instrument.performance_test.sample_composition.product",
    label=_(
        "metadata/general_parameters/instrument/performance_test/sample_composition/product.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_additional_identifiers = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.additional_identifiers",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/additional_identifiers.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_additional_specifications = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.additional_specifications",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/additional_specifications.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_obtained_by = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.concentration.obtained_by",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/concentration/obtained_by.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_obtained_protocol_description = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.concentration.obtained_protocol.description",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/concentration/obtained_protocol/description.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_obtained_protocol_name = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.concentration.obtained_protocol.name",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/concentration/obtained_protocol/name.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_unit = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.concentration.unit",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/concentration/unit.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.concentration.value",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/concentration/value.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.concentration.value_error.error_level",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/concentration/value_error/error_level.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.concentration.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/concentration/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.concentration.value_error.lower_error",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/concentration/value_error/lower_error.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_concentration_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.concentration.value_error.upper_error",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/concentration/value_error/upper_error.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_inchikey = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.inchikey",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/inchikey.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_isotopic_labeling = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.isotopic_labeling",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/isotopic_labeling.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_unit = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.molecular_weight.unit",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/molecular_weight/unit.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.molecular_weight.value",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/molecular_weight/value.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.molecular_weight.value_error.error_level",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/molecular_weight/value_error/error_level.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.molecular_weight.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/molecular_weight/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.molecular_weight.value_error.lower_error",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/molecular_weight/value_error/lower_error.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_molecular_weight_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.molecular_weight.value_error.upper_error",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/molecular_weight/value_error/upper_error.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_name = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.name",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/name.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_parameter = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.parameter",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/parameter.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_report = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.report",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/report.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.duration.unit",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/duration/unit.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.duration.value",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/duration/value.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.duration.value_error.error_level",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/duration/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.duration.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/duration/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.duration.value_error.lower_error",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/duration/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_duration_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.duration.value_error.upper_error",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/duration/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.storage_preparation.description",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/storage_preparation/description.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.storage_preparation.name",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/storage_preparation/name.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_controlled = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.temperature.controlled",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/temperature/controlled.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_obtained_by = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.temperature.obtained_by",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/temperature/obtained_by.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_operational_value = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.temperature.operational_value",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/temperature/operational_value.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.temperature.unit",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/temperature/unit.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.temperature.value",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/temperature/value.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value_error_error_level = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.temperature.value_error.error_level",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/temperature/value_error/error_level.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value_error_errors_are_relative = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.temperature.value_error.errors_are_relative",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/temperature/value_error/errors_are_relative.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value_error_lower_error = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.temperature.value_error.lower_error",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/temperature/value_error/lower_error.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_storage_until_measurement_temperature_value_error_upper_error = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.storage_until_measurement.temperature.value_error.upper_error",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/storage_until_measurement/temperature/value_error/upper_error.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_quality_controls_technique = NestedLabeledFacet(
    path="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.quality_controls.technique",
        label=_(
            "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/quality_controls/technique.label"
        ),
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_supplier_catalog_number = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.supplier.catalog_number",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/supplier/catalog_number.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_supplier_further_information = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.supplier.further_information",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/supplier/further_information.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_supplier_name = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.supplier.name",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/supplier/name.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_atmosphere_composition_type = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.atmosphere.composition.type",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/atmosphere/composition/type.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_humidity_controlled = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.humidity.controlled",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/humidity/controlled.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_humidity_obtained_by = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.humidity.obtained_by",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/humidity/obtained_by.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_humidity_unit = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.humidity.unit",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/humidity/unit.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.humidity.value",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/humidity/value.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.humidity.value_error.error_level",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/humidity/value_error/error_level.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.humidity.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/humidity/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.humidity.value_error.lower_error",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/humidity/value_error/lower_error.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_humidity_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.humidity.value_error.upper_error",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/humidity/value_error/upper_error.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_pressure_controlled = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.pressure.controlled",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/pressure/controlled.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_pressure_obtained_by = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.pressure.obtained_by",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/pressure/obtained_by.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_pressure_unit = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.pressure.unit",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/pressure/unit.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.pressure.value",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/pressure/value.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.pressure.value_error.error_level",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/pressure/value_error/error_level.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.pressure.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/pressure/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.pressure.value_error.lower_error",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/pressure/value_error/lower_error.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_pressure_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.pressure.value_error.upper_error",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/pressure/value_error/upper_error.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_temperature_controlled = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.temperature.controlled",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/temperature/controlled.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_temperature_obtained_by = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.temperature.obtained_by",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/temperature/obtained_by.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_temperature_operational_value = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.temperature.operational_value",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/temperature/operational_value.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_temperature_unit = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.temperature.unit",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/temperature/unit.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.temperature.value",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/temperature/value.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value_error_error_level = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.temperature.value_error.error_level",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/temperature/value_error/error_level.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value_error_errors_are_relative = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.temperature.value_error.errors_are_relative",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/temperature/value_error/errors_are_relative.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value_error_lower_error = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.temperature.value_error.lower_error",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/temperature/value_error/lower_error.label"
    ),
)

metadata_general_parameters_physical_conditions_at_sample_handling_temperature_value_error_upper_error = TermsFacet(
    field="metadata.general_parameters.physical_conditions_at_sample_handling.temperature.value_error.upper_error",
    label=_(
        "metadata/general_parameters/physical_conditions_at_sample_handling/temperature/value_error/upper_error.label"
    ),
)

metadata_general_parameters_record_information_access_rights = TermsFacet(
    field="metadata.general_parameters.record_information.access_rights",
    label=_("metadata/general_parameters/record_information/access_rights.label"),
)

metadata_general_parameters_record_information_date_available = DateTimeFacet(
    field="metadata.general_parameters.record_information.date_available",
    label=_("metadata/general_parameters/record_information/date_available.label"),
)

metadata_general_parameters_record_information_deposition_date = DateTimeFacet(
    field="metadata.general_parameters.record_information.deposition_date",
    label=_("metadata/general_parameters/record_information/deposition_date.label"),
)

metadata_general_parameters_record_information_identifier = TermsFacet(
    field="metadata.general_parameters.record_information.identifier",
    label=_("metadata/general_parameters/record_information/identifier.label"),
)

metadata_general_parameters_record_information_internal_id = TermsFacet(
    field="metadata.general_parameters.record_information.internal_id",
    label=_("metadata/general_parameters/record_information/internal_id.label"),
)

metadata_general_parameters_record_information_keywords = TermsFacet(
    field="metadata.general_parameters.record_information.keywords",
    label=_("metadata/general_parameters/record_information/keywords.label"),
)

metadata_general_parameters_record_information_measurement_group_id = TermsFacet(
    field="metadata.general_parameters.record_information.measurement_group_id",
    label=_(
        "metadata/general_parameters/record_information/measurement_group_id.label"
    ),
)

metadata_general_parameters_record_information_metadata_access_rights = TermsFacet(
    field="metadata.general_parameters.record_information.metadata_access_rights",
    label=_(
        "metadata/general_parameters/record_information/metadata_access_rights.label"
    ),
)

metadata_general_parameters_record_information_project_description = TermsFacet(
    field="metadata.general_parameters.record_information.project.description",
    label=_("metadata/general_parameters/record_information/project/description.label"),
)

metadata_general_parameters_record_information_project_id = TermsFacet(
    field="metadata.general_parameters.record_information.project.id",
    label=_("metadata/general_parameters/record_information/project/id.label"),
)

metadata_general_parameters_record_information_project_owner_affiliations = VocabularyFacet(
    field="metadata.general_parameters.record_information.project.owner.affiliations",
    label=_(
        "metadata/general_parameters/record_information/project/owner/affiliations.label"
    ),
    vocabulary="affiliations",
)

metadata_general_parameters_record_information_project_owner_family_name = TermsFacet(
    field="metadata.general_parameters.record_information.project.owner.family_name",
    label=_(
        "metadata/general_parameters/record_information/project/owner/family_name.label"
    ),
)

metadata_general_parameters_record_information_project_owner_given_name = TermsFacet(
    field="metadata.general_parameters.record_information.project.owner.given_name",
    label=_(
        "metadata/general_parameters/record_information/project/owner/given_name.label"
    ),
)

metadata_general_parameters_record_information_project_owner_identifiers = TermsFacet(
    field="metadata.general_parameters.record_information.project.owner.identifiers",
    label=_(
        "metadata/general_parameters/record_information/project/owner/identifiers.label"
    ),
)

metadata_general_parameters_record_information_project_title = TermsFacet(
    field="metadata.general_parameters.record_information.project.title",
    label=_("metadata/general_parameters/record_information/project/title.label"),
)

metadata_general_parameters_record_information_publisher = TermsFacet(
    field="metadata.general_parameters.record_information.publisher",
    label=_("metadata/general_parameters/record_information/publisher.label"),
)

metadata_general_parameters_record_information_resource_type = TermsFacet(
    field="metadata.general_parameters.record_information.resource_type",
    label=_("metadata/general_parameters/record_information/resource_type.label"),
)

metadata_general_parameters_record_information_resource_type_general = TermsFacet(
    field="metadata.general_parameters.record_information.resource_type_general",
    label=_(
        "metadata/general_parameters/record_information/resource_type_general.label"
    ),
)

metadata_general_parameters_record_information_subject_category = TermsFacet(
    field="metadata.general_parameters.record_information.subject_category",
    label=_("metadata/general_parameters/record_information/subject_category.label"),
)

metadata_general_parameters_record_information_title = TermsFacet(
    field="metadata.general_parameters.record_information.title",
    label=_("metadata/general_parameters/record_information/title.label"),
)

metadata_general_parameters_schema_version = TermsFacet(
    field="metadata.general_parameters.schema_version",
    label=_("metadata/general_parameters/schema_version.label"),
)

metadata_general_parameters_technique = TermsFacet(
    field="metadata.general_parameters.technique",
    label=_("metadata/general_parameters/technique.label"),
)

metadata_method_specific_parameters_data_analysis_data_fitting_model = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.data_fitting.model",
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_fitting/model.label"
    ),
)

metadata_method_specific_parameters_data_analysis_data_fitting_quality = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.data_fitting.quality",
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_fitting/quality.label"
    ),
)

metadata_method_specific_parameters_data_analysis_data_fitting_quality_type = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.data_fitting.quality_type",
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_fitting/quality_type.label"
    ),
)

metadata_method_specific_parameters_data_analysis_data_fitting_software_name = TermsFacet(
    field=(
        "metadata.method_specific_parameters.data_analysis.data_fitting.software_name"
    ),
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_fitting/software_name.label"
    ),
)

metadata_method_specific_parameters_data_analysis_data_fitting_software_version = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.data_fitting.software_version",
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_fitting/software_version.label"
    ),
)

metadata_method_specific_parameters_data_analysis_data_processing_steps_description = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.data_processing_steps.description",
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_processing_steps/description.label"
    ),
)

metadata_method_specific_parameters_data_analysis_data_processing_steps_link_to_source_code = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.data_processing_steps.link_to_source_code",
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_processing_steps/link_to_source_code.label"
    ),
)

metadata_method_specific_parameters_data_analysis_data_processing_steps_name = TermsFacet(
    field=(
        "metadata.method_specific_parameters.data_analysis.data_processing_steps.name"
    ),
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_processing_steps/name.label"
    ),
)

metadata_method_specific_parameters_data_analysis_data_processing_steps_software_name = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.data_processing_steps.software_name",
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_processing_steps/software_name.label"
    ),
)

metadata_method_specific_parameters_data_analysis_data_processing_steps_software_tool = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.data_processing_steps.software_tool",
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_processing_steps/software_tool.label"
    ),
)

metadata_method_specific_parameters_data_analysis_data_processing_steps_software_version = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.data_processing_steps.software_version",
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_processing_steps/software_version.label"
    ),
)

metadata_method_specific_parameters_data_analysis_derived_parameter__version = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.derived_parameter.@v",
    label=_(
        "metadata/method_specific_parameters/data_analysis/derived_parameter/@v.label"
    ),
)

metadata_method_specific_parameters_experiment_type = TermsFacet(
    field="metadata.method_specific_parameters.experiment_type",
    label=_("metadata/method_specific_parameters/experiment_type.label"),
)

metadata_method_specific_parameters_measurement_positions_flow_cell = TermsFacet(
    field="metadata.method_specific_parameters.measurement_positions.flow_cell",
    label=_(
        "metadata/method_specific_parameters/measurement_positions/flow_cell.label"
    ),
)

metadata_method_specific_parameters_measurement_positions_id = TermsFacet(
    field="metadata.method_specific_parameters.measurement_positions.id",
    label=_("metadata/method_specific_parameters/measurement_positions/id.label"),
)

metadata_method_specific_parameters_measurement_positions_ligand_information_ligand__version = TermsFacet(
    field="metadata.method_specific_parameters.measurement_positions.ligand_information.ligand.@v",
    label=_(
        "metadata/method_specific_parameters/measurement_positions/ligand_information/ligand/@v.label"
    ),
)

metadata_method_specific_parameters_measurement_positions_ligand_information_ligand_immobilization_chemistry = TermsFacet(
    field="metadata.method_specific_parameters.measurement_positions.ligand_information.ligand_immobilization_chemistry",
    label=_(
        "metadata/method_specific_parameters/measurement_positions/ligand_information/ligand_immobilization_chemistry.label"
    ),
)

metadata_method_specific_parameters_measurement_positions_ligand_information_ligand_immobilization_protocol_description = TermsFacet(
    field="metadata.method_specific_parameters.measurement_positions.ligand_information.ligand_immobilization_protocol.description",
    label=_(
        "metadata/method_specific_parameters/measurement_positions/ligand_information/ligand_immobilization_protocol/description.label"
    ),
)

metadata_method_specific_parameters_measurement_positions_ligand_information_ligand_immobilization_protocol_name = TermsFacet(
    field="metadata.method_specific_parameters.measurement_positions.ligand_information.ligand_immobilization_protocol.name",
    label=_(
        "metadata/method_specific_parameters/measurement_positions/ligand_information/ligand_immobilization_protocol/name.label"
    ),
)

metadata_method_specific_parameters_measurement_positions_name = TermsFacet(
    field="metadata.method_specific_parameters.measurement_positions.name",
    label=_("metadata/method_specific_parameters/measurement_positions/name.label"),
)

metadata_method_specific_parameters_measurement_positions_position = TermsFacet(
    field="metadata.method_specific_parameters.measurement_positions.position",
    label=_("metadata/method_specific_parameters/measurement_positions/position.label"),
)

metadata_method_specific_parameters_measurement_protocol_flow_direction = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.flow.direction",
    label=_(
        "metadata/method_specific_parameters/measurement_protocol/flow/direction.label"
    ),
)

metadata_method_specific_parameters_measurement_protocol_flow_path__version = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.flow.path.@v",
    label=_(
        "metadata/method_specific_parameters/measurement_protocol/flow/path/@v.label"
    ),
)

metadata_method_specific_parameters_measurement_protocol_flow_rate = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.flow.rate",
    label=_("metadata/method_specific_parameters/measurement_protocol/flow/rate.label"),
)

metadata_method_specific_parameters_measurement_protocol_flow_unit = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.flow.unit",
    label=_("metadata/method_specific_parameters/measurement_protocol/flow/unit.label"),
)

metadata_method_specific_parameters_measurement_protocol_id = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.id",
    label=_("metadata/method_specific_parameters/measurement_protocol/id.label"),
)

metadata_method_specific_parameters_measurement_protocol_name = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.name",
    label=_("metadata/method_specific_parameters/measurement_protocol/name.label"),
)

metadata_method_specific_parameters_measurement_protocol_start_time_unit = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.start_time.unit",
    label=_(
        "metadata/method_specific_parameters/measurement_protocol/start_time/unit.label"
    ),
)

metadata_method_specific_parameters_measurement_protocol_start_time_value = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.start_time.value",
    label=_(
        "metadata/method_specific_parameters/measurement_protocol/start_time/value.label"
    ),
)

metadata_method_specific_parameters_measurement_protocol_start_time_value_error_error_level = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.start_time.value_error.error_level",
    label=_(
        "metadata/method_specific_parameters/measurement_protocol/start_time/value_error/error_level.label"
    ),
)

metadata_method_specific_parameters_measurement_protocol_start_time_value_error_errors_are_relative = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.start_time.value_error.errors_are_relative",
    label=_(
        "metadata/method_specific_parameters/measurement_protocol/start_time/value_error/errors_are_relative.label"
    ),
)

metadata_method_specific_parameters_measurement_protocol_start_time_value_error_lower_error = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.start_time.value_error.lower_error",
    label=_(
        "metadata/method_specific_parameters/measurement_protocol/start_time/value_error/lower_error.label"
    ),
)

metadata_method_specific_parameters_measurement_protocol_start_time_value_error_upper_error = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.start_time.value_error.upper_error",
    label=_(
        "metadata/method_specific_parameters/measurement_protocol/start_time/value_error/upper_error.label"
    ),
)

metadata_method_specific_parameters_measurement_protocol_time_length_unit = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.time_length.unit",
    label=_(
        "metadata/method_specific_parameters/measurement_protocol/time_length/unit.label"
    ),
)

metadata_method_specific_parameters_measurement_protocol_time_length_value = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.time_length.value",
    label=_(
        "metadata/method_specific_parameters/measurement_protocol/time_length/value.label"
    ),
)

metadata_method_specific_parameters_measurement_protocol_time_length_value_error_error_level = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.time_length.value_error.error_level",
    label=_(
        "metadata/method_specific_parameters/measurement_protocol/time_length/value_error/error_level.label"
    ),
)

metadata_method_specific_parameters_measurement_protocol_time_length_value_error_errors_are_relative = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.time_length.value_error.errors_are_relative",
    label=_(
        "metadata/method_specific_parameters/measurement_protocol/time_length/value_error/errors_are_relative.label"
    ),
)

metadata_method_specific_parameters_measurement_protocol_time_length_value_error_lower_error = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.time_length.value_error.lower_error",
    label=_(
        "metadata/method_specific_parameters/measurement_protocol/time_length/value_error/lower_error.label"
    ),
)

metadata_method_specific_parameters_measurement_protocol_time_length_value_error_upper_error = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.time_length.value_error.upper_error",
    label=_(
        "metadata/method_specific_parameters/measurement_protocol/time_length/value_error/upper_error.label"
    ),
)

metadata_method_specific_parameters_measurement_protocol_type = TermsFacet(
    field="metadata.method_specific_parameters.measurement_protocol.type",
    label=_("metadata/method_specific_parameters/measurement_protocol/type.label"),
)

metadata_method_specific_parameters_measurements_measurement_position__version = TermsFacet(
    field="metadata.method_specific_parameters.measurements.measurement_position.@v",
    label=_(
        "metadata/method_specific_parameters/measurements/measurement_position/@v.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_measurement_position__version = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_measurement_position.@v",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_measurement_position/@v.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_analytes_concentration_obtained_by = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.analytes.concentration.obtained_by",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/analytes/concentration/obtained_by.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_analytes_concentration_obtained_protocol_description = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.analytes.concentration.obtained_protocol.description",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/analytes/concentration/obtained_protocol/description.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_analytes_concentration_obtained_protocol_name = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.analytes.concentration.obtained_protocol.name",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/analytes/concentration/obtained_protocol/name.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_analytes_concentration_unit = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.analytes.concentration.unit",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/analytes/concentration/unit.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_analytes_concentration_value = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.analytes.concentration.value",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/analytes/concentration/value.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_analytes_concentration_value_error_error_level = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.analytes.concentration.value_error.error_level",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/analytes/concentration/value_error/error_level.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_analytes_concentration_value_error_errors_are_relative = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.analytes.concentration.value_error.errors_are_relative",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/analytes/concentration/value_error/errors_are_relative.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_analytes_concentration_value_error_lower_error = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.analytes.concentration.value_error.lower_error",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/analytes/concentration/value_error/lower_error.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_analytes_concentration_value_error_upper_error = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.analytes.concentration.value_error.upper_error",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/analytes/concentration/value_error/upper_error.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_analytes_entity__version = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.analytes.entity.@v",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/analytes/entity/@v.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_chemical_environment__version = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.chemical_environment.@v",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/chemical_environment/@v.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_measurement_step__version = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.measurement_step.@v",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/measurement_step/@v.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_position = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.position",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/position.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_preparation_description = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.preparation.description",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/preparation/description.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_preparation_name = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.preparation.name",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/preparation/name.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_temperature_controlled = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.temperature.controlled",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/temperature/controlled.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_temperature_obtained_by = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.temperature.obtained_by",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/temperature/obtained_by.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_temperature_operational_value = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.temperature.operational_value",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/temperature/operational_value.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_temperature_unit = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.temperature.unit",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/temperature/unit.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_temperature_value = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.temperature.value",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/temperature/value.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_temperature_value_error_error_level = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.temperature.value_error.error_level",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/temperature/value_error/error_level.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_temperature_value_error_errors_are_relative = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.temperature.value_error.errors_are_relative",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/temperature/value_error/errors_are_relative.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_temperature_value_error_lower_error = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.temperature.value_error.lower_error",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/temperature/value_error/lower_error.label"
    ),
)

metadata_method_specific_parameters_measurements_reference_samples_temperature_value_error_upper_error = TermsFacet(
    field="metadata.method_specific_parameters.measurements.reference_samples.temperature.value_error.upper_error",
    label=_(
        "metadata/method_specific_parameters/measurements/reference_samples/temperature/value_error/upper_error.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_analytes_concentration_obtained_by = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.analytes.concentration.obtained_by",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/analytes/concentration/obtained_by.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_analytes_concentration_obtained_protocol_description = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.analytes.concentration.obtained_protocol.description",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/analytes/concentration/obtained_protocol/description.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_analytes_concentration_obtained_protocol_name = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.analytes.concentration.obtained_protocol.name",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/analytes/concentration/obtained_protocol/name.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_analytes_concentration_unit = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.analytes.concentration.unit",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/analytes/concentration/unit.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_analytes_concentration_value = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.analytes.concentration.value",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/analytes/concentration/value.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_analytes_concentration_value_error_error_level = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.analytes.concentration.value_error.error_level",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/analytes/concentration/value_error/error_level.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_analytes_concentration_value_error_errors_are_relative = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.analytes.concentration.value_error.errors_are_relative",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/analytes/concentration/value_error/errors_are_relative.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_analytes_concentration_value_error_lower_error = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.analytes.concentration.value_error.lower_error",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/analytes/concentration/value_error/lower_error.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_analytes_concentration_value_error_upper_error = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.analytes.concentration.value_error.upper_error",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/analytes/concentration/value_error/upper_error.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_analytes_entity__version = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.analytes.entity.@v",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/analytes/entity/@v.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_chemical_environment__version = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.chemical_environment.@v",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/chemical_environment/@v.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_measurement_step__version = TermsFacet(
    field=(
        "metadata.method_specific_parameters.measurements.samples.measurement_step.@v"
    ),
    label=_(
        "metadata/method_specific_parameters/measurements/samples/measurement_step/@v.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_position = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.position",
    label=_("metadata/method_specific_parameters/measurements/samples/position.label"),
)

metadata_method_specific_parameters_measurements_samples_preparation_description = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.preparation.description",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/preparation/description.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_preparation_name = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.preparation.name",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/preparation/name.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_temperature_controlled = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.temperature.controlled",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/temperature/controlled.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_temperature_obtained_by = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.temperature.obtained_by",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/temperature/obtained_by.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_temperature_operational_value = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.temperature.operational_value",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/temperature/operational_value.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_temperature_unit = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.temperature.unit",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/temperature/unit.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_temperature_value = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.temperature.value",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/temperature/value.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_temperature_value_error_error_level = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.temperature.value_error.error_level",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/temperature/value_error/error_level.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_temperature_value_error_errors_are_relative = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.temperature.value_error.errors_are_relative",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/temperature/value_error/errors_are_relative.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_temperature_value_error_lower_error = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.temperature.value_error.lower_error",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/temperature/value_error/lower_error.label"
    ),
)

metadata_method_specific_parameters_measurements_samples_temperature_value_error_upper_error = TermsFacet(
    field="metadata.method_specific_parameters.measurements.samples.temperature.value_error.upper_error",
    label=_(
        "metadata/method_specific_parameters/measurements/samples/temperature/value_error/upper_error.label"
    ),
)

metadata_method_specific_parameters_schema_version = TermsFacet(
    field="metadata.method_specific_parameters.schema_version",
    label=_("metadata/method_specific_parameters/schema_version.label"),
)

metadata_method_specific_parameters_sensor_id = TermsFacet(
    field="metadata.method_specific_parameters.sensor.id",
    label=_("metadata/method_specific_parameters/sensor/id.label"),
)

metadata_method_specific_parameters_sensor_previously_used = TermsFacet(
    field="metadata.method_specific_parameters.sensor.previously_used",
    label=_("metadata/method_specific_parameters/sensor/previously_used.label"),
)

metadata_method_specific_parameters_sensor_sensor_initialization = TermsFacet(
    field="metadata.method_specific_parameters.sensor.sensor_initialization",
    label=_("metadata/method_specific_parameters/sensor/sensor_initialization.label"),
)

metadata_method_specific_parameters_sensor_supplier_catalog_number = TermsFacet(
    field="metadata.method_specific_parameters.sensor.supplier.catalog_number",
    label=_("metadata/method_specific_parameters/sensor/supplier/catalog_number.label"),
)

metadata_method_specific_parameters_sensor_supplier_further_information = TermsFacet(
    field="metadata.method_specific_parameters.sensor.supplier.further_information",
    label=_(
        "metadata/method_specific_parameters/sensor/supplier/further_information.label"
    ),
)

metadata_method_specific_parameters_sensor_supplier_name = TermsFacet(
    field="metadata.method_specific_parameters.sensor.supplier.name",
    label=_("metadata/method_specific_parameters/sensor/supplier/name.label"),
)

metadata_method_specific_parameters_sensor_surface_properties = TermsFacet(
    field="metadata.method_specific_parameters.sensor.surface_properties",
    label=_("metadata/method_specific_parameters/sensor/surface_properties.label"),
)

updated = DateTimeFacet(field="updated", label=_("updated.label"))
