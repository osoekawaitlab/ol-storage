from pytest_mock import MockerFixture

from olstorage import genesis_layer
from olstorage.backends.base import BaseBackend
from olstorage.models import Data, DataId
from olstorage.settings import GenesisLayerSettings, MemoryBackendSettings


def test_create_genesis_layer(mocker: MockerFixture) -> None:
    create_backend = mocker.patch("olstorage.genesis_layer.create_backend")
    settings = GenesisLayerSettings(backend_settings=MemoryBackendSettings())
    actual = genesis_layer.create_genesis_layer(settings=settings)
    create_backend.assert_called_once_with(settings=settings.backend_settings)
    assert isinstance(actual, genesis_layer.GenesisLayer)
    assert actual.backend == create_backend.return_value


def test_genesis_layer_save_new_data(mocker: MockerFixture) -> None:
    backend = mocker.Mock(spec=BaseBackend)
    backend.has_data.return_value = False
    genesis_layer_instance = genesis_layer.GenesisLayer(backend=backend)
    data = Data(content=b"Hello, World!")
    genesis_layer_instance.save(data=data)
    backend.has_data.assert_called_once_with(data_id=data.id)
    backend.add_data.assert_called_once_with(data=data)
    backend.commit.assert_called_once()


def test_genesis_layer_has_data(mocker: MockerFixture) -> None:
    backend = mocker.Mock(spec=BaseBackend)
    backend.has_data.return_value = True
    data_id = DataId.generate()
    genesis_layer_instance = genesis_layer.GenesisLayer(backend=backend)
    assert genesis_layer_instance.has_data(data_id=data_id)
    backend.has_data.assert_called_once_with(data_id=data_id)


def test_genesis_layer_get_data(mocker: MockerFixture) -> None:
    backend = mocker.Mock(spec=BaseBackend)
    data_id = DataId.generate()
    expected_data = Data(content=b"Test Data")
    backend.get_data.return_value = expected_data
    genesis_layer_instance = genesis_layer.GenesisLayer(backend=backend)
    actual_data = genesis_layer_instance.get_data(data_id=data_id)
    assert actual_data == expected_data
    backend.get_data.assert_called_once_with(data_id=data_id)
