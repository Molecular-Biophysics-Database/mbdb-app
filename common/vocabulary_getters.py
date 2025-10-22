import requests
import math
from oarepo_vocabularies.authorities.providers import AuthorityProvider



class ApiGet:
    """Helper class to get data from an api endpoint."""
    def __init__(self, url, params: dict = None):
        self.url = url
        self.params = params or {}
        self.response: requests.Response = requests.get(url, params=params)
        self.err_msg = None

    @property
    def json(self):
        """Returns the json response from the api endpoint.
        Raises ConnectionError if response isn't ok."""
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


class RORServiceV1(AuthorityProvider):
    """API v1 compatible ROR AuthorityProvider for affiliations"""
    search_url = "https://api.ror.org/v1/organizations"
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
        """Converts schema/API version 1 of a ROR record to a MBDB vocabulary record."""
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

    @staticmethod
    def convert_ror_record(affiliation):
        """Converts schema/API version 2.1 of a ROR record to a MBDB vocabulary record."""

        # Information is only extracted from the first elements in titles and locations
        aff_entry = {
            "id": f"ror:{affiliation['id'].split('/')[-1]}",
            "title": {"en": affiliation["names"][0]["value"]},
            "props": {
                "city": affiliation["locations"][0]["geonames_details"]["name"],
                "country": affiliation["locations"][0]["geonames_details"]["country_name"],
            },
        }
        state = affiliation["locations"][0]["geonames_details"].get("country_subdivision_name")
        if state:
            aff_entry["props"]["state"] = state
        return aff_entry

class RORServiceV2(AuthorityProvider):
    """API v2 compatible ROR AuthorityProvider for affiliations"""
    search_url = "https://api.ror.org/v2/organizations"
    get_url = f"{search_url}/"

    def search(self, identity, params, **kwargs):
        # ROR API uses a fixed page size of 20
        page = params.get("page", 1)
        size = params.get("size", 10)
        api_size = 20

        size_ratio = size / api_size
        n_api_pages = math.ceil(size_ratio) + int(exceeds_page(page, size, api_size))
        affiliations = []
        total = 0

        for offset in range(n_api_pages, 0, -1):
            api_page = math.ceil(page * size_ratio) - offset + 1
            q_params = {"query": params.get("q", ""), "page": api_page}

            json = ApiGet(url=self.search_url, params=q_params).json
            total = json.get("number_of_results", 0)
            items = json.get("items", [])
            affiliations += [self.convert_ror_record(aff) for aff in items]

        start_pos = start_pos_api_page(page, size, api_size)
        return affiliations[start_pos:start_pos + size], total, size

    def get(self, identity, item_id, *, uow, value, **kwargs):
        if not item_id.startswith("ror:"):
            raise KeyError(f'item_id "{item_id}" is not a valid ROR id')
        json = ApiGet(url=f"{self.get_url}{item_id[4:]}").json
        return self.convert_ror_record(json)

    @staticmethod
    def convert_ror_record(affiliation):
        """Converts schema/API version 2.1 of a ROR record to MBDB vocabulary format."""
        try:
            name = affiliation["names"][0]["value"]
        except (KeyError, IndexError):
            name = affiliation.get("name", "Unknown Organization")

        try:
            geo = affiliation["locations"][0]["geonames_details"]
            city = geo.get("name")
            country = geo.get("country_name")
            state = geo.get("country_subdivision_name")
        except (KeyError, IndexError, TypeError):
            city = country = state = None
            geo = {}

        aff_entry = {
            "id": f"ror:{affiliation['id'].split('/')[-1]}",
            "title": {"en": name},
            "props": {},
        }

        if city:
            aff_entry["props"]["city"] = city
        if country:
            aff_entry["props"]["country"] = country
        if state:
            aff_entry["props"]["state"] = state

        lat = geo.get("latitude")
        lon = geo.get("longitude")
        if lat is not None and lon is not None:
            aff_entry["props"]["coordinates"] = {"lat": lat, "lon": lon}

        return aff_entry

class RORService(RORServiceV2):
    """ROR AuthorityProvider for affiliations"""
    pass


class NCBIService(AuthorityProvider):
    """API v2 compatible NCBI AuthorityProvider for organisms"""
    base_url = "https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy"
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
        """Converts V2 of an NCBI record to a MBDB vocabulary record."""
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


class OpenAireService(AuthorityProvider):
    """OpenAire AuthorityProvider for grants"""
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
        """Converts an openAIRE record to a MBDB vocabulary record."""
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
    """PubChem AuthorityProvider for chemicals"""

    # The PUG-REST API of PubChem is full of idiosyncrasies and is poorly
    # Documented which makes it rather difficult to work with. Hence, this
    # class is help together with programming ducttape. Be careful when
    # changing things.

    base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound"
    search_url = f"{base_url}/name/"
    get_url = f"{base_url}/InChIKey/"
    properties = "Title,MolecularFormula,MolecularWeight,InChIKey"

    def search(self, identity, params, **kwargs):
        # neither page nor size can be specified for this endpoint
        size = params.get("size", 10)
        query = params.get("q", "")

        url = f"{self.search_url}{query}/property/{self.properties}/JSON?name_type=word"
        chemicals = self.modified_api_get(url)
        chemicals = self.filter_hits(chemicals)

        total = len(chemicals)
        chemicals = [self.convert_pubchem_record(chem) for chem in chemicals]
        # all records are returned on a single page
        start_pos = start_pos_api_page(params.get("page", 1), size, (total or 1))
        return chemicals[start_pos : start_pos + size], total, size

    def get(self, identity, item_id, *, uow, value, **kwargs):
        if not item_id.startswith("inchikey:"):
            raise KeyError(f'item_id, "{item_id}", is not an InchIKey')

        url = f"{self.get_url}{item_id[9:]}/property/{self.properties}/JSON"
        records = self.filter_hits(self.modified_api_get(url))
        return self.convert_pubchem_record(records[0])

    def filter_hits(self, hits):
        """Helper function to remove incomplete Pubchem records."""
        
        # Occasionally, there are  multiple CID for the same compound (e.g. 5'-GMP)
        # even though this shouldn't happen. In those case there seem to
        # be a single preferred record (explicit documentation of this has not
        # been found). The non-preferred are marked by being incomplete,
        # in particular, the (mandatory) title is often missing.
        complete_records = []
        for hit in hits:
            try:
                self.convert_pubchem_record(hit)
                complete_records.append(hit)
            except KeyError:
                continue
        return complete_records

    @staticmethod
    def modified_api_get(url):
        """
        Adapter function that catches the 404 error returned when no results
        are found and returns an empty dict instead.
        """

        chemicals = ApiGet(url)
        if chemicals.response.ok:
            return chemicals.json["PropertyTable"]["Properties"]
        # 404 means the no results were found. In case the endpoint
        # changes this might unfortunately lead to silently catching this error
        elif chemicals.response.status_code == 404:
            return {}
        # Server errors and other problems will be handled by ApiGet as usual
        else:
            return chemicals.json

    @staticmethod
    def convert_pubchem_record(chemical):
        """converts a PubChem record to a MBDB vocabulary record."""
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
