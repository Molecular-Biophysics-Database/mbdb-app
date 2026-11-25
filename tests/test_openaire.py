"""Conversion of OpenAIRE projects to awards; run with pytest, no network or services needed."""

import pytest
from flask import Flask

from common import openaire


@pytest.fixture(autouse=True)
def app_context():
    app = Flask(__name__)
    app.config["VOCABULARIES_AWARDS_OPENAIRE_FUNDERS"] = openaire.CZECH_FUNDERS
    app.config["VOCABULARIES_AWARDS_EC_ROR_ID"] = "00k4n6c32"
    with app.app_context():
        yield


def project(**kwargs):
    return {
        "id": "ga0_________::abc",
        "code": "GA1",
        "title": "A &amp; B",
        "acronym": None,
        "fundings": [{"fundingStream": {"id": None}}],
        **kwargs,
    }


def test_award():
    assert openaire._award(project()) == {
        "id": "01pv73b02::GA1",
        "number": "GA1",
        "title": {"en": "A & B"},
        "funder": {"id": "01pv73b02"},
    }


@pytest.mark.parametrize(
    "unusable", [{"id": "unknown_____::abc"}, {"code": "unidentified"}, {"title": None}]
)
def test_unusable_project_is_left_out(unusable):
    assert openaire._award(project(**unusable)) is None


def test_search_terms_have_no_operators():
    assert openaire._search_terms('protein AND ("IF/1-2: kinase') == "protein IF/1-2 kinase"


def test_get_award_of_the_right_funder(monkeypatch):
    other = project(id="ta0_________::abc")
    monkeypatch.setattr(openaire, "_projects", lambda params: [other, project()])
    assert openaire.get_award("01pv73b02::GA1")["funder"] == {"id": "01pv73b02"}
    with pytest.raises(openaire.OpenAIRENotFoundError):
        openaire.get_award("05k73zm37::GA1")
