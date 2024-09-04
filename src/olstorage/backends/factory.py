from ..settings import (
    BackendSettings,
    MemoryBackendSettings,
    SqliteCollectionsBackendSettings,
)
from .base import BaseBackend
from .memory import MemoryBackend
from .sqlitecollections import SqliteCollectionsBackend


def create_backend(settings: BackendSettings) -> BaseBackend:
    if isinstance(settings, MemoryBackendSettings):
        return MemoryBackend()
    elif isinstance(settings, SqliteCollectionsBackendSettings):
        return SqliteCollectionsBackend(file_path=settings.file_path)
    raise ValueError("Invalid settings")
