from oarepo_runtime.records.dumpers import SearchDumper
from oarepo_runtime.records.systemfields.mapping import SystemFieldDumperExt

from bli.records.dumpers.edtf import (
    BliDraftEDTFIntervalDumperExt,
    BliEDTFIntervalDumperExt,
)


class BliDumper(SearchDumper):
    """BliRecord opensearch dumper."""

    extensions = [SystemFieldDumperExt(), BliEDTFIntervalDumperExt()]


class BliDraftDumper(SearchDumper):
    """BliDraft opensearch dumper."""

    extensions = [SystemFieldDumperExt(), BliDraftEDTFIntervalDumperExt()]
