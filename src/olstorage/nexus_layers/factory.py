from ..settings import NexusLayerSettings
from .base import BaseNexusLayer


def create_nexus_layer(settings: NexusLayerSettings) -> BaseNexusLayer:
    raise NotImplementedError
