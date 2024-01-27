from mst.records.dumpers.edtf import (
    MstDraftEDTFIntervalDumperExt,
    MstEDTFIntervalDumperExt,
)
from oarepo_runtime.records.dumpers import SearchDumper
from oarepo_runtime.records.systemfields.mapping import SystemFieldDumperExt


class MstDumper(SearchDumper):
    """MstRecord opensearch dumper."""

    extensions = [SystemFieldDumperExt(), MstEDTFIntervalDumperExt()]


class MstDraftDumper(SearchDumper):
    """MstDraft opensearch dumper."""

    extensions = [SystemFieldDumperExt(), MstDraftEDTFIntervalDumperExt()]
