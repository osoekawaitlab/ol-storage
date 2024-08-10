from .models import Document, DocumentId
from .settings import StorageCoreSettings


class StorageCore:
    @classmethod
    def create(cls, settings: StorageCoreSettings) -> "StorageCore":
        return cls()

    def save(self, document: Document) -> Document:
        raise NotImplementedError

    def get(self, document_id: DocumentId) -> Document:
        raise NotImplementedError
