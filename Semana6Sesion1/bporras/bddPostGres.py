import psycopg2
from psycopg2 import Error


conn = psycopg2.connect(user='postgres',
                        password='1234',
                        host="localhost",
                        port="5432",
                        database="bporras")
cur = conn.cursor()
cur.execute("Select version();")
record = cur.fetchone()
print(record)