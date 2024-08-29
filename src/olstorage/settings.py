from enum import Enum
from typing import Annotated, Dict, Literal

from oltl.settings import BaseSettings as OltlBaseSettings
from pydantic import Field
from pydantic_settings import SettingsConfigDict


class BaseSettings(OltlBaseSettings):
    model_config = SettingsConfigDict(env_prefix="OLSTORAGE_")


class BackendType(str, Enum):
    MEMORY = "MEMORY"


class BaseBackendSettings(BaseSettings):
    type: BackendType


class MemoryBackendSettings(BaseBackendSettings):
    type: Literal[BackendType.MEMORY] = BackendType.MEMORY


BackendSettings = Annotated[MemoryBackendSettings, Field(discriminator="type")]


class BaseBackendedSettings(BaseSettings):
    backend_settings: BackendSettings


class GenesisLayerSettings(BaseBackendedSettings): ...


class NexusLayerType(str, Enum):
    KVS = "KVS"


class BaseNexusLayerSettings(BaseBackendedSettings):
    nexus_type: NexusLayerType


class KvsNexusLayerSettings(BaseNexusLayerSettings):
    nexus_type: Literal[NexusLayerType.KVS] = NexusLayerType.KVS


NexusLayerSettings = Annotated[KvsNexusLayerSettings, Field(discriminator="nexus_type")]


class StorageCoreSettings(BaseSettings):
    genesis_layer_settings: GenesisLayerSettings
    nexus_layers_settings: Dict[NexusLayerType, NexusLayerSettings]
