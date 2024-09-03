from .backends.base import BaseBackend
from .backends.factory import create_backend
from .models import Data, DataId
from .settings import GenesisLayerSettings


class GenesisLayer:
    def __init__(self, backend: BaseBackend):
        self._backend = backend

    @property
    def backend(self) -> BaseBackend:
        return self._backend

    def save(self, data: Data) -> Data:
        if not self.backend.has_data(data_id=data.id):
            self.backend.add_data(data=data)
            self.backend.commit()
        return data

    def has_data(self, data_id: DataId) -> bool:
        return self.backend.has_data(data_id=data_id)

    def get_data(self, data_id: DataId) -> Data:
        raise NotImplementedError


def create_genesis_layer(settings: GenesisLayerSettings) -> GenesisLayer:
    backend = create_backend(settings=settings.backend_settings)
    return GenesisLayer(backend=backend)
