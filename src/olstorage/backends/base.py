from abc import ABC, abstractmethod
from typing import Generic, Hashable, Type, TypeVar

from ..models import BaseData, CollectionName, Data, DataId

DataT = TypeVar("DataT", bound=BaseData[DataId])
ExactMatchIndexT = TypeVar("ExactMatchIndexT", bound=Hashable)


class BaseIndex(ABC, Generic[DataT]):
    def __init__(self, collection_name: CollectionName) -> None:
        self._collection_name = collection_name

    @property
    def collection_name(self) -> CollectionName:
        return self._collection_name


class BaseExactMatchIndex(BaseIndex[DataT], Generic[DataT, ExactMatchIndexT]):
    @abstractmethod
    def set(self, key: ExactMatchIndexT, value: DataT) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, key: ExactMatchIndexT) -> DataT | None:
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def __contains__(self, key: ExactMatchIndexT) -> bool:
        raise NotImplementedError


class BaseBackend(ABC):
    @abstractmethod
    def has_data(self, data_id: DataId) -> bool:
        raise NotImplementedError

    @abstractmethod
    def add_data(self, data: Data) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_data(self, data_id: DataId) -> Data:
        raise NotImplementedError

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def create_exact_match_index(
        self, collection_name: CollectionName, key_type: Type[ExactMatchIndexT], value_type: Type[DataT]
    ) -> "BaseExactMatchIndex[DataT, ExactMatchIndexT]":
        raise NotImplementedError

    @abstractmethod
    def get_exact_match_index(self, collection_name: CollectionName) -> "BaseExactMatchIndex[DataT, ExactMatchIndexT]":
        raise NotImplementedError
