import conexion

<<<<<<< HEAD
manager = conexion.conexionBDD(3)


=======
manager = conexion.conexionBDD(1)
>>>>>>> upstream/develop
query = "SELECT * FROM alumno;"
datos = manager.consultarBDD(query)
query = "INSERT INTO alumno (aliasAlumno, edadAlumno, mailAlumno) values('Roberto','36','rpineda@pachaqtec.edu.pe')"
datos = manager.ejecutarBDD(query)
if(datos):
    print("Se ejecuto correctamente")
else:
    print("hubo un error")

query = "SELECT * FROM alumno;"
datos = manager.consultarBDD(query)
print(datos)

query = "Update  alumno set aliasAlumno = 'Karen' where idalumno = 1"
datos = manager.ejecutarBDD(query)
if(datos):
    print("Se ejecuto correctamente")
else:
    print("hubo un error")

query = "Delete  from alumno  where idalumno = 3"
datos = manager.ejecutarBDD(query)
if(datos):
     print("Se ejecuto correctamente")
else:
     print("hubo un error")

query = "SELECT * FROM alumno;"
datos = manager.consultarBDD(query)   
print(datos)
