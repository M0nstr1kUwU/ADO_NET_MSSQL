import mssql_python

str_connect = ("Server=COMP7A2\\SQLEXPRESS;"
               "Database=TestIndex;"
               "Trusted_Connection=yes;"
               "Encrypt=yes;"
               "TrustServerCertificate=yes;")

conn = mssql_python.connect(str_connect)
cursor = conn.cursor()
sql_command = "SELECT TOP 10 * FROM dbo.orders"
cursor.execute(sql_command)
rows = cursor.fetchall()
for row in rows:
    print(row)
