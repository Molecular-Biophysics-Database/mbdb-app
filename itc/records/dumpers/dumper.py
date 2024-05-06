from oarepo_runtime.records.dumpers import SearchDumper
from oarepo_runtime.records.systemfields.mapping import SystemFieldDumperExt

from itc.records.dumpers.edtf import (
    ItcDraftEDTFIntervalDumperExt,
    ItcEDTFIntervalDumperExt,
)


class ItcDumper(SearchDumper):
    """ItcRecord opensearch dumper."""

    extensions = [SystemFieldDumperExt(), ItcEDTFIntervalDumperExt()]


class ItcDraftDumper(SearchDumper):
    """ItcDraft opensearch dumper."""

    extensions = [SystemFieldDumperExt(), ItcDraftEDTFIntervalDumperExt()]
