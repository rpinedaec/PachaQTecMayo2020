import psycopg2
from psycopg2 import Error

conn = None
try:
    conn = psycopg2.connect(user='root',
                            password="1984RICARDO2011PAPO",
                            host="localhost",
                            port="3306",
                            database="avellaneda")
    cur = conn.cursor()
    cur.execute("Select version();")
    record = cur.fetchone()
    print(record)
except Error as error:
    # print(f"Hubo un error: {str(error)}")
    print("El error es el siguiente: " + str(error))
finally:
    if(conn):
        cur.close()
        conn.close()

try:
    conn = psycopg2.connect(user='postgres',
                            password="1984RICARDO2011PAPO",
                            host="localhost",
                            port="5432",
                            database="avellaneda")
    cur = conn.cursor()
    query = "insert into alumno (aliasAlumno, edadAlumno, mailAlumno) values('Denisse Garcia 2', '25', 'denisse@pachaqtec.pexls ');"
    cur.execute(query)
    conn.commit()
    query = "select * from alumno;"
    cur.execute(query)
    record = cur.fetchall()
    print(record)
except Error as error:
    # print(f"Hubo un error: {str(error)}")
    print("El error es el siguiente: " + str(error))
finally:
    if(conn):
        cur.close()
        conn.close()

'''
try:
    conn = psycopg2.connect(user='postgres',
                               password="1984RICARDO2011PAPO",
                               host="localhost",
                               port="5432",
                               database="avellaneda")
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
'''
