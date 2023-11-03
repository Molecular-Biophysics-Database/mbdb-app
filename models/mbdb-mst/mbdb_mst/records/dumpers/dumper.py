from oarepo_runtime.records.dumpers import SearchDumper

from mbdb_mst.records.dumpers.edtf import (
    MbdbMstDraftEDTFIntervalDumperExt,
    MbdbMstEDTFIntervalDumperExt,
)


class MbdbMstDumper(SearchDumper):
    """MbdbMstRecord opensearch dumper."""

    extensions = [MbdbMstEDTFIntervalDumperExt()]


class MbdbMstDraftDumper(SearchDumper):
    """MbdbMstDraft opensearch dumper."""

    extensions = [MbdbMstDraftEDTFIntervalDumperExt()]
