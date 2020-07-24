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
        #self.intBDD= intBDD
        self.intBDD= 1
#si es 1 conectarnos a Mysql, si es 2 conectarnos a postgres y si 3 conectarnos sqlite
    
    def conexion(self):
        if(self.intBDD == 1):
            try:
                conn = mysql.connector.connect(user='admin',
                                password='cocakola2020',
                                host="localhost",
                                port="3306",
                                database="hackaton6asamaniego")
                return conn
            except(mysql.connector.Error, Exception) as error:
                return False
            
        elif(self.intBDD == 2):
            try:
                conn = psycopg2.connect(user='postgres',
                            password='cocakola2020',
                            host="localhost",
                            port="5432",
                            database="asamaniego")
                return conn
            except Exception as error:
                return False
            
        else:
            try:
                conn = sqlite3.connect('asamaniego.db')
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
        #conexion = self.conexion()
        
        try:
            conexion = self.conexion()
            print("paso")
            cur = conexion.cursor()
            cur.execute(query)
            conexion.commit()
            exito = True
            return exito
        except Exception as identifier:
            print(identifier)
            return False