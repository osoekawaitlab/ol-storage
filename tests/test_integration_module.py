import olstorage


def test_core_module() -> None:
    settings = olstorage.StorageCoreSettings(storage_settings={"type": "MEMORY"})
    core = olstorage.core.create(settings=settings)
    document = core.Document(content="Hello, World!")
    saved_document = core.save(document)
    assert saved_document.content == "Hello, World!"
    actual = core.get(saved_document.id)
    assert actual.content == "Hello, World!"
