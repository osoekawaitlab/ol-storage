from pytest_mock import MockerFixture

from olstorage.backends.base import BaseBackend
from olstorage.models import BaseData, CollectionName
from olstorage.nexus_layers import kvs


def test_kvs_nexus_layer_set(mocker: MockerFixture) -> None:
    backend = mocker.MagicMock(spec=BaseBackend)
    nexus_layer = kvs.KvsNexusLayer(backend=backend)

    class Value(BaseData):
        value: str

    val = Value(value="value0")

    nexus_layer.set(key="key0", value=val)
    backend.get_or_create_exact_match_index.assert_called_once_with(
        collection_name=CollectionName.from_str("kvs.default"), key_type=str, value_type=Value
    )
    backend.get_or_create_exact_match_index.return_value.set.assert_called_once_with(key="key0", value=val)
