from pytest_mock import MockerFixture

from olstorage.core import StorageCore
from olstorage.settings import StorageCoreSettings


def test_core_create(mocker: MockerFixture) -> None:
    create_storage = mocker.patch("olstorage.core.create_storage")
    settings = StorageCoreSettings(storage_settings={"type": "MEMORY"})
    actual = StorageCore.create(settings=settings)
    assert actual.storage == create_storage.return_value
    create_storage.assert_called_once_with(settings=settings.storage_settings)
