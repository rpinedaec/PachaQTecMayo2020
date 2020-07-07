import sqlite3
conn = sqlite3.connect('martinperez.db')
cur = conn.cursor()
#cur.execute("Select sqlite_version();")
cur.execute("Select * from alumno")
record = cur.fetchone()
print(record)