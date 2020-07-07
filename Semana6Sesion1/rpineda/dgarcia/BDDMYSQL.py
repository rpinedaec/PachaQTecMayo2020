import mysql.connector

try:
    conn = mysql.connector.connect(user='root',
                            password="W8Y6N6G7",
                            host="localhost",
                            port="3306",
                            database="dgarcia")

    cur = conn.cursor()
    cur.execute("Select version();")

    record = cur.fetchone()
    print(record)
except (mysql.connector.Error, Exception) as error:
    print(f"Hubo un error: {error}")
finally:
    if(conn):
        cur.close()
        conn.close()