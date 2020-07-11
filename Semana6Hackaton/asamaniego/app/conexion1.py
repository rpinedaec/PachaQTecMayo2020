#CRUD en una clase generica
#Mysql
class conexion1:
    def __init__(self,conn):
        self.conexion1_Ok = conn
    
    def consultarBDD(self, query): 
        try:
            conex = self.conexion1_Ok
            cur = conex.cursor()
            cur.execute(query)
            records = cur.fetchall()
            return records
        except Exception as error:
            return False
    

    def ejecutarBDD(self, query):
        #conexion = self.conexion()
        
        try:
            conex = self.conexion1_Ok
            cur = conex.cursor()
            cur.execute(query)
            conex.commit()
            exito = True
            return exito
        except Exception as identifier:
            print(identifier)
            return False