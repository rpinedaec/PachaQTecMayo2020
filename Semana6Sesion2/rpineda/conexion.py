#CRUD en una clase generica
#Mysql
import mysql.connector
from mysql.connector import errorcode
#Posgres
import psycopg2
from psycopg2 import Error
<<<<<<< HEAD
#sqlite
<<<<<<< HEAD
<<<<<<< HEAD
import sqlite3
 
class conexionBDD:   
    def __init__(self,intBDD):
        self.intBDD= intBDD
=======
=======

>>>>>>> rpineda/master
=======
>>>>>>> rpineda/develop
import sqlite3 


class conexionBDD:
    def __init__(self, intBDD):
        self.intBDD = intBDD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> upstream/develop
=======

>>>>>>> rpineda/master
#si es 1 conectarnos a Mysql, si es 2 conectarnos a postgres y si 3 conectarnos sqlite
=======
>>>>>>> rpineda/develop

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

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    def consultarBDD(self, query): 
        try:    
=======
    def consultarBDD(self, query):
        try:
>>>>>>> upstream/develop
=======
    def consultarBDD(self, query):
        try:
>>>>>>> upstream/develop
=======
    def consultarBDD(self, query):
        try:

>>>>>>> rpineda/master
=======

    def consultarBDD(self, query): 
        try:    
>>>>>>> rpineda/develop
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
