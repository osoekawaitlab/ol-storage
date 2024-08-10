import pytest

from olstorage.settings import BaseStorageSettings, StorageType
from olstorage.storages import factory


def test_create_storage_raises_value_error_when_invalid_settings_passed() -> None:
    settings = BaseStorageSettings(type=StorageType.MEMORY)
    with pytest.raises(ValueError):
        factory.create_storage(settings=settings)  # type: ignore[arg-type]
