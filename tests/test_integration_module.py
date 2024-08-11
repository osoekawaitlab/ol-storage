import pytest

import olstorage


@pytest.mark.e2e
def test_core_module() -> None:
    settings = olstorage.StorageCoreSettings(storage_settings={"type": "MEMORY"})
    core = olstorage.StorageCore.create(settings=settings)
    document = olstorage.Document(content="Hello, World!")
    saved_document = core.save(document)
    assert saved_document.content == "Hello, World!"
    actual = core.get(saved_document.id)
    assert actual.content == "Hello, World!"


@pytest.mark.e2e
def test_core_module_raises_key_error_when_document_not_found() -> None:
    settings = olstorage.StorageCoreSettings(storage_settings={"type": "MEMORY"})
    core = olstorage.StorageCore.create(settings=settings)
    document = olstorage.Document(content="Hello, World!")
    with pytest.raises(KeyError):
        core.get(document.id)
