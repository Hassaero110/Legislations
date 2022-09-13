from pyodbc import Connection

from src.api.sql_helper import run_sql_command


def query_legislation(
    *,
    title_search_term="",
    content_search_term="",
    issuing_body_search_term="",
    jurisdiction_search_term="",
    satisfy_all=False,
    database: Connection,
):
    """
    Search the database for legislation matching criteria
    minimum text search across legislation and part title and content
    """

    if satisfy_all:
        cond = "and"
    else:
        cond = "or"

    query = (
        f"select l.legislationversionid, l.title, p.content, ib.name [Issuing Body Name], j.name [Jurisdiction Name] from legislations l "
        f"join leg_part_relationship lpr "
        f"on l.LegislationSourceId = lpr.LegislationSourceId "
        f"and l.LegislationVersionOrdinal = lpr.LegislationVersionOrdinal "
        f"left join part p "
        f"on "
        f"lpr.PartSourceId = p.PartSourceId "
        f"and lpr.PartVersionOrdinal = p.PartVersionOrdinal "
        f"left join issuing_body ib "
        f"on "
        f"l.IssuingBodySourceId = ib.SourceId "
        f"left join jurisdiction j "
        f"on "
        f"l.JurisdictionSourceId = j.SourceId "
        f"where "
        f"l.title like '%{title_search_term}%' "
        f"{cond} "
        f"p.content like '%{content_search_term}%' "
        f"{cond} "
        f"ib.name like '%{issuing_body_search_term}%' "
        f"{cond} "
        f"j.name like '%{jurisdiction_search_term}%' "
    )

    result = run_sql_command(query, database)

    return result
