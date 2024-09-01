from typing import Dict

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


class TagId(Id):
    pass


class TagName(NonEmptySingleLineUnderscoredTrimmedString):
    pass


class TagDescription(NonEmptySingleLineTrimmedString):
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


class Data(BaseEntity[DataId], BaseUpdateTimeAwareModel):  # type: ignore[misc]
    content: DataContent
