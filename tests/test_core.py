from pytest_mock import MockerFixture

from olstorage.core import StorageCore
from olstorage.models import Document
from olstorage.settings import StorageCoreSettings
from olstorage.storages.base import BaseStorage


def test_core_create(mocker: MockerFixture) -> None:
    create_storage = mocker.patch("olstorage.core.create_storage")
    settings = StorageCoreSettings(storage_settings={"type": "MEMORY"})
    actual = StorageCore.create(settings=settings)
    assert actual.storage == create_storage.return_value
    create_storage.assert_called_once_with(settings=settings.storage_settings)


def test_core_save_new_document(mocker: MockerFixture) -> None:
    storage = mocker.MagicMock(spec=BaseStorage)
    storage.__contains__.return_value = False
    sut = StorageCore(storage=storage)
    document = Document(content="content")
    actual = sut.save(document=document)
    assert actual == storage.create_document.return_value
    storage.__contains__.assert_called_once_with(document.id)
    storage.create_document.assert_called_once_with(document=document)


def test_core_get(mocker: MockerFixture) -> None:
    document = Document(content="content")
    storage = mocker.MagicMock(spec=BaseStorage)
    storage.get.return_value = document
    sut = StorageCore(storage=storage)
    actual = sut.get(document_id=document.id)
    assert actual == document
    storage.get.assert_called_once_with(document_id=document.id)
