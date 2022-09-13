import json
from pathlib import Path

if __name__ == "__main__":
    lists = []

    # Indent json files so they can be eaily read by humans
    for path in Path("data").rglob("Legislation*.json"):
        save = True
        with open(path, encoding="utf8") as infile:
            text = json.load(infile)
            for _l in text:
                lists.append(str(_l["PartSourceId"]) + str(_l["PartVersionOrdinal"]))

    print(len(lists))
    print(len(set(lists)))
