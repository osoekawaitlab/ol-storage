from pathlib import Path
from typing import Dict as PyDict
from typing import Type

from sqlitecollections import Dict

from ..models import CollectionName, Data, DataId
from .base import BaseBackend, BaseExactMatchIndex, DataT, ExactMatchIndexT

DATA_COLLECTION_NAME = "data"


class SqliteCollectionsBackend(BaseBackend):
    def __init__(self, file_path: Path) -> None:
        self._file_path = file_path
        self._data: None | Dict[DataId, Data] = None
        self._data_cache: PyDict[DataId, Data] = {}

    @property
    def file_path(self) -> Path:
        return self._file_path

    @property
    def data(self) -> Dict[DataId, Data]:
        if self._data is None:
            self._data = Dict(
                connection=str(self._file_path),
                table_name=DATA_COLLECTION_NAME,
                key_serializer=lambda k: k.bytes,
                key_deserializer=lambda k: DataId(k),
                value_serializer=lambda v: v.model_dump_json().encode(),
                value_deserializer=lambda v: Data.model_validate_json(v.decode()),
            )
        return self._data

    @property
    def data_cache(self) -> PyDict[DataId, Data]:
        return self._data_cache

    def add_data(self, data: Data) -> None:
        self.data_cache[data.id] = data

    def commit(self) -> None:
        self.data.update(self.data_cache)
        self.data_cache.clear()

    def has_data(self, id: DataId) -> bool:
        return id in self.data_cache or id in self.data

    def get_data(self, id: DataId) -> Data:
        res = self.data_cache.get(id, self.data.get(id))
        if res is None:
            raise KeyError(f"Data with id {id} not found")
        return res

    def create_exact_match_index(
        self, collection_name: CollectionName, key_type: Type[ExactMatchIndexT], value_type: Type[DataT]
    ) -> BaseExactMatchIndex[DataT, ExactMatchIndexT]:
        raise NotImplementedError

    def get_exact_match_index(self, collection_name: CollectionName) -> BaseExactMatchIndex[DataT, ExactMatchIndexT]:
        raise NotImplementedError
