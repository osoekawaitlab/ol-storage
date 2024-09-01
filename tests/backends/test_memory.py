from olstorage.backends import memory
from olstorage.models import Data


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
