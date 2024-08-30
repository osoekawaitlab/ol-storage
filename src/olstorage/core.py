from typing import Dict

from .genesis_layer import GenesisLayer, create_genesis_layer
from .nexus_layers.base import BaseNexusLayer
from .nexus_layers.factory import create_nexus_layer
from .settings import NexusLayerType, StorageCoreSettings


class StorageCore:
    def __init__(self, genesis_layer: GenesisLayer, nexus_layers: Dict[NexusLayerType, BaseNexusLayer]):
        self._genesis_layer = genesis_layer
        self._nexus_layers = nexus_layers

    @property
    def genesis_layer(self) -> GenesisLayer:
        return self._genesis_layer

    @property
    def nexus_layers(self) -> Dict[NexusLayerType, BaseNexusLayer]:
        return self._nexus_layers

    @classmethod
    def create(cls, settings: StorageCoreSettings) -> "StorageCore":
        genesis_layer = create_genesis_layer(settings=settings.genesis_layer_settings)
        nexus_layers = {
            layer_type: create_nexus_layer(settings=layer_settings)
            for layer_type, layer_settings in settings.nexus_layers_settings.items()
        }
        return cls(genesis_layer=genesis_layer, nexus_layers=nexus_layers)
