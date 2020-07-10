import conexion

data = {"nombreTipoPago": "Contado"}
conn = conexion.conexionBDD(4)
datas = [
    {"nombreTipoPago": "Credito"}, 
    {"nombreTipoPago": "Tarjeta de Credito"}]
#coll = conn.insertarMongo("tipopago",data)
#coll = conn.insertarResgistros("tipopago", datas)
data = {"nombreTipoPago": "Credito"}
#coll = conn.leerRegistro("tipopago",data)
coll = conn.leerRegistros("tipopago",data)

for obj in coll:
    print(obj)

dataActualizar = {"nombreTipoPago": "Credito 60 dias"}
coll = conn.actualizarResgistro("tipopago",data,dataActualizar)
print (coll)
data = {}
coll = conn.leerRegistros("tipopago",data)
for obj in coll:
    print(obj)
