from pymongo import MongoClient, errors

class Conexion:
    def __init__(self, uri, database):
        self.client = MongoClient(uri)
        self.db = self.client[database]
        print('Conexión a la base de datos, exitosa')
    
    def insertar_registro(self, collection, data):
        collection = self.db[collection]
        result = collection.insert_one(data)
        print(f'Inserted row: {result.inserted_id}')
    
    def insertar_registros(self,collection, data):
        collection = self.db[collection]
        result = collection.insert_many(data)
        print(f'Inserted rows: {result.inserted_ids}')        

    def obtener_registros(self, collection, condition={}):
        collection = self.db[collection]
        data = collection.find(condition)
        return list(data)

    def obtener_registro(self, collection, condition={}):
        collection = self.db[collection]
        data = collection.find_one(condition)
        return list(data)

    def actualizar_registro(self, collection, condition, change):
        collection = self.db[collection]
        collection.update_one(condition, {
            '$set': change
        })
        print(f'Se actualizo un registro')

    def eliminar_registro(self, collection, condition):
        collection = self.db[collection]
        collection.delete_one(condition)
        print(f'Se elimino un registro')
        
    def cerrar_conexion(self):
        self.db.close()
        print('Se cerro la conexión con exito !')
        return True
    