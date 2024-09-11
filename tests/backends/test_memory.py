from olstorage.backends import memory
from olstorage.models import BaseData, CollectionName, Data


def test_memory_backend_data_save_and_commit() -> None:
    sut = memory.MemoryBackend()
    data = Data(content=b"Hello, World!")
    actual = sut.has_data(data_id=data.id)
    assert actual is False
    sut.add_data(data=data)
    actual = sut.has_data(data_id=data.id)
    assert actual is True
    sut.commit()
    actual = sut.has_data(data_id=data.id)
    assert actual is True


def test_memory_exact_match_index() -> None:
    class Value(BaseData):
        value: str

    val = Value(value="value0")
    sut = memory.MemoryExactMatchIndex[Value, str](collection_name=CollectionName.from_str("test"))
    assert len(sut) == 0
    sut.set(key="key0", value=val)
    actual = sut.get(key="key0")
    assert actual == val
    assert len(sut) == 1
