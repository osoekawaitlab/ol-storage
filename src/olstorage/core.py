from typing import Dict

from .errors import DataNotFoundError, InvalidNexusLayerType, NoSuchNexusLayer
from .genesis_layer import GenesisLayer, create_genesis_layer
from .models import Data, DataId
from .nexus_layers.base import BaseNexusLayer
from .nexus_layers.factory import create_nexus_layer
from .nexus_layers.kvs import KvsNexusLayer
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

    def save(self, data: Data) -> Data:
        return self.genesis_layer.save(data)

    def get(self, data_id: DataId) -> Data:
        if not self.genesis_layer.has_data(data_id=data_id):
            raise DataNotFoundError(f"Data with id {data_id} not found")
        return self.genesis_layer.get_data(data_id=data_id)

    @property
    def key_value_store(self) -> KvsNexusLayer:
        if NexusLayerType.KVS not in self.nexus_layers:
            raise NoSuchNexusLayer(layer_type=NexusLayerType.KVS)
        kvs = self.nexus_layers[NexusLayerType.KVS]
        if not isinstance(kvs, KvsNexusLayer):
            raise InvalidNexusLayerType(expected_layer_type=str(NexusLayerType.KVS), actual_layer_type=str(type(kvs)))
        return kvs

    @property
    def kvs(self) -> KvsNexusLayer:
        return self.key_value_store
