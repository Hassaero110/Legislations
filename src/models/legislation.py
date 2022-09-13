import json
from dataclasses import asdict, dataclass
from types import NoneType

from src.utils.json_encoder_decoder import CustomJsonDecoder

directory = "Legislation"


@dataclass(kw_only=True)
class Legislation:
    LegislationVersionId: int
    LegislationSourceId: str  # unique identifier
    LegislationVersionOrdinal: int
    Title: str
    NativeTitle: str | NoneType
    JurisdictionSourceId: str  # unique identifier
    JurisdictionName: str
    IssuingBodySourceId: str  # unique identifier
    IssuingBodyName: str
    PartVersionId: int
    PartSourceId: str  # unique identifier
    PartVersionOrdinal: int
    OrderNum: int
    Content: str  # HTML
    NativeContent: str | NoneType
    ParentPartVersionId: int | NoneType
    ParentPartSourceId: str | NoneType  # unique identifier
    ParentPartVersionOrdinal: int | NoneType

    @staticmethod
    def listFromJson(json_file):
        list_of_legislation = []
        with open(json_file, "r", encoding="utf-8-sig") as f:
            list_of_versions = json.load(f, cls=CustomJsonDecoder)
        for ver_dict in list_of_versions:
            list_of_legislation.append(Legislation(**ver_dict))

        return list_of_legislation

    def __post_init__(self):
        pass  # Error checking logic

    def as_dict(self):
        """
        Return as dictionary
        """
        return asdict(self)
