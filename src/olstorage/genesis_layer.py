from .backends.base import BaseBackend
from .backends.factory import create_backend
from .models import Data
from .settings import GenesisLayerSettings


class GenesisLayer:
    def __init__(self, backend: BaseBackend):
        self._backend = backend

    @property
    def backend(self) -> BaseBackend:
        return self._backend

    def save(self, data: Data) -> Data:
        raise NotImplementedError


def create_genesis_layer(settings: GenesisLayerSettings) -> GenesisLayer:
    backend = create_backend(settings=settings.backend_settings)
    return GenesisLayer(backend=backend)
