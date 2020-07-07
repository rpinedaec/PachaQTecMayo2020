import mysql.connector
 
try:
    conn = mysql.connector.connect(user='root',
                            password='3179billace',
                            host="localhost",
                            port="3306",
                            database="bberlangas")
    cur = conn.cursor()
    
    cur.execute("Select version();")
    record = cur.fetchone()
    print(record)
except (Exception) as error:
    print(f"Hubo un error: {error}")
finally:
    if(conn):
        cur.close()
        conn.close()