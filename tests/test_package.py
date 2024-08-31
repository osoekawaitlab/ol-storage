import re

import olstorage


def test_olstorage_has_version() -> None:
    assert re.match(r"\d+\.\d+\.\d+", olstorage.__version__)


def test_olstorage_core() -> None:
    assert olstorage.StorageCore == olstorage.core.StorageCore


def test_olstorage_exports_some_models() -> None:
    assert olstorage.Document == olstorage.models.Document


def test_olstorage_exports_settings() -> None:
    assert olstorage.StorageCoreSettings == olstorage.settings.StorageCoreSettings
    assert olstorage.NexusLayerType == olstorage.settings.NexusLayerType
    assert olstorage.GenesisLayerSettings == olstorage.settings.GenesisLayerSettings
    assert olstorage.MemoryBackendSettings == olstorage.settings.MemoryBackendSettings
    assert olstorage.KvsNexusLayerSettings == olstorage.settings.KvsNexusLayerSettings
