from bli.records.dumpers.edtf import (
    BliDraftEDTFIntervalDumperExt,
    BliEDTFIntervalDumperExt,
)
from oarepo_runtime.records.dumpers import SearchDumper
from oarepo_runtime.records.systemfields.mapping import SystemFieldDumperExt


class BliDumper(SearchDumper):
    """BliRecord opensearch dumper."""

    extensions = [SystemFieldDumperExt(), BliEDTFIntervalDumperExt()]


class BliDraftDumper(SearchDumper):
    """BliDraft opensearch dumper."""

    extensions = [SystemFieldDumperExt(), BliDraftEDTFIntervalDumperExt()]
