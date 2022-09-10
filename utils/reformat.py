import json

from pathlib import Path

if __name__ == "__main__":
# Indent json files so they can be eaily read by humans
    for path in Path('Legislation').rglob('*.json'):
        with open(path, encoding="utf8") as infile:
            text = json.load(infile)

        with open(path, "w") as outfile:
            json.dump(text, outfile, indent=1)