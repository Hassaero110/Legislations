
## Prerequisites

1. Install `pyodbc` 
1. Install "SQL ODBC Driver" ['link']
1. SMSS

## Installation

## Steps

1. Copy `config/sql_database.ini.dist` to `config/sql_database.ini`
2. Add appropriate details for your database
3. Create tables on SSMS or other IDE use `legislation_schema.sql` in `sql_files` directory
4. Run `main.py` to upload json to sql tables
5. Query text through `main.py`
6. Can use stored procedure: `sp_search_legislation` in sql_files by passing @search_text -> run using exec search_legislation @search_text = 'Type search text here'