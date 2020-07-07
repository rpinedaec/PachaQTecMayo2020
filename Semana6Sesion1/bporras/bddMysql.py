import mysql.connector
from mysql.connector import errorcode
try:
    conn = mysql.connector.connect(user = "root",
                                password = "1234",
                                host = "127.0.0.1",
                                port = "3306",
                                database = "bporras")
    cur = conn.cursor()
    cur.execute("Select version_();")
    record = cur.fetchone()
    print(record)
except (mysql.connector.Error, Exception) as error:
    print(f"Hubo el ERROR {error}")
finally:
    if(conn):
        cur.close()
        conn.close()