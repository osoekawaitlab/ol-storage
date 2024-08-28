from enum import Enum
from typing import Annotated, List, Literal

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


class LayerType(str, Enum):
    GENESIS = "GENESIS"
    NEXUS = "NEXUS"


class BaseLayerSettings(BaseSettings):
    layer_type: LayerType
    backend_settings: BackendSettings


class GenesisLayerSettings(BaseLayerSettings):
    layer_type: Literal[LayerType.GENESIS] = LayerType.GENESIS


class NexusLayerType(str, Enum):
    KVS = "KVS"


class BaseNexusLayerSettings(BaseLayerSettings):
    layer_type: Literal[LayerType.NEXUS] = LayerType.NEXUS
    nexus_type: NexusLayerType


class KvsNexusLayerSettings(BaseNexusLayerSettings):
    nexus_type: Literal[NexusLayerType.KVS] = NexusLayerType.KVS


NexusLayerSettings = Annotated[KvsNexusLayerSettings, Field(discriminator="nexus_type")]


class StorageSettings(BaseSettings):
    genesis_layer_settings: GenesisLayerSettings
    nexus_layers_settings: List[NexusLayerSettings]
