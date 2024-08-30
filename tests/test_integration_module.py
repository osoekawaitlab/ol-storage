import pytest

import olstorage


@pytest.mark.e2e
def test_core_module_has_document_storage() -> None:
    settings = olstorage.StorageCoreSettings(
        genesis_layer_settings=olstorage.GenesisLayerSettings(backend_settings=olstorage.MemoryBackendSettings()),
        nexus_layers_settings={
            olstorage.NexusLayerType.KVS: olstorage.KvsNexusLayerSettings(
                backend_settings=olstorage.MemoryBackendSettings()
            )
        },
    )
    core = olstorage.StorageCore.create(settings=settings)
    document = olstorage.Document(content="Hello, World!")
    saved_document = core.save(document)
    assert saved_document.content == "Hello, World!"
    actual = core.get(saved_document.id)
    assert actual.content == "Hello, World!"
