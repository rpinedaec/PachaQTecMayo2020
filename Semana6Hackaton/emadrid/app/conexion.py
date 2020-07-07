#CRUD en una clase generica
#Mysql
import mysql.connector
from mysql.connector import errorcode

class conexionBDD:   
    def __init__(self,intBDD):
        self.intBDD= intBDD
#si es 1 conectarnos a Mysql, si es 2 conectarnos a postgres y si 3 conectarnos sqlite
    
    def conexion(self):
        if(self.intBDD == 1):
            try:
                conn = mysql.connector.connect(user='root',
                                password='L1m42020$',
                                host="localhost",
                                port="3306",
                                database="hackaton6emadrid")
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
        except Exception as errorcode:
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