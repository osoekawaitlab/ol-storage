from pytest_mock import MockerFixture

from olstorage.core import StorageCore
from olstorage.settings import (
    GenesisLayerSettings,
    KvsNexusLayerSettings,
    MemoryBackendSettings,
    NexusLayerType,
    StorageCoreSettings,
)


def test_core_create(mocker: MockerFixture) -> None:
    create_genesis_layer = mocker.patch("olstorage.core.create_genesis_layer")
    create_nexus_layer = mocker.patch("olstorage.core.create_nexus_layer")
    settings = StorageCoreSettings(
        genesis_layer_settings=GenesisLayerSettings(backend_settings=MemoryBackendSettings()),
        nexus_layers_settings={NexusLayerType.KVS: KvsNexusLayerSettings(backend_settings=MemoryBackendSettings())},
    )
    actual = StorageCore.create(settings=settings)
    create_genesis_layer.assert_called_once_with(settings=settings.genesis_layer_settings)
    create_nexus_layer.assert_called_once_with(settings=settings.nexus_layers_settings[NexusLayerType.KVS])
    assert actual.genesis_layer == create_genesis_layer.return_value
    assert actual.nexus_layers == {NexusLayerType.KVS: create_nexus_layer.return_value}
