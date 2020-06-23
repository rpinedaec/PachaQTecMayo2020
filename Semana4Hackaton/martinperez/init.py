import os
import utils
from time import sleep
import json
import clases


#Variables Globales
log = utils.log("INIT")
fileProducto = utils.fileManager("Productos.txt")
lstProductos = []
lstProductosDic = []
fileCliente = utils.fileManager("Clientes.txt")
lstClientes = []
lstClientesDic = []
fileEmpleados = utils.fileManager("Empleados.txt")
lstEmpleados = []
lstEmpleadosDic = [] 
fileUnidadMedida = utils.fileManager("UnidadMedida.txt")
lstUnidadMedida = []
lstUnidadMedidaDic = [] 

listUnidadMedida = ["UN","KG","LT","TON","MG","ML"]



def seleccionUnidadMedida(listUnidadMedida):
    strRetornar = "" 
    while strRetornar=="":
        strSeleccionUM=utils.validarEntero("Para agregar UM=99 /Ingrese numero de UM: ")
        if(strSeleccionUM==99):
            pasarTrue = True 
            while pasarTrue:
                strNuevo = input("0=Salir / Nueva UM: ")
                if(strNuevo=="0"):
                    pasarTrue=False
                    break
                intConta = 0
                for p in listUnidadMedida:
                    if(strNuevo==p.nombre):
                        intConta+=1
                if(intConta>0):
                    pasarTrue=True
                    print("Valor existente.")
                else:
                    pasarTrue=False
                    strRetornar=strNuevo
                    mayor=utils.AutogenerarMayorMasUno(listUnidadMedida)
                    unidad = clases.UnidadMedidad(mayor, strNuevo)
                    fileUnidadMedida.borrarArchivo()
                    lstUnidadMedidaDic.append(unidad.dictUnidadMedida()) 
                    jsonStr = json.dumps(lstUnidadMedidaDic) 
                    fileUnidadMedida.escribirArchivo(jsonStr)
                    break
        else:
            intContar2 = 0
            for p in listUnidadMedida:
                intContar2+=1
                if(intContar2==int(strSeleccionUM)):
                    strRetornar = p.nombre
                    break
    return strRetornar



def cargarUnidadMedida():
    try:
        pasar = True
        while pasar:
            res = fileUnidadMedida.leerArchivo()
            try:
                lstUnidadMedidaTemp = json.loads(res) 
                for dicUnidad in lstUnidadMedidaTemp:
                    objUnidadMedida = clases.UnidadMedidad(dicUnidad["codigo"], dicUnidad["nombre"])
                    lstUnidadMedida.append(objUnidadMedida)
                    lstUnidadMedidaDic.append(dicUnidad) 
                    pasar=False
            except Exception as error:
                contador=0
                for p in listUnidadMedida:
                    contador += 1 
                    unidad = clases.UnidadMedidad(contador,p)
                    try: 
                        fileUnidadMedida.borrarArchivo()
                        lstUnidadMedidaDic.append(unidad.dictUnidadMedida()) 
                        jsonStr = json.dumps(lstUnidadMedidaDic) 
                        fileUnidadMedida.escribirArchivo(jsonStr)  
                    except Exception as error:
                        log.error(error) 
    except Exception as erro:
        log.error(erro) 



def cargarProductos():
    try:
        res = fileProducto.leerArchivo() 
        lstProducto = json.loads(res)
        for dicProducto in lstProducto:
            objProducto = clases.Producto(dicProducto["codigo"], dicProducto["nombre"],
                                dicProducto["cantidadProducto"], dicProducto["unidad"],
                                dicProducto["costoProducto"], dicProducto["total"])
            lstProductos.append(objProducto)
            lstProductosDic.append(dicProducto)
        #log.debug(lstProductosDic) 
    except Exception as erro:
        log.error(erro)


def cargarClientes():
    try:
        res = fileCliente.leerArchivo() 
        lstClientesTemp = json.loads(res)
        for dicCliente in lstClientesTemp:
            objCliente = clases.Cliente(dicCliente["codigo"],dicCliente["dni"], dicCliente["nombre"],
                                dicCliente["apellido"], dicCliente["edad"], dicCliente["codCliente"])
            lstClientes.append(objCliente)
            lstClientesDic.append(dicCliente)
        #log.debug(lstClientesDic) 
    except Exception as erro:
        log.error(erro)


def cargarEmpleados():
    try:
        res = fileEmpleados.leerArchivo() 
        lstEmpleadosTemp = json.loads(res)
        for dicEmpleado in lstEmpleadosTemp:
            objEmpleado = clases.Empleado(dicEmpleado["codigo"],dicEmpleado["dni"], dicEmpleado["nombre"],
                                dicEmpleado["apellido"], dicEmpleado["edad"], dicEmpleado["codEmpleado"])
            lstEmpleados.append(objEmpleado)
            lstEmpleadosDic.append(dicEmpleado)  
    except Exception as erro:
        log.error(erro)


cargarUnidadMedida()
cargarProductos()
cargarClientes()
cargarEmpleados()


dicOpcionesMenuPrincipal = {"Cliente": 1, "Empleado": 2, "Productos": 3}
menuPrincipal = clases.Menu("Menu de Inicio", dicOpcionesMenuPrincipal)

dicOpcionesAdministrador = {"Nuevo": 1, "Listar Todos": 2,"Eliminar":3}
menuAdministrador = clases.Menu("Menu Administrador", dicOpcionesAdministrador)

ControladorGeneral = True

while (ControladorGeneral):
    opcionMenuPrincipal = menuPrincipal.mostrarMenu()
    if(opcionMenuPrincipal == 9): 
        print(opcionMenuPrincipal)
        ControladorGeneral= False
        break
    elif(opcionMenuPrincipal == 1):
        salirCreacionCliente =True
        while salirCreacionCliente:
            res = menuAdministrador.mostrarMenu()
            if res==9:
                salirCreacionCliente = False
                break
            elif(res == 3):
                print("\n-------------CLIENTE A ELIMINAR-------------")
                utils.listaSimple(lstClientes, opcionMenuPrincipal)
                lstClientesTem = []
                ClienteEliminar = False
                boolEliminar =True
                while boolEliminar:
                    numero = utils.validarEntero("999:Para cancelar / Ingresa el codigo: ")
                    if(numero == 999):
                        boolEliminar = False
                        break
                    contarlis=0
                    lstClienteNew = []
                    for p in lstClientes:
                        contarlis+=1
                        if(p.codigo == numero):
                            lstClientestemporal = clases.Cliente(p.codigo,p.dni,p.nombre,p.apellido,p.edad,p.codCliente)
                            lstClientesTem.append(lstClientestemporal)                 
                            lstClientes.pop(contarlis-1)
                            ClienteEliminar = True
                            boolEliminar=False
                        else:
                            ClienteTemp = clases.Cliente(p.codigo,p.dni,p.nombre,p.apellido,p.edad,p.codCliente)
                            lstClienteNew.append(ClienteTemp.dictCliente())                            
                    fileCliente.borrarArchivo()
                    jsonStr = json.dumps(lstClienteNew)
                    fileCliente.escribirArchivo(jsonStr)
                if ClienteEliminar ==True:
                    print("\n-------------CLIENTE ELIMINADO-------------")
                    utils.listaSimple(lstClientesTem, opcionMenuPrincipal)
                    input("Enter para continuar...")
            elif(res == 2): 
                utils.listaSimple(lstClientes, opcionMenuPrincipal)
                input("Enter para continuar...")
            elif(res == 1):
                codigo = utils.AutogenerarMayorMasUno(lstClientes)
                dni = utils.validarDniEnLista(lstClientes,"DNI: ") 
                nombre = input("Nombre: ")
                apellido = input("Apellido: ") 
                edad = utils.validarEntero("Edad: ")
                cliente = clases.Cliente(codigo, dni, nombre, apellido, edad, codigo) 
                lstClientetemp = []
                lstClientetemp.append(cliente)
                try:
                    fileCliente.borrarArchivo()
                    lstClientesDic.append(cliente.dictCliente())
                    lstClientes.append(cliente)
                    jsonStr = json.dumps(lstClientesDic)
                    fileCliente.escribirArchivo(jsonStr)
                    print("\n-------------CLIENTE AGREGADO-------------")
                    utils.listaSimple(lstClientetemp, opcionMenuPrincipal)
                    input("Enter para continuar...") 
                except Exception as error:
                    log.error(error)  
    elif(opcionMenuPrincipal == 2):
        salirCreacionEmpleado =True
        while salirCreacionEmpleado:
            res = menuAdministrador.mostrarMenu()
            if res==9:
                salirCreacionEmpleado = False
                break
            elif(res == 3):
                print("\n-------------EMPLEADO A ELIMINAR-------------")
                utils.listaSimple(lstEmpleados, opcionMenuPrincipal)
                lstEmpleadosTem = []
                EmpleadoEliminar = False
                boolEliminar =True
                while boolEliminar:
                    numero = utils.validarEntero("999:Para cancelar / Ingresa el codigo: ")
                    if(numero == 999):
                        boolEliminar = False
                        break
                    contarlis=0
                    lstEmpleadosNew = []
                    for p in lstEmpleados:
                        contarlis+=1
                        if(p.codigo == numero):
                            lstEmpleadostemporal = clases.Empleado(p.codigo,p.dni,p.nombre,p.apellido,p.edad,p.codEmpleado)
                            lstEmpleadosTem.append(lstEmpleadostemporal)                 
                            lstEmpleados.pop(contarlis-1)
                            EmpleadoEliminar = True
                            boolEliminar=False
                        else:
                            EmpleadoTemp = clases.Empleado(p.codigo,p.dni,p.nombre,p.apellido,p.edad,p.codEmpleado)
                            lstEmpleadosNew.append(EmpleadoTemp.dictEmpleado())                            
                    fileEmpleados.borrarArchivo()
                    jsonStr = json.dumps(lstEmpleadosNew)
                    fileEmpleados.escribirArchivo(jsonStr)
                if EmpleadoEliminar ==True:
                    print("\n-------------EMPLEADO ELIMINADO-------------")
                    utils.listaSimple(lstEmpleadosTem, opcionMenuPrincipal)
                    input("Enter para continuar...")
            elif(res == 2): 
                utils.listaSimple(lstEmpleados, opcionMenuPrincipal)
                input("Enter para continuar...")
            elif(res == 1):
                codigo = utils.AutogenerarMayorMasUno(lstEmpleados)
                dni = utils.validarDniEnLista(lstEmpleados,"DNI: ") 
                nombre = input("Nombre: ")
                apellido = input("Apellido: ") 
                edad = utils.validarEntero("Edad: ")
                empleado = clases.Empleado(codigo, dni, nombre, apellido, edad, codigo) 
                lstEmpleadotemp = []
                lstEmpleadotemp.append(empleado)
                try:
                    fileEmpleados.borrarArchivo()
                    lstEmpleadosDic.append(empleado.dictEmpleado())
                    lstEmpleados.append(empleado)
                    jsonStr = json.dumps(lstEmpleadosDic)
                    fileEmpleados.escribirArchivo(jsonStr)
                    print("\n-------------EMPLEADO AGREGADO-------------")
                    utils.listaSimple(lstEmpleadotemp, opcionMenuPrincipal) 
                    input("Enter para continuar...") 
                except Exception as error:
                    log.error(error)  
    elif(opcionMenuPrincipal == 3):
        salirCreacionProducto = True
        while salirCreacionProducto:
            res = menuAdministrador.mostrarMenu() 
            if(res == 9):
                salirCreacionProducto = False 
                break
            elif(res==3):
                print("\n-------------PRODUCTO A ELIMINAR-------------")
                utils.listaSimple(lstProductos, 111)
                lstProductosTem = []
                ProductoEliminar = False
                boolEliminar =True
                while boolEliminar:
                    numero = utils.validarEntero("999:Para cancelar / Ingresa el codigo: ")
                    if(numero == 999):
                        boolEliminar = False
                        break
                    contarlis=0
                    lstProductosNew = []
                    for p in lstProductos:
                        contarlis+=1
                        if(p.codigo == numero):
                            lstProductostemporal = clases.Producto(p.codigo,p.nombre,p.cantidadProducto
                                                                    ,p.unidad,p.costoProducto,p.total)
                            lstProductosTem.append(lstProductostemporal)                 
                            lstProductos.pop(contarlis-1)
                            ProductoEliminar = True
                            boolEliminar=False
                        else:
                            productoTemp = clases.Producto(p.codigo,p.nombre,p.cantidadProducto
                                                            ,p.unidad,p.costoProducto,p.total)
                            lstProductosNew.append(productoTemp.dictProducto())                            
                    fileProducto.borrarArchivo()
                    jsonStr = json.dumps(lstProductosNew)
                    fileProducto.escribirArchivo(jsonStr)
                if ProductoEliminar ==True:
                    print("\n-------------PRODUCTO ELIMINADO-------------")
                    utils.listaSimple(lstProductosTem, 111)
                    input("Enter para continuar...")
            elif(res==2):
                utils.listaSimple(lstProductos, opcionMenuPrincipal)
            elif(res == 1):
                codigo = utils.AutogenerarMayorMasUno(lstProductos)
                nomProducto = utils.validarNombreEnLista(lstProductos,"Nombre: ") 
                cantProducto = utils.validarFloat("Cantidad: ") 
                utils.listarUnidadMedida(lstUnidadMedida)
                unidad = seleccionUnidadMedida(lstUnidadMedida)
                costProducto = utils.validarFloat("Costo: ")
                total = cantProducto * costProducto
                producto = clases.Producto(codigo, nomProducto,
                                    cantProducto,unidad, costProducto,total) 
                lstProductostemp = []
                lstProductostemp.append(producto)
                try:
                    fileProducto.borrarArchivo()
                    lstProductosDic.append(producto.dictProducto())
                    lstProductos.append(producto)
                    jsonStr = json.dumps(lstProductosDic)
                    fileProducto.escribirArchivo(jsonStr)
                    print("\n-------------PRODUCTO AGREGADO-------------")
                    utils.listaSimple(lstProductostemp, 111)
                    input("Enter para continuar...")
                except Exception as error:
                    log.error(error)
 