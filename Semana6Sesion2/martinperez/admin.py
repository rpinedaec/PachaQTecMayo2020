import conexion

manager = conexion.conexionBDD(1)
query = "SELECT * FROM alumno;"
datos = manager.consultarBDD(query)
query = "INSERT INTO alumno (nombre, edad, correo) values('PruebaFinal','39','prueba@pachaqtec.edu.pe')"
datos = manager.ejecutarBDD(query)
if(datos):
    print("Se ejecuto Insertar correctamente")
else:
    print("hubo un error")


query = "SELECT * FROM alumno;"
datos = manager.consultarBDD(query)
print(datos)


query = "Update  alumno set nombre = 'Karen' where idalumno> 0 and nombre='PruebaFinal'"
datos = manager.ejecutarBDD(query)
if(datos):
    print("Se ejecuto Actualizar correctamente")
else:
    print("hubo un error")

query = "SELECT * FROM alumno;"
datos = manager.consultarBDD(query)   
print(datos)

query = "Delete  from alumno  where idalumno>0 and nombre='Karen'"
datos = manager.ejecutarBDD(query)
if(datos):
     print("Se ejecuto Eliminar correctamente")
else:
     print("hubo un error")

query = "SELECT * FROM alumno;"
datos = manager.consultarBDD(query)   
print(datos)
