from oltl import BaseEntity, BaseUpdateTimeAwareModel, Id


class DocumentId(Id):
    pass


class Document(BaseEntity[DocumentId], BaseUpdateTimeAwareModel):  # type: ignore[misc]
    content: str
