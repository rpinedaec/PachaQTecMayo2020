import psycopg2
import sys

conn = psycopg2.connect(user='postgres',
                        password='',
                        host="localhost",
                        port="5432",
                        database="rpineda")
                        