from pytest_mock import MockerFixture

from olstorage import genesis_layer
from olstorage.settings import GenesisLayerSettings, MemoryBackendSettings


def test_create_genesis_layer(mocker: MockerFixture) -> None:
    create_backend = mocker.patch("olstorage.genesis_layer.create_backend")
    settings = GenesisLayerSettings(backend_settings=MemoryBackendSettings())
    actual = genesis_layer.create_genesis_layer(settings=settings)
    create_backend.assert_called_once_with(settings=settings.backend_settings)
    assert isinstance(actual, genesis_layer.GenesisLayer)
    assert actual.backend == create_backend.return_value
