from .models import Document, DocumentId
from .settings import StorageCoreSettings
from .storages.base import BaseStorage
from .storages.factory import create_storage


class StorageCore:
    def __init__(self, storage: BaseStorage) -> None:
        self._storage = storage

    @property
    def storage(self) -> BaseStorage:
        return self._storage

    @classmethod
    def create(cls, settings: StorageCoreSettings) -> "StorageCore":
        return cls(storage=create_storage(settings=settings.storage_settings))

    def save(self, document: Document) -> Document:
        raise NotImplementedError

    def get(self, document_id: DocumentId) -> Document:
        raise NotImplementedError
