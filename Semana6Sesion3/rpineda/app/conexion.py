#CRUD en una clase generica
#Mysql
import mysql.connector
from mysql.connector import errorcode
#Posgres
import psycopg2
from psycopg2 import Error
#sqlite
import sqlite3

class conexionBDD:   
    def __init__(self,intBDD):
        self.intBDD= intBDD
#si es 1 conectarnos a Mysql, si es 2 conectarnos a postgres y si 3 conectarnos sqlite
    
    def conexion(self):
        if(self.intBDD == 1):
            try:
                conn = mysql.connector.connect(user='root',
                                password='pachaqtec',
                                host="localhost",
                                port="3306",
                                database="rpineda")
                return conn
            except(mysql.connector.Error, Exception) as error:
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
                conn = sqlite3.connect('rpineda.db')
                return conn
            except Exception as error:
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