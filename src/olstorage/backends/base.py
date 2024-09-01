from abc import ABC, abstractmethod

from ..models import Data, DataId


class BaseBackend(ABC):
    @abstractmethod
    def has_data(self, data_id: DataId) -> bool:
        raise NotImplementedError

    @abstractmethod
    def add_data(self, data: Data) -> None:
        raise NotImplementedError

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError
