import psycopg2
conn = psycopg2.connect(user='postgres',
                        password='741852',
                        host="localhost",
                        port="5432",
                        database="rcornejo")

cur = conn.cursor()
cur.execute("Select version();")
returnData = cur.fetchone()
print(returnData)

    
    
