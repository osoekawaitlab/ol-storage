from abc import ABC, abstractmethod

from ..models import Document, DocumentId


class BaseStorage(ABC):
    @abstractmethod
    def __contains__(self, document_id: DocumentId) -> bool:
        pass

    @abstractmethod
    def create_document(self, document: Document) -> Document:
        pass
