import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(user='root',
                            password='pachaqtec',
                            host="localhost",
                            port="3306",
                            database="rpineda")
    cur = conn.cursor()
    cur.execute("Select version_();")
    record = cur.fetchone()
    print(record)
except (mysql.connector.Error, Exception) as error:
    print(f"Hubo un error: {error}")
finally:
    if(conn):
        cur.close()
        conn.close()

