import json
from pathlib import Path


def reformat_json_file(path: Path, inplace=True, prefix="reformatted_"):
    """
    Reformat json file by adding indentation to make it easier for humans to read.
    If `inplace` is `True` then the file will be overwritten with changes, if `False`
    then `prefix` is added to the json filename.
    """
    # Indent json files so they can be eaily read by humans
    with open(path, encoding="utf8") as infile:
        text = json.load(infile)

    if inplace:
        reform_path = path
    else:
        reform_path = Path(path.parent, prefix + path.name)

    with open(reform_path, "w") as outfile:
        json.dump(text, outfile, indent=1)


def reformat_legislation_json_files(inplace=True, prefix="reformatted_"):
    for path in Path("Legislation").rglob("*.json"):
        reformat_json_file(path, inplace=inplace, prefix=prefix)


if __name__ == "__main__":
    reformat_legislation_json_files()
