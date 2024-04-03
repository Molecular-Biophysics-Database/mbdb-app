from oarepo_vocabularies.authorities.proxies import authorities
from oarepo_vocabularies.proxies import current_type_service
from oarepo_runtime.utils.path import PathTraversal
from invenio_pidstore.errors import PIDDoesNotExistError


class ForeignVocabularyFetcher:
    def __init__(self, data, paths=None):
        self.data = data
        self.paths = paths
        if paths is None:
            self.paths = self.vocabulary_paths()
        self._load_if_missing()

    @property
    def _paths(self):
        return PathTraversal(self.paths)

    def _load_if_missing(self):
        for path in self._paths.iter(self.data):
            vocab_record = path[-1].current
            vocabulary_id, vocabulary_type = vocab_record["id"], vocab_record["type"]
            if not self._stored_locally(vocabulary_id, vocabulary_type):
                self._create(vocabulary_id, vocabulary_type)

    @staticmethod
    def _create(vocabulary_id, vocabulary_type):
        authority_service = authorities.get_authority_api(vocabulary_type)
        record = authority_service.get(vocabulary_id)
        if not record:
            raise ValueError(f"A record with id: {vocabulary_id} was not found")
        vocabulary = current_type_service.get(vocabulary_type)
        vocabulary.create(record)

    @staticmethod
    def _stored_locally(vocabulary_id, vocabulary_type):
        vocabulary = current_type_service.get(vocabulary_type)
        try:
            vocabulary.get(vocabulary_id)
            return True
        except PIDDoesNotExistError:
            return False

    @staticmethod
    def make_path(*args: str):
        args = [arg for arg in args]
        return ".".join(args)

    def vocabulary_paths(self):
        gp = "metadata.general_parameters"
        depositors = self.make_path(gp, "depositors")
        entities = self.make_path(gp, "entities_of_interest")

        paths = [
            (depositors, "depositors", "affiliations"),
            (depositors, "principal_contact", "affiliations"),
            (depositors, "contributors", "affiliations"),
            (gp, "funding_references"),
            # polymer
            (entities, "source_organism"),
            (entities, "expression_organism"),
            # virion
            (entities, "host_organism"),
            # molecular assembly -> polymer
            (entities, "components", "source_organism"),
            (entities, "components", "expression_organism"),
        ]
        return [self.make_path(*path) for path in paths]
