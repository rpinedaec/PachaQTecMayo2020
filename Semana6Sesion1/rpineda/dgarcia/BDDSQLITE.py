import sqlite3

conn = sqlite3.connector(database="dgarcia")

cur = conn.cursor()
cur.execute("Select version();")

record = cur.fetchone()
print(record)