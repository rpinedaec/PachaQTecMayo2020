import sqlite3
conn = sqlite3.connect('rpineda.db')
cur = conn.cursor()
cur.execute('SELECT * FROM alumno')
returnData = cur.fetchone()
print(returnData)
