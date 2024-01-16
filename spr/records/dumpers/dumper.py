from oarepo_runtime.records.dumpers import SearchDumper
from oarepo_runtime.records.systemfields.mapping import SystemFieldDumperExt
from spr.records.dumpers.edtf import (
    SprDraftEDTFIntervalDumperExt,
    SprEDTFIntervalDumperExt,
)


class SprDumper(SearchDumper):
    """SprRecord opensearch dumper."""

    extensions = [SystemFieldDumperExt(), SprEDTFIntervalDumperExt()]


class SprDraftDumper(SearchDumper):
    """SprDraft opensearch dumper."""

    extensions = [SystemFieldDumperExt(), SprDraftEDTFIntervalDumperExt()]
