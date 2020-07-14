import mysql.connector


conn = mysql.connector.connect(user='root',
                               password="ciritaPc30",
                               host="localhost",
                               port="3306",
                               database="asamaniego")
cur = conn.cursor()
cur.execute("insert into alumno (nombreAlumno, edadAlumno, correoAlumno) values('Denisse Garcia', '24', 'denisse@pachaqtec.pe');")
conn.commit()
cur.execute("Select * from alumno;")