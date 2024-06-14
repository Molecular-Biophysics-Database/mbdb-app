from typing import Callable, List, Tuple, Any, TypeVar, Type
import json
import pytest
import requests


from common.vocabulary_getters import (
    ApiGet,
    start_pos_api_page,
    exceeds_page,
    RORService,
)

# to enable using exceptions as typehint (copied from pytest source)
E = TypeVar("E", bound=BaseException)


def assert_all(func: Callable, tests: List[Tuple[dict, Any]], param=None):
    for test, result in tests:
        output = func(**test)
        if param is not None:
            output = getattr(output, param)
        assert output == result


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


class TestApiGet:
    test_url = "https://test.com"
    test_json = {"foo": "bar"}

    def test_ok_response(self, requests_mock):
        requests_mock.get(self.test_url, json=self.test_json)
        test_codes = [200, 201, 300]
        for code in test_codes:
            test_api = ApiGet(self.test_url)
            test_api.response.status_code = code
            assert test_api.json == self.test_json
            assert not test_api.err_msg

    def test_not_ok_response(self, requests_mock):
        requests_mock.get(self.test_url, json=self.test_json)
        test_codes = [404, 500]

        for code in test_codes:
            test_api = ApiGet(self.test_url)
            test_api.response.status_code = code
            assert not test_api.json
            assert test_api.err_msg

    def test_with_ok_url(self, requests_mock):
        requests_mock.get(self.test_url, json=self.test_json)
        tests = [
            ({"url": self.test_url}, self.test_json),
            ({"url": self.test_url, "params": {"baz": 1}}, self.test_json),
        ]
        assert_all(ApiGet, tests, param="json")

    def test_without_ok_url(self, requests_mock):
        requests_mock.get(self.test_url, status_code=404)
        tests = [
            ({"url": self.test_url}, {}),
            ({"url": self.test_url, "params": {"baz": 1}}, {}),
        ]
        assert_all(ApiGet, tests, param="json")


class TestRORService:
    R = RORService()
    mocked_url = R.search_url
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
        params = {"q": "st", "page": 1, "size": 2}
        search_result, _, size = self.R.search(params=params, identity="blah")
        assert search_result
        assert len(search_result) == 2
        assert size == 2

    def test_get_valid_id(self, requests_mock):
        requests_mock.get(f"{self.mocked_url}/{self.test_hit_id}", json=self.test_hit)
        get_result = self.R.get(
            identity="blah", item_id="ror:0442wxc77", uow="", value=""
        )
        assert get_result == self.test_hit_expected

    def test_get_invalid_id(self, requests_mock):
        requests_mock.get(f"{self.mocked_url}/{self.test_hit_id}", json=self.test_hit)
        with pytest.raises(KeyError):
            self.R.get(identity="blah", item_id="not a ROR id", uow="", value="")
