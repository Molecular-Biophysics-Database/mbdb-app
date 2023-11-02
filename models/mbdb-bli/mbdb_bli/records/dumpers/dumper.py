from oarepo_runtime.records.dumpers import SearchDumper

from mbdb_bli.records.dumpers.edtf import (
    MbdbBliDraftEDTFIntervalDumperExt,
    MbdbBliEDTFIntervalDumperExt,
)


class MbdbBliDumper(SearchDumper):
    """MbdbBliRecord opensearch dumper."""

    extensions = [MbdbBliEDTFIntervalDumperExt()]


class MbdbBliDraftDumper(SearchDumper):
    """MbdbBliDraft opensearch dumper."""

    extensions = [MbdbBliDraftEDTFIntervalDumperExt()]
