from invenio_communities.records.records.systemfields import CommunitiesField
from invenio_drafts_resources.records.api import Draft as InvenioDraft
from invenio_drafts_resources.records.api import DraftRecordIdProviderV2, ParentRecord
from invenio_drafts_resources.records.api import Record as InvenioRecord
from invenio_records.systemfields import ConstantField, ModelField
from invenio_records_resources.records.systemfields import FilesField, IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from oarepo_communities.records.systemfields.communities import (
    OARepoCommunitiesFieldContext,
)
from oarepo_runtime.records.relations import (
    InternalRelation,
    PIDRelation,
    RelationsField,
)
from oarepo_runtime.records.systemfields.has_draftcheck import HasDraftCheckField
from oarepo_runtime.records.systemfields.owner import OwnersField
from oarepo_runtime.records.systemfields.record_status import RecordStatusSystemField
from oarepo_vocabularies.records.api import Vocabulary
from oarepo_workflows.records.systemfields.state import RecordStateField
from oarepo_workflows.records.systemfields.workflow import WorkflowField

from mst.files.api import MstFile, MstFileDraft
from mst.records.dumpers.dumper import MstDraftDumper, MstDumper
from mst.records.models import (
    MstCommunitiesMetadata,
    MstDraftMetadata,
    MstMetadata,
    MstParentMetadata,
    MstParentState,
)


class MstParentRecord(ParentRecord):
    model_cls = MstParentMetadata

    workflow = WorkflowField()

    communities = CommunitiesField(
        MstCommunitiesMetadata, context_cls=OARepoCommunitiesFieldContext
    )

    owners = OwnersField()


class MstIdProvider(DraftRecordIdProviderV2):
    pid_type = "mst"


class MstRecord(InvenioRecord):

    model_cls = MstMetadata

    schema = ConstantField("$schema", "local://mst-1.0.0.json")

    index = IndexField(
        "mst-mst-1.0.0",
    )

    pid = PIDField(provider=MstIdProvider, context_cls=PIDFieldContext, create=True)

    dumper = MstDumper()

    state = RecordStateField(initial="published")

    relations = RelationsField(
        expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        basic_information=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.basic_information",
            keys=[
                "id",
                "title",
                "chemical_formula",
                "additional_identifiers",
                "molecular_weight",
            ],
            pid_field=Vocabulary.pid.with_type_ctx("chemicals"),
        ),
        Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Chemical_basic_information=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.components.basic_information",
            keys=[
                "id",
                "title",
                "chemical_formula",
                "additional_identifiers",
                "molecular_weight",
            ],
            pid_field=Vocabulary.pid.with_type_ctx("chemicals"),
        ),
        fluid=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.fluid",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("body_fluids"),
        ),
        Body_fluid_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        fraction=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.fraction",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("cell_fractions"),
        ),
        Cell_fraction_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        host_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Virion_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Solid_tissue_sample_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        environment_type=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.environment_type",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("environment_types"),
        ),
        components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        components_Chemical_basic_information=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.components.basic_information",
            keys=[
                "id",
                "title",
                "chemical_formula",
                "additional_identifiers",
                "molecular_weight",
            ],
            pid_field=Vocabulary.pid.with_type_ctx("chemicals"),
        ),
        product=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.product",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("products"),
        ),
        solvent_Chemical_basic_information=PIDRelation(
            "metadata.general_parameters.chemical_environments.solvent.basic_information",
            keys=[
                "id",
                "title",
                "chemical_formula",
                "additional_identifiers",
                "molecular_weight",
            ],
            pid_field=Vocabulary.pid.with_type_ctx("chemicals"),
        ),
        affiliations=PIDRelation(
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
        entities_of_interest_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        entities_of_interest_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        entities_of_interest_Chemical_basic_information=PIDRelation(
            "metadata.general_parameters.entities_of_interest.basic_information",
            keys=[
                "id",
                "title",
                "chemical_formula",
                "additional_identifiers",
                "molecular_weight",
            ],
            pid_field=Vocabulary.pid.with_type_ctx("chemicals"),
        ),
        Molecular_assembly_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Molecular_assembly_components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Molecular_assembly_components_Chemical_basic_information=PIDRelation(
            "metadata.general_parameters.entities_of_interest.components.basic_information",
            keys=[
                "id",
                "title",
                "chemical_formula",
                "additional_identifiers",
                "molecular_weight",
            ],
            pid_field=Vocabulary.pid.with_type_ctx("chemicals"),
        ),
        Body_fluid_fluid=PIDRelation(
            "metadata.general_parameters.entities_of_interest.fluid",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("body_fluids"),
        ),
        Complex_substance_of_biological_origin_Body_fluid_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Cell_fraction_fraction=PIDRelation(
            "metadata.general_parameters.entities_of_interest.fraction",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("cell_fractions"),
        ),
        Complex_substance_of_biological_origin_Cell_fraction_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Virion_host_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Virion_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Solid_tissue_sample_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_environmental_origin_environment_type=PIDRelation(
            "metadata.general_parameters.entities_of_interest.environment_type",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("environment_types"),
        ),
        Lipid_assembly_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Lipid_assembly_components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Lipid_assembly_components_Chemical_basic_information=PIDRelation(
            "metadata.general_parameters.entities_of_interest.components.basic_information",
            keys=[
                "id",
                "title",
                "chemical_formula",
                "additional_identifiers",
                "molecular_weight",
            ],
            pid_field=Vocabulary.pid.with_type_ctx("chemicals"),
        ),
        Complex_substance_of_industrial_origin_product=PIDRelation(
            "metadata.general_parameters.entities_of_interest.product",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("products"),
        ),
        funding_references=PIDRelation(
            "metadata.general_parameters.funding_references",
            keys=[
                "id",
                "title",
                {"key": "props.funder_name", "target": "funder_name"},
                {"key": "props.grant_id", "target": "grant_id"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("grants"),
        ),
        instrument=PIDRelation(
            "metadata.general_parameters.instrument",
            keys=[
                "id",
                "title",
                {"key": "props.manufacturer", "target": "manufacturer"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("instruments"),
        ),
        entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Constant_of_association_KA_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Constant_of_dissociation_KD_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Association_rate_kOn_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Dissociation_rate_kOff_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Change_in_enthalpy_deltaH_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Change_in_entropy_deltaS_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Change_in_Gibbs_free_energy_deltaG_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Molecular_weight_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Half_maximal_effective_concentration_EC50_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Hill_coefficient_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        measurements=InternalRelation(
            "metadata.method_specific_parameters.data_analysis.measurements",
            keys=["id", "name"],
            related_part="metadata.method_specific_parameters.measurements",
        ),
        results=InternalRelation(
            "metadata.method_specific_parameters.data_analysis.results",
            keys=["id", "name"],
            related_part="metadata.general_parameters.results",
        ),
        chemical_environment=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample.chemical_environment",
            keys=["id", "name"],
            related_part="metadata.general_parameters.chemical_environments",
        ),
        ligands_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample.ligands.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        targets_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample.targets.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
    )

    versions_model_cls = MstParentState

    parent_record_cls = MstParentRecord
    record_status = RecordStatusSystemField()
    has_draft = HasDraftCheckField(
        draft_cls=lambda: MstDraft, config_key="HAS_DRAFT_CUSTOM_FIELD"
    )

    files = FilesField(file_cls=MstFile, store=False, create=False, delete=False)

    bucket_id = ModelField(dump=False)
    bucket = ModelField(dump=False)


class MstDraft(InvenioDraft):

    model_cls = MstDraftMetadata

    schema = ConstantField("$schema", "local://mst-1.0.0.json")

    index = IndexField("mst-mst_draft-1.0.0", search_alias="mst")

    pid = PIDField(
        provider=MstIdProvider, context_cls=PIDFieldContext, create=True, delete=False
    )

    dumper = MstDraftDumper()

    state = RecordStateField()

    relations = RelationsField(
        expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        basic_information=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.basic_information",
            keys=[
                "id",
                "title",
                "chemical_formula",
                "additional_identifiers",
                "molecular_weight",
            ],
            pid_field=Vocabulary.pid.with_type_ctx("chemicals"),
        ),
        Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Chemical_basic_information=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.components.basic_information",
            keys=[
                "id",
                "title",
                "chemical_formula",
                "additional_identifiers",
                "molecular_weight",
            ],
            pid_field=Vocabulary.pid.with_type_ctx("chemicals"),
        ),
        fluid=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.fluid",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("body_fluids"),
        ),
        Body_fluid_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        fraction=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.fraction",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("cell_fractions"),
        ),
        Cell_fraction_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        host_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Virion_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Solid_tissue_sample_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        environment_type=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.environment_type",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("environment_types"),
        ),
        components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        components_Chemical_basic_information=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.components.basic_information",
            keys=[
                "id",
                "title",
                "chemical_formula",
                "additional_identifiers",
                "molecular_weight",
            ],
            pid_field=Vocabulary.pid.with_type_ctx("chemicals"),
        ),
        product=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.product",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("products"),
        ),
        solvent_Chemical_basic_information=PIDRelation(
            "metadata.general_parameters.chemical_environments.solvent.basic_information",
            keys=[
                "id",
                "title",
                "chemical_formula",
                "additional_identifiers",
                "molecular_weight",
            ],
            pid_field=Vocabulary.pid.with_type_ctx("chemicals"),
        ),
        affiliations=PIDRelation(
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
        entities_of_interest_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        entities_of_interest_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        entities_of_interest_Chemical_basic_information=PIDRelation(
            "metadata.general_parameters.entities_of_interest.basic_information",
            keys=[
                "id",
                "title",
                "chemical_formula",
                "additional_identifiers",
                "molecular_weight",
            ],
            pid_field=Vocabulary.pid.with_type_ctx("chemicals"),
        ),
        Molecular_assembly_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Molecular_assembly_components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Molecular_assembly_components_Chemical_basic_information=PIDRelation(
            "metadata.general_parameters.entities_of_interest.components.basic_information",
            keys=[
                "id",
                "title",
                "chemical_formula",
                "additional_identifiers",
                "molecular_weight",
            ],
            pid_field=Vocabulary.pid.with_type_ctx("chemicals"),
        ),
        Body_fluid_fluid=PIDRelation(
            "metadata.general_parameters.entities_of_interest.fluid",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("body_fluids"),
        ),
        Complex_substance_of_biological_origin_Body_fluid_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Cell_fraction_fraction=PIDRelation(
            "metadata.general_parameters.entities_of_interest.fraction",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("cell_fractions"),
        ),
        Complex_substance_of_biological_origin_Cell_fraction_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Virion_host_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.host_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Virion_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_biological_origin_Solid_tissue_sample_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Complex_substance_of_environmental_origin_environment_type=PIDRelation(
            "metadata.general_parameters.entities_of_interest.environment_type",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("environment_types"),
        ),
        Lipid_assembly_components_Polymer_expression_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.components.expression_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Lipid_assembly_components_Polymer_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.components.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
        ),
        Lipid_assembly_components_Chemical_basic_information=PIDRelation(
            "metadata.general_parameters.entities_of_interest.components.basic_information",
            keys=[
                "id",
                "title",
                "chemical_formula",
                "additional_identifiers",
                "molecular_weight",
            ],
            pid_field=Vocabulary.pid.with_type_ctx("chemicals"),
        ),
        Complex_substance_of_industrial_origin_product=PIDRelation(
            "metadata.general_parameters.entities_of_interest.product",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("products"),
        ),
        funding_references=PIDRelation(
            "metadata.general_parameters.funding_references",
            keys=[
                "id",
                "title",
                {"key": "props.funder_name", "target": "funder_name"},
                {"key": "props.grant_id", "target": "grant_id"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("grants"),
        ),
        instrument=PIDRelation(
            "metadata.general_parameters.instrument",
            keys=[
                "id",
                "title",
                {"key": "props.manufacturer", "target": "manufacturer"},
            ],
            pid_field=Vocabulary.pid.with_type_ctx("instruments"),
        ),
        entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Constant_of_association_KA_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Constant_of_dissociation_KD_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Association_rate_kOn_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Dissociation_rate_kOff_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Change_in_enthalpy_deltaH_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Change_in_entropy_deltaS_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Change_in_Gibbs_free_energy_deltaG_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Molecular_weight_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Half_maximal_effective_concentration_EC50_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        Hill_coefficient_entities_involved_entity=InternalRelation(
            "metadata.general_parameters.results.entities_involved.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        measurements=InternalRelation(
            "metadata.method_specific_parameters.data_analysis.measurements",
            keys=["id", "name"],
            related_part="metadata.method_specific_parameters.measurements",
        ),
        results=InternalRelation(
            "metadata.method_specific_parameters.data_analysis.results",
            keys=["id", "name"],
            related_part="metadata.general_parameters.results",
        ),
        chemical_environment=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample.chemical_environment",
            keys=["id", "name"],
            related_part="metadata.general_parameters.chemical_environments",
        ),
        ligands_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample.ligands.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        targets_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample.targets.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
    )

    versions_model_cls = MstParentState

    parent_record_cls = MstParentRecord
    record_status = RecordStatusSystemField()

    has_draft = HasDraftCheckField(config_key="HAS_DRAFT_CUSTOM_FIELD")

    files = FilesField(file_cls=MstFileDraft, store=False)

    bucket_id = ModelField(dump=False)
    bucket = ModelField(dump=False)


MstFile.record_cls = MstRecord

MstFileDraft.record_cls = MstDraft
