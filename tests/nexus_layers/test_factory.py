import pytest

from olstorage.nexus_layers import factory
from olstorage.settings import (
    BaseNexusLayerSettings,
    MemoryBackendSettings,
    NexusLayerType,
)


def test_create_nexus_layer_raises_value_error_for_unknown_layer_type() -> None:
    settings = BaseNexusLayerSettings(type=NexusLayerType.KVS, backend_settings=MemoryBackendSettings())
    with pytest.raises(ValueError):
        factory.create_nexus_layer(settings=settings)  # type: ignore[arg-type]
