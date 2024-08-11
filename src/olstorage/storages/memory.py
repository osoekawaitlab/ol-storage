from olstorage.models import Document, DocumentId

from .base import BaseStorage


class MemoryStorage(BaseStorage):
    def __contains__(self, document_id: DocumentId) -> bool:
        raise NotImplementedError

    def create_document(self, document: Document) -> Document:
        raise NotImplementedError
