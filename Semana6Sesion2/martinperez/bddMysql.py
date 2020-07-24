import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(user='root',
                                    password='passmysqlmartin',
                                    host="localhost",
                                    port="3306",
                                    database="martinperez")
    cur = conn.cursor()
    cur.execute("select version();")
    returnData = cur.fetchone()
    print(returnData)
except (mysql.connector.Error, Exception) as error:
    print(f"Hubo un error: {error}")
finally:
    if(conn):
        cur.close()
        conn.close()
