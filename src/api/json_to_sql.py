from pathlib import Path

from pyodbc import Connection

from src.api.json_to_sql_helper import (
    post_issuing_bodies_to_sql,
    post_jurisdiction_to_sql,
    post_legislation_to_sql,
    post_part_relationship_to_sql,
    post_part_to_sql,
)
from src.models.legislation import Legislation


def json_to_sql(*, database: Connection):
    """
    Takes json files from the data directory and inputs them into a SQL database
    """
    for path in Path("data").rglob("Legislation*.json"):
        print("name: ", path)
        leg_list = Legislation.listFromJson(path)
        # Each legislation file has
        post_issuing_bodies_to_sql(leg_list[0], database=database)
        post_jurisdiction_to_sql(leg_list[0], database=database)
        post_legislation_to_sql(leg_list[0], database=database)
        for _leg in leg_list:
            post_part_relationship_to_sql(_leg, database=database)
            post_part_to_sql(_leg, database=database)
