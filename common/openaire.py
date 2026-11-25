#
# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o.
# SPDX-License-Identifier: MIT
#
"""Live OpenAIRE Graph API: award (grant) suggestions.

Same pattern as ``common.ror``: the deposit form's award picker searches OpenAIRE through the
blueprint below, and a picked award is created in the local vocabulary when the record is saved
(``common.vocabularies.AutoCreateFundingSchema``). Award ids are Invenio's
``<funder ROR id>::<grant number>``; projects of funders without a known ROR id
(``VOCABULARIES_AWARDS_OPENAIRE_FUNDERS``) are left out, the depositor enters them manually.
"""

from __future__ import annotations

import html
import re
from typing import TYPE_CHECKING, Any

import requests
from flask import Blueprint, current_app, jsonify, request
from invenio_vocabularies.contrib.awards.datastreams import OpenAIREProjectTransformer
from invenio_vocabularies.datastreams import StreamEntry
from invenio_vocabularies.datastreams.errors import TransformerError

if TYPE_CHECKING:
    from flask import Flask

OPENAIRE_PROJECTS_URL = "https://api.openaire.eu/graph/v3/projects"

# OpenAIRE prefixes of Czech funders, missing in Invenio's default mapping
CZECH_FUNDERS = {
    "av0_________": "053avzc18",  # Czech Academy of Sciences
    "ga0_________": "01pv73b02",  # Czech Science Foundation
    "mo0_________": "00r7raa16",  # Ministry of Defence
    "mpo_________": "03j4eb467",  # Ministry of Industry and Trade
    "msm_________": "037n8p820",  # Ministry of Education, Youth and Sports
    "mz0_________": "00y6khe77",  # Ministry of Health
    "ta0_________": "04v0fk911",  # Technology Agency of the Czech Republic
}

_COPIED_KEYS = ("id", "code", "title", "acronym", "startDate", "endDate")


class OpenAIREError(Exception):
    """The OpenAIRE API could not be reached or answered with an error."""


class OpenAIRENotFoundError(OpenAIREError):
    """OpenAIRE has no project for the given award id."""


def _projects(params: dict[str, Any]) -> list[dict[str, Any]]:
    try:
        response = requests.get(OPENAIRE_PROJECTS_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json().get("results") or []
    except requests.RequestException as e:
        raise OpenAIREError(f"OpenAIRE API request failed: {e}") from e


def _award(project: dict[str, Any]) -> dict[str, Any] | None:
    """Return a project as an awards vocabulary payload, or None if it cannot be one."""
    if not project.get("code") or project["code"] == "unidentified":
        return None
    # the transformer reads the dump's format: no nulls, `funding` instead of `fundings`
    record = {key: project[key] for key in _COPIED_KEYS if project.get(key)}
    if "title" in record:
        record["title"] = html.unescape(record["title"])  # "Corruption &amp; social norms"
    record["funding"] = [
        f for f in project.get("fundings") or [] if (f.get("fundingStream") or {}).get("id")
    ]
    try:
        return OpenAIREProjectTransformer().apply(StreamEntry(record)).entry
    except TransformerError:
        return None


def _suggestion(project: dict[str, Any]) -> dict[str, Any] | None:
    """Return a project as a serialized vocabulary suggestion."""
    award = _award(project)
    if not award:
        return None
    funder = (project.get("funding") or {}).get("funder") or {}
    return {
        "id": award["id"],
        "number": award["number"],
        "title_l10n": award["title"]["en"],
        "acronym": award.get("acronym"),
        "funder": {"id": award["funder"]["id"], "name": funder.get("name")},
    }


def _search_terms(query: str) -> str:
    """Return the query without the operators of OpenAIRE's query language (it answers them with 400)."""
    words = re.sub(r"[^\w\-./]", " ", query).split()
    return " ".join(w for w in words if w.upper() not in ("AND", "OR", "NOT"))


def search_awards(query: str) -> list[dict[str, Any]]:
    """Search projects by query (number, acronym, title), as serialized vocabulary suggestions."""
    terms = _search_terms(query)
    if not terms:
        return []
    projects = _projects({"search": terms, "pageSize": 20})
    # projects can share an id (the same grant collected twice); the dropdown needs it unique
    hits = {hit["id"]: hit for project in projects if (hit := _suggestion(project))}
    return list(hits.values())


def _find_project(award_id: str) -> dict[str, Any]:
    number = award_id.partition("::")[2].replace('"', "")
    if number:
        for project in _projects({"code": f'"{number}"', "pageSize": 100}):
            award = _award(project)
            if award and award["id"] == award_id:
                return project
    raise OpenAIRENotFoundError(f"OpenAIRE has no project for award {award_id}")


def get_award(award_id: str) -> dict[str, Any]:
    """Fetch one project by its award id, as an awards vocabulary payload."""
    return _award(_find_project(award_id))


def create_blueprint(
    app: Flask,  # noqa: ARG001 -- part of the entry-point signature, the route needs no app state
) -> Blueprint:
    """Create the /api/openaire/awards suggest endpoint (RemoteSelectField shape)."""
    blueprint = Blueprint("mbdb_openaire", __name__)

    @blueprint.get("/openaire/awards")
    def suggest_awards() -> Any:
        """Search OpenAIRE by the dropdown's ?q= and return invenio-style hits."""
        try:
            hits = search_awards(request.args.get("q") or "")
        except OpenAIREError:
            # A down OpenAIRE must not break the form: awards can be entered manually.
            current_app.logger.exception("OpenAIRE award suggest failed")
            hits = []
        return jsonify({"hits": {"hits": hits}})

    # path: grant numbers can contain slashes
    @blueprint.get("/openaire/awards/<path:award_id>")
    def read_award(award_id: str) -> Any:
        """Return one award by its id, for awards not in the local vocabulary yet."""
        try:
            return jsonify(_suggestion(_find_project(award_id)))
        except OpenAIRENotFoundError as e:
            return jsonify({"message": str(e)}), 404
        except OpenAIREError:
            current_app.logger.exception("OpenAIRE award read failed")
            return jsonify({"message": "OpenAIRE is unavailable"}), 502

    return blueprint
