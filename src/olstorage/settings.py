from enum import Enum
from typing import Annotated, Literal

from oltl.settings import BaseSettings as OltlBaseSettings
from pydantic import Field
from pydantic_settings import SettingsConfigDict


class BaseSettings(OltlBaseSettings):
    model_config = SettingsConfigDict(env_prefix="OLSTORAGE_")


class BackendType(str, Enum):
    MEMORY = "MEMORY"


class BaseBackendSettings(BaseSettings):
    type: BackendType


class MemoryStorageSettings(BaseBackendSettings):
    type: Literal[BackendType.MEMORY] = BackendType.MEMORY


BackendSettings = Annotated[MemoryStorageSettings, Field(discriminator="type")]


class StorageType(str, Enum):
    BLOB = "BLOB"
    KEY_VALUE = "KEY_VALUE"
    VECTOR = "VECTOR"


class BaseStorageSettings(BaseSettings):
    type: StorageType
    backend_settings: BackendSettings


StorageSettings = Annotated[MemoryStorageSettings, Field(discriminator="type")]


class StorageCoreSettings(BaseSettings):
    storage_settings: StorageSettings
