from typing import Dict

from ..models import Data, DataId
from .base import BaseBackend


class MemoryBackend(BaseBackend):
    def __init__(self) -> None:
        self._data: Dict[DataId, Data] = {}

    def has_data(self, data_id: DataId) -> bool:
        return data_id in self._data

    def add_data(self, data: Data) -> None:
        self._data[data.id] = data

    def get_data(self, data_id: DataId) -> Data:
        return self._data[data_id]

    def commit(self) -> None:
        pass
