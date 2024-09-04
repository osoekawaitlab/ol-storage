import tempfile
from pathlib import Path

from olstorage.backends import sqlitecollections
from olstorage.models import Data


def test_sqlitecollections() -> None:
    with tempfile.NamedTemporaryFile() as temp_file:
        backend = sqlitecollections.SqliteCollectionsBackend(file_path=Path(temp_file.name))
        data = Data(content=b"test")
        assert not backend.has_data(id=data.id)
        backend.add_data(data=data)
        backend.commit()
        assert backend.get_data(id=data.id) == data
        assert backend.has_data(id=data.id)
