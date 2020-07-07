import mysql.connector

conn = mysql.connector.connect(
                            user='root', 
                            password='1984RICARDO2011PAPO', 
                            host='localhost',
                            port="3306", 
                            database='avellaneda')

cur = conn.cursor()
cur.execute("SELECT version();")
returnData = cur.fetchone()

print(returnData)

