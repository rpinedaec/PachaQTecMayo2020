import conexion

conn = conexion.conexionBDD(3)

print(conn)

collection = conn["clientes"]
data = {"nombreCliente":"Edwin", "apellidoCliente": "Pineda", "dni": "0002"}