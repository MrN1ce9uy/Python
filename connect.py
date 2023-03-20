import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='database_name',
                                       user='username',
                                       password='password')
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn

    except Error as e:
        print(e)

def query(conn, query):
    """ Query data from MySQL database """
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    return rows

if __name__ == '__main__':
    conn = connect()
    query = "SELECT * FROM table_name WHERE column_name = 'search_input'"
    results = query(conn, query)
    print(results)
