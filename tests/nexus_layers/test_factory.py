import pytest
from pytest_mock import MockerFixture

from olstorage.nexus_layers import factory
from olstorage.settings import (
    BaseNexusLayerSettings,
    KvsNexusLayerSettings,
    MemoryBackendSettings,
    NexusLayerType,
)


def test_create_nexus_layer_raises_value_error_for_unknown_layer_type() -> None:
    settings = BaseNexusLayerSettings(type=NexusLayerType.KVS, backend_settings=MemoryBackendSettings())
    with pytest.raises(ValueError):
        factory.create_nexus_layer(settings=settings)  # type: ignore[arg-type]


def test_create_nexus_layer_returns_kvs_nexus_layer(mocker: MockerFixture) -> None:
    settings = KvsNexusLayerSettings(backend_settings=MemoryBackendSettings())
    KvsNexusLayer = mocker.patch("olstorage.nexus_layers.factory.KvsNexusLayer")
    create_backend = mocker.patch("olstorage.nexus_layers.factory.create_backend")
    actual = factory.create_nexus_layer(settings=settings)
    assert actual == KvsNexusLayer.return_value
    KvsNexusLayer.assert_called_once_with(backend=create_backend.return_value)
    create_backend.assert_called_once_with(settings=settings.backend_settings)
