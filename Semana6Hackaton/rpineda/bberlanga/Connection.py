import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='3179billace',
    database='hackaton6bberlanga'
)
mycursor = mydb.cursor()
