import pytest
from pytest_mock import MockerFixture

from olstorage.settings import BaseStorageSettings, MemoryStorageSettings, StorageType
from olstorage.storages import factory


def test_create_storage_raises_value_error_when_invalid_settings_passed() -> None:
    settings = BaseStorageSettings(type=StorageType.MEMORY)
    with pytest.raises(ValueError):
        factory.create_storage(settings=settings)  # type: ignore[arg-type]


def test_create_storage_create_memory_storage(mocker: MockerFixture) -> None:
    MemoryStorage = mocker.patch("olstorage.storages.factory.MemoryStorage")
    settings = MemoryStorageSettings()
    actual = factory.create_storage(settings=settings)
    assert actual == MemoryStorage.return_value
    MemoryStorage.assert_called_once_with()
