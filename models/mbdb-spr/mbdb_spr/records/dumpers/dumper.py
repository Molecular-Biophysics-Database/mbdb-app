from oarepo_runtime.records.dumpers import SearchDumper

from mbdb_spr.records.dumpers.edtf import (
    MbdbSprDraftEDTFIntervalDumperExt,
    MbdbSprEDTFIntervalDumperExt,
)


class MbdbSprDumper(SearchDumper):
    """MbdbSprRecord opensearch dumper."""

    extensions = [MbdbSprEDTFIntervalDumperExt()]


class MbdbSprDraftDumper(SearchDumper):
    """MbdbSprDraft opensearch dumper."""

    extensions = [MbdbSprDraftEDTFIntervalDumperExt()]
