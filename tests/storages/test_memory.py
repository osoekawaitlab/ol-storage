from olstorage.models import Document
from olstorage.storages.memory import MemoryStorage


def test_memory_storage() -> None:
    document = Document(content="content")
    sut = MemoryStorage()
    assert document.id not in sut
    actual = sut.create_document(document=document)
    assert document.id in sut
    document2 = sut.get(document_id=document.id)
    assert document2 == actual
    assert document2 == document
