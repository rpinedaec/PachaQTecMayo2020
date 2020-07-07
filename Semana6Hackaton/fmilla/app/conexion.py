#Mysql
import mysql.connector
#Posgres
import psycopg2

class conexionBDD:   
    def __init__(self,intBDD):
        self.intBDD= intBDD
    
    def conexion(self):
        if(self.intBDD == 1):
            try:
                conn = mysql.connector.connect(user='root',
                                    password='SH4wnM3nd3s',
                                    host='localhost',
                                    database='Hackatons6fmilla')
                return conn
            except:
                return False
            
        elif(self.intBDD == 2):
            try:
                conn = psycopg2.connect(user='postgres',
                            password='SH4wnM3nd3s',
                            host="localhost",
                            port="5432",
                            database="fmilla")
                return conn
            except:
                return False

    def consultarBDD(self, query): 
        try:
            conexion = self.conexion()
            cur = conexion.cursor()
            cur.execute(query)
            records = cur.fetchall()
            return records
        except:
            return False
    
    def ejecutarBDD(self, query):
        try:
            conexion = self.conexion()
            cur = conexion.cursor()
            cur.execute(query)
            conexion.commit()
            exito = True
            return exito
        except:
            return False