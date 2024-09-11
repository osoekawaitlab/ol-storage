from typing import Any

from ..backends.base import BaseBackend, BaseExactMatchIndex
from ..models import CollectionName
from .base import BaseNexusLayer


class KvsNexusLayer(BaseNexusLayer):
    def __init__(self, backend: BaseBackend) -> None:
        self._backend = backend

    @property
    def backend(self) -> BaseBackend:
        return self._backend

    def _get_default_collection_name(self) -> CollectionName:
        return CollectionName.from_str("kvs.default")

    def set(self, key: Any, value: Any) -> None:
        collection_name = self._get_default_collection_name()
        c: BaseExactMatchIndex[Any, Any]
        try:
            c = self.backend.get_exact_match_index(collection_name=collection_name)
        except KeyError:
            c = self.backend.create_exact_match_index(
                collection_name=collection_name, key_type=type(key), value_type=type(value)
            )
        c.set(key=key, value=value)

    def get(self, key: Any) -> Any:
        collection_name = self._get_default_collection_name()
        try:
            c: BaseExactMatchIndex[Any, Any] = self.backend.get_exact_match_index(collection_name=collection_name)
        except KeyError:
            return None
        return c.get(key=key)

    def __len__(self) -> int:
        collection_name = self._get_default_collection_name()
        try:
            c: BaseExactMatchIndex[Any, Any] = self.backend.get_exact_match_index(collection_name=collection_name)
        except KeyError:
            return 0
        return len(c)

    def __contains__(self, key: Any) -> bool:
        collection_name = self._get_default_collection_name()
        try:
            c: BaseExactMatchIndex[Any, Any] = self.backend.get_exact_match_index(collection_name=collection_name)
        except KeyError:
            return False
        return key in c
