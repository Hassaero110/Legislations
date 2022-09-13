
## Prerequisites

1. Install `pyodbc` 
1. Install "SQL ODBC Driver" ['link']
1. SMSS

## Installation

## Steps

1. Create tables on SSMS or other IDE us legislation_schema.sql in sql_files
2. Run main.py to upload json to sql tables
3. Query text through main.py
4. Can use stored procedure: sp_search_legislation in sql_files by passing @search_text -> run using exec search_legislation @search_text = 'Type search text here'