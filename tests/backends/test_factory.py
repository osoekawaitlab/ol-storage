import tempfile
from pathlib import Path

import pytest
from pytest_mock import MockerFixture

from olstorage.backends import factory
from olstorage.settings import (
    BackendType,
    BaseBackendSettings,
    MemoryBackendSettings,
    SqliteCollectionsBackendSettings,
)


def test_create_backend_raises_value_error_when_invalid_settings_passed() -> None:
    settings = BaseBackendSettings(type=BackendType.MEMORY)
    with pytest.raises(ValueError):
        factory.create_backend(settings=settings)  # type: ignore[arg-type]


def test_create_backend_create_document_backend(mocker: MockerFixture) -> None:
    MemoryBackend = mocker.patch("olstorage.backends.factory.MemoryBackend")
    settings = MemoryBackendSettings()
    actual = factory.create_backend(settings=settings)
    assert actual == MemoryBackend.return_value
    MemoryBackend.assert_called_once_with()


def test_create_backend_creates_sqlite_collections_backend(mocker: MockerFixture) -> None:
    SqliteCollectionsBackend = mocker.patch("olstorage.backends.factory.SqliteCollectionsBackend")
    with tempfile.NamedTemporaryFile() as temp_file:
        settings = SqliteCollectionsBackendSettings(file_path=temp_file.name)
        actual = factory.create_backend(settings=settings)
        assert actual == SqliteCollectionsBackend.return_value
        SqliteCollectionsBackend.assert_called_once_with(file_path=Path(temp_file.name))
