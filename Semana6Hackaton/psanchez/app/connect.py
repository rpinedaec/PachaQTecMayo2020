import mysql.connector
from mysql.connector import errorcode

class conexionBDD:   
    def __init__(self,intBDD):
        self.intBDD= intBDD

    def conexion(self, conn):
        try:
            conn = mysql.connector.connect(user='root',
                            password='pachaqtec',
                            host="localhost",
                            port="3306",
                            database="hackathons6")
            return conn
        except(mysql.connector.Error, Exception) as error:
            return False            

    def consultarBDD(self, query): 
        try:
            conexion = self.conexion()
            cur = conexion.cursor()
            cur.execute(query)
            records = cur.fetchall()
            return records
        except Error as error:
            return False
    
    def ejecutarBDD(self, query):
        try:
            conexion = self.conexion()
            cur = conexion.cursor()
            cur.execute(query)
            conexion.commit()
            exito = True
            return exito
        except Exception as identifier:
            return False