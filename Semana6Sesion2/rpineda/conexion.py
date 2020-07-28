#CRUD en una clase generica
#Mysql
import mysql.connector
from mysql.connector import errorcode
#Posgres
import psycopg2
from psycopg2 import Error
import sqlite3 


class conexionBDD:
    def __init__(self, intBDD):
        self.intBDD = intBDD

    def conexion(self):
        if(self.intBDD == 1):
            try:
                conn = mysql.connector.connect(user='root',
                                               password="1984RICARDO2011PAPO",
                                               host="localhost",
                                               port="3306",
                                               database="avellaneda")
                return conn
            except(mysql.connector.Error, Exception) as error:
                return False

        elif(self.intBDD == 2):
            try:
                conn = psycopg2.connect(user='postgres',
                                        password="1984RICARDO2011PAPO",
                                        host="localhost",
                                        port="5432",
                                        database="avellaneda")
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
