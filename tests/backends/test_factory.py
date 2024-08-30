import pytest
from pytest_mock import MockerFixture

from olstorage.backends import factory
from olstorage.settings import BackendType, BaseBackendSettings, MemoryBackendSettings


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
