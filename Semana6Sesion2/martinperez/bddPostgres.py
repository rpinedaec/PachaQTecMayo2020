import psycopg2
from psycopg2 import Error



try:
    conn = psycopg2.connect(user='postgres',
                            password='passmysqlmartin',
                            host="localhost",
                            port="5432",
                            database="martinperez")
    cur = conn.cursor()
    cur.execute("select version();")
    retornoData = cur.fetchone()
    print(retornoData)
except Error as error:
    print(f"Se produjo un error: {str(error)}")
finally:
    if(conn):
        cur.close()
        conn.close()


try:
    conn = psycopg2.connect(user='postgres',
                            password='passmysqlmartin',
                            host="localhost",
                            port="5432",
                            database="martinperez")
    cur = conn.cursor()
    query="insert into alumno(nombre,edad,correo) values('Tercero',29,'tercero@pachaqtec.edu.pe')"
    cur.execute(query)
    conn.commit()
    query="select * from alumno;"
    cur.execute(query)
    retornoSelect = cur.fetchall()
    print(retornoSelect)
except Error as error:
    print(f"Error: {str(error)}")
finally:
    if(conn):
        cur.close()
        conn.close()

 


try:
    conn = psycopg2.connect(user='postgres',
                            password='passmysqlmartin',
                            host="localhost",
                            port="5432",
                            database="martinperez")
    cur = conn.cursor()
    query="update alumno set nombre='Pedro Jonas',edad=34,correo='pedrojonas@pachaqtec.edu.pe' where idalumno=17"
    cur.execute(query)
    conn.commit()
    query="select * from alumno;"
    cur.execute(query)
    retornoSelect = cur.fetchall()
    print(retornoSelect)
except Error as error:
    print(f"Error: {str(error)}")
finally:
    if(conn):
        cur.close()
        conn.close()


