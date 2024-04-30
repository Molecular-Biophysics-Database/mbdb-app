from typing import Callable, List, Tuple, Any, TypeVar, Type
import json
import pytest
import requests


from common.vocabulary_getters import (
    start_pos_api_page,
    exceeds_page,
    get_last_page,
    make_endpoint,
    make_links,
    hit_dict,
    empty_hits,
    check_response,
    fetch_json,
    RORService,
)

# to enable using exceptions as typehint (copied from pytest source)
E = TypeVar("E", bound=BaseException)


def assert_all(func: Callable, tests: List[Tuple[dict, Any]]):
    for test, result in tests:
        assert func(**test) == result


def raise_all(func: Callable, tests: List[dict], err: Type[E]):
    with pytest.raises(err):
        for test in tests:
            func(**test)


def get_json_dict(path):
    with open(path) as fp:
        return json.load(fp)


class TestStartPosApiPage:
    @staticmethod
    def test_positive():
        tests = [
            ({"page": 1, "size": 10, "api_size": 20}, 0),
            ({"page": 2, "size": 10, "api_size": 20}, 10),
            ({"page": 2, "size": 4, "api_size": 3}, 1),
        ]
        assert_all(start_pos_api_page, tests)

    @staticmethod
    def test_raises_on_lt_one():
        tests = [
            {"page": 0, "size": 10, "api_size": 20},
            {"page": 1, "size": 0, "api_size": 20},
            {"page": 2, "size": 4, "api_size": -1},
        ]
        raise_all(start_pos_api_page, tests, ValueError)


def test_exceed_with_correct_input():
    tests = [
        ({"page": 1, "size": 10, "api_size": 20}, False),
        ({"page": 2, "size": 10, "api_size": 20}, False),
        ({"page": 2, "size": 4, "api_size": 5}, True),
    ]
    assert_all(exceeds_page, tests)


class TestGetLastPage:
    @staticmethod
    def test_positive():
        tests = [
            ({"total": 1, "size": 2}, 1),
            ({"total": 3, "size": 2}, 2),
            ({"total": 0, "size": 2}, 0),
        ]
        assert_all(get_last_page, tests)

    @staticmethod
    def test_negative():
        tests = [{"total": -1, "size": 2}, {"total": 1, "size": -1}]
        raise_all(get_last_page, tests, ValueError)


def test_make_endpoint_with_correct_input():
    tests = [
        (
            {
                "query": "foo",
                "page": 1,
                "size": 2,
                "vocabulary_type": "bar",
                "url": "baz",
            },
            "baz/vocabularies/bar/authoritative?q=foo&page=1&size=2",
        ),
        (
            {
                "query": "+ěščř",
                "page": 1,
                "size": 2,
                "vocabulary_type": "bar",
                "url": "baz",
            },
            "baz/vocabularies/bar/authoritative?q=+ěščř&page=1&size=2",
        ),
    ]
    assert_all(make_endpoint, tests)


class TestMakeLinks:
    @staticmethod
    def test_links_with_next_page():
        tests = [
            (
                {
                    "query": "foo",
                    "page": 1,
                    "size": 2,
                    "total": 4,
                    "vocabulary_type": "bar",
                    "url": "baz",
                },
                {
                    "self": "baz/vocabularies/bar/authoritative?q=foo&page=1&size=2",
                    "next": "baz/vocabularies/bar/authoritative?q=foo&page=2&size=2",
                },
            ),
        ]
        assert_all(make_links, tests)

    @staticmethod
    def test_links_without_next_page():
        tests = [
            (
                {
                    "query": "foo",
                    "page": 100,
                    "size": 2,
                    "total": 1,
                    "vocabulary_type": "bar",
                    "url": "baz",
                },
                {"self": "baz/vocabularies/bar/authoritative?q=foo&page=100&size=2"},
            ),
        ]
        assert_all(make_links, tests)


def test_hit_dict_with_valid_input():
    tests = [
        (
            {"hits": [{"foo": "bar"}], "total": 42, "links": {"test.com"}},
            {"hits": {"hits": [{"foo": "bar"}], "total": 42}, "links": {"test.com"}},
        )
    ]
    assert_all(hit_dict, tests)


class TestEmptyHits:
    @staticmethod
    def test_returns_empty():
        tests = [({"total": 0, "page": 1}, [])]
        assert_all(empty_hits, tests)

    @staticmethod
    def test_raises_on_beyond():
        from invenio_records_rest.errors import SearchPaginationRESTError

        tests = [{"total": 1, "page": 2}, {"total": 0, "page": 2}]
        raise_all(empty_hits, tests, SearchPaginationRESTError)


class TestCheckResponse:
    test_response = requests.Response()

    def test_ok_response(self):
        test_codes = [200, 201, 300]
        for code in test_codes:
            self.test_response.status_code = code
            assert check_response(self.test_response) is None

    def test_not_ok_response(self):
        test_codes = [404, 500]
        with pytest.raises(ConnectionError):
            for code in test_codes:
                self.test_response.status_code = code
                check_response(self.test_response)


class TestFetchJson:
    test_url = "https://test.com"

    def test_with_ok_url(self, requests_mock):
        test_json = {"foo": "bar"}
        requests_mock.get(self.test_url, json=test_json)
        tests = [
            ({"url": self.test_url}, test_json),
            ({"url": self.test_url, "params": {"baz": 1}}, test_json),
        ]
        assert_all(fetch_json, tests)

    def test_without_ok_url(self, requests_mock):
        requests_mock.get(self.test_url, status_code=404)
        tests = [
            {"url": self.test_url},
            {"url": self.test_url, "params": {"baz": 1}},
        ]
        raise_all(fetch_json, tests, ConnectionError)


class TestRORService:
    R = RORService()
    mocked_url = R.base_url
    test_json = get_json_dict("ROR_search_test.json")
    test_hit = test_json["items"][0]
    test_hit_expected = {
        "id": "ror:0442wxc77",
        "title": {"en": "STMicroelectronics (United Kingdom)"},
        "props": {"city": "Marlow", "country": "United Kingdom", "state": "England"},
    }
    test_hit_id = "0442wxc77"

    def test_convert_ror_record(self):
        converted = self.R.convert_ror_record(self.test_hit)
        assert converted == self.test_hit_expected

    def test_search(self, requests_mock):
        requests_mock.get(self.mocked_url, json=self.test_json)
        search_result = self.R.search(query="st", page=1, size=2, url="test.com")
        assert search_result
        assert len(search_result["hits"]["hits"]) == 2

    def test_get_valid_id(self, requests_mock):
        requests_mock.get(f"{self.mocked_url}/{self.test_hit_id}", json=self.test_hit)
        get_result = self.R.get("ror:0442wxc77")
        assert get_result == self.test_hit_expected

    def test_get_invalid_id(self, requests_mock):
        requests_mock.get(f"{self.mocked_url}/{self.test_hit_id}", json=self.test_hit)
        with pytest.raises(KeyError):
            self.R.get("not a ROR id")
