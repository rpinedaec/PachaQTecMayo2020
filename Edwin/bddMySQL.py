import mysql.connector
from mysql.connector import errorcode



try:
    # Hago la conexión a la base de datos:
    conexion = mysql.connector.connect(user = 'root',
                            password = 'Lana2409',
                            host = 'localhost',
                            port = '3306',
                            database = 'db_ezagastizabal')
    cursor = conexion.cursor()
    cursor.execute("Select version_();")
    record = cursor.fetchone()
    print(record)
except (mysql.connector.Error, Exception) as error:
    print(f"Hubo un error {error}")
finally:
    if (conexion):
        cursor.close()
        conexion.close()

