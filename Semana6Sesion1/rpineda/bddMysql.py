import mysql.connector
from mysql.connector import errorcode
try:
    conn = mysql.connector.connect(user='root',
                               password="pachaqtec",
                               host="localhost",
                               port="3306",
                               database="rpineda")
    cur = conn.cursor()
    cur.execute("insert into alumno (nombreAlumno, edadAlumno, correoAlumno) values('Denisse Garcia', '24', 'denisse@pachaqtec.pe');")
    conn.commit()
    cur.execute("Select * from alumno;")
    
    returnData = cur.fetchall()
    print(returnData)
except mysql.connector.Error as err:
    print(f"El error es el siguiente: {err}")
finally:
    if(conn):
        cur.close()
        conn.close()                              

