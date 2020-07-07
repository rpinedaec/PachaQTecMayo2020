# impory mysql
import mysql.connector
from mysql.connector import errorcode

conn = None
try:
    conn = mysql.connector.connect(user='root',
                               password="1984RICARDO2011PAPO",
                               host="localhost",
                               port="3306",
                               database="avellaneda")
    cur = conn.cursor()
    cur.execute("insert into alumno (aliasAlumno, edadAlumno, mailAlumno) values('Denisse Garcia 2', '26', 'denisse@pachaqtec.pex');")
    conn.commit()
    # imprimir contenido
    cur.execute("Select * from alumno;")
    returnData = cur.fetchall()
    print(returnData)
except mysql.connector.Error as err:
    print("El error es el siguiente: " + str(err)) 
finally:
    if(conn):
        cur.close()
        conn.close()                              

