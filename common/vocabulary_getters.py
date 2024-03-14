import requests
import math
from oarepo_vocabularies.authorities.service import AuthorityService
from invenio_records_resources.services.base import LinksTemplate
from invenio_records_rest.errors import SearchPaginationRESTError


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


def make_endpoint(query: str, page: int, size: int, vocabulary_type: str):
    """helper function that makes an endpoint using app context"""
    # This isn't really how LinksTemplate is intended to be initialized, but we only need it for
    # the app context, so it's okay
    template = LinksTemplate(links=None)
    url = template.context["api"]
    return f"{url}/vocabularies/{vocabulary_type}/authoritative?q={query}&page={page}&size={size}"


def make_links(
    query: str, page: int, size: int, total: int, vocabulary_type: str
) -> dict:
    """helper function that construct the link section of the returned dict from AuthorityService.search"""
    links = {"self": make_endpoint(query, page, size, vocabulary_type)}
    if page < get_last_page(total, size):
        links["next"] = make_endpoint(query, page + 1, size, vocabulary_type)
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
            # the offset is the page offset from the last page we need to fetch,
            # i.e. we fetch api_page e.g. 2, 3, 4 as offset is decreases with each iteration
            api_page = math.ceil(page * size_ratio) - offset + 1

            params = {"query": query, "page": api_page}
            response = requests.get(url, params=params)
            response_json = response.json()
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
        hits = hits[start_pos: start_pos + size]
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
            taxids = [hit["tax_id"] for hit in suggested_json["sci_name_and_ids"]]
        except KeyError:
            taxids = []
        total = len(taxids)

        # make sure we don't return elements beyond the last page
        if page > get_last_page(total, size):
            hits = empty_hits(total, page)
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

        # note that elements in organism are not in the order they were fetched in!
        # We need to enforce they're in the same order as the taxids list,
        # as the list is a search based ranking and pagination also becomes meaningless otherwise

        order = {taxid: i for i, taxid in enumerate(taxids)}
        organisms.sort(key=lambda x: order[x["id"][6:]])
        return organisms


class OpenAireService(AuthorityService):  # noqa
    def search(self, *, query=None, page=1, size=10, **kwargs):
        # both page and size can be specified direct to this endpoint
        url = "https://api.openaire.eu/search/projects"
        params = {"keywords": query, "page": page, "size": size, "format": "json"}

        response = requests.get(url=url, params=params)
        response_json = response.json()

        total = response_json["response"]["header"]["total"]["$"]

        # make sure we don't return elements beyond the last page
        if page > get_last_page(total, size):
            hits = empty_hits(total, page)
        else:
            hits = [
                self.convert_oa_record(hit)
                for hit in response_json["response"]["results"]["result"]
            ]

        links = make_links(query, page, size, total, vocabulary_type="grants")
        return hit_dict(hits, total, links)

    def get(self, item_id, **kwargs):
        if not item_id.startswith("oa:"):
            raise KeyError(f'item_id, "{item_id}", is not a OpenAire id')  # noqa

        params = {"openaireProjectID": item_id[3:], "format": "json"}
        url = "https://api.openaire.eu/search/projects"
        response = requests.get(url, params=params).json()
        return self.convert_oa_record(response["response"]["results"]["result"][0])

    @staticmethod
    def convert_oa_record(hit):
        funding_tree = hit["metadata"]["oaf:entity"]["oaf:project"]["fundingtree"]
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

class PubChemService(AuthorityService):
    def search(self, *, query=None, page=1, size=10, **kwargs):
        # both page and size can be specified direct to this endpoint
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{query}/property/Title,MolecularFormula,MolecularWeight,InChIKey/JSON?name_type=word"
        response = requests.get(url)
        response_json = response.json()

        response_json = self.get_other_id(response_json)  # Selecting hits with title and InchiKey and adding other identifiers

        total = len(response_json)

        if page > get_last_page(total, size):
            hits = empty_hits(total, page)
        else:
            hits = [
                self.convert_pubchem_record(hit)
                for hit in response
            ]
        
        start_pos = start_pos_api_page(page, size, total) 
        hits = hits[start_pos : start_pos + size]
        links = make_links(query, page, size, total, vocabulary_type="chemical")
        return hit_dict(hits, total, links)
    

    def get_other_id(response_json):
        
        '''
        Obtain all hits with a valid Title and InChIKey, and retrieve their additional identifiers.
        '''

        response = []
        for hit in response_json["PropertyTable"]["Properties"]:
            if 'Title' in hit and 'InchiKey' in hit:
                cid = hit['CID']
                ids =[f'CID: {cid}']

                url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/{cid}/xrefs/RegistryID,RN/JSON'  # Calling Pubchem API to obtain other identifiers of the compound
                other_ids_json = requests.get(url).json()

                if 'RN' in other_ids_json:
                    ids.append(f'cas: {cas}' for cas in other_ids_json['RN'])

                elif 'CHEMBL' in other_ids_json['RegistryID']:
                    ids.append(f'chembl: {chembl}' for chembl in other_ids_json['RegistryID'] if "CHEMBL" in chembl)

            hit['additional_identifiers'] = ids
            response.append(hit)
        
        return response


    @staticmethod
    def convert_pubchem_record(hit):
        try:
            formattedData = {
                'id': f'InChiKey: {hit["InChIKey"]}',
                'title': {'en': hit['Title']},
                'props': {
                    'inchikey': hit['InChIKey'],
                    'molecular_formula': hit['MolecularFormula'],
                    'molecular_weight': hit['MolecularWeight'],
                    'additional_identifiers': hit['additional_identifiers']
                }
            }
            return formattedData
        except KeyError:
            pass

    def get(self, item_id, **kwargs):
        if not item_id.startswith("InChiKey:"):
            raise KeyError(f'item_id, "{item_id}", is not a PubChem id')
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{item_id[9:]}/property/Title,MolecularFormula,MolecularWeight,InChIKey/JSON"
        
        r = requests.get(url).json()
        r = self.get_other_id(r)
        return self.convert_pubchem_record(r[0][0])