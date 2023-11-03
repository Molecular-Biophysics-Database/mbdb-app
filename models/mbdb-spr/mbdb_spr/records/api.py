from invenio_drafts_resources.records.api import Draft as InvenioDraft
from invenio_drafts_resources.records.api import DraftRecordIdProviderV2, ParentRecord
from invenio_drafts_resources.records.api import Record as InvenioRecord
from invenio_records.systemfields import ConstantField, ModelField
from invenio_records_resources.records.systemfields import FilesField, IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from invenio_vocabularies.records.api import Vocabulary
from oarepo_runtime.drafts.systemfields.has_draftcheck import HasDraftCheckField
from oarepo_runtime.relations import InternalRelation, PIDRelation, RelationsField

from mbdb_spr.files.api import MbdbSprFile, MbdbSprFileDraft
from mbdb_spr.records.dumpers.dumper import MbdbSprDraftDumper, MbdbSprDumper
from mbdb_spr.records.models import (
    MbdbSprDraftMetadata,
    MbdbSprMetadata,
    MbdbSprParentMetadata,
    MbdbSprParentState,
)


class MbdbSprParentRecord(ParentRecord):
    model_cls = MbdbSprParentMetadata


class MbdbSprIdProvider(DraftRecordIdProviderV2):
    pid_type = "spr"


class MbdbSprRecord(InvenioRecord):
    model_cls = MbdbSprMetadata

    schema = ConstantField("$schema", "local://mbdb_spr-1.0.0.json")

    index = IndexField("mbdb_spr-mbdb_spr-1.0.0")

    pid = PIDField(provider=MbdbSprIdProvider, context_cls=PIDFieldContext, create=True)

    dumper = MbdbSprDumper()

    relations = RelationsField(
        affiliations=PIDRelation(
            "metadata.general_parameters.associated_publications.additional.authors.affiliations",
            keys=[
                "id",
                "title",
                {"key": "props.city", "target": "city"},
                {"key": "props.state", "target": "state"},
                {"key": "props.country", "target": "country"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        authors_affiliations=PIDRelation(
            "metadata.general_parameters.associated_publications.main.authors.affiliations",
            keys=[
                "id",
                "title",
                {"key": "props.city", "target": "city"},
                {"key": "props.state", "target": "state"},
                {"key": "props.country", "target": "country"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Body_fluid_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Cell_fraction_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        host_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Virion_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        entities_of_interest_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        entities_of_interest_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Molecular_assembly_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Molecular_assembly_components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Body_fluid_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Cell_fraction_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Virion_host_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Virion_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        details_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.details.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        details_components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.details.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        contributors_affiliations=PIDRelation(
            "metadata.general_parameters.depositors.contributors.affiliations",
            keys=[
                "id",
                "title",
                {"key": "props.city", "target": "city"},
                {"key": "props.state", "target": "state"},
                {"key": "props.country", "target": "country"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        depositor_affiliations=PIDRelation(
            "metadata.general_parameters.depositors.depositor.affiliations",
            keys=[
                "id",
                "title",
                {"key": "props.city", "target": "city"},
                {"key": "props.state", "target": "state"},
                {"key": "props.country", "target": "country"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        principal_contact_affiliations=PIDRelation(
            "metadata.general_parameters.depositors.principal_contact.affiliations",
            keys=[
                "id",
                "title",
                {"key": "props.city", "target": "city"},
                {"key": "props.state", "target": "state"},
                {"key": "props.country", "target": "country"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        entity=InternalRelation(
            "metadata.general_parameters.derived_parameters.entities_involved.entity",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.entities_of_interest"
            ),
        ),
        funding_reference=PIDRelation(
            "metadata.general_parameters.funding_reference",
            keys=["id", "title", {"key": "props.funder_name", "target": "funder_name"}],
            pid_field=Vocabulary.pid.with_type_ctx("grants"),
        ),
        published_test_protocol_authors_affiliations=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.published_test_protocol.authors.affiliations",
            keys=[
                "id",
                "title",
                {"key": "props.city", "target": "city"},
                {"key": "props.state", "target": "state"},
                {"key": "props.country", "target": "country"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        sample_composition_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Molecular_assembly_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Molecular_assembly_components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Complex_substance_of_biological_origin_Body_fluid_source_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Complex_substance_of_biological_origin_Cell_fraction_source_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Virion_host_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Complex_substance_of_biological_origin_Virion_source_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_chemical_origin_details_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.details.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_chemical_origin_details_components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.details.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        owner_affiliations=PIDRelation(
            "metadata.general_parameters.record_information.project.owner.affiliations",
            keys=[
                "id",
                "title",
                {"key": "props.city", "target": "city"},
                {"key": "props.state", "target": "state"},
                {"key": "props.country", "target": "country"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        derived_parameter=InternalRelation(
            "metadata.method_specific_parameters.data_analysis.derived_parameter",
            keys=["id", "name"],
            related_part="metadata.general_parameters.derived_parameters",
        ),
        measurements=InternalRelation(
            "metadata.method_specific_parameters.data_analysis.measurements",
            keys=["id", "name"],
            related_part="metadata.method_specific_parameters.measurements",
        ),
        ligand=InternalRelation(
            "metadata.method_specific_parameters.measurement_positions.ligand_information.ligand",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.entities_of_interest"
            ),
        ),
        path=InternalRelation(
            "metadata.method_specific_parameters.measurement_protocol.flow.path",
            keys=["id", "name"],
            related_part="metadata.method_specific_parameters.measurement_positions",
        ),
        measurement_position=InternalRelation(
            "metadata.method_specific_parameters.measurements.measurement_position",
            keys=["id", "name"],
            related_part="metadata.method_specific_parameters.measurement_positions",
        ),
        reference_measurement_position=InternalRelation(
            "metadata.method_specific_parameters.measurements.reference_measurement_position",
            keys=["id", "name"],
            related_part="metadata.method_specific_parameters.measurement_positions",
        ),
        analytes_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.reference_samples.analytes.entity",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.entities_of_interest"
            ),
        ),
        chemical_environment=InternalRelation(
            "metadata.method_specific_parameters.measurements.reference_samples.chemical_environment",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.chemical_environments"
            ),
        ),
        measurement_step=InternalRelation(
            "metadata.method_specific_parameters.measurements.reference_samples.measurement_step",
            keys=["id", "name"],
            related_part="metadata.method_specific_parameters.measurement_protocol",
        ),
        samples_analytes_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.samples.analytes.entity",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.entities_of_interest"
            ),
        ),
        samples_chemical_environment=InternalRelation(
            "metadata.method_specific_parameters.measurements.samples.chemical_environment",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.chemical_environments"
            ),
        ),
        samples_measurement_step=InternalRelation(
            "metadata.method_specific_parameters.measurements.samples.measurement_step",
            keys=["id", "name"],
            related_part="metadata.method_specific_parameters.measurement_protocol",
        ),
    )

    versions_model_cls = MbdbSprParentState

    parent_record_cls = MbdbSprParentRecord

    files = FilesField(file_cls=MbdbSprFile, store=False, create=False, delete=False)

    bucket_id = ModelField(dump=False)
    bucket = ModelField(dump=False)


class MbdbSprDraft(InvenioDraft):
    model_cls = MbdbSprDraftMetadata

    schema = ConstantField("$schema", "local://mbdb_spr-1.0.0.json")

    index = IndexField("mbdb_spr-mbdb_spr_draft-1.0.0")

    pid = PIDField(
        provider=MbdbSprIdProvider,
        context_cls=PIDFieldContext,
        create=True,
        delete=False,
    )

    dumper = MbdbSprDraftDumper()

    relations = RelationsField(
        affiliations=PIDRelation(
            "metadata.general_parameters.associated_publications.additional.authors.affiliations",
            keys=[
                "id",
                "title",
                {"key": "props.city", "target": "city"},
                {"key": "props.state", "target": "state"},
                {"key": "props.country", "target": "country"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        authors_affiliations=PIDRelation(
            "metadata.general_parameters.associated_publications.main.authors.affiliations",
            keys=[
                "id",
                "title",
                {"key": "props.city", "target": "city"},
                {"key": "props.state", "target": "state"},
                {"key": "props.country", "target": "country"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Body_fluid_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Cell_fraction_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        host_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Virion_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        entities_of_interest_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        entities_of_interest_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Molecular_assembly_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Molecular_assembly_components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Body_fluid_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Cell_fraction_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Virion_host_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Virion_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        details_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.details.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        details_components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.details.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        contributors_affiliations=PIDRelation(
            "metadata.general_parameters.depositors.contributors.affiliations",
            keys=[
                "id",
                "title",
                {"key": "props.city", "target": "city"},
                {"key": "props.state", "target": "state"},
                {"key": "props.country", "target": "country"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        depositor_affiliations=PIDRelation(
            "metadata.general_parameters.depositors.depositor.affiliations",
            keys=[
                "id",
                "title",
                {"key": "props.city", "target": "city"},
                {"key": "props.state", "target": "state"},
                {"key": "props.country", "target": "country"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        principal_contact_affiliations=PIDRelation(
            "metadata.general_parameters.depositors.principal_contact.affiliations",
            keys=[
                "id",
                "title",
                {"key": "props.city", "target": "city"},
                {"key": "props.state", "target": "state"},
                {"key": "props.country", "target": "country"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        entity=InternalRelation(
            "metadata.general_parameters.derived_parameters.entities_involved.entity",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.entities_of_interest"
            ),
        ),
        funding_reference=PIDRelation(
            "metadata.general_parameters.funding_reference",
            keys=["id", "title", {"key": "props.funder_name", "target": "funder_name"}],
            pid_field=Vocabulary.pid.with_type_ctx("grants"),
        ),
        published_test_protocol_authors_affiliations=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.published_test_protocol.authors.affiliations",
            keys=[
                "id",
                "title",
                {"key": "props.city", "target": "city"},
                {"key": "props.state", "target": "state"},
                {"key": "props.country", "target": "country"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        sample_composition_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Molecular_assembly_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Molecular_assembly_components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Complex_substance_of_biological_origin_Body_fluid_source_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Complex_substance_of_biological_origin_Cell_fraction_source_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Virion_host_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Complex_substance_of_biological_origin_Virion_source_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_chemical_origin_details_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.details.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_chemical_origin_details_components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.details.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        owner_affiliations=PIDRelation(
            "metadata.general_parameters.record_information.project.owner.affiliations",
            keys=[
                "id",
                "title",
                {"key": "props.city", "target": "city"},
                {"key": "props.state", "target": "state"},
                {"key": "props.country", "target": "country"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        derived_parameter=InternalRelation(
            "metadata.method_specific_parameters.data_analysis.derived_parameter",
            keys=["id", "name"],
            related_part="metadata.general_parameters.derived_parameters",
        ),
        measurements=InternalRelation(
            "metadata.method_specific_parameters.data_analysis.measurements",
            keys=["id", "name"],
            related_part="metadata.method_specific_parameters.measurements",
        ),
        ligand=InternalRelation(
            "metadata.method_specific_parameters.measurement_positions.ligand_information.ligand",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.entities_of_interest"
            ),
        ),
        path=InternalRelation(
            "metadata.method_specific_parameters.measurement_protocol.flow.path",
            keys=["id", "name"],
            related_part="metadata.method_specific_parameters.measurement_positions",
        ),
        measurement_position=InternalRelation(
            "metadata.method_specific_parameters.measurements.measurement_position",
            keys=["id", "name"],
            related_part="metadata.method_specific_parameters.measurement_positions",
        ),
        reference_measurement_position=InternalRelation(
            "metadata.method_specific_parameters.measurements.reference_measurement_position",
            keys=["id", "name"],
            related_part="metadata.method_specific_parameters.measurement_positions",
        ),
        analytes_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.reference_samples.analytes.entity",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.entities_of_interest"
            ),
        ),
        chemical_environment=InternalRelation(
            "metadata.method_specific_parameters.measurements.reference_samples.chemical_environment",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.chemical_environments"
            ),
        ),
        measurement_step=InternalRelation(
            "metadata.method_specific_parameters.measurements.reference_samples.measurement_step",
            keys=["id", "name"],
            related_part="metadata.method_specific_parameters.measurement_protocol",
        ),
        samples_analytes_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.samples.analytes.entity",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.entities_of_interest"
            ),
        ),
        samples_chemical_environment=InternalRelation(
            "metadata.method_specific_parameters.measurements.samples.chemical_environment",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.chemical_environments"
            ),
        ),
        samples_measurement_step=InternalRelation(
            "metadata.method_specific_parameters.measurements.samples.measurement_step",
            keys=["id", "name"],
            related_part="metadata.method_specific_parameters.measurement_protocol",
        ),
    )

    versions_model_cls = MbdbSprParentState

    parent_record_cls = MbdbSprParentRecord
    has_draft = HasDraftCheckField(config_key="HAS_DRAFT_CUSTOM_FIELD")

    files = FilesField(file_cls=MbdbSprFileDraft, store=False)

    bucket_id = ModelField(dump=False)
    bucket = ModelField(dump=False)


MbdbSprFile.record_cls = MbdbSprRecord

MbdbSprRecord.has_draft = HasDraftCheckField(
    draft_cls=MbdbSprDraft, config_key="HAS_DRAFT_CUSTOM_FIELD"
)

MbdbSprFileDraft.record_cls = MbdbSprDraft
