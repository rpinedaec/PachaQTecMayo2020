import mysql.connector
from mysql.connector import errorcode
import conexion1

try:
    conn = mysql.connector.connect(user='admin',
                                password='cocakola2020',
                                host="localhost",
                                port="3306",
                                database="hackaton6asamaniego")

    
except(mysql.connector.Error, Exception) as error:
    print(error)

     
def buscarEmpresa(resultQueryE,item):
    a = 0
    tamanio = len(resultQueryE)
    ciclo = True
    nombre ="no existe "

    while ciclo == True:
        cadena = resultQueryE[a][1].strip()
        print(f"cadena: {cadena}")
        print(f"item: {item}")
        
        if cadena  == item:
            nombre = resultQueryE[a][2]
            break
        
        
            
        
        a = a +1
        if tamanio > a:
            break

    return(nombre)
    
def buscarCliente(resultQueryC,item):
    a = 0
    tamanio = len(resultQueryC)
    ciclo = True
    nombre ="no existe"

    while ciclo == True:
        
        if resultQueryC[a][0]== item:
            nombre = resultQueryC[a][1]
            break
        
        
            
        
        a = a +1
        if tamanio > a:
            break

    return(nombre)       

def buscarProducto(resultQueryP,item):
    a = 0
    tamanio = len(resultQueryP)
    ciclo = True
    nombre ="no existe"

    while ciclo == True:
        cadena = resultQueryP[a][0]
        #print(f"cadena: {cadena}")
        #print(f"item: {item}")
        
        
        if cadena  == item:
            tipoP = str(resultQueryP[a][3])
            precio = str(resultQueryP[a][2])
            nombre = precio +'*'+ tipoP + resultQueryP[a][1]
            break
        
        
            
        
        a = a +1
        if tamanio == a:
            break

    return(nombre)         

cnx1 =  conexion1.conexion1(conn)
import datetime
fechaHoy = datetime.datetime.now()

queryClientes = "select idCliente, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;"
queryEmpresas = "SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;"

dataClientes = cnx1.consultarBDD(queryClientes)
queryProductos = "SELECT idproducto, nombreProducto as Nombre, valorProducto as Valor, igvProducto as IGV FROM productos;"

dato= 12
ruc = '2121212121'
dataEmpresas = cnx1.consultarBDD(queryEmpresas)
dataProductos = cnx1.consultarBDD(queryProductos)
#print(dataEmpresas[a][1]) 
#print(dataEmpresas)
#print(len(dataEmpresas))
#print(dataEmpresas[0][0], data[1][0], data[2][0])

#print(buscar(queryClientes,dato))
#print(buscarEmpresa(dataEmpresas,ruc))

   

def emitirFactura(lstEmpresa):
    ruc = input('ingresa el RUC: ')
    nombreE = buscarEmpresa(lstEmpresa, ruc)
    if nombreE == "no existe":
        print("no existe la empresa ")
        print("Ingresa los datos de la empresa")
        print("-------------------------------")
        print(f"RUC:  {ruc}")
        print(f"Fecha: {fechaHoy.strftime('%d-%m-%Y')}")
        empresa = input("Razón Social: ")
        direcEmpresa = input("Dirección: ")
    else:
        print("Datos de la empresa")
        print("-------------------------------")
        print(f"Razón Social: {nombreE}")
        print(f"RUC:  {ruc}")
        print(f"Fecha: {fechaHoy.strftime('%d-%m-%Y')}")
        

    print("-------------------------------")
    print("Ingreso de Productos: ")
    print("-------------------------------")
    sigue = True       
    subtotalItem = 0
    subtotalIGV =0
    subtotalSinIGV = 0
    detalle=[]
    cabecera = []
    idcabeceraF=2
    while sigue == True: 
        prod = int(input('ingresa el código del producto: '))
        nombreProd = buscarProducto(dataProductos, prod)
        pos = nombreProd.find("*")
        precio = nombreProd[0:pos] 
        precio = float(precio)
        igv = int(nombreProd[pos+1:pos+2])  
        producto = nombreProd[pos+2:]
        print(f"Producto: {producto}") 
        print(f"precio unitario : {precio}")
        print(f"tiene IGV : {igv}")
        cant = int(input('ingresa la cantidad: '))
        subtotalItem = precio * cant
        print(f"subtotalitem {subtotalItem}")
        if igv ==1:
              subtotalIGV= subtotalIGV + subtotalItem
        elif igv == 2:
              subtotalSinIGV= subtotalSinIGV + subtotalItem
        
        print(f"Subtotal : {subtotalItem}")
        #cabecera.append(subtotalIGV, subtotalItem, total,idpyme, )      
        #detalle.append((cant, idcabeceraF, prod,subtotalItem))

        opcion = int(input('[1] Ingresar más productos \n [2] Total a pagar'))
        if (opcion == 2):
                     break
                     
    total = subtotalItem + subtotalSinIGV
    #print(f"Subtotal : {}")
    IGVTotal = float(subtotalIGV / 1.18)
    
    print(f"IGV : {IGVTotal}")
    print(f"Total : {total}")

def emitirBoleta():
    print("hola")


comprobante = True
while comprobante:
    print(' ------------------------------')
    print(' -----Comprobante de pago------')
    print(' ------------------------------')
    print(' ')
    print('Desea emitir una boleta o factura? Elija la opción: ')
    comprobante = input('[1] Factura \n [2] Boleta \n [3] Salir  ')
    if comprobante == '1':
        emitirFactura(dataEmpresas)
    elif comprobante == '2':
        emitirBoleta()
    else:
        combrobante = False
        break

