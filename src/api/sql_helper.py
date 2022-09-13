import pyodbc
from pyodbc import Connection

from src.utils.read_config import read_sql_config


def connect_to_database(
    server=read_sql_config("server"),
    driver=read_sql_config("driver"),
    database=read_sql_config("database"),
    trusted_connection=read_sql_config("trusted_connection"),
    trust_server_certificate=read_sql_config("trust_server_certificate"),
):
    cstring = (
        f"DRIVER={driver};"
        f"Server={server};"
        f"Database={database};"
        f"Trusted_Connection={trusted_connection};"
        f"TrustServerCertificate={trust_server_certificate}"  # This line is not best practice.
        # see https://stackoverflow.com/questions/17615260/the-certificate-chain-was-issued-by-an-authority-that-is-not-trusted-when-conn
    )
    print(f"{cstring = }")
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
