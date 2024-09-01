import pytest

import olstorage


@pytest.mark.e2e
def test_core_module_has_data_storage() -> None:
    settings = olstorage.StorageCoreSettings(
        genesis_layer_settings=olstorage.GenesisLayerSettings(backend_settings=olstorage.MemoryBackendSettings()),
        nexus_layers_settings={
            olstorage.NexusLayerType.KVS: olstorage.KvsNexusLayerSettings(
                backend_settings=olstorage.MemoryBackendSettings()
            )
        },
    )
    core = olstorage.StorageCore.create(settings=settings)
    data = olstorage.Data(content=b"Hello, World!")
    saved_data = core.save(data)
    assert saved_data.content == b"Hello, World!"
    actual = core.get(saved_data.id)
    assert actual.content == b"Hello, World!"
