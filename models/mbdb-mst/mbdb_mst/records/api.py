from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records.systemfields import ConstantField, RelationsField
from invenio_records_resources.records.api import Record as InvenioRecord
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from invenio_vocabularies.records.api import Vocabulary
from oarepo_runtime.relations import InternalRelation, PIDRelation, RelationsField

from mbdb_mst.records.dumper import MbdbMstDumper
from mbdb_mst.records.models import MbdbMstMetadata


class MbdbMstIdProvider(RecordIdProviderV2):
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
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        authors_affiliations=PIDRelation(
            "metadata.general_parameters.associated_publications.main.authors.affiliations",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        contributors_affiliations=PIDRelation(
            "metadata.general_parameters.depositors.contributors.affiliations",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        depositor_affiliations=PIDRelation(
            "metadata.general_parameters.depositors.depositor.affiliations",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        principal_contact_affiliations=PIDRelation(
            "metadata.general_parameters.depositors.principal_contact.affiliations",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        entity=InternalRelation(
            "metadata.general_parameters.derived_parameters.entities_involved.entity",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.entities_of_interest"
            ),
        ),
        published_test_protocol_authors_affiliations=PIDRelation(
            "metadata.general_parameters.instrument.performance_test.published_test_protocol.authors.affiliations",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        owner_affiliations=PIDRelation(
            "metadata.general_parameters.record.project.owner.affiliations",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("affiliations"),
        ),
        derived_parameter=InternalRelation(
            "metadata.method_specific_parameters.data_analysis.derived_parameter",
            keys=["id", "name"],
            related_part="metadata.general_parameters.derived_parameters",
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
