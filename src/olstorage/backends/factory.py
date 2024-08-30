from ..settings import BackendSettings, MemoryBackendSettings
from .base import BaseBackend
from .memory import MemoryBackend


def create_backend(settings: BackendSettings) -> BaseBackend:
    if isinstance(settings, MemoryBackendSettings):
        return MemoryBackend()
    raise ValueError("Invalid settings")
