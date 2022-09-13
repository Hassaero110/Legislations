import html
import json


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, bytes):
            return o.decode("utf-8")

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
