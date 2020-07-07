import psycopg2
from psycopg2 import Error

try:
    conn = psycopg2.connect(user='postgres',
                            password='3179billace',
                            host='localhost',
                            port='5432',
                            database='Braulio Berlanga')

    cur = conn.cursor()
# Read
    #fetchone
    # query="SELECT * FROM alumno"
    # cur.execute(query)
    # n_1=cur.fetchone()
    # n_2=cur.fetchone()
    # print(n_1,n_2)

    #fetchmany(size=n)
    # query="SELECT * FROM alumno"
    # cur.execute(query)
    # record=cur.fetchmany(size=2)    
    # print(record)

    # query="SELECT * FROM alumno"
    # cur.execute(query)
    # records=cur.fetchmany(4)
    # for row in records:
    #     print(f'ID: {row[0]}')
    #     print(f'Model: {row[1]}')
    #     print(f'Price: {row[2]}')

# Update
    # Insert
    # query="INSERT INTO alumno(nombre_alumno,edad_alumno,correo_alumno,id_salon) VALUES (%s,%s,%s,%s)"
    # record_insert=[('Manuel',62,'brabesa@gmail.com',18),('Araceli',60,'arsvs@gmail.com',2)]
    # cur.executemany(query,record_insert)
    # conn.commit()
    # count=cur.rowcount
    # print(f'{count} registros insertados en la tabla alumno')

    # Update
    # query="UPDATE alumno SET id_salon=%s where id_alumno =%s"
    # alumno_id=(2,1)
    # cur.execute(query,alumno_id)
    # conn.commit()

# Delete
    # query="DELETE from alumno where id_alumno=%s"
    # alumno_n=(25, )
    # cur.execute(query,alumno_n)
    # conn.commit()

except Error as error:
    print(f"Hubo un error: {str(error)}")
finally:
    if(conn):
        cur.close()
        conn.close()
