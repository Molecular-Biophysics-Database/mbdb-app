import requests
import math
import flask_restful
from oarepo_vocabularies.authorities.service import AuthorityService
from invenio_records_resources.services.base import LinksTemplate


def start_pos_api_page(page: int, size: int, api_size: int) -> int:
    """helper function to calculates start position in a list that represents a page"""
    return ((page - 1) * size) % api_size


def exceeds_page(page: int, size: int, api_size: int) -> bool:
    """helper function to calculate if the page extends beyond the api_page it starts on"""
    start_pos = start_pos_api_page(page, size, api_size)
    remaining_elements_on_api_page = api_size - start_pos - (size % api_size)
    return remaining_elements_on_api_page < 0


def get_last_page(total: int, size: int) -> int:
    """helper function to calculated which page the last hits will be on"""
    return math.ceil(total / size)


def make_endpoint(query, page, size, vocabulary_type):
    """helper function make endpoint based on the app context"""
    # Not really how LinksTemplate is intended to be initialized but we only need the context so it should be okay
    template = LinksTemplate(links=None)
    url = template.context["api"]
    return f"{url}/vocabularies/{vocabulary_type}/authoritative?q={query}&page={page}&size={size}"


def make_links(query, page, size, total, vocabulary_type):
    links = {"self": make_endpoint(query, page, size, vocabulary_type)}
    if page < get_last_page(total, size):
        links["next"] = make_endpoint(query, page + 1, size, vocabulary_type)
    return links


def hit_dict(hits: list, total: int, links: dict):
    return {"hits": {"total": total, "hits": hits}, "links": links}


def empty_if_last_page(total, page):
    if total == 0 and page == 1:
        return []
    else:
        flask_restful.abort(
            400, message=f"page is bigger than the number of available pages"
        )


class RORService(AuthorityService):
    def search(self, *, query=None, page=1, size=10, **kwargs):
        url = "https://api.ror.org/organizations"

        #  the size for this API is fixed to 20 so in the following cases we should
        #  fetch multiple pages from the api:
        #   1. size > api_size
        #   2. when size > remaining element on the api_page where the page begins

        api_size = 20
        size_ratio = size / api_size
        n_api_pages = math.ceil(size_ratio) + int(exceeds_page(page, size, api_size))
        affiliations = []
        total = 0
        for offset in range(n_api_pages, 0, -1):
            api_page = math.ceil(page * size_ratio) - offset + 1
            params = {"query": query, "page": api_page}
            response = requests.get(url, params=params)
            response_json = response.json()
            total = response_json["number_of_results"]

            affiliations += [
                self.convert_ror_record(hit) for hit in response_json["items"]
            ]

        if page > get_last_page(total, size):
            hits = empty_if_last_page(total, page)
        else:
            hits = affiliations[start_pos : start_pos + size]

        # construct the return object
        start_pos = start_pos_api_page(page, size, api_size)
        links = make_links(query, page, size, total, vocabulary_type="affiliations")
        return hit_dict(hits, total, links)

    def get(self, item_id, **kwargs):
        if not item_id.startswith("ror:"):
            raise KeyError(f'item_id, "{item_id}", is not a ROR id')

        url = f"https://api.ror.org/organizations/{item_id[4:]}"
        r = requests.get(url).json()
        return self.convert_ror_record(r)

    @staticmethod
    def convert_ror_record(hit):
        return {
            "id": f"ror:{hit['id'].split('/')[-1]}",
            "title": {"en": hit["name"]},
            "props": {
                "city": hit["addresses"][0]["city"],
                "state": hit["addresses"][0]["state"],
                "country": hit["country"]["country_name"],
            },
        }


class NCBIService(AuthorityService):
    def search(self, *, query=None, page=1, size=10, **kwargs):
        # paging and size cannot be supplied and I can't find documentation on how many results
        # can maximally be returned, however, 20 appears to be maximum
        api_size = 20

        # This endpoint is unstable in terms of which hits are returned
        search_url = (
            f"https://api.ncbi.nlm.nih.gov/datasets/v1/taxonomy/taxon_suggest/{query}"
        )
        suggested = requests.get(search_url)
        suggested_json = suggested.json()

        try:
            taxids = [
                hit["tax_id"] for hit in suggested_json["sci_name_and_ids"]
            ]  # noqa
        except KeyError:
            taxids = []
        total = len(taxids)

        # make sure we don't return elements beyond the last page
        if page > get_last_page(total, size):
            hits = empty_if_last_page(total, page)
        else:
            hits = self.from_taxid(taxids)

        start_pos = start_pos_api_page(page, size, api_size)
        hits = hits[start_pos : start_pos + size]
        links = make_links(query, page, size, total, vocabulary_type="organisms")
        return hit_dict(hits, total, links)

    def get(self, item_id, **kwargs):
        if not item_id.startswith("taxid:"):
            raise KeyError(f'item_id, "{item_id}", is not a NCBI tax id')

        return self.from_taxid([item_id[6:]])[0]

    @staticmethod
    def convert_ncbi_record(hit):
        try:
            rank = hit["rank"]
        except KeyError:
            rank = "NO RANK"
        return {
            "id": f'taxid:{hit["tax_id"]}',
            "title": {"en": hit["organism_name"]},
            "props": {"rank": rank},
        }

    def from_taxid(self, taxids):
        taxid_url = "https://api.ncbi.nlm.nih.gov/datasets/v1/taxonomy/taxon/"
        taxid_params = {"returned_content": "TAXIDS"}  # noqa

        response = requests.get(f"{taxid_url}{','.join(taxids)}", params=taxid_params)
        organisms = []
        for hit in response.json()["taxonomy_nodes"]:
            hit = hit["taxonomy"]
            organisms.append(self.convert_ncbi_record(hit))

        # note that elements in organism are not in the order they were supplied in!
        # We need to enforce they're in the same order the taxids list,
        # as the list is a search based ranking and pagination also becomes meaningless otherwise

        order = {taxid: i for i, taxid in enumerate(taxids)}
        organisms.sort(key=lambda x: order[x["id"][6:]])
        return organisms


class OpenAireService(AuthorityService):  # noqa
    def search(self, *, query=None, page=1, size=10, **kwargs):
        # both page and size can be specified for the endpoint
        url = "https://api.openaire.eu/search/projects"
        params = {"keywords": query, "page": page, "size": size, "format": "json"}

        response = requests.get(url=url, params=params)
        response_json = response.json()

        total = response_json["response"]["header"]["total"]["$"]

        if page > get_last_page(total, size):
            grants = empty_if_last_page(total, page)
        else:
            grants = [
                self.convert_oa_record(hit)
                for hit in response_json["response"]["results"]["result"]
            ]

        links = make_links(query, page, size, total, vocabulary_type="grants")
        return hit_dict(grants, total, links)

    def get(self, item_id, **kwargs):
        if not item_id.startswith("oa:"):
            raise KeyError(f'item_id, "{item_id}", is not a OpenAire id')  # noqa

        params = {"openaireProjectID": item_id[3:], "format": "json"}
        url = "https://api.openaire.eu/search/projects"
        response = requests.get(url, params=params).json()
        return self.convert_oa_record(response["response"]["results"]["result"][0])

    @staticmethod
    def convert_oa_record(hit):
        funding_tree = hit["metadata"]["oaf:entity"]["oaf:project"][
            "fundingtree"
        ]  # noqa
        if not isinstance(funding_tree, list):
            funding_tree = [funding_tree]

        funders = set([tree["funder"]["name"]["$"] for tree in funding_tree])
        funder_name = " and ".join(funders)

        try:
            title = hit["metadata"]["oaf:entity"]["oaf:project"]["title"]["$"]
        except KeyError:
            title = "NO TITLE AVAILABLE"

        return {
            "id": f'oa:{hit["header"]["dri:objIdentifier"]["$"]}',
            "title": {"en": title},
            "props": {
                "grant_id": str(
                    hit["metadata"]["oaf:entity"]["oaf:project"]["code"]["$"]
                ),
                "funder_name": funder_name,
            },
        }
