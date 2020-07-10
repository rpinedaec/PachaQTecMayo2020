import mysql.connector
from mysql.connector import errorcode


try:
    conn = mysql.connector.connect(user='admin',
                                password='cocakola2020',
                                host="localhost",
                                port="3306",
                                database="hackaton6asamaniego")

    
except(mysql.connector.Error, Exception) as error:
    print(error)
