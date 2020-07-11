import conexionEZ

# manager = conexionEZ.ConexionBDD(2)
# query = "SELECT * FROM alumnos;"
# datos = manager.getData(query)
# print(datos)

manager = conexionEZ.ConexionBDD(2)
query = "INSERT INTO alumnos (nombre_alumno, edad_alumno, correo_alumno) values('Diego Rios', '26', 'dieriios@gmail.com');"
datos = manager.insertData(query)


# manager = conexionEZ.ConexionBDD(1)
# query = "DELETE FROM alumnos WHERE id_alumno = 4;"
# datos = manager.insertData(query)

# if (datos):
#     print("Se ejecuto correctamente")
# else:
#     print("Hubo error")

query = "SELECT * FROM alumnos;"
datos = manager.getData(query)
print(datos)