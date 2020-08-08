import psycopg2
from psycopg2 import Error

try:
    # Hago la conexión a la base de datos:
    conexion = psycopg2.connect(user = 'postgres',
                            password = 'Lana2409',
                            host = 'localhost',
                            port = '5432',
                            database = 'db_ezagastizabal')

    cursor = conexion.cursor()
    query = "UPDATE alumnos SET correo_alumno = 'edwin.zagastizabal@gmail.com' WHERE id_alumno = 3;"
    cursor.execute(query)
    conexion.commit()
    
    query = "SELECT * FROM alumnos;"
    cursor.execute(query)
    record = cursor.fetchall()
    print(record)

except Error as error:
    print(f"Hubo un error: {str(error)}")
finally:
    if (conexion):
        cursor.close()
        conexion.close()
