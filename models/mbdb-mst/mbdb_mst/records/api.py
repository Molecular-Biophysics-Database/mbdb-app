from invenio_drafts_resources.records.api import Draft as InvenioDraft
from invenio_drafts_resources.records.api import DraftRecordIdProviderV2, ParentRecord
from invenio_drafts_resources.records.api import Record as InvenioRecord
from invenio_records.systemfields import ConstantField, ModelField, RelationsField
from invenio_records_resources.records.systemfields import FilesField, IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from invenio_vocabularies.records.api import Vocabulary
from oarepo_runtime.drafts.systemfields.has_draftcheck import HasDraftCheckField
from oarepo_runtime.relations import InternalRelation, PIDRelation, RelationsField

from mbdb_mst.files.api import MbdbMstFile, MbdbMstFileDraft
from mbdb_mst.records.dumper import MbdbMstDraftDumper, MbdbMstDumper
from mbdb_mst.records.models import (
    MbdbMstDraftMetadata,
    MbdbMstMetadata,
    MbdbMstParentMetadata,
    MbdbMstParentState,
)


class MbdbMstParentRecord(ParentRecord):
    model_cls = MbdbMstParentMetadata

    # schema = ConstantField(
    #    "$schema", "local://parent-v1.0.0.json"
    # )


class MbdbMstIdProvider(DraftRecordIdProviderV2):
    pid_type = "mst"


class MbdbMstRecord(InvenioRecord):
    model_cls = MbdbMstMetadata

    schema = ConstantField("$schema", "local://mbdb_mst-1.0.0.json")

    index = IndexField("mbdb_mst-mbdb_mst-1.0.0")

    pid = PIDField(provider=MbdbMstIdProvider, context_cls=PIDFieldContext, create=True)

    dumper_extensions = []
    dumper = MbdbMstDumper(extensions=dumper_extensions)

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
        organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Polymer_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.components.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Body_fluid_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Cell_fraction_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        host_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Virion_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        components_Polymer_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        entities_of_interest_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        entities_of_interest_Polymer_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Molecular_assembly_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Molecular_assembly_components_Polymer_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.components.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Body_fluid_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Cell_fraction_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Virion_host_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Virion_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        details_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.details.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        details_components_Polymer_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.details.components.organism",
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
        sample_composition_Polymer_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Molecular_assembly_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Molecular_assembly_components_Polymer_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.components.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Complex_substance_of_biological_origin_Body_fluid_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Complex_substance_of_biological_origin_Cell_fraction_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Virion_host_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Complex_substance_of_biological_origin_Virion_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_chemical_origin_details_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.details.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_chemical_origin_details_components_Polymer_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.details.components.organism",
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
        chemical_environment=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample.chemical_environment",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.chemical_environments"
            ),
        ),
        ligands_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample.ligands.entity",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.entities_of_interest"
            ),
        ),
        targets_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample.targets.entity",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.entities_of_interest"
            ),
        ),
    )

    versions_model_cls = MbdbMstParentState

    parent_record_cls = MbdbMstParentRecord

    files = FilesField(file_cls=MbdbMstFile, store=False, create=False, delete=False)

    bucket_id = ModelField(dump=False)
    bucket = ModelField(dump=False)


class MbdbMstDraft(InvenioDraft):
    model_cls = MbdbMstDraftMetadata

    schema = ConstantField("$schema", "local://mbdb_mst-1.0.0.json")

    index = IndexField("mbdb_mst-mbdb_mst_draft-1.0.0")

    pid = PIDField(
        provider=MbdbMstIdProvider,
        context_cls=PIDFieldContext,
        create=True,
        delete=False,
    )

    dumper_extensions = []
    dumper = MbdbMstDraftDumper(extensions=dumper_extensions)

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
        organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Polymer_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.components.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Body_fluid_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Cell_fraction_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        host_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Virion_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        components_Polymer_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.chemical_environments.constituents.details.components.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        entities_of_interest_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        entities_of_interest_Polymer_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Molecular_assembly_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Molecular_assembly_components_Polymer_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.components.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Body_fluid_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Cell_fraction_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Virion_host_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Virion_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        details_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.details.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        details_components_Polymer_organism=PIDRelation(
            "metadata.general_parameters.chemical_information.entities_of_interest.details.components.organism",
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
        sample_composition_Polymer_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Molecular_assembly_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Molecular_assembly_components_Polymer_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.components.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Complex_substance_of_biological_origin_Body_fluid_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Complex_substance_of_biological_origin_Cell_fraction_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Virion_host_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        sample_composition_Complex_substance_of_biological_origin_Virion_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_chemical_origin_details_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.details.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_chemical_origin_details_components_Polymer_organism=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.sample_composition.details.components.organism",
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
        chemical_environment=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample.chemical_environment",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.chemical_environments"
            ),
        ),
        ligands_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample.ligands.entity",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.entities_of_interest"
            ),
        ),
        targets_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample.targets.entity",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.entities_of_interest"
            ),
        ),
    )

    versions_model_cls = MbdbMstParentState

    parent_record_cls = MbdbMstParentRecord
    has_draft = HasDraftCheckField(config_key="HAS_DRAFT_CUSTOM_FIELD")

    files = FilesField(file_cls=MbdbMstFileDraft, store=False)

    bucket_id = ModelField(dump=False)
    bucket = ModelField(dump=False)


MbdbMstFile.record_cls = MbdbMstRecord

MbdbMstRecord.has_draft = HasDraftCheckField(
    draft_cls=MbdbMstDraft, config_key="HAS_DRAFT_CUSTOM_FIELD"
)

MbdbMstFileDraft.record_cls = MbdbMstDraft
