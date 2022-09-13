import pyodbc
from pyodbc import Connection


def connect_to_database(
    server="localhost\SQLEXPRESS",
    driver="{ODBC Driver 18 for SQL Server}",
    database="master",
):
    cstring = (
        f"DRIVER={driver};"
        f"Server={server};"
        f"Database={database};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes"  # This line is not best practice.
        # see https://stackoverflow.com/questions/17615260/the-certificate-chain-was-issued-by-an-authority-that-is-not-trusted-when-conn
    )
    cnxn = pyodbc.connect(cstring, autocommit=True)  # CHANGE Later to manually commit
    cnxn.setdecoding(pyodbc.SQL_CHAR, encoding="utf8")
    cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding="utf8")
    cnxn.setencoding(encoding="utf8")
    return cnxn


def run_sql_command(sql, database: Connection, verbose=False):
    """
    Run SQL command `sql` on `database`
    """
    if verbose:
        print("---------SQL COMMAND-----------")
        print(sql)
    cursor = database.cursor()
    return cursor.execute(sql)
