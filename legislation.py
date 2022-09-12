import html
import json
import os
from dataclasses import asdict, dataclass
from types import NoneType

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


######
class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, bytes):
            return o.decode("utf-8")
        if isinstance(o, Legislation):
            return {"__leg__": asdict(o)}
        return super().default(o)


class CustomJsonDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        for _k, _v in dct.items():
            # If string, clean it
            if isinstance(_v, str):
                dct[_k] = html.escape(_v)

            # if dict, clean every string in dict
            if isinstance(_v, dict):
                dct[_k] = self.object_hook(_v)

        return dct


if __name__ == "__main__":
    True
