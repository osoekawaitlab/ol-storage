from typing import Any, Dict, Generic, Type

from ..models import CollectionName, Data, DataId
from .base import BaseBackend, BaseExactMatchIndex, DataT, ExactMatchIndexT


class MemoryExactMatchIndex(BaseExactMatchIndex[DataT, ExactMatchIndexT], Generic[DataT, ExactMatchIndexT]):
    def __init__(self, collection_name: CollectionName) -> None:
        super(MemoryExactMatchIndex, self).__init__(collection_name=collection_name)
        self._data: Dict[ExactMatchIndexT, DataT] = {}


class MemoryBackend(BaseBackend):
    def __init__(self) -> None:
        self._data: Dict[DataId, Data] = {}
        self._exact_match_indexes: Dict[CollectionName, MemoryExactMatchIndex[Any, Any]] = {}

    def has_data(self, data_id: DataId) -> bool:
        return data_id in self._data

    def add_data(self, data: Data) -> None:
        self._data[data.id] = data

    def get_data(self, data_id: DataId) -> Data:
        return self._data[data_id]

    def commit(self) -> None:
        pass

    def get_or_create_exact_match_index(
        self, collection_name: CollectionName, key_type: Type[ExactMatchIndexT], value_type: Type[DataT]
    ) -> BaseExactMatchIndex[DataT, ExactMatchIndexT]:
        if collection_name not in self._exact_match_indexes:
            self._exact_match_indexes[collection_name] = MemoryExactMatchIndex[DataT, ExactMatchIndexT](
                collection_name=collection_name
            )
        return self._exact_match_indexes[collection_name]
