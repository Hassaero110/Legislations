import pyodbc 

# server = 'tcp:myserver.database.windows.net' 
# database = 'mydb' 
# username = 'myusername' 
# password = 'mypassword' 
if __name__ == "__main__":
    cnxn = pyodbc.connect("DRIVER={ODBC Driver 18 for SQL Server};"
                        "Server=localhost\SQLEXPRESS;"
                        "Database=master;"
                        "Trusted_Connection=yes;"
                        "TrustServerCertificate=yes") # This line is not best practice. 
                        # see https://stackoverflow.com/questions/17615260/the-certificate-chain-was-issued-by-an-authority-that-is-not-trusted-when-conn

    # 
    cursor = cnxn.cursor()
    #Sample select query
    cursor.execute("SELECT @@version;") 
    row = cursor.fetchone() 
    while row: 
        print(row[0])
        row = cursor.fetchone()

