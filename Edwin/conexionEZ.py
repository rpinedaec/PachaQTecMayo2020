#CRUD para todos

#MySQL
import mysql.connector
from mysql.connector import errorcode

#Postgres
import psycopg2
from psycopg2 import Error


class ConexionBDD:
    def __init__ (self, intBDD):
        self.intBDD = intBDD
    
    def conexion(self):
        if(self.intBDD == 1):#Nos conectanos a MySQL
            try:
                conexion = mysql.connector.connect(user = 'root',
                                            password = 'Lana2409',
                                            host = 'localhost',
                                            port = '3306',
                                            database = 'db_ezagastizabal')
                return conexion
            except (mysql.connector.Error, Exception) as error:
                print(f"{error}")

        elif(self.intBDD == 2):#Nos conectanos a Postgres
            try:
                conexion = psycopg2.connect(user = 'postgres',
                                    password = 'Lana2409',
                                    host = 'localhost',
                                    port = '5432',
                                    database = 'db_ezagastizabal')
                return conexion
            except Exception as error:
                return False
        else:
            pass
    
    def getData(self, query):
        conexion = self.conexion()
        cursor = conexion.cursor()
        cursor.execute(query)
        record = cursor.fetchall()
        return record
    
    def insertData(self,query):
        conexion = self.conexion()
        cursor = conexion.cursor()
        cursor.execute(query)
        conexion.commit()
        exito = True
        return exito