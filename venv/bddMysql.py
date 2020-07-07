import mysql.connector

conn = mysql.connector.connect(user= 'root',
                              password= '741852',
                              host='localhost',
                              prot= '3306',
                              database='rcornejo')
cur = conn.cursor()
cur.execute('SELECT version();')
returnData = cur.fetchone()

print (returnData)

