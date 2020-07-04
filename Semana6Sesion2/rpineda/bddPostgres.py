import psycopg2
from psycopg2 import Error

try:
    conn = psycopg2.connect(user='postgres',
                            password='pachaqtec',
                            host="localhost",
                            port="5432",
                            database="rpineda")
    cur = conn.cursor()
    cur.execute("Select version();")
    record = cur.fetchone()
    print(record)
except Error as error:
    print(f"Hubo un error: {str(error)}")
finally:
    if(conn):
        cur.close()
        conn.close()

try:
    conn = psycopg2.connect(user='postgres',
                            password='pachaqtec',
                            host="localhost",
                            port="5432",
                            database="rpineda")
    cur = conn.cursor()
    query = "insert into alumno (nombreAlumno, edadAlumno, correoAlumno) values('Denisse Garcia', '24', 'denisse@pachaqtec.pe');"
    cur.execute(query)
    conn.commit()
    query = "select * from alumno;"
    cur.execute(query)
    record = cur.fetchall()
    print(record)
except Error as error:
    print(f"Hubo un error: {str(error)}")
finally:
    if(conn):
        cur.close()
        conn.close()


try:
    conn = psycopg2.connect(user='postgres',
                            password='pachaqtec',
                            host="localhost",
                            port="5432",
                            database="rpineda")
    cur = conn.cursor()
    query = "update alumno set  nombreAlumno = 'Pepito', edadAlumno = '30',  correoAlumno = 'pepito@pachaqtec.pe' where idAlumno = 2;"
    cur.execute(query)
    conn.commit()
    query = "select * from alumno;"
    cur.execute(query)
    record = cur.fetchall()
    print(record)
except Error as error:
    print(f"Hubo un error: {str(error)}")
finally:
    if(conn):
        cur.close()
        conn.close()


