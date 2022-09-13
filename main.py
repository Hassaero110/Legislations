from src.api.json_to_sql import json_to_sql
from src.api.sql_helper import connect_to_database
from src.api.sql_query import query_legislation

directory = "Legislation"

debug = True


if __name__ == "__main__":

    # Open database
    database = connect_to_database(database="master")
    # Convvert json to database
    json_to_sql(database=database)

    # query database
    result = query_legislation(
        title_search_term="annual",
        content_search_term="corrects",
        satisfy_all=True,
        database=database,
    )

    # Print results
    row = result.fetchone()
    while row:
        print(row[0])
        row = result.fetchone()
