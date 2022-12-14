from pyodbc import Connection

from src.api.sql_helper import run_sql_command
from src.models.legislation import Legislation


############# IssuingBody ###################
def check_issuing_body_exists(*, sql_table="dbo.issuing_body", database):
    result = get_issuing_body_from_sql(database=database)
    SourceID_list = []

    row = result.fetchone()
    while row:
        SourceID_list.append(row[0])
        row = result.fetchone()

    return SourceID_list


def get_issuing_body_from_sql(*, sql_table="dbo.issuing_body", database: Connection):
    result = run_sql_command(f"SELECT SourceID FROM {sql_table};", database)

    return result


def post_issuing_bodies_to_sql(legislation_data: Legislation, database: Connection):
    if legislation_data.IssuingBodySourceId.upper() not in check_issuing_body_exists(
        database=database
    ):
        sql_command = (
            "INSERT INTO dbo.issuing_body (Name, SourceID)VALUES"
            f" ('{legislation_data.IssuingBodyName}',"
            f" '{legislation_data.IssuingBodySourceId}');"
        )

        run_sql_command(sql_command, database)


############### Jurisdiction ##################


def get_jurisdiction_from_sql(*, sql_table="dbo.jurisdiction", database: Connection):
    result = run_sql_command(f"SELECT SourceID FROM {sql_table};", database)

    return result


def check_jurisdiction_exists(*, database):
    result = get_jurisdiction_from_sql(database=database)
    SourceID_list = []

    row = result.fetchone()
    while row:
        SourceID_list.append(row[0])
        row = result.fetchone()

    return SourceID_list


def post_jurisdiction_to_sql(legislation_data: Legislation, database: Connection):
    if legislation_data.JurisdictionSourceId.upper() not in check_jurisdiction_exists(
        database=database
    ):
        sql_command = (
            "INSERT INTO dbo.jurisdiction (Name, SourceID)VALUES"
            f" ('{legislation_data.JurisdictionName}',"
            f" '{legislation_data.JurisdictionSourceId}');"
        )

        run_sql_command(sql_command, database)


########### Legislations ###########


def get_legislation_from_sql(*, sql_table="dbo.legislations", database: Connection):
    result = run_sql_command(f"SELECT LegislationVersionId FROM {sql_table};", database)

    return result


def check_legislation_exists(*, database):
    result = get_legislation_from_sql(database=database)
    SourceID_list = []
    row = result.fetchone()

    while row:
        SourceID_list.append(row[0])
        row = result.fetchone()

    return SourceID_list


def post_legislation_to_sql(legislation_data: Legislation, database: Connection):
    if legislation_data.LegislationVersionId not in check_legislation_exists(
        database=database
    ):
        sql_command = (
            "INSERT INTO dbo.legislations (LegislationVersionId, LegislationSourceId,"
            " LegislationVersionOrdinal, Title, NativeTitle, IssuingBodySourceId,"
            f" JurisdictionSourceId)VALUES ('{legislation_data.LegislationVersionId}',"
            f" '{legislation_data.LegislationSourceId}' ,"
            f" '{legislation_data.LegislationVersionOrdinal}','{legislation_data.Title}',"
            f" '{legislation_data.NativeTitle}',"
            f" '{legislation_data.IssuingBodySourceId}',"
            f" '{legislation_data.JurisdictionSourceId}');"
        )
        run_sql_command(sql_command, database)


############ Part ##############


def check_part_exists(*, database, sql_table="dbo.part", legislation_data: Legislation):
    result = run_sql_command(
        f"SELECT PartSourceId, PartVersionOrdinal FROM {sql_table} WHERE PartSourceId ="
        f" '{legislation_data.PartSourceId.upper()}' AND PartVersionOrdinal ="
        f" {legislation_data.PartVersionOrdinal};",
        database,
        verbose=True,
    )
    row = result.fetchone()

    if row is None:
        return False

    else:
        return True


def post_part_to_sql(legislation_data: Legislation, database: Connection):
    if not check_part_exists(legislation_data=legislation_data, database=database):
        sql_command = (
            "INSERT INTO dbo.part (PartVersionId, PartSourceId, PartVersionOrdinal,"
            " OrderNum, Content, NativeContent, ParentPartVersionId)VALUES"
            f" ('{legislation_data.PartVersionId}', '{legislation_data.PartSourceId}',"
            f" '{legislation_data.PartVersionOrdinal}', '{legislation_data.OrderNum}',"
            f" '{legislation_data.Content}', '{legislation_data.NativeContent}',"
            f" '{legislation_data.ParentPartVersionId}');"
        )
        run_sql_command(sql_command, database)


##############################################################################################
def post_part_relationship_to_sql(legislation_data: Legislation, database: Connection):
    sql_command = (
        "INSERT INTO dbo.leg_part_relationship (PartVersionId, LegislationVersionId,"
        " PartSourceId, PartVersionOrdinal, LegislationVersionOrdinal,"
        f" LegislationSourceId)VALUES ('{legislation_data.PartVersionId}',"
        f" '{legislation_data.LegislationVersionId}',"
        f" '{legislation_data.PartSourceId}', '{legislation_data.PartVersionOrdinal}',"
        f" '{legislation_data.LegislationVersionOrdinal}',"
        f" '{legislation_data.LegislationSourceId}');"
    )
    run_sql_command(sql_command, database)
