from ..settings import MemoryStorageSettings, StorageSettings
from .base import BaseStorage
from .memory import MemoryStorage


def create_storage(settings: StorageSettings) -> BaseStorage:
    if isinstance(settings, MemoryStorageSettings):
        return MemoryStorage()
    raise ValueError("Invalid settings")
