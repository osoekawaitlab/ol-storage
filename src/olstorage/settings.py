from enum import Enum
from typing import Annotated, Dict, Literal, Union

from oltl import NewOrExistingFilePath
from oltl.settings import BaseSettings as OltlBaseSettings
from pydantic import Field
from pydantic_settings import SettingsConfigDict


class BaseSettings(OltlBaseSettings):
    model_config = SettingsConfigDict(env_prefix="OLSTORAGE_")


class BackendType(str, Enum):
    MEMORY = "MEMORY"
    SQLITE_COLLECTIONS = "SQLITE_COLLECTIONS"


class BaseBackendSettings(BaseSettings):
    type: BackendType


class MemoryBackendSettings(BaseBackendSettings):
    type: Literal[BackendType.MEMORY] = BackendType.MEMORY


class SqliteCollectionsBackendSettings(BaseBackendSettings):
    type: Literal[BackendType.SQLITE_COLLECTIONS] = BackendType.SQLITE_COLLECTIONS
    file_path: NewOrExistingFilePath


BackendSettings = Annotated[Union[MemoryBackendSettings, SqliteCollectionsBackendSettings], Field(discriminator="type")]


class BaseBackendedSettings(BaseSettings):
    backend_settings: BackendSettings


class GenesisLayerSettings(BaseBackendedSettings): ...


class NexusLayerType(str, Enum):
    SEQUENCE = "SEQUENCE"
    KVS = "KVS"


class BaseNexusLayerSettings(BaseBackendedSettings):
    type: NexusLayerType


class KvsNexusLayerSettings(BaseNexusLayerSettings):
    type: Literal[NexusLayerType.KVS] = NexusLayerType.KVS


class SequenceNexusLayerSettings(BaseNexusLayerSettings):
    type: Literal[NexusLayerType.SEQUENCE] = NexusLayerType.SEQUENCE


NexusLayerSettings = Annotated[Union[KvsNexusLayerSettings, SequenceNexusLayerSettings], Field(discriminator="type")]


class StorageCoreSettings(BaseSettings):
    genesis_layer_settings: GenesisLayerSettings
    nexus_layers_settings: Dict[NexusLayerType, NexusLayerSettings]
