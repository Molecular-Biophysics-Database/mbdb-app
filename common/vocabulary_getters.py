import requests
import math
from oarepo_vocabularies.authorities.service import AuthorityService
from invenio_records_resources.services.base import LinksTemplate
from invenio_records_rest.errors import SearchPaginationRESTError


def start_pos_api_page(page: int, size: int, api_size: int) -> int:
    """helper function to calculates start position in a list that represents a page"""
    if not all([x > 0 for x in [page, size, api_size]]):
        raise ValueError(
            f"page, size and api_size must be positive numbers but was {page}, {size}, and {api_size}"
        )
    return ((page - 1) * size) % api_size


def exceeds_page(page: int, size: int, api_size: int) -> bool:
    """helper function to calculate if the page extends beyond the api_page it starts on"""
    start_pos = start_pos_api_page(page, size, api_size)
    remaining_elements_on_api_page = api_size - start_pos - (size % api_size)
    return remaining_elements_on_api_page < 0


def get_last_page(total: int, size: int) -> int:
    """helper function to calculated which page the last hits will be on"""
    if not ((total >= 0) and (size > 0)):
        raise ValueError(
            f"total and size must be positive numbers but was {total} and {size}"
        )
    return math.ceil(total / size)


def make_endpoint(
    query: str, page: int, size: int, vocabulary_type: str, url: str = None
):
    """helper function that makes an endpoint using app context"""
    # This isn't really how LinksTemplate is intended to be initialized, but we only need it for
    # the app context, so it's okay
    if not url:
        template = LinksTemplate(links=None)
        url = template.context["api"]
    return f"{url}/vocabularies/{vocabulary_type}/authoritative?q={query}&page={page}&size={size}"


def make_links(
    query: str,
    page: int,
    size: int,
    total: int,
    vocabulary_type: str,
    url: str = None,
) -> dict:
    """helper function that construct the link section of the returned dict from AuthorityService.search"""
    links = {"self": make_endpoint(query, page, size, vocabulary_type, url)}
    if page < get_last_page(total, size):
        links["next"] = make_endpoint(query, page + 1, size, vocabulary_type, url)
    return links


def hit_dict(hits: list[dict], total: int, links: dict) -> dict:
    """assembles the dict that AuthorityService.search returns"""
    return {"hits": {"total": total, "hits": hits}, "links": links}


def empty_hits(total: int, page: int) -> list:
    """helper function that raise an error if we move beyond the last page"""
    # in case there were no results, even the first page would be beyond the last page,
    # however that is not considered an error state, so we return an empty list
    if total == 0 and page == 1:
        return []
    else:
        raise SearchPaginationRESTError(
            description=f"Page '{page}' is bigger than the number of available pages",
        )


def check_response(response: requests.Response):
    """helper function that raise an error if the response didn't return ok"""
    if not response.ok:
        msg = f"{response.status_code}: {response.content}"
        raise ConnectionError(msg)


def fetch_json(url, params: dict = None):
    """helper function that makes the request and returns a json dictionary"""
    if params is None:
        params = {}
    response = requests.get(url=url, params=params)
    check_response(response)
    return response.json()


class RORService(AuthorityService):
    base_url = "https://api.ror.org/organizations"
    search_url = base_url
    get_url = f"{base_url}/"

    def search(self, *, query=None, page=1, size=10, **kwargs):
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
            # the offset is the page offset from the last page we need to fetch,
            # i.e. we fetch api_page e.g. 2, 3, 4 as offset is decreases with each iteration
            api_page = math.ceil(page * size_ratio) - offset + 1

            params = {"query": query, "page": api_page}
            response_json = fetch_json(self.search_url, params=params)
            total = response_json["number_of_results"]

            affiliations += [
                self.convert_ror_record(hit) for hit in response_json["items"]
            ]

        # make sure we don't return elements beyond the last page
        if page > get_last_page(total, size):
            hits = empty_hits(total, page)
        else:
            hits = affiliations

        # construct the return object
        start_pos = start_pos_api_page(page, size, api_size)
        hits = hits[start_pos : start_pos + size]
        links = make_links(
            query, page, size, total, vocabulary_type="affiliations", **kwargs
        )
        return hit_dict(hits, total, links)

    def get(self, item_id, **kwargs):
        if not item_id.startswith("ror:"):
            raise KeyError(f'item_id, "{item_id}", is not a ROR id')
        response_json = fetch_json(f"{self.get_url}{item_id[4:]}")
        return self.convert_ror_record(response_json)

    @staticmethod
    def convert_ror_record(hit):
        aff_entry = {
            "id": f"ror:{hit['id'].split('/')[-1]}",
            "title": {"en": hit["name"]},
            "props": {
                "city": hit["addresses"][0]["city"],
                "country": hit["country"]["country_name"],
            },
        }
        state = hit["addresses"][0].get("state")
        if state:
            aff_entry["props"]["state"] = state
        return aff_entry


class NCBIService(AuthorityService):
    base_url = "https://api.ncbi.nlm.nih.gov/datasets/v2alpha/taxonomy"
    search_url = f"{base_url}/taxon_suggest/"
    get_url = f"{base_url}/taxon/"

    def search(self, *, query=None, page=1, size=10, **kwargs):
        # paging and size cannot be supplied and I can't find documentation on how many results
        # can maximally be returned, however, 20 appears to be maximum
        api_size = 20

        params = {
            "tax_rank_filter": "higher_taxon",
            "taxon_resource_filter": "TAXON_RESOURCE_FILTER_ALL",
        }
        suggested_json = fetch_json(f"{self.search_url}{query}", params)

        try:
            taxids = suggested_json["sci_name_and_ids"]
        except KeyError:
            taxids = []
        total = len(taxids)

        # make sure we don't return elements beyond the last page
        if page > get_last_page(total, size):
            hits = empty_hits(total, page)
        else:
            hits = [self.convert_ncbi_record(hit) for hit in taxids]

        start_pos = start_pos_api_page(page, size, api_size)
        hits = hits[start_pos : start_pos + size]
        links = make_links(query, page, size, total, vocabulary_type="organisms")
        return hit_dict(hits, total, links)

    def get(self, item_id, **kwargs):
        if not item_id.startswith("taxid:"):
            raise KeyError(f'item_id, "{item_id}", is not a NCBI tax id')

        response_json = fetch_json(f"{self.get_url}{item_id[6:]}")
        record = response_json["taxonomy_nodes"][0]["taxonomy"]
        return self.convert_ncbi_record(record)

    @staticmethod
    def convert_ncbi_record(hit):
        rank = hit.get("rank")
        if not rank:
            rank = "NO RANK"

        title = hit.get("organism_name")
        if not title:
            title = hit["sci_name"]

        return {
            "id": f'taxid:{hit["tax_id"]}',
            "title": {"en": title},
            "props": {"rank": rank},
        }


class OpenAireService(AuthorityService):  # noqa
    base_url = "https://api.openaire.eu/search/projects"
    search_url = base_url
    get_url = base_url

    def search(self, *, query=None, page=1, size=10, **kwargs):
        # both page and size can be specified direct to this endpoint
        params = {"keywords": query, "page": page, "size": size, "format": "json"}
        hits = fetch_json(url=self.search_url, params=params)["response"]
        total = int(hits["header"]["total"]["$"])

        # make sure we don't return elements beyond the last page
        if page > get_last_page(total, size):
            hits = empty_hits(total, page)
        else:
            hits = [self.convert_oa_record(hit) for hit in hits["results"]["result"]]

        links = make_links(query, page, size, total, vocabulary_type="grants")
        return hit_dict(hits, total, links)

    def get(self, item_id, **kwargs):
        if not item_id.startswith("oa:"):
            raise KeyError(f'item_id, "{item_id}", is not a OpenAire id')  # noqa

        params = {"openaireProjectID": item_id[3:], "format": "json"}
        response = fetch_json(self.get_url, params=params)
        return self.convert_oa_record(response["response"]["results"]["result"][0])

    @staticmethod
    def convert_oa_record(hit):
        project = hit["metadata"]["oaf:entity"]["oaf:project"]

        try:
            funding_tree = project["fundingtree"]
            if not isinstance(funding_tree, list):
                funding_tree = [funding_tree]
            funders = set([tree["funder"]["name"]["$"] for tree in funding_tree])
            funder_name = " and ".join(funders)

        except KeyError:
            funder_name = None

        try:
            title = project["title"]["$"]
        except KeyError:
            title = "NO TITLE AVAILABLE"

        ret = {
            "id": f'oa:{hit["header"]["dri:objIdentifier"]["$"]}',
            "title": {"en": title},
            "props": {
                "grant_id": str(project["code"]["$"]),
            },
        }
        if funder_name is not None:
            ret["props"].update({"funder_name": funder_name})

        return ret


class PubChemService(AuthorityService):
    base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound"
    search_url = f"{base_url}/name/"
    get_url = f"{base_url}/InChIKey/"
    properties = "Title,MolecularFormula,MolecularWeight,InChIKey"

    def search(self, *, query=None, page=1, size=10, **kwargs):
        # neither page nor size can be specified for this endpoint
        url = f"{self.search_url}{query}/property/{self.properties}/JSON?name_type=word"
        hits = fetch_json(url)["PropertyTable"]["Properties"]
        hits = self.filter_hits(hits)  # Selecting hits with title and InChIKey

        total = len(hits)
        if page > get_last_page(total, size):
            hits = empty_hits(total, page)
        else:
            hits = [self.convert_pubchem_record(hit) for hit in hits]

        start_pos = start_pos_api_page(page, size, total)
        hits = hits[start_pos : start_pos + size]
        links = make_links(query, page, size, total, vocabulary_type="chemicals")
        return hit_dict(hits, total, links)

    def get(self, item_id, **kwargs):
        if not item_id.startswith("inchikey:"):
            raise KeyError(f'item_id, "{item_id}", is not an InchIKey')

        url = f"{self.get_url}{item_id[9:]}/property/{self.properties}/JSON"
        response = fetch_json(url)
        return self.convert_pubchem_record(response["PropertyTable"]["Properties"][0])

    @staticmethod
    def filter_hits(hits):
        return [hit for hit in hits if ("Title" in hit) and ("InChIKey" in hit)]

    @staticmethod
    def convert_pubchem_record(hit):
        formatted_data = {
            "id": f'inchikey:{hit["InChIKey"]}',
            "title": {"en": hit["Title"]},
            "chemical_formula": hit["MolecularFormula"],
            "molecular_weight": {
                    "value": float(hit["MolecularWeight"]),
                    "unit": "g/mol",
            },
            "additional_identifiers": [f"cid:{hit['CID']}"],
            }
        return formatted_data
