from typing import Dict, Generic, TypeVar

from oltl import (
    BaseBytes,
    BaseEntity,
    BaseUpdateTimeAwareModel,
    Id,
    NonEmptyStringMixIn,
    RegexSubstitutedStringMixIn,
)


class NonEmptySingleLineTrimmedString(NonEmptyStringMixIn, RegexSubstitutedStringMixIn):
    @classmethod
    def get_filling_character(cls) -> str:
        return " "

    @classmethod
    def get_pattern_to_repl_map(cls) -> Dict[str, str]:
        return {
            r"^\s+": "",
            r"\s+$": "",
            r"\s+": cls.get_filling_character(),
        }


class NonEmptySingleLineUnderscoredTrimmedString(NonEmptySingleLineTrimmedString):
    @classmethod
    def get_filling_character(cls) -> str:
        return "_"


class DataId(Id):
    pass


DataIdT = TypeVar("DataIdT", bound=DataId)


class TagId(Id):
    pass


class TagName(NonEmptySingleLineUnderscoredTrimmedString):
    pass


class TagDescription(NonEmptySingleLineTrimmedString):
    pass


class CollectionName(NonEmptySingleLineTrimmedString):
    pass


class Tag(BaseEntity[TagId], BaseUpdateTimeAwareModel):  # type: ignore[misc]
    name: TagName
    description: TagDescription

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tag):
            return False
        return self.id == other.id


class DataContent(BaseBytes):
    pass


class BaseData(BaseEntity[DataIdT], BaseUpdateTimeAwareModel, Generic[DataIdT]):  # type: ignore[misc]
    pass


class Data(BaseData[DataId]):
    content: DataContent


DataT = TypeVar("DataT", bound=BaseData[DataId])
