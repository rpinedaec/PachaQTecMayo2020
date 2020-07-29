import psycopg2
from psycopg2 import Error
conn = psycopg2.connect(user='postgres',
                        password='3179billace',
                        host="localhost",
                        port="5432",
                        database="Braulio Berlanga")



cur = conn.cursor()
cur.execute("SELECT version();")

# try:
#     cur = conn.cursor()
#     cur.execute("SELECT version();")
#     returnData = cur.fetchone()
#     print(returnData)
# except Exception as error:
#     print(f"el error es : {error}")
# finally:
#     if(conn):
#         cur.close()
#         conn.close()

