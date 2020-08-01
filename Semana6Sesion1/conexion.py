#CRUD en una clase genérica
import mysql.connector
from mysql.connector import errorcode

import psycopg2
from psycopg2 import Error

import sqlite

class ConexionBDD:
    conn = None
    def __init__(self, intBDD):
        self.intBDD = intBDD

#Si es 1 (SQL), 2(POSGRES), 3(SQLite)
    def conexion:
        if (self.intBDD == 1):
            try:
                conn = mysql.connector.connect(user = 'root',
                    password = 'Lana2409',
                    host = "localhost",
                    port = "3306",
                    database = 'db_ezagastizabal')
                return conn
            except (mysql.connector.Error, Exception) as error:
                return False
            finally:
                if(self.conn):
                    self.conn.close
        elif(self.intBDD == 2):
            try:
                conn = psycopg2.connect(user = 'postgres',
                    password = 'Lana2409',
                    host = 'localhost',
                    port = '5432',
                    database = 'db_ezagastizabal')
                return conn
            except Exception as error:
                return False
            finally:
                if(self.conn):
                    self.conn.close()
        else:
            pass
    
    def traerDatos(self,query):
        try:
            cur = self.conn.cursor()
            cur.execute("select version();")
            records = cur.fetchall()
            return records
        except Error as error:
            return False
    
    def insertarDatos(self, query):
        try:
            cur = self.conn.cursor()
            cur.execute("select version();")
            self.conn.commit()
            exito = True
            return exito
        except expression as identifier:
            return False
        else:
            pass
        finally:
            pass

    
    def actualizarDatos(self,query):
        try:
            cur = self.conn.cursor()
            cur.execute("select version();")
            self.conn.commit()
            exito = True
        return exito
        except Error as Error:
            return False
        finally:
            pass

    
    def borrarDatos(self,query):
        try:
            cur = self.conn.cursor()
            cur.execute("select version();")
            self.conn.commit()
            exito = True
            return exito
        except Exception as error:
            return False


    

    