
from invenio_records_resources.services.files.components.processor import FileProcessorComponent
from invenio_records_resources.services.uow import Operation
from invenio_records_resources.tasks import extract_file_metadata
from invenio_records_resources.proxies import current_service_registry

class SynchronousTaskOp(Operation):
    """A celery task operation.

    Celery tasks are always execute after the entire commit phase.
    """

    def __init__(self, processor, *args, **kwargs):
        """Initialize the task operation."""
        self._processor_task = processor
        self._args = args
        self._kwargs = kwargs

    def on_post_commit(self, uow):
        """Run the post task operation."""
        self._processor_task(*self._args, **self._kwargs)



class SynchronousFileProcessorComponent(FileProcessorComponent):
    def commit_file(self, identity, id, file_key, record):
        """Post commit file handler."""
        # Ship off a task to extract file metadata once a file is committed.
        service_id = current_service_registry.get_service_id(self.service)
        self.uow.register(SynchronousTaskOp(extract_file_metadata, service_id, id, file_key))
