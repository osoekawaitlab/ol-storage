from unittest.mock import call

from pytest_mock import MockerFixture

from olstorage.backends.base import BaseBackend
from olstorage.models import BaseData, CollectionName
from olstorage.nexus_layers import kvs


def test_kvs_nexus_layer_calls_create_exact_match_index(mocker: MockerFixture) -> None:
    backend = mocker.MagicMock(spec=BaseBackend)
    backend.get_exact_match_index.side_effect = KeyError

    class Value(BaseData):
        value: str

    val = Value(value="value0")

    nexus_layer = kvs.KvsNexusLayer(backend=backend)
    nexus_layer.set(key="key0", value=val)
    backend.create_exact_match_index.assert_called_once_with(
        collection_name=CollectionName.from_str("kvs.default"), key_type=str, value_type=Value
    )


def test_kvs_nexus_layer_set(mocker: MockerFixture) -> None:
    backend = mocker.MagicMock(spec=BaseBackend)
    nexus_layer = kvs.KvsNexusLayer(backend=backend)

    class Value(BaseData):
        value: str

    val = Value(value="value0")

    nexus_layer.set(key="key0", value=val)
    actual = nexus_layer.get(key="key0")
    backend.get_exact_match_index.assert_has_calls(
        [
            call(collection_name=CollectionName.from_str("kvs.default")),
            call().set(key="key0", value=val),
            call(collection_name=CollectionName.from_str("kvs.default")),
            call().get(key="key0"),
        ]
    )
    assert actual == backend.get_exact_match_index.return_value.get.return_value
