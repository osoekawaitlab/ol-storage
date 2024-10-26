import pytest

import olstorage


@pytest.mark.e2e
def test_core_module_has_data_storage() -> None:
    settings = olstorage.StorageCoreSettings(
        genesis_layer_settings=olstorage.GenesisLayerSettings(backend_settings=olstorage.MemoryBackendSettings()),
        nexus_layers_settings={},
    )
    core = olstorage.StorageCore.create(settings=settings)
    data = olstorage.Data(content=b"Hello, World!")
    saved_data = core.save(data)
    assert saved_data.content == b"Hello, World!"
    actual = core.get(saved_data.id)
    assert actual.content == b"Hello, World!"


@pytest.mark.e2e
def test_core_module_has_kvs() -> None:
    settings = olstorage.StorageCoreSettings(
        genesis_layer_settings=olstorage.GenesisLayerSettings(backend_settings=olstorage.MemoryBackendSettings()),
        nexus_layers_settings={
            olstorage.NexusLayerType.KVS: olstorage.KvsNexusLayerSettings(
                backend_settings=olstorage.MemoryBackendSettings()
            ),
        },
    )

    class SomeValue(olstorage.BaseData):
        value: int

    core = olstorage.StorageCore.create(settings=settings)
    data = SomeValue(value=123)
    sut = core.key_value_store[str, SomeValue].create()
    sut.set("key0", data)
    actual = sut.get("key0")
    assert actual.value == 123
    assert actual == data
