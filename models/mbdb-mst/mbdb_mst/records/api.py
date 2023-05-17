from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records.systemfields import ConstantField, RelationsField
from invenio_records_resources.records.api import Record as InvenioRecord
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from oarepo_runtime.relations import InternalRelation, RelationsField

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
        entity=InternalRelation(
            "metadata.general_parameters.derived_parameters.entities_involved.entity",
            keys=["id", "name"],
            related_part=(
                "metadata.general_parameters.chemical_information.entities_of_interest"
            ),
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
