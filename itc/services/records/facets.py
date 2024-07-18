"""Facet definitions."""

from invenio_records_resources.services.records.facets import TermsFacet
from oarepo_runtime.i18n import lazy_gettext as _
from oarepo_runtime.services.facets.date import DateTimeFacet
from oarepo_runtime.services.facets.nested_facet import NestedLabeledFacet
from oarepo_vocabularies.services.facets import VocabularyFacet

metadata_general_parameters_associated_publication_journal = TermsFacet(
    field="metadata.general_parameters.associated_publication.journal",
    label=_("metadata/general_parameters/associated_publication/journal.label"),
)

metadata_general_parameters_associated_publication_pid = TermsFacet(
    field="metadata.general_parameters.associated_publication.pid",
    label=_("metadata/general_parameters/associated_publication/pid.label"),
)

metadata_general_parameters_associated_publication_title = TermsFacet(
    field="metadata.general_parameters.associated_publication.title",
    label=_("metadata/general_parameters/associated_publication/title.label"),
)

metadata_general_parameters_associated_publication_type = TermsFacet(
    field="metadata.general_parameters.associated_publication.type",
    label=_("metadata/general_parameters/associated_publication/type.label"),
)

metadata_general_parameters_associated_publication_publisher = TermsFacet(
    field="metadata.general_parameters.associated_publication.publisher",
    label=_("metadata/general_parameters/associated_publication/publisher.label"),
)

metadata_general_parameters_associated_publication_degree_type = TermsFacet(
    field="metadata.general_parameters.associated_publication.degree_type",
    label=_("metadata/general_parameters/associated_publication/degree_type.label"),
)

metadata_general_parameters_chemical_environments_additional_specifications = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.additional_specifications",
        label=_(
            "metadata/general_parameters/chemical_environments/additional_specifications.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_additional_specifications = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.additional_specifications",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/additional_specifications.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_concentration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.concentration.unit",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/concentration/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_concentration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.concentration.value",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/concentration/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_expression_organism = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_environments.constituents.expression_organism",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/expression_organism.label"
        ),
        vocabulary="organisms",
    ),
)

metadata_general_parameters_chemical_environments_constituents_expression_source_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.expression_source_type",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/expression_source_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_external_databases = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.external_databases",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/external_databases.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_modifications_biological_postprocessing_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.modifications.biological_postprocessing.position",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/modifications/biological_postprocessing/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_modifications_biological_postprocessing_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.modifications.biological_postprocessing.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/modifications/biological_postprocessing/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_modifications_biological_postprocessing_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.modifications.biological_postprocessing.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/modifications/biological_postprocessing/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_modifications_biological_postprocessing_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.modifications.biological_postprocessing.type",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/modifications/biological_postprocessing/type.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_modifications_chemical_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.modifications.chemical.position",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/modifications/chemical/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_modifications_chemical_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.modifications.chemical.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/modifications/chemical/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_modifications_chemical_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.modifications.chemical.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/modifications/chemical/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_modifications_chemical_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.modifications.chemical.type",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/modifications/chemical/type.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_modifications_synthesis_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.modifications.synthesis.position",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/modifications/synthesis/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_modifications_synthesis_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.modifications.synthesis.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/modifications/synthesis/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_modifications_synthesis_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.modifications.synthesis.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/modifications/synthesis/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_modifications_synthesis_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.modifications.synthesis.type",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/modifications/synthesis/type.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_molecular_weight_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.molecular_weight.unit",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/molecular_weight/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_molecular_weight_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.molecular_weight.value",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/molecular_weight/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.name",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_polymer_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.polymer_type",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/polymer_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_quality_controls_homogeneity_checked = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.quality_controls.homogeneity.checked",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/quality_controls/homogeneity/checked.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_quality_controls_homogeneity_expected_number_of_species = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.quality_controls.homogeneity.expected_number_of_species",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/quality_controls/homogeneity/expected_number_of_species.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_quality_controls_homogeneity_method = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.quality_controls.homogeneity.method",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/quality_controls/homogeneity/method.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_quality_controls_homogeneity_number_of_species_observed = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.quality_controls.homogeneity.number_of_species_observed",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/quality_controls/homogeneity/number_of_species_observed.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_quality_controls_identity_by_fingerprinting_method = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.quality_controls.identity.by_fingerprinting.method",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/quality_controls/identity/by_fingerprinting/method.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_quality_controls_identity_by_intact_mass_deviation_from_expected_mass_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.quality_controls.identity.by_intact_mass.deviation_from_expected_mass.unit",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/quality_controls/identity/by_intact_mass/deviation_from_expected_mass/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_quality_controls_identity_by_intact_mass_deviation_from_expected_mass_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.quality_controls.identity.by_intact_mass.deviation_from_expected_mass.value",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/quality_controls/identity/by_intact_mass/deviation_from_expected_mass/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_quality_controls_identity_by_intact_mass_method = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.quality_controls.identity.by_intact_mass.method",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/quality_controls/identity/by_intact_mass/method.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_quality_controls_identity_by_sequencing_coverage = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.quality_controls.identity.by_sequencing.coverage",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/quality_controls/identity/by_sequencing/coverage.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_quality_controls_identity_by_sequencing_method = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.quality_controls.identity.by_sequencing.method",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/quality_controls/identity/by_sequencing/method.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_quality_controls_identity_checked = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.quality_controls.identity.checked",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/quality_controls/identity/checked.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_quality_controls_purity_checked = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.quality_controls.purity.checked",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/quality_controls/purity/checked.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_quality_controls_purity_method = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.quality_controls.purity.method",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/quality_controls/purity/method.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_quality_controls_purity_purity_percentage = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.quality_controls.purity.purity_percentage",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/quality_controls/purity/purity_percentage.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_sequence = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.sequence",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/sequence.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_source_organism = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_environments.constituents.source_organism",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/source_organism.label"
        ),
        vocabulary="organisms",
    ),
)

metadata_general_parameters_chemical_environments_constituents_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.type",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/type.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_variant = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.variant",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/variant.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_basic_information = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_environments.constituents.basic_information",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/basic_information.label"
        ),
        vocabulary="chemicals",
    ),
)

metadata_general_parameters_chemical_environments_constituents_chemical_modifications_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.chemical_modifications",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.chemical_modifications.position",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/chemical_modifications/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_chemical_modifications_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.chemical_modifications",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.chemical_modifications.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/chemical_modifications/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_chemical_modifications_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.chemical_modifications",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.chemical_modifications.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/chemical_modifications/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_chemical_modifications_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.chemical_modifications",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.chemical_modifications.type",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/chemical_modifications/type.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_additional_specifications = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.additional_specifications",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/additional_specifications.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_copy_number = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.copy_number",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/copy_number.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_expression_organism = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.expression_organism",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/expression_organism.label"
        ),
        vocabulary="organisms",
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_expression_source_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.expression_source_type",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/expression_source_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_external_databases = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.external_databases",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/external_databases.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_modifications_biological_postprocessing_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.components.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.components.modifications.biological_postprocessing.position",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/components/modifications/biological_postprocessing/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_modifications_biological_postprocessing_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.components.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.components.modifications.biological_postprocessing.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/components/modifications/biological_postprocessing/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_modifications_biological_postprocessing_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.components.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.components.modifications.biological_postprocessing.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/components/modifications/biological_postprocessing/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_modifications_biological_postprocessing_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.components.modifications.biological_postprocessing",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.components.modifications.biological_postprocessing.type",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/components/modifications/biological_postprocessing/type.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_modifications_chemical_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.components.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.components.modifications.chemical.position",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/components/modifications/chemical/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_modifications_chemical_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.components.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.components.modifications.chemical.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/components/modifications/chemical/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_modifications_chemical_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.components.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.components.modifications.chemical.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/components/modifications/chemical/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_modifications_chemical_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.components.modifications.chemical",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.components.modifications.chemical.type",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/components/modifications/chemical/type.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_modifications_synthesis_position = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.components.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.components.modifications.synthesis.position",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/components/modifications/synthesis/position.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_modifications_synthesis_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.components.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.components.modifications.synthesis.protocol.description",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/components/modifications/synthesis/protocol/description.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_modifications_synthesis_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.components.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.components.modifications.synthesis.protocol.name",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/components/modifications/synthesis/protocol/name.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_modifications_synthesis_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=NestedLabeledFacet(
        path="metadata.general_parameters.chemical_environments.constituents.components.modifications.synthesis",
        nested_facet=TermsFacet(
            field="metadata.general_parameters.chemical_environments.constituents.components.modifications.synthesis.type",
            label=_(
                "metadata/general_parameters/chemical_environments/constituents/components/modifications/synthesis/type.label"
            ),
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_molecular_weight_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.molecular_weight.unit",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/molecular_weight/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_molecular_weight_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.molecular_weight.value",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/molecular_weight/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.name",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_polymer_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.polymer_type",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/polymer_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_quality_controls_homogeneity_checked = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.quality_controls.homogeneity.checked",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/quality_controls/homogeneity/checked.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_quality_controls_homogeneity_expected_number_of_species = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.quality_controls.homogeneity.expected_number_of_species",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/quality_controls/homogeneity/expected_number_of_species.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_quality_controls_homogeneity_method = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.quality_controls.homogeneity.method",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/quality_controls/homogeneity/method.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_quality_controls_homogeneity_number_of_species_observed = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.quality_controls.homogeneity.number_of_species_observed",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/quality_controls/homogeneity/number_of_species_observed.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_quality_controls_identity_by_fingerprinting_method = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.quality_controls.identity.by_fingerprinting.method",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/quality_controls/identity/by_fingerprinting/method.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_quality_controls_identity_by_intact_mass_deviation_from_expected_mass_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.quality_controls.identity.by_intact_mass.deviation_from_expected_mass.unit",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/quality_controls/identity/by_intact_mass/deviation_from_expected_mass/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_quality_controls_identity_by_intact_mass_deviation_from_expected_mass_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.quality_controls.identity.by_intact_mass.deviation_from_expected_mass.value",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/quality_controls/identity/by_intact_mass/deviation_from_expected_mass/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_quality_controls_identity_by_intact_mass_method = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.quality_controls.identity.by_intact_mass.method",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/quality_controls/identity/by_intact_mass/method.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_quality_controls_identity_by_sequencing_coverage = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.quality_controls.identity.by_sequencing.coverage",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/quality_controls/identity/by_sequencing/coverage.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_quality_controls_identity_by_sequencing_method = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.quality_controls.identity.by_sequencing.method",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/quality_controls/identity/by_sequencing/method.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_quality_controls_identity_checked = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.quality_controls.identity.checked",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/quality_controls/identity/checked.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_quality_controls_purity_checked = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.quality_controls.purity.checked",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/quality_controls/purity/checked.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_quality_controls_purity_method = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.quality_controls.purity.method",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/quality_controls/purity/method.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_quality_controls_purity_purity_percentage = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.quality_controls.purity.purity_percentage",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/quality_controls/purity/purity_percentage.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_sequence = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.sequence",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/sequence.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_source_organism = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.source_organism",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/source_organism.label"
        ),
        vocabulary="organisms",
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.type",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/type.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_variant = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.variant",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/variant.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_components_basic_information = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_environments.constituents.components.basic_information",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/components/basic_information.label"
        ),
        vocabulary="chemicals",
    ),
)

metadata_general_parameters_chemical_environments_constituents_derived_from = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.derived_from",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/derived_from.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_fluid = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.fluid",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/fluid.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_health_status = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.health_status",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/health_status.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_preparation_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.preparation_protocol.description",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/preparation_protocol/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_preparation_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.preparation_protocol.name",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/preparation_protocol/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_storage_duration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.storage.duration.unit",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/storage/duration/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_storage_duration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.storage.duration.value",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/storage/duration/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_storage_storage_preparation_description = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.storage.storage_preparation.description",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/storage/storage_preparation/description.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_storage_storage_preparation_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.storage.storage_preparation.name",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/storage/storage_preparation/name.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_storage_temperature_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.storage.temperature.unit",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/storage/temperature/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_storage_temperature_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.storage.temperature.value",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/storage/temperature/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_cell_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.cell_type",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/cell_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_fraction = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.fraction",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/fraction.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_organ = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.organ",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/organ.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_tissue = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.tissue",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/tissue.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_capsid_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.capsid_type",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/capsid_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_envelope_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.envelope_type",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/envelope_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_genetic_material = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.genetic_material",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/genetic_material.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_host_cell_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.host_cell_type",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/host_cell_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_host_organism = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_environments.constituents.host_organism",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/host_organism.label"
        ),
        vocabulary="organisms",
    ),
)

metadata_general_parameters_chemical_environments_constituents_location_latitude = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.location.latitude",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/location/latitude.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_location_longitude = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.location.longitude",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/location/longitude.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_source = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.source",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/source.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_assembly_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.assembly_type",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/assembly_type.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_class = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.class",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/class.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_number_of_mono_layers = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.number_of_mono_layers",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/number_of_mono_layers.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_size_lower = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.size.lower",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/size/lower.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_size_mean = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.size.mean",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/size/mean.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_size_median = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.size.median",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/size/median.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_size_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.size.type",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/size/type.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_size_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.size.unit",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/size/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_size_upper = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.size.upper",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/size/upper.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_constituents_product = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.constituents.product",
        label=_(
            "metadata/general_parameters/chemical_environments/constituents/product.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_id = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.id",
        label=_("metadata/general_parameters/chemical_environments/id.label"),
    ),
)

metadata_general_parameters_chemical_environments_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.name",
        label=_("metadata/general_parameters/chemical_environments/name.label"),
    ),
)

metadata_general_parameters_chemical_environments_ph = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.ph",
        label=_("metadata/general_parameters/chemical_environments/ph.label"),
    ),
)

metadata_general_parameters_chemical_environments_solvent_additional_specifications = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.solvent.additional_specifications",
        label=_(
            "metadata/general_parameters/chemical_environments/solvent/additional_specifications.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_solvent_basic_information = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=VocabularyFacet(
        field="metadata.general_parameters.chemical_environments.solvent.basic_information",
        label=_(
            "metadata/general_parameters/chemical_environments/solvent/basic_information.label"
        ),
        vocabulary="chemicals",
    ),
)

metadata_general_parameters_chemical_environments_solvent_concentration_unit = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.solvent.concentration.unit",
        label=_(
            "metadata/general_parameters/chemical_environments/solvent/concentration/unit.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_solvent_concentration_value = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.solvent.concentration.value",
        label=_(
            "metadata/general_parameters/chemical_environments/solvent/concentration/value.label"
        ),
    ),
)

metadata_general_parameters_chemical_environments_solvent_name = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.solvent.name",
        label=_("metadata/general_parameters/chemical_environments/solvent/name.label"),
    ),
)

metadata_general_parameters_chemical_environments_solvent_type = NestedLabeledFacet(
    path="metadata.general_parameters.chemical_environments",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.chemical_environments.solvent.type",
        label=_("metadata/general_parameters/chemical_environments/solvent/type.label"),
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

metadata_general_parameters_entities_of_interest_additional_specifications = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.additional_specifications",
    label=_(
        "metadata/general_parameters/entities_of_interest/additional_specifications.label"
    ),
)

metadata_general_parameters_entities_of_interest_expression_organism = VocabularyFacet(
    field="metadata.general_parameters.entities_of_interest.expression_organism",
    label=_(
        "metadata/general_parameters/entities_of_interest/expression_organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_entities_of_interest_expression_source_type = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.expression_source_type",
    label=_(
        "metadata/general_parameters/entities_of_interest/expression_source_type.label"
    ),
)

metadata_general_parameters_entities_of_interest_external_databases = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.external_databases",
    label=_(
        "metadata/general_parameters/entities_of_interest/external_databases.label"
    ),
)

metadata_general_parameters_entities_of_interest_id = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.id",
    label=_("metadata/general_parameters/entities_of_interest/id.label"),
)

metadata_general_parameters_entities_of_interest_modifications_biological_postprocessing_position = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.modifications.biological_postprocessing.position",
        label=_(
            "metadata/general_parameters/entities_of_interest/modifications/biological_postprocessing/position.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_modifications_biological_postprocessing_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.modifications.biological_postprocessing.protocol.description",
        label=_(
            "metadata/general_parameters/entities_of_interest/modifications/biological_postprocessing/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_modifications_biological_postprocessing_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.modifications.biological_postprocessing.protocol.name",
        label=_(
            "metadata/general_parameters/entities_of_interest/modifications/biological_postprocessing/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_modifications_biological_postprocessing_type = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.modifications.biological_postprocessing.type",
        label=_(
            "metadata/general_parameters/entities_of_interest/modifications/biological_postprocessing/type.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_modifications_chemical_position = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.modifications.chemical.position",
        label=_(
            "metadata/general_parameters/entities_of_interest/modifications/chemical/position.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_modifications_chemical_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.modifications.chemical.protocol.description",
        label=_(
            "metadata/general_parameters/entities_of_interest/modifications/chemical/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_modifications_chemical_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.modifications.chemical.protocol.name",
        label=_(
            "metadata/general_parameters/entities_of_interest/modifications/chemical/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_modifications_chemical_type = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.modifications.chemical.type",
        label=_(
            "metadata/general_parameters/entities_of_interest/modifications/chemical/type.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_modifications_synthesis_position = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.modifications.synthesis.position",
        label=_(
            "metadata/general_parameters/entities_of_interest/modifications/synthesis/position.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_modifications_synthesis_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.modifications.synthesis.protocol.description",
        label=_(
            "metadata/general_parameters/entities_of_interest/modifications/synthesis/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_modifications_synthesis_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.modifications.synthesis.protocol.name",
        label=_(
            "metadata/general_parameters/entities_of_interest/modifications/synthesis/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_modifications_synthesis_type = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.modifications.synthesis.type",
        label=_(
            "metadata/general_parameters/entities_of_interest/modifications/synthesis/type.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_molecular_weight_unit = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.molecular_weight.unit",
    label=_(
        "metadata/general_parameters/entities_of_interest/molecular_weight/unit.label"
    ),
)

metadata_general_parameters_entities_of_interest_molecular_weight_value = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.molecular_weight.value",
    label=_(
        "metadata/general_parameters/entities_of_interest/molecular_weight/value.label"
    ),
)

metadata_general_parameters_entities_of_interest_name = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.name",
    label=_("metadata/general_parameters/entities_of_interest/name.label"),
)

metadata_general_parameters_entities_of_interest_polymer_type = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.polymer_type",
    label=_("metadata/general_parameters/entities_of_interest/polymer_type.label"),
)

metadata_general_parameters_entities_of_interest_quality_controls_homogeneity_checked = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.quality_controls.homogeneity.checked",
    label=_(
        "metadata/general_parameters/entities_of_interest/quality_controls/homogeneity/checked.label"
    ),
)

metadata_general_parameters_entities_of_interest_quality_controls_homogeneity_expected_number_of_species = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.quality_controls.homogeneity.expected_number_of_species",
    label=_(
        "metadata/general_parameters/entities_of_interest/quality_controls/homogeneity/expected_number_of_species.label"
    ),
)

metadata_general_parameters_entities_of_interest_quality_controls_homogeneity_method = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.quality_controls.homogeneity.method",
    label=_(
        "metadata/general_parameters/entities_of_interest/quality_controls/homogeneity/method.label"
    ),
)

metadata_general_parameters_entities_of_interest_quality_controls_homogeneity_number_of_species_observed = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.quality_controls.homogeneity.number_of_species_observed",
    label=_(
        "metadata/general_parameters/entities_of_interest/quality_controls/homogeneity/number_of_species_observed.label"
    ),
)

metadata_general_parameters_entities_of_interest_quality_controls_identity_by_fingerprinting_method = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.quality_controls.identity.by_fingerprinting.method",
    label=_(
        "metadata/general_parameters/entities_of_interest/quality_controls/identity/by_fingerprinting/method.label"
    ),
)

metadata_general_parameters_entities_of_interest_quality_controls_identity_by_intact_mass_deviation_from_expected_mass_unit = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.quality_controls.identity.by_intact_mass.deviation_from_expected_mass.unit",
    label=_(
        "metadata/general_parameters/entities_of_interest/quality_controls/identity/by_intact_mass/deviation_from_expected_mass/unit.label"
    ),
)

metadata_general_parameters_entities_of_interest_quality_controls_identity_by_intact_mass_deviation_from_expected_mass_value = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.quality_controls.identity.by_intact_mass.deviation_from_expected_mass.value",
    label=_(
        "metadata/general_parameters/entities_of_interest/quality_controls/identity/by_intact_mass/deviation_from_expected_mass/value.label"
    ),
)

metadata_general_parameters_entities_of_interest_quality_controls_identity_by_intact_mass_method = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.quality_controls.identity.by_intact_mass.method",
    label=_(
        "metadata/general_parameters/entities_of_interest/quality_controls/identity/by_intact_mass/method.label"
    ),
)

metadata_general_parameters_entities_of_interest_quality_controls_identity_by_sequencing_coverage = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.quality_controls.identity.by_sequencing.coverage",
    label=_(
        "metadata/general_parameters/entities_of_interest/quality_controls/identity/by_sequencing/coverage.label"
    ),
)

metadata_general_parameters_entities_of_interest_quality_controls_identity_by_sequencing_method = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.quality_controls.identity.by_sequencing.method",
    label=_(
        "metadata/general_parameters/entities_of_interest/quality_controls/identity/by_sequencing/method.label"
    ),
)

metadata_general_parameters_entities_of_interest_quality_controls_identity_checked = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.quality_controls.identity.checked",
    label=_(
        "metadata/general_parameters/entities_of_interest/quality_controls/identity/checked.label"
    ),
)

metadata_general_parameters_entities_of_interest_quality_controls_purity_checked = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.quality_controls.purity.checked",
    label=_(
        "metadata/general_parameters/entities_of_interest/quality_controls/purity/checked.label"
    ),
)

metadata_general_parameters_entities_of_interest_quality_controls_purity_method = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.quality_controls.purity.method",
    label=_(
        "metadata/general_parameters/entities_of_interest/quality_controls/purity/method.label"
    ),
)

metadata_general_parameters_entities_of_interest_quality_controls_purity_purity_percentage = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.quality_controls.purity.purity_percentage",
    label=_(
        "metadata/general_parameters/entities_of_interest/quality_controls/purity/purity_percentage.label"
    ),
)

metadata_general_parameters_entities_of_interest_sequence = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.sequence",
    label=_("metadata/general_parameters/entities_of_interest/sequence.label"),
)

metadata_general_parameters_entities_of_interest_source_organism = VocabularyFacet(
    field="metadata.general_parameters.entities_of_interest.source_organism",
    label=_("metadata/general_parameters/entities_of_interest/source_organism.label"),
    vocabulary="organisms",
)

metadata_general_parameters_entities_of_interest_type = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.type",
    label=_("metadata/general_parameters/entities_of_interest/type.label"),
)

metadata_general_parameters_entities_of_interest_variant = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.variant",
    label=_("metadata/general_parameters/entities_of_interest/variant.label"),
)

metadata_general_parameters_entities_of_interest_basic_information = VocabularyFacet(
    field="metadata.general_parameters.entities_of_interest.basic_information",
    label=_("metadata/general_parameters/entities_of_interest/basic_information.label"),
    vocabulary="chemicals",
)

metadata_general_parameters_entities_of_interest_chemical_modifications_position = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.chemical_modifications",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.chemical_modifications.position",
        label=_(
            "metadata/general_parameters/entities_of_interest/chemical_modifications/position.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_chemical_modifications_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.chemical_modifications",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.chemical_modifications.protocol.description",
        label=_(
            "metadata/general_parameters/entities_of_interest/chemical_modifications/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_chemical_modifications_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.chemical_modifications",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.chemical_modifications.protocol.name",
        label=_(
            "metadata/general_parameters/entities_of_interest/chemical_modifications/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_chemical_modifications_type = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.chemical_modifications",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.chemical_modifications.type",
        label=_(
            "metadata/general_parameters/entities_of_interest/chemical_modifications/type.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_components_additional_specifications = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.additional_specifications",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/additional_specifications.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_copy_number = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.copy_number",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/copy_number.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_expression_organism = VocabularyFacet(
    field="metadata.general_parameters.entities_of_interest.components.expression_organism",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/expression_organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_entities_of_interest_components_expression_source_type = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.expression_source_type",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/expression_source_type.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_external_databases = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.external_databases",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/external_databases.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_modifications_biological_postprocessing_position = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.components.modifications.biological_postprocessing.position",
        label=_(
            "metadata/general_parameters/entities_of_interest/components/modifications/biological_postprocessing/position.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_components_modifications_biological_postprocessing_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.components.modifications.biological_postprocessing.protocol.description",
        label=_(
            "metadata/general_parameters/entities_of_interest/components/modifications/biological_postprocessing/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_components_modifications_biological_postprocessing_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.components.modifications.biological_postprocessing.protocol.name",
        label=_(
            "metadata/general_parameters/entities_of_interest/components/modifications/biological_postprocessing/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_components_modifications_biological_postprocessing_type = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.components.modifications.biological_postprocessing",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.components.modifications.biological_postprocessing.type",
        label=_(
            "metadata/general_parameters/entities_of_interest/components/modifications/biological_postprocessing/type.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_components_modifications_chemical_position = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.components.modifications.chemical.position",
        label=_(
            "metadata/general_parameters/entities_of_interest/components/modifications/chemical/position.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_components_modifications_chemical_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.components.modifications.chemical.protocol.description",
        label=_(
            "metadata/general_parameters/entities_of_interest/components/modifications/chemical/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_components_modifications_chemical_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.components.modifications.chemical.protocol.name",
        label=_(
            "metadata/general_parameters/entities_of_interest/components/modifications/chemical/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_components_modifications_chemical_type = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.components.modifications.chemical",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.components.modifications.chemical.type",
        label=_(
            "metadata/general_parameters/entities_of_interest/components/modifications/chemical/type.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_components_modifications_synthesis_position = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.components.modifications.synthesis.position",
        label=_(
            "metadata/general_parameters/entities_of_interest/components/modifications/synthesis/position.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_components_modifications_synthesis_protocol_description = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.components.modifications.synthesis.protocol.description",
        label=_(
            "metadata/general_parameters/entities_of_interest/components/modifications/synthesis/protocol/description.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_components_modifications_synthesis_protocol_name = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.components.modifications.synthesis.protocol.name",
        label=_(
            "metadata/general_parameters/entities_of_interest/components/modifications/synthesis/protocol/name.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_components_modifications_synthesis_type = NestedLabeledFacet(
    path="metadata.general_parameters.entities_of_interest.components.modifications.synthesis",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.entities_of_interest.components.modifications.synthesis.type",
        label=_(
            "metadata/general_parameters/entities_of_interest/components/modifications/synthesis/type.label"
        ),
    ),
)

metadata_general_parameters_entities_of_interest_components_molecular_weight_unit = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.molecular_weight.unit",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/molecular_weight/unit.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_molecular_weight_value = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.molecular_weight.value",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/molecular_weight/value.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_name = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.name",
    label=_("metadata/general_parameters/entities_of_interest/components/name.label"),
)

metadata_general_parameters_entities_of_interest_components_polymer_type = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.polymer_type",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/polymer_type.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_quality_controls_homogeneity_checked = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.quality_controls.homogeneity.checked",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/quality_controls/homogeneity/checked.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_quality_controls_homogeneity_expected_number_of_species = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.quality_controls.homogeneity.expected_number_of_species",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/quality_controls/homogeneity/expected_number_of_species.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_quality_controls_homogeneity_method = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.quality_controls.homogeneity.method",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/quality_controls/homogeneity/method.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_quality_controls_homogeneity_number_of_species_observed = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.quality_controls.homogeneity.number_of_species_observed",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/quality_controls/homogeneity/number_of_species_observed.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_quality_controls_identity_by_fingerprinting_method = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.quality_controls.identity.by_fingerprinting.method",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/quality_controls/identity/by_fingerprinting/method.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_quality_controls_identity_by_intact_mass_deviation_from_expected_mass_unit = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.quality_controls.identity.by_intact_mass.deviation_from_expected_mass.unit",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/quality_controls/identity/by_intact_mass/deviation_from_expected_mass/unit.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_quality_controls_identity_by_intact_mass_deviation_from_expected_mass_value = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.quality_controls.identity.by_intact_mass.deviation_from_expected_mass.value",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/quality_controls/identity/by_intact_mass/deviation_from_expected_mass/value.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_quality_controls_identity_by_intact_mass_method = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.quality_controls.identity.by_intact_mass.method",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/quality_controls/identity/by_intact_mass/method.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_quality_controls_identity_by_sequencing_coverage = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.quality_controls.identity.by_sequencing.coverage",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/quality_controls/identity/by_sequencing/coverage.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_quality_controls_identity_by_sequencing_method = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.quality_controls.identity.by_sequencing.method",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/quality_controls/identity/by_sequencing/method.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_quality_controls_identity_checked = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.quality_controls.identity.checked",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/quality_controls/identity/checked.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_quality_controls_purity_checked = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.quality_controls.purity.checked",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/quality_controls/purity/checked.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_quality_controls_purity_method = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.quality_controls.purity.method",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/quality_controls/purity/method.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_quality_controls_purity_purity_percentage = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.quality_controls.purity.purity_percentage",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/quality_controls/purity/purity_percentage.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_sequence = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.sequence",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/sequence.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_source_organism = VocabularyFacet(
    field="metadata.general_parameters.entities_of_interest.components.source_organism",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/source_organism.label"
    ),
    vocabulary="organisms",
)

metadata_general_parameters_entities_of_interest_components_type = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.type",
    label=_("metadata/general_parameters/entities_of_interest/components/type.label"),
)

metadata_general_parameters_entities_of_interest_components_variant = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.components.variant",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/variant.label"
    ),
)

metadata_general_parameters_entities_of_interest_components_basic_information = VocabularyFacet(
    field="metadata.general_parameters.entities_of_interest.components.basic_information",
    label=_(
        "metadata/general_parameters/entities_of_interest/components/basic_information.label"
    ),
    vocabulary="chemicals",
)

metadata_general_parameters_entities_of_interest_derived_from = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.derived_from",
    label=_("metadata/general_parameters/entities_of_interest/derived_from.label"),
)

metadata_general_parameters_entities_of_interest_fluid = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.fluid",
    label=_("metadata/general_parameters/entities_of_interest/fluid.label"),
)

metadata_general_parameters_entities_of_interest_health_status = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.health_status",
    label=_("metadata/general_parameters/entities_of_interest/health_status.label"),
)

metadata_general_parameters_entities_of_interest_preparation_protocol_description = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.preparation_protocol.description",
    label=_(
        "metadata/general_parameters/entities_of_interest/preparation_protocol/description.label"
    ),
)

metadata_general_parameters_entities_of_interest_preparation_protocol_name = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.preparation_protocol.name",
    label=_(
        "metadata/general_parameters/entities_of_interest/preparation_protocol/name.label"
    ),
)

metadata_general_parameters_entities_of_interest_storage_duration_unit = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.storage.duration.unit",
    label=_(
        "metadata/general_parameters/entities_of_interest/storage/duration/unit.label"
    ),
)

metadata_general_parameters_entities_of_interest_storage_duration_value = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.storage.duration.value",
    label=_(
        "metadata/general_parameters/entities_of_interest/storage/duration/value.label"
    ),
)

metadata_general_parameters_entities_of_interest_storage_storage_preparation_description = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.storage.storage_preparation.description",
    label=_(
        "metadata/general_parameters/entities_of_interest/storage/storage_preparation/description.label"
    ),
)

metadata_general_parameters_entities_of_interest_storage_storage_preparation_name = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.storage.storage_preparation.name",
    label=_(
        "metadata/general_parameters/entities_of_interest/storage/storage_preparation/name.label"
    ),
)

metadata_general_parameters_entities_of_interest_storage_temperature_unit = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.storage.temperature.unit",
    label=_(
        "metadata/general_parameters/entities_of_interest/storage/temperature/unit.label"
    ),
)

metadata_general_parameters_entities_of_interest_storage_temperature_value = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.storage.temperature.value",
    label=_(
        "metadata/general_parameters/entities_of_interest/storage/temperature/value.label"
    ),
)

metadata_general_parameters_entities_of_interest_cell_type = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.cell_type",
    label=_("metadata/general_parameters/entities_of_interest/cell_type.label"),
)

metadata_general_parameters_entities_of_interest_fraction = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.fraction",
    label=_("metadata/general_parameters/entities_of_interest/fraction.label"),
)

metadata_general_parameters_entities_of_interest_organ = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.organ",
    label=_("metadata/general_parameters/entities_of_interest/organ.label"),
)

metadata_general_parameters_entities_of_interest_tissue = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.tissue",
    label=_("metadata/general_parameters/entities_of_interest/tissue.label"),
)

metadata_general_parameters_entities_of_interest_capsid_type = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.capsid_type",
    label=_("metadata/general_parameters/entities_of_interest/capsid_type.label"),
)

metadata_general_parameters_entities_of_interest_envelope_type = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.envelope_type",
    label=_("metadata/general_parameters/entities_of_interest/envelope_type.label"),
)

metadata_general_parameters_entities_of_interest_genetic_material = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.genetic_material",
    label=_("metadata/general_parameters/entities_of_interest/genetic_material.label"),
)

metadata_general_parameters_entities_of_interest_host_cell_type = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.host_cell_type",
    label=_("metadata/general_parameters/entities_of_interest/host_cell_type.label"),
)

metadata_general_parameters_entities_of_interest_host_organism = VocabularyFacet(
    field="metadata.general_parameters.entities_of_interest.host_organism",
    label=_("metadata/general_parameters/entities_of_interest/host_organism.label"),
    vocabulary="organisms",
)

metadata_general_parameters_entities_of_interest_location_latitude = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.location.latitude",
    label=_("metadata/general_parameters/entities_of_interest/location/latitude.label"),
)

metadata_general_parameters_entities_of_interest_location_longitude = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.location.longitude",
    label=_(
        "metadata/general_parameters/entities_of_interest/location/longitude.label"
    ),
)

metadata_general_parameters_entities_of_interest_source = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.source",
    label=_("metadata/general_parameters/entities_of_interest/source.label"),
)

metadata_general_parameters_entities_of_interest_assembly_type = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.assembly_type",
    label=_("metadata/general_parameters/entities_of_interest/assembly_type.label"),
)

metadata_general_parameters_entities_of_interest_class = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.class",
    label=_("metadata/general_parameters/entities_of_interest/class.label"),
)

metadata_general_parameters_entities_of_interest_number_of_mono_layers = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.number_of_mono_layers",
    label=_(
        "metadata/general_parameters/entities_of_interest/number_of_mono_layers.label"
    ),
)

metadata_general_parameters_entities_of_interest_size_lower = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.size.lower",
    label=_("metadata/general_parameters/entities_of_interest/size/lower.label"),
)

metadata_general_parameters_entities_of_interest_size_mean = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.size.mean",
    label=_("metadata/general_parameters/entities_of_interest/size/mean.label"),
)

metadata_general_parameters_entities_of_interest_size_median = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.size.median",
    label=_("metadata/general_parameters/entities_of_interest/size/median.label"),
)

metadata_general_parameters_entities_of_interest_size_type = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.size.type",
    label=_("metadata/general_parameters/entities_of_interest/size/type.label"),
)

metadata_general_parameters_entities_of_interest_size_unit = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.size.unit",
    label=_("metadata/general_parameters/entities_of_interest/size/unit.label"),
)

metadata_general_parameters_entities_of_interest_size_upper = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.size.upper",
    label=_("metadata/general_parameters/entities_of_interest/size/upper.label"),
)

metadata_general_parameters_entities_of_interest_product = TermsFacet(
    field="metadata.general_parameters.entities_of_interest.product",
    label=_("metadata/general_parameters/entities_of_interest/product.label"),
)

metadata_general_parameters_funding_references = VocabularyFacet(
    field="metadata.general_parameters.funding_references",
    label=_("metadata/general_parameters/funding_references.label"),
    vocabulary="grants",
)

metadata_general_parameters_instrument = VocabularyFacet(
    field="metadata.general_parameters.instrument",
    label=_("metadata/general_parameters/instrument.label"),
    vocabulary="instruments",
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

metadata_general_parameters_record_information_external_identifier = TermsFacet(
    field="metadata.general_parameters.record_information.external_identifier",
    label=_("metadata/general_parameters/record_information/external_identifier.label"),
)

metadata_general_parameters_record_information_metadata_access_rights = TermsFacet(
    field="metadata.general_parameters.record_information.metadata_access_rights",
    label=_(
        "metadata/general_parameters/record_information/metadata_access_rights.label"
    ),
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

metadata_general_parameters_results_entities_involved_copy_number = NestedLabeledFacet(
    path="metadata.general_parameters.results.entities_involved",
    nested_facet=TermsFacet(
        field="metadata.general_parameters.results.entities_involved.copy_number",
        label=_(
            "metadata/general_parameters/results/entities_involved/copy_number.label"
        ),
    ),
)

metadata_general_parameters_results_id = TermsFacet(
    field="metadata.general_parameters.results.id",
    label=_("metadata/general_parameters/results/id.label"),
)

metadata_general_parameters_results_name = TermsFacet(
    field="metadata.general_parameters.results.name",
    label=_("metadata/general_parameters/results/name.label"),
)

metadata_general_parameters_results_type = TermsFacet(
    field="metadata.general_parameters.results.type",
    label=_("metadata/general_parameters/results/type.label"),
)

metadata_general_parameters_results_unit = TermsFacet(
    field="metadata.general_parameters.results.unit",
    label=_("metadata/general_parameters/results/unit.label"),
)

metadata_general_parameters_results_value = TermsFacet(
    field="metadata.general_parameters.results.value",
    label=_("metadata/general_parameters/results/value.label"),
)

metadata_general_parameters_results_value_error_is_relative = TermsFacet(
    field="metadata.general_parameters.results.value_error.is_relative",
    label=_("metadata/general_parameters/results/value_error/is_relative.label"),
)

metadata_general_parameters_results_value_error_lower = TermsFacet(
    field="metadata.general_parameters.results.value_error.lower",
    label=_("metadata/general_parameters/results/value_error/lower.label"),
)

metadata_general_parameters_results_value_error_upper = TermsFacet(
    field="metadata.general_parameters.results.value_error.upper",
    label=_("metadata/general_parameters/results/value_error/upper.label"),
)

metadata_general_parameters_schema_version = TermsFacet(
    field="metadata.general_parameters.schema_version",
    label=_("metadata/general_parameters/schema_version.label"),
)

metadata_general_parameters_technique = TermsFacet(
    field="metadata.general_parameters.technique",
    label=_("metadata/general_parameters/technique.label"),
)

metadata_method_specific_parameters_cell_temperature_unit = TermsFacet(
    field="metadata.method_specific_parameters.cell_temperature.unit",
    label=_("metadata/method_specific_parameters/cell_temperature/unit.label"),
)

metadata_method_specific_parameters_cell_temperature_value = TermsFacet(
    field="metadata.method_specific_parameters.cell_temperature.value",
    label=_("metadata/method_specific_parameters/cell_temperature/value.label"),
)

metadata_method_specific_parameters_cell_volume_unit = TermsFacet(
    field="metadata.method_specific_parameters.cell_volume.unit",
    label=_("metadata/method_specific_parameters/cell_volume/unit.label"),
)

metadata_method_specific_parameters_cell_volume_value = TermsFacet(
    field="metadata.method_specific_parameters.cell_volume.value",
    label=_("metadata/method_specific_parameters/cell_volume/value.label"),
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
    field="metadata.method_specific_parameters.data_analysis.data_fitting.software_name",
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

metadata_method_specific_parameters_data_analysis_data_processing_description = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.data_processing.description",
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_processing/description.label"
    ),
)

metadata_method_specific_parameters_data_analysis_data_processing_link_to_source_code = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.data_processing.link_to_source_code",
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_processing/link_to_source_code.label"
    ),
)

metadata_method_specific_parameters_data_analysis_data_processing_name = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.data_processing.name",
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_processing/name.label"
    ),
)

metadata_method_specific_parameters_data_analysis_data_processing_software_name = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.data_processing.software_name",
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_processing/software_name.label"
    ),
)

metadata_method_specific_parameters_data_analysis_data_processing_software_version = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.data_processing.software_version",
    label=_(
        "metadata/method_specific_parameters/data_analysis/data_processing/software_version.label"
    ),
)

metadata_method_specific_parameters_measurements_id = TermsFacet(
    field="metadata.method_specific_parameters.measurements.id",
    label=_("metadata/method_specific_parameters/measurements/id.label"),
)

metadata_method_specific_parameters_measurements_name = TermsFacet(
    field="metadata.method_specific_parameters.measurements.name",
    label=_("metadata/method_specific_parameters/measurements/name.label"),
)

metadata_method_specific_parameters_data_analysis_type = TermsFacet(
    field="metadata.method_specific_parameters.data_analysis.type",
    label=_("metadata/method_specific_parameters/data_analysis/type.label"),
)

metadata_method_specific_parameters_feedback_mode = TermsFacet(
    field="metadata.method_specific_parameters.feedback_mode",
    label=_("metadata/method_specific_parameters/feedback_mode.label"),
)

metadata_method_specific_parameters_injection_mode_type = TermsFacet(
    field="metadata.method_specific_parameters.injection_mode.type",
    label=_("metadata/method_specific_parameters/injection_mode/type.label"),
)

metadata_method_specific_parameters_injection_mode_volume_unit = TermsFacet(
    field="metadata.method_specific_parameters.injection_mode.volume.unit",
    label=_("metadata/method_specific_parameters/injection_mode/volume/unit.label"),
)

metadata_method_specific_parameters_injection_mode_volume_value = TermsFacet(
    field="metadata.method_specific_parameters.injection_mode.volume.value",
    label=_("metadata/method_specific_parameters/injection_mode/volume/value.label"),
)

metadata_method_specific_parameters_injection_mode_injection_parameters_n_injections = TermsFacet(
    field="metadata.method_specific_parameters.injection_mode.injection_parameters.n_injections",
    label=_(
        "metadata/method_specific_parameters/injection_mode/injection_parameters/n_injections.label"
    ),
)

metadata_method_specific_parameters_injection_mode_injection_parameters_volume_unit = TermsFacet(
    field="metadata.method_specific_parameters.injection_mode.injection_parameters.volume.unit",
    label=_(
        "metadata/method_specific_parameters/injection_mode/injection_parameters/volume/unit.label"
    ),
)

metadata_method_specific_parameters_injection_mode_injection_parameters_volume_value = TermsFacet(
    field="metadata.method_specific_parameters.injection_mode.injection_parameters.volume.value",
    label=_(
        "metadata/method_specific_parameters/injection_mode/injection_parameters/volume/value.label"
    ),
)

metadata_method_specific_parameters_injection_mode_number_injections = TermsFacet(
    field="metadata.method_specific_parameters.injection_mode.number_injections",
    label=_(
        "metadata/method_specific_parameters/injection_mode/number_injections.label"
    ),
)

metadata_method_specific_parameters_measurements_sample_in_cell_preparation_protocol_description = TermsFacet(
    field="metadata.method_specific_parameters.measurements.sample_in_cell.preparation_protocol.description",
    label=_(
        "metadata/method_specific_parameters/measurements/sample_in_cell/preparation_protocol/description.label"
    ),
)

metadata_method_specific_parameters_measurements_sample_in_cell_preparation_protocol_name = TermsFacet(
    field="metadata.method_specific_parameters.measurements.sample_in_cell.preparation_protocol.name",
    label=_(
        "metadata/method_specific_parameters/measurements/sample_in_cell/preparation_protocol/name.label"
    ),
)

metadata_method_specific_parameters_measurements_sample_in_cell_targets_concentration_unit = TermsFacet(
    field="metadata.method_specific_parameters.measurements.sample_in_cell.targets.concentration.unit",
    label=_(
        "metadata/method_specific_parameters/measurements/sample_in_cell/targets/concentration/unit.label"
    ),
)

metadata_method_specific_parameters_measurements_sample_in_cell_targets_concentration_value = TermsFacet(
    field="metadata.method_specific_parameters.measurements.sample_in_cell.targets.concentration.value",
    label=_(
        "metadata/method_specific_parameters/measurements/sample_in_cell/targets/concentration/value.label"
    ),
)

metadata_method_specific_parameters_measurements_sample_in_syringe_preparation_protocol_description = TermsFacet(
    field="metadata.method_specific_parameters.measurements.sample_in_syringe.preparation_protocol.description",
    label=_(
        "metadata/method_specific_parameters/measurements/sample_in_syringe/preparation_protocol/description.label"
    ),
)

metadata_method_specific_parameters_measurements_sample_in_syringe_preparation_protocol_name = TermsFacet(
    field="metadata.method_specific_parameters.measurements.sample_in_syringe.preparation_protocol.name",
    label=_(
        "metadata/method_specific_parameters/measurements/sample_in_syringe/preparation_protocol/name.label"
    ),
)

metadata_method_specific_parameters_measurements_sample_in_syringe_targets_concentration_unit = TermsFacet(
    field="metadata.method_specific_parameters.measurements.sample_in_syringe.targets.concentration.unit",
    label=_(
        "metadata/method_specific_parameters/measurements/sample_in_syringe/targets/concentration/unit.label"
    ),
)

metadata_method_specific_parameters_measurements_sample_in_syringe_targets_concentration_value = TermsFacet(
    field="metadata.method_specific_parameters.measurements.sample_in_syringe.targets.concentration.value",
    label=_(
        "metadata/method_specific_parameters/measurements/sample_in_syringe/targets/concentration/value.label"
    ),
)

metadata_method_specific_parameters_reference_power_unit = TermsFacet(
    field="metadata.method_specific_parameters.reference_power.unit",
    label=_("metadata/method_specific_parameters/reference_power/unit.label"),
)

metadata_method_specific_parameters_reference_power_value = TermsFacet(
    field="metadata.method_specific_parameters.reference_power.value",
    label=_("metadata/method_specific_parameters/reference_power/value.label"),
)

metadata_method_specific_parameters_schema_version = TermsFacet(
    field="metadata.method_specific_parameters.schema_version",
    label=_("metadata/method_specific_parameters/schema_version.label"),
)

metadata_method_specific_parameters_stirring_speed_unit = TermsFacet(
    field="metadata.method_specific_parameters.stirring_speed.unit",
    label=_("metadata/method_specific_parameters/stirring_speed/unit.label"),
)

metadata_method_specific_parameters_stirring_speed_value = TermsFacet(
    field="metadata.method_specific_parameters.stirring_speed.value",
    label=_("metadata/method_specific_parameters/stirring_speed/value.label"),
)


record_status = TermsFacet(field="record_status", label=_("record_status"))

has_draft = TermsFacet(field="has_draft", label=_("has_draft"))
