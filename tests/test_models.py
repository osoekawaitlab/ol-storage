from olstorage import models


def test_data_inheritance() -> None:
    class SomeDataId(models.DataId):
        pass

    class SomeData(models.BaseData[SomeDataId]):
        data: str

    actual = SomeData(data="test")
    assert actual.data == "test"
    assert isinstance(actual.id, SomeDataId)
