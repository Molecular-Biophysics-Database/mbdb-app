import requests
import math
from oarepo_vocabularies.authorities.providers import AuthorityProvider



class ApiGet:
    def __init__(self, url, params: dict = None):
        self.url = url
        self.params = params or {}
        self.response: requests.Response = requests.get(url, params=params)
        self.err_msg = None

    @property
    def json(self):
        if not self.response.ok:
            self.err_msg = f"status: {self.response.status_code}, content: {self.response.content}"
            raise ConnectionError(self.err_msg)
        return self.response.json()

    def __repr__(self):
        return f"<ApiGet(status_code={self.response.status_code})>)"


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


class RORService(AuthorityProvider):
    search_url = "https://api.ror.org/organizations"
    get_url = f"{search_url}/"

    def search(self, identity, params, **kwargs):
        #  the size for this API is fixed to 20 so in the following cases we should
        #  fetch multiple pages from the api:
        #   1. size > api_size
        #   2. when size > remaining element on the api_page where the page begins
        page = params.get("page", 1)
        size = params.get("size", 10)

        api_size = 20
        size_ratio = size / api_size
        n_api_pages = math.ceil(size_ratio) + int(exceeds_page(page, size, api_size))
        affiliations = []
        total = 0

        for offset in range(n_api_pages, 0, -1):
            # the offset is the page offset from the last page we need to fetch,
            # i.e. we fetch api_page e.g. 2, 3, 4 as offset is decreases with each iteration
            api_page = math.ceil(page * size_ratio) - offset + 1

            q_params = {"query": params.get("q", ""), "page": api_page}
            json = ApiGet(url=self.search_url, params=q_params).json
            total = json["number_of_results"]

            affiliations += [self.convert_ror_record(aff) for aff in json["items"]]

        # construct the return object
        start_pos = start_pos_api_page(page, size, api_size)
        return affiliations[start_pos : start_pos + size], total, size

    def get(self, identity, item_id, *, uow, value, **kwargs):
        if not item_id.startswith("ror:"):
            raise KeyError(f'item_id, "{item_id}", is not a ROR id')
        json = ApiGet(url=f"{self.get_url}{item_id[4:]}").json
        return self.convert_ror_record(json)

    @staticmethod
    def convert_ror_record(affiliation):
        aff_entry = {
            "id": f"ror:{affiliation['id'].split('/')[-1]}",
            "title": {"en": affiliation["name"]},
            "props": {
                "city": affiliation["addresses"][0]["city"],
                "country": affiliation["country"]["country_name"],
            },
        }
        state = affiliation["addresses"][0].get("state")
        if state:
            aff_entry["props"]["state"] = state
        return aff_entry


class NCBIService(AuthorityProvider):
    base_url = "https://api.ncbi.nlm.nih.gov/datasets/v2alpha/taxonomy"
    search_url = f"{base_url}/taxon_suggest/"
    get_url = f"{base_url}/taxon/"

    def search(self, identity, params, **kwargs):
        # paging and size cannot be supplied and I can't find documentation on how many results
        # can maximally be returned, however, 20 appears to be maximum
        size = params.get("size", 10)
        query = params.get("q", "")
        api_size = 20

        q_params = {
            "tax_rank_filter": "higher_taxon",
            "taxon_resource_filter": "TAXON_RESOURCE_FILTER_ALL",
        }

        hits = ApiGet(f"{self.search_url}{query}", q_params).json

        organisms = hits.get("sci_name_and_ids", [])
        total = len(organisms)
        organisms = [self.convert_ncbi_record(org) for org in organisms]
        start_pos = start_pos_api_page(params.get("page", 1), size, api_size)

        return organisms[start_pos : start_pos + size], total, size

    def get(self, identity, item_id, *, uow, value, **kwargs):
        if not item_id.startswith("taxid:"):
            raise KeyError(f'item_id, "{item_id}", is not a NCBI tax id')

        response_json = ApiGet(f"{self.get_url}{item_id[6:]}").json
        record = response_json["taxonomy_nodes"][0]["taxonomy"]
        return self.convert_ncbi_record(record)

    @staticmethod
    def convert_ncbi_record(organism):
        rank = organism.get("rank")
        if not rank:
            rank = "NO RANK"

        title = organism.get("organism_name")
        if not title:
            title = organism["sci_name"]

        return {
            "id": f'taxid:{organism["tax_id"]}',
            "title": {"en": title},
            "props": {"rank": rank},
        }


class OpenAireService(AuthorityProvider):  # noqa
    search_url = "https://api.openaire.eu/search/projects"
    get_url = search_url

    def search(self, identity, params, **kwargs):
        # both page and size can be specified directly to this endpoint
        size = params.get("size", 10)

        q_params = {
            "keywords": params.get("q", ""),
            "page": params.get("page", 1),
            "size": size,
            "format": "json",
        }
        hits = ApiGet(url=self.search_url, params=q_params).json["response"]
        total = int(hits["header"]["total"]["$"])

        grants = [self.convert_oa_record(hit) for hit in hits["results"]["result"]]

        return grants, total, size

    def get(self, identity, item_id, *, uow, value, **kwargs):
        if not item_id.startswith("oa:"):
            raise KeyError(f'item_id, "{item_id}", is not a OpenAire id')  # noqa

        params = {"openaireProjectID": item_id[3:], "format": "json"}
        response = ApiGet(self.get_url, params=params).json
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
        if funder_name:
            ret["props"].update({"funder_name": funder_name})

        return ret


class PubChemService(AuthorityProvider):
    base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound"
    search_url = f"{base_url}/name/"
    get_url = f"{base_url}/InChIKey/"
    properties = "Title,MolecularFormula,MolecularWeight,InChIKey"

    def search(self, identity, params, **kwargs):
        # neither page nor size can be specified for this endpoint
        size = params.get("size", 10)
        query = params.get("q", "")

        url = f"{self.search_url}{query}/property/{self.properties}/JSON?name_type=word"
        chemicals = ApiGet(url).json["PropertyTable"]["Properties"]
        chemicals = self.filter_hits(chemicals)

        total = len(chemicals)
        chemicals = [self.convert_pubchem_record(chem) for chem in chemicals]
        start_pos = start_pos_api_page(params.get("page", 1), size, total)
        return chemicals[start_pos : start_pos + size], total, size

    def get(self, identity, item_id, *, uow, value, **kwargs):
        if not item_id.startswith("inchikey:"):
            raise KeyError(f'item_id, "{item_id}", is not an InchIKey')

        url = f"{self.get_url}{item_id[9:]}/property/{self.properties}/JSON"
        response = ApiGet(url).json
        records = self.filter_hits(response["PropertyTable"]["Properties"])
        return self.convert_pubchem_record(records[0])

    def filter_hits(self, hits):
        # Occasionally, multiple CID for the same compound (e.g. 5'-GMP)
        # even though this shouldn't happen. In those case there seem to
        # be a single preferred record. The non-preferred are marked
        # by being incomplete, especially the title are often missing. This
        # function filters these away.
        complete_records = []
        for hit in hits:
            try:
                self.convert_pubchem_record(hit)
                complete_records.append(hit)
            except KeyError:
                continue
        return complete_records

    @staticmethod
    def convert_pubchem_record(chemical):
        return {
            "id": f'inchikey:{chemical["InChIKey"]}',
            "title": {"en": chemical["Title"]},
            "chemical_formula": chemical["MolecularFormula"],
            "molecular_weight": {
                "value": float(chemical["MolecularWeight"]),
                "unit": "g/mol",
            },
            "additional_identifiers": [f"cid:{chemical['CID']}"],
        }
