from ..models import Data, DataId
from .base import BaseBackend


class MemoryBackend(BaseBackend):
    def has_data(self, data_id: DataId) -> bool:
        raise NotImplementedError

    def add_data(self, data: Data) -> None:
        raise NotImplementedError

    def commit(self) -> None:
        raise NotImplementedError
