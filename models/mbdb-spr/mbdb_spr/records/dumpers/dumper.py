from oarepo_runtime.records.dumpers import SearchDumper
from oarepo_runtime.records.systemfields.mapping import SystemFieldDumperExt

from mbdb_spr.records.dumpers.edtf import (
    MbdbSprDraftEDTFIntervalDumperExt,
    MbdbSprEDTFIntervalDumperExt,
)


class MbdbSprDumper(SearchDumper):
    """MbdbSprRecord opensearch dumper."""

    extensions = [SystemFieldDumperExt(), MbdbSprEDTFIntervalDumperExt()]


class MbdbSprDraftDumper(SearchDumper):
    """MbdbSprDraft opensearch dumper."""

    extensions = [SystemFieldDumperExt(), MbdbSprDraftEDTFIntervalDumperExt()]
