#CRUD en una clase generica
import utils
#Mysql
import mysql.connector
from mysql.connector import errorcode
#Posgres
import psycopg2
from psycopg2 import Error


class conexionBDD:
    __log = utils.log("Conexion")

    def __init__(self,intBDD, usuario, clave, host, BD):
        self.intBDD= intBDD
        self.usuario = usuario
        self.clave = clave
        self.host = host
        self.BD = BD
    #si es 1 conectarnos a Mysql, si es 2 conectarnos a postgres y si 3 conectarnos oracle 11g
    
    def conexion(self):
        if(self.intBDD == 1):
            try:
                conn = mysql.connector.connect(user=self.usuario,
                                password=self.clave,
                                host=self.host,
                                port="3306",
                                database=self.BD)
                self.__log.debug("Conexion Correcta")
                return conn
            except(mysql.connector.Error, Exception) as e:
                self.__log.error(f"Conexion Incorrecta --- {e}")
                return False
            
        elif(self.intBDD == 2):
            try:
                conn = psycopg2.connect(user='postgres',
                            password='pachaqtec',
                            host="localhost",
                            port="5432",
                            database="rpineda")
                return conn
            except Exception as error:
                return False
            
        else:
            try:                
                #Oracle 11g
                import cx_Oracle
                con =  cx_Oracle.connect('system/system@localhost/xe')
                return conn
            except Exception as error:
                return False

    def CreateDB(self, query):
        try:
            conexion = self.conexion()
            conexion.autocommit = True
            cur = conexion.cursor()
            cur.execute(query)
            self.__log.debug("La base de datos se ah creado")
            return True
        except Exception as identifier:
            self.__log.debug("Hubo un problema al crear la BD")
            return False    

    def consultarBDD(self, query):
        self.__log.info(query) 
        try:
            conexion = self.conexion()
            cur = conexion.cursor()
            cur.execute(query)
            records = cur.fetchall()
            return records           
            self.__log.info("La consulta fue exitosa")
        except Error as error:
            self.__log.info("Hubo un error en la consulta")
            return False
    
    def ejecutarBDD(self, query):
        self.__log.info(query)
        try:            
            conexion = self.conexion()
            cur = conexion.cursor()
            cur.execute(query)
            conexion.commit()
            exito = True
            self.__log.debug("Se ejecuto correcto el query")
            return exito
        except Exception as e:
            self.__log.error(f"Hubo un error al ejecutar la query --- {e}")
            return False

