from genericpath import isfile
from msilib.schema import Directory
from typing import List
import pyodbc
from pyodbc import Connection
import os
from legislation import Legislation 

directory = 'Legislation'

def connect_to_database(
    server='localhost\SQLEXPRESS', 
    driver='{ODBC Driver 18 for SQL Server}', 
    database='master'):
# username = 'myusername' 
# password = 'mypassword' 

    cstring = (
        f"DRIVER={driver};"
        f"Server={server};"
        f"Database={database};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes"# This line is not best practice.
        # see https://stackoverflow.com/questions/17615260/the-certificate-chain-was-issued-by-an-authority-that-is-not-trusted-when-conn

    )
    cnxn = pyodbc.connect(cstring, autocommit=True)  # CHANGE Later to manually commit  
    return cnxn

def run_sql_command(sql, database):
    print("---------DEBUG-----------")
    print(sql)
    cursor = database.cursor()
    return cursor.execute(sql)

def check_issuing_body_exists(*, sql_table='dbo.issuing_body', database):
    result = get_issuing_body_from_sql(database=database)
    SourceID_list =[]

    row = result.fetchone() 
    while row: 
        SourceID_list.append(row[0])
        row = result.fetchone()

    return SourceID_list

def post_issuing_bodies_to_sql(legislation_data: Legislation, database: Connection):
    _leg = legislation_data

    if _leg.IssuingBodySourceId.upper() not in check_issuing_body_exists(database=database):
            sql_command = (
                f"INSERT INTO dbo.issuing_body (Name, SourceID)"
                f"VALUES ('{_leg.IssuingBodyName}', '{_leg.IssuingBodySourceId}');"
            )

            run_sql_command(sql_command, database)

def get_issuing_body_from_sql(*, sql_table='dbo.issuing_body', database: Connection):
    #Sample select query
    result = run_sql_command(f"SELECT SourceID FROM {sql_table};", database)
    return result

def json_to_sql():
    pass

def query_legislation():
    '''
    Search the database for legislation matching criteria
    minimum text search across legislation and part title and content
    '''

def optional_no_sql_database_version():
    pass

if __name__ == "__main__":

    database = connect_to_database(database="master")

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
    # checking if it is a file
        if os.path.isfile(f) and f.endswith(".json"):

            leg_list = Legislation.listFromJson(f)
            x = leg_list[0]
            post_issuing_bodies_to_sql(x, database=database)
            
            

    