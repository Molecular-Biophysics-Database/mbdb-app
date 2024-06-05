from invenio_drafts_resources.records.api import Draft as InvenioDraft
from invenio_drafts_resources.records.api import DraftRecordIdProviderV2, ParentRecord
from invenio_drafts_resources.records.api import Record as InvenioRecord
from invenio_records.systemfields import ConstantField, ModelField
from invenio_records_resources.records.systemfields import FilesField, IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from invenio_vocabularies.records.api import Vocabulary
from oarepo_runtime.records.relations import (
    InternalRelation,
    PIDRelation,
    RelationsField,
)
from oarepo_runtime.records.systemfields.has_draftcheck import HasDraftCheckField
from oarepo_runtime.records.systemfields.owner import OwnersField
from oarepo_runtime.records.systemfields.record_status import RecordStatusSystemField

from itc.files.api import ItcFile, ItcFileDraft
from itc.records.dumpers.dumper import ItcDraftDumper, ItcDumper
from itc.records.models import (
    ItcDraftMetadata,
    ItcMetadata,
    ItcParentMetadata,
    ItcParentState,
)


class ItcParentRecord(ParentRecord):
    model_cls = ItcParentMetadata

    owners = OwnersField()


class ItcIdProvider(DraftRecordIdProviderV2):
    pid_type = "itc"


class ItcRecord(InvenioRecord):

    model_cls = ItcMetadata

    schema = ConstantField("$schema", "local://itc-1.0.0.json")

    index = IndexField(
        "itc-itc-1.0.0",
    )

    pid = PIDField(provider=ItcIdProvider, context_cls=PIDFieldContext, create=True)

    dumper = ItcDumper()

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
        Body_fluid_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
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
        Complex_substance_of_biological_origin_Body_fluid_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
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
            "metadata.method_specific_parameters.measurements.sample_in_cell.chemical_environment",
            keys=["id", "name"],
            related_part="metadata.general_parameters.chemical_environments",
        ),
        targets_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample_in_cell.targets.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        sample_in_syringe_chemical_environment=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample_in_syringe.chemical_environment",
            keys=["id", "name"],
            related_part="metadata.general_parameters.chemical_environments",
        ),
        sample_in_syringe_targets_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample_in_syringe.targets.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
    )

    versions_model_cls = ItcParentState

    parent_record_cls = ItcParentRecord
    record_status = RecordStatusSystemField()
    has_draft = HasDraftCheckField(
        draft_cls=lambda: ItcDraft, config_key="HAS_DRAFT_CUSTOM_FIELD"
    )

    files = FilesField(file_cls=ItcFile, store=False, create=False, delete=False)

    bucket_id = ModelField(dump=False)
    bucket = ModelField(dump=False)


class ItcDraft(InvenioDraft):

    model_cls = ItcDraftMetadata

    schema = ConstantField("$schema", "local://itc-1.0.0.json")

    index = IndexField("itc-itc_draft-1.0.0", search_alias="itc")

    pid = PIDField(
        provider=ItcIdProvider, context_cls=PIDFieldContext, create=True, delete=False
    )

    dumper = ItcDraftDumper()

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
        Body_fluid_source_organism=PIDRelation(
            "metadata.general_parameters.chemical_environments.constituents.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
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
        Complex_substance_of_biological_origin_Body_fluid_source_organism=PIDRelation(
            "metadata.general_parameters.entities_of_interest.source_organism",
            keys=["id", "title", {"key": "props.rank", "target": "rank"}],
            pid_field=Vocabulary.pid.with_type_ctx("organisms"),
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
            "metadata.method_specific_parameters.measurements.sample_in_cell.chemical_environment",
            keys=["id", "name"],
            related_part="metadata.general_parameters.chemical_environments",
        ),
        targets_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample_in_cell.targets.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
        sample_in_syringe_chemical_environment=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample_in_syringe.chemical_environment",
            keys=["id", "name"],
            related_part="metadata.general_parameters.chemical_environments",
        ),
        sample_in_syringe_targets_entity=InternalRelation(
            "metadata.method_specific_parameters.measurements.sample_in_syringe.targets.entity",
            keys=["id", "name"],
            related_part="metadata.general_parameters.entities_of_interest",
        ),
    )

    versions_model_cls = ItcParentState

    parent_record_cls = ItcParentRecord
    record_status = RecordStatusSystemField()

    has_draft = HasDraftCheckField(config_key="HAS_DRAFT_CUSTOM_FIELD")

    files = FilesField(file_cls=ItcFileDraft, store=False)

    bucket_id = ModelField(dump=False)
    bucket = ModelField(dump=False)


ItcFile.record_cls = ItcRecord

ItcFileDraft.record_cls = ItcDraft
