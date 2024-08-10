from enum import Enum
from typing import Annotated, Literal

from oltl.settings import BaseSettings as OltlBaseSettings
from pydantic import Field
from pydantic_settings import SettingsConfigDict


class BaseSettings(OltlBaseSettings):
    model_config = SettingsConfigDict(env_prefix="OLSTORAGE_")


class StorageType(str, Enum):
    MEMORY = "MEMORY"


class BaseStorageSettings(BaseSettings):
    type: StorageType


class MemoryStorageSettings(BaseStorageSettings):
    type: Literal[StorageType.MEMORY] = StorageType.MEMORY


StorageSettings = Annotated[MemoryStorageSettings, Field(discriminator="type")]


class StorageCoreSettings(BaseSettings):
    storage_settings: StorageSettings
