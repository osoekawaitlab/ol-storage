from ..settings import StorageSettings
from .base import BaseStorage


def create_storage(settings: StorageSettings) -> BaseStorage:
    raise NotImplementedError
