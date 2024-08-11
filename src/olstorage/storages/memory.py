from typing import Dict

from ..models import Document, DocumentId
from .base import BaseStorage


class MemoryStorage(BaseStorage):
    def __init__(self) -> None:
        self._documents: Dict[DocumentId, Document] = {}

    def __contains__(self, document_id: DocumentId) -> bool:
        return document_id in self._documents

    def create_document(self, document: Document) -> Document:
        self._documents[document.id] = document
        return self._documents[document.id]

    def get(self, document_id: DocumentId) -> Document:
        return self._documents[document_id]
