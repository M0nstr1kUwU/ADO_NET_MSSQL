import pyodbc


def connect():
    connection_string = ("DRIVER={ODBC Driver 18 for SQL Server};"
                         "Server=COMP7A2\\SQLEXPRESS;"
                         "Database=TestIndex;"
                         "Trusted_Connection=yes;"
                         "Encrypt=yes;"
                         "TrustServerCertificate=yes;")
    connection = pyodbc.connect(connection_string)
    return connection


def main():
    table_name = "orders"
    conn = connect()
    print_data(select_data(conn, table_name))
    add_data(conn, table_name)


def select_data(conn, name):
    cursor = conn.cursor()
    sql_command = f"SELECT TOP 10 * FROM dbo.{name}"
    cursor.execute(sql_command)
    return cursor


def add_data(conn, name):
    cursor = conn.cursor()
    sql_command = f"INSERT INTO dbo.{name}(id, product_id, customer_id, price) VALUES(?, ?, ?, ?)"
    cursor.execute(sql_command, 'faifa', 'cocacola', 'ded', 150.0)
    cursor.commit()


def print_data(cursor):
    rows = cursor.fetchall()
    for row in rows:
        print(row)


main()
