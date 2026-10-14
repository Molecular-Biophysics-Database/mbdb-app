#
# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o.
# SPDX-License-Identifier: MIT
#
"""Live ROR (Research Organization Registry) API: affiliation suggestions.

The affiliations vocabulary keeps a small local dump; the deposit form's
affiliation picker searches the live ROR API instead (parity with
mbdb-app-rdm-12). The blueprint below proxies the search and the read of one
organization (schema/API v2), so the browser never talks to api.ror.org directly — one place converts
the records, and the network stays server-side.

An affiliation picked this way is created in the local vocabulary when the
record is saved (``common.vocabularies.AutoCreateAffiliationsMixin``), so the
pid relation resolves and later reads show its title.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import requests
from flask import Blueprint, current_app, jsonify, request

if TYPE_CHECKING:
    from flask import Flask

ROR_SEARCH_URL = "https://api.ror.org/v2/organizations"
ROR_NOT_FOUND = 404

# The affiliations vocabulary is Invenio's built-in one, so items created from
# ROR must match its record shape (see app_data/vocabularies/affiliations.yaml
# and its converter): name and title from the ROR display name, city/country
# into location_name/country_name, the ROR id as a ror-scheme identifier.
ROR_IDENTIFIER_SCHEME = "ror"


class RORError(Exception):
    """The ROR API could not be reached or answered with an error."""


class RORNotFoundError(RORError):
    """The ROR API answered 404: no organization with the given id."""


def _ror_request(url: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == ROR_NOT_FOUND:
            raise RORNotFoundError(f"ROR API has no record for {url}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise RORError(f"ROR API request failed: {e}") from e


def ror_display_name(record: dict[str, Any]) -> str | None:
    """Return the display name of a ROR record: the ror_display name, else a label."""
    names = record.get("names") or []
    for name in names:
        if "ror_display" in (name.get("types") or []):
            return name.get("value")
    for name in names:
        if "label" in (name.get("types") or []):
            return name.get("value")
    return None


def _geonames(record: dict[str, Any]) -> dict[str, Any]:
    return (record.get("locations") or [{}])[0].get("geonames_details") or {}


def _ror_id(record: dict[str, Any]) -> str:
    """Return the bare ROR id of a record ('https://ror.org/02j46qs45' → '02j46qs45')."""
    return (record.get("id") or "").rstrip("/").rsplit("/", 1)[-1]


def _ror_suggestion(record: dict[str, Any]) -> dict[str, Any] | None:
    """Return a ROR record as a serialized vocabulary suggestion, or None without name/id."""
    name = ror_display_name(record)
    ror_id = _ror_id(record)
    if not name or not ror_id:
        return None
    geonames = _geonames(record)
    return {
        "id": ror_id,
        "title_l10n": name,
        "props": {
            "city": geonames.get("name"),
            "state": geonames.get("country_subdivision_name"),
            "country": geonames.get("country_name"),
        },
    }


def search_ror(query: str) -> list[dict[str, Any]]:
    """Search organizations by query, as serialized vocabulary suggestions."""
    data = _ror_request(ROR_SEARCH_URL, params={"query": query})
    return [hit for record in data.get("items") or [] if (hit := _ror_suggestion(record))]


def read_ror(ror_id: str) -> dict[str, Any] | None:
    """Fetch one organization by its bare id, as a serialized vocabulary suggestion."""
    return _ror_suggestion(_ror_request(f"{ROR_SEARCH_URL}/{ror_id}"))


def get_ror(ror_id: str) -> dict[str, Any]:
    """Fetch one ROR organization by its bare id, as an affiliations vocabulary payload."""
    record = _ror_request(f"{ROR_SEARCH_URL}/{ror_id}")
    name = ror_display_name(record)
    if not name:
        raise RORError(f"ROR record {ror_id} has no display name")
    geonames = _geonames(record)
    payload: dict[str, Any] = {
        "id": _ror_id(record) or ror_id,
        "name": name,
        "title": {"en": name},
        "identifiers": [{"identifier": _ror_id(record) or ror_id, "scheme": ROR_IDENTIFIER_SCHEME}],
        "status": "active",
    }
    if geonames.get("name"):
        payload["location_name"] = geonames["name"]
    if geonames.get("country_name"):
        payload["country_name"] = geonames["country_name"]
    return payload


def create_blueprint(
    app: Flask,  # noqa: ARG001 -- part of the entry-point signature, the route needs no app state
) -> Blueprint:
    """Create the /api/ror/affiliations suggest endpoint (RemoteSelectField shape).

    Registered under ``invenio_base.api_blueprints``: the WSGI dispatcher serves
    that app under ``/api``, so the rule itself carries only ``/ror/affiliations``.
    """
    blueprint = Blueprint("mbdb_ror", __name__)

    @blueprint.get("/ror/affiliations")
    def suggest_affiliations() -> Any:
        """Search ROR by the dropdown's ?q= and return invenio-style hits."""
        query = (request.args.get("q") or "").strip()
        if not query:
            return jsonify({"hits": {"hits": []}})
        try:
            hits = search_ror(query)
        except RORError:
            # A down ROR must not break the form: the dropdown shows no
            # results, the error stays in the server log.
            current_app.logger.exception("ROR affiliation suggest failed")
            return jsonify({"hits": {"hits": []}})
        return jsonify({"hits": {"hits": hits}})

    @blueprint.get("/ror/affiliations/<ror_id>")
    def read_affiliation(ror_id: str) -> Any:
        """Return one ROR organization (title_l10n, props) by its bare id.

        The form's title lookup falls back here when an affiliation id is not
        in the local vocabulary yet (picked from ROR, prefilled from ORCID, or
        sample data), so the name shows instead of the id.
        """
        try:
            item = read_ror(ror_id)
        except RORNotFoundError:
            item = None
        except RORError:
            current_app.logger.exception("ROR affiliation read failed")
            return jsonify({"message": "ROR is unavailable"}), 502
        if item is None:
            return jsonify({"message": f"No ROR organization {ror_id}"}), ROR_NOT_FOUND
        return jsonify(item)

    return blueprint
