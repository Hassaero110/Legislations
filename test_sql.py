from typing import List
import pyodbc
from pyodbc import Connection

from legislation import Legislation 



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
    cursor = database.cursor()
    return cursor.execute(sql)

def post_data_to_sql(legislation_data: Legislation, database: Connection):

    print('Type =')
    print(type(legislation_data))

    #for _leg in legislation_data:
    #
    #    sql_command = (
    #        f"INSERT INTO dbo.issuing_body (Name, SourceID)"
    #        f"VALUES ({_leg.IssuingBodyName}, {_leg.IssuingBodySourceId});"
    #    )
#
    #    run_sql_command(sql_command, database)

def get_data_from_sql(*, sql_table='dbo.issuing_body', database: Connection):
    #Sample select query
    result = run_sql_command(f"SELECT * FROM {sql_table};", database)
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

    database = connect_to_database(database="legislation")
    print(f"{type(database)}")

    Leg = Legislation.fromJson('Legislation/Legislation_822.json')



   # post_data_to_sql(3, database)
   # result = get_data_from_sql(database=database)
#
   # row = result.fetchone() 
   # while row: 
   #     print(row[0], row[1], row[2])
   #     row = result.fetchone()


    #result = run_sql_command("SELECT * FROM dbo.issuing_body;", database)
    #for i in [column[0] for column in result.description]:
    #    print(i)






