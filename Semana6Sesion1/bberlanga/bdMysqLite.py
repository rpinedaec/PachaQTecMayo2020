import sqlite3
conn = sqlite3.connect('bberlanga.db')
cur = conn.cursor()
cur.execute("Select sqlite_version();")
record = cur.fetchone()
print(record)