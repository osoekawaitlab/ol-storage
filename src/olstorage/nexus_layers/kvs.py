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

    def set(self, key: Any, value: Any) -> None:
        collection_name = CollectionName.from_str("kvs.default")
        c: BaseExactMatchIndex[Any, Any]
        try:
            c = self.backend.get_exact_match_index(collection_name=collection_name)
        except KeyError:
            c = self.backend.create_exact_match_index(
                collection_name=collection_name, key_type=type(key), value_type=type(value)
            )
        c.set(key=key, value=value)

    def get(self, key: Any) -> Any:
        collection_name = CollectionName.from_str("kvs.default")
        c: BaseExactMatchIndex[Any, Any] = self.backend.get_exact_match_index(collection_name=collection_name)
        return c.get(key=key)

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, key: Any) -> bool:
        raise NotImplementedError
