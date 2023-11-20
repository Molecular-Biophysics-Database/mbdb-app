from oarepo_runtime.records.dumpers import SearchDumper
from oarepo_runtime.records.systemfields.mapping import SystemFieldDumperExt

from mbdb_mst.records.dumpers.edtf import (
    MbdbMstDraftEDTFIntervalDumperExt,
    MbdbMstEDTFIntervalDumperExt,
)


class MbdbMstDumper(SearchDumper):
    """MbdbMstRecord opensearch dumper."""

    extensions = [SystemFieldDumperExt(), MbdbMstEDTFIntervalDumperExt()]


class MbdbMstDraftDumper(SearchDumper):
    """MbdbMstDraft opensearch dumper."""

    extensions = [SystemFieldDumperExt(), MbdbMstDraftEDTFIntervalDumperExt()]
