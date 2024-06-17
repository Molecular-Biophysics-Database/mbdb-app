from invenio_access.permissions import system_identity
from oarepo_vocabularies.authorities.proxies import authorities
from invenio_vocabularies.proxies import current_service as vocabulary_service
from oarepo_runtime.utils.path import PathTraversal
from invenio_pidstore.errors import PIDDoesNotExistError
from invenio_records_resources.services.records.components.base import ServiceComponent
from typing import (
    Tuple,
)


class ForeignVocabularyFetcherComponent(ServiceComponent):
    def __init__(self, service, paths=None):
        super().__init__(service=service)
        self.paths = paths
        if paths is None:
            self.paths = self.vocabulary_paths()

    def create(self, identity, data=None, **kwargs):
        self._load_if_missing(data, identity)

    def update(self, identity, data=None, **kwargs):
        self._load_if_missing(data, identity)

    def update_draft(self, identity, data=None, **kwargs):
        self._load_if_missing(data, identity)

    def _load_if_missing(self, data, identity):
        for vocabulary_type, paths in self.paths.items():
            for path in paths.iter(data):
                vocab_record = path[-1].current
                vocabulary_id = vocab_record["id"]
                if not self._stored_locally(vocabulary_id, vocabulary_type):
                    self._create(vocabulary_id, vocabulary_type, identity)

    def _create(self, vocabulary_id, vocabulary_type, identity):
        authority_service = authorities.get_authority_api(vocabulary_type)
        record = authority_service.get(
            item_id=vocabulary_id, identity=identity, uow=self.uow, value={}
        )
        if not record:
            raise ValueError(f"A record with id: {vocabulary_id} was not found")
        record["type"] = vocabulary_type
        result = vocabulary_service.create(system_identity, record)
        if result.errors:
            raise ValueError(
                f"Could not create vocabulary with id {vocabulary_id}:{result.errors=}"
            )
        vocabulary_service.indexer.refresh()

    @staticmethod
    def _stored_locally(vocabulary_id, vocabulary_type):
        try:
            vocabulary_service.read(system_identity, (vocabulary_type, vocabulary_id))
            return True
        except PIDDoesNotExistError:
            return False

    @staticmethod
    def make_paths(*paths: Tuple[str, ...]):
        return PathTraversal(["/".join(path) for path in paths])

    def vocabulary_paths(self):
        gp = "metadata/general_parameters"
        depositors = gp + "/depositors"
        entities = gp + "/entities_of_interest"
        chem_env = gp + "/chemical_environments"
        return {
            "chemicals": self.make_paths(
                (entities, "basic_information"),
                (entities, "components", "basic_information"),
                (chem_env, "constituents", "basic_information"),
                (chem_env, "solvent", "basic_information"),
            ),
            "affiliations": self.make_paths(
                (depositors, "depositor", "affiliations"),
                (depositors, "principal_contact", "affiliations"),
                (depositors, "contributors", "affiliations"),
            ),
            "grants": self.make_paths((gp, "funding_references")),
            "organisms": self.make_paths(
                (entities, "source_organism"),
                (entities, "expression_organism"),
                # virion
                (entities, "host_organism"),
                # molecular assembly -> polymer
                (entities, "components", "source_organism"),
                (entities, "components", "expression_organism"),
            ),
        }
