import psycopg2

conn = psycopg2.connect(user='postgres',
                        password='e8310180',
                        host="localhost",
                        port="5432",
                        database="dgarcia")

cur = conn.cursor()
cur.execute("Select version();")

record = cur.fetchone()
print(record)