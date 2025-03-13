from oarepo_runtime.records.dumpers import SearchDumper
from oarepo_runtime.records.systemfields.mapping import SystemFieldDumperExt

from mp.records.dumpers.edtf import (
    MpDraftEDTFIntervalDumperExt,
    MpEDTFIntervalDumperExt,
)


class MpDumper(SearchDumper):
    """MpRecord opensearch dumper."""

    extensions = [SystemFieldDumperExt(), MpEDTFIntervalDumperExt()]


class MpDraftDumper(SearchDumper):
    """MpDraft opensearch dumper."""

    extensions = [SystemFieldDumperExt(), MpDraftEDTFIntervalDumperExt()]
