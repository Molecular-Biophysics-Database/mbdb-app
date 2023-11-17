from oarepo_runtime.records.dumpers import SearchDumper
from oarepo_runtime.records.systemfields.mapping import SystemFieldDumperExt

from mbdb_bli.records.dumpers.edtf import (
    MbdbBliDraftEDTFIntervalDumperExt,
    MbdbBliEDTFIntervalDumperExt,
)


class MbdbBliDumper(SearchDumper):
    """MbdbBliRecord opensearch dumper."""

    extensions = [SystemFieldDumperExt(), MbdbBliEDTFIntervalDumperExt()]


class MbdbBliDraftDumper(SearchDumper):
    """MbdbBliDraft opensearch dumper."""

    extensions = [SystemFieldDumperExt(), MbdbBliDraftEDTFIntervalDumperExt()]
