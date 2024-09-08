from ..backends.factory import create_backend
from ..settings import KvsNexusLayerSettings, NexusLayerSettings
from .base import BaseNexusLayer
from .kvs import KvsNexusLayer


def create_nexus_layer(settings: NexusLayerSettings) -> BaseNexusLayer:
    if isinstance(settings, KvsNexusLayerSettings):
        return KvsNexusLayer(backend=create_backend(settings=settings.backend_settings))
    raise ValueError(f"Unknown layer type: {settings.type}")
