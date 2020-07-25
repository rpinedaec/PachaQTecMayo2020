from connection.conn import Conexion

class Cliente:
    def __init__(self,dni,nombre,apellido,correo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
#insertar registro
'''
conn = Conexion('mongodb://localhost:27017','bporras')
cliente = Cliente(71206369, 'Raul', 'Lopez', 'raul.lopez@correo.pe')
conn.insertar_registro('cliente', {
    'dni': cliente.dni,
    'nombre': cliente.nombre,
    'apellido': cliente.apellido,
    'correo': cliente.correo
})
'''

#insertar registros
'''
conn = Conexion('mongodb://localhost:27017','bporras')
cliente_1 = Cliente(55206369, 'Juan', 'Soto', 'juan.soto@correo.pe')
cliente_2 = Cliente(70206369, 'Luis', 'Rojas', 'luis.rojas@correo.pe')
conn.insertar_registros('cliente', [
    {
    'dni': cliente_1.dni,
    'nombre': cliente_1.nombre,
    'apellido': cliente_1.apellido,
    'correo': cliente_1.correo
    },
    {
    'dni': cliente_2.dni,
    'nombre': cliente_2.nombre,
    'apellido': cliente_2.apellido,
    'correo': cliente_2.correo
    }
])
'''
# recuperar registro
'''
conn = Conexion('mongodb://localhost:27017','bporras')
row = conn.obtener_registro('cliente',{'nombre':'Bruce'})
print(row)
print(conn.cerrar_conexion())
'''
# actualizar registro
'''
conn = Conexion('mongodb://localhost:27017','bporras')
conn.actualizar_registro('cliente', {
    'dni':71206364
},{
    'dni':10101010
})
'''

# eliminar un registro

conn = Conexion('mongodb://localhost:27017','bporras')
conn.eliminar_registro('cliente', {
    'dni':10101010
})