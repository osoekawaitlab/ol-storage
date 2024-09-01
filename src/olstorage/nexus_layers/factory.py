from ..settings import NexusLayerSettings
from .base import BaseNexusLayer


def create_nexus_layer(settings: NexusLayerSettings) -> BaseNexusLayer:
    raise ValueError(f"Unknown layer type: {settings.nexus_type}")
