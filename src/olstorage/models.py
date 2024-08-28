from oltl import BaseEntity, BaseUpdateTimeAwareModel, Id, TrimmedStringMixIn


class DataId(Id):
    pass


class DocumentId(DataId):
    pass


class Key(TrimmedStringMixIn):
    pass


class Document(BaseEntity[DocumentId], BaseUpdateTimeAwareModel):  # type: ignore[misc]
    content: str
