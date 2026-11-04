"""
Common code shared across model definitions
"""
from __future__ import annotations

from oarepo_communities.model.presets import communities_preset
from oarepo_model.presets.internal_relations import internal_relations_preset
from oarepo_rdm.model import rdm_minimal_preset
from oarepo_requests.model.presets.requests import requests_preset
from oarepo_workflows.model.presets import workflows_preset

common_presets = [
    rdm_minimal_preset,
    workflows_preset,
    requests_preset,
    communities_preset,
    internal_relations_preset,
]
