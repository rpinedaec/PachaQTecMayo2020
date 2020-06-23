from flask import Flask, render_template, request, redirect
import json
import webbrowser
import pyrebase

### Init Firebase ####
config = {
    "apiKey": "AIzaSyBE-4dojM9D6-IV3LUlIxg9K3Z6p6qnDR0",
    "authDomain": "pachaqtec-60f35.firebaseapp.com",
    "databaseURL": "https://pachaqtec-60f35.firebaseio.com",
    "projectId": "pachaqtec-60f35",
    "storageBucket": "pachaqtec-60f35.appspot.com",
    "messagingSenderId": "823061206994",
    "appId": "1:823061206994:web:677f59642383e20ab59a0b"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#### Init Flask ######
app = Flask(__name__)

localDb = {}
allProducts = {}


def showDb():
    allProducts = db.child("productos").get()
    # print(allProducts.val()["name"])
    print(json.dumps(allProducts.val(), sort_keys=True, indent=4))


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        localDb[request.form['ingresoProducto']] = {
            # 'name': productEntered,
            'value': request.form['ingresoValorProducto'],
            'quantity': request.form['ingresoCantidad'],
            'location': request.form['ubicacionProducto']
        }
        db.child("productos").child(request.form['ingresoProducto']).set(
            {
                # 'name': productEntered,
                'value': float(request.form['ingresoValorProducto']),
                'quantity': int(request.form['ingresoCantidad']),
                'location': request.form['ubicacionProducto']
            }
        )

        return redirect('/')
    else:
        return render_template('index.html', products=(db.child("productos").get()).val(), totalInventario=valueInventory())


def runWeb():
    print("Run Web")
    webbrowser.open_new('http://127.0.0.1:3000/')
    app.run(port=3000, debug=False, use_reloader=False)


def addProducts():
    KeepEntering = True
    while KeepEntering:

        rightEntered = True
        userEntered = input("Ingresar: A , SALIR: Q \n")
        if userEntered == "A":
            # INGRESO DE PRODUCTO
            while rightEntered:
                productEntered = input(
                    "Ingrese Nombre del Producto \n ").strip().lower()  # strip para eliminar espacios en blanco al comienzo y al final , LOWER, todo a miniscula

                asserUser = input('El valor agregar sera el siguiente : ' + productEntered +
                                  " . ¿Esta de acuerdo? ACEPTA: INGRESA => OK , OTRA TECLA: INGRESA DE NUEVO \n")
                if asserUser == "OK":
                    rightEntered = False

            # INGRESO DE VALOR
            while True:
                try:
                    valueEntered = float(
                        input("Ingrese Valor del producto en soles \n").strip())

                    break
                except ValueError:
                    print('Valor ingresado no es un numero. Ingrese de nuevo')

            # INGRESO DE CANTIDAD
            while True:
                try:
                    quantityEntered = int(
                        input("Ingrese Cantidad del producto \n").strip())
                    break
                except ValueError:
                    print('Valor ingresado no es un numero. Ingrese denuevo ')

            # INGRESO DE LUGAR UBICACION DEL PRODUCTO
            locationEntered = input(
                "Ingrese Locacion del  producto \n").strip()

            # Ingreso a la variable Local
            localDb[productEntered] = {
                # 'name': productEntered,
                'value': valueEntered,
                'quantity': quantityEntered,
                'location': locationEntered
            }

            # Ingreso a la base de datos remota
            db.child("productos").child(productEntered).set(
                {
                    # 'name': productEntered,
                    'value': valueEntered,
                    'quantity': quantityEntered,
                    'location': locationEntered
                }
            )
        elif userEntered == "Q":
            KeepEntering = False

        else:
            KeepEntering = True
            rightEntered = True


def RemoveProductByName():
    products = (db.child("productos").get()).val()
    print(json.dumps(products, indent=4))
    rightEntered = True
    while rightEntered:
        valueDelete = input("Ingrese nombre del elemento a eliminar \n")
        try:
            val = products[valueDelete]
            break
        except KeyError:
            print("Producto a borrar no existe. Intente de nuevo")

    # De la DB de FireBase

    db.child("productos").child(valueDelete).remove()
    print("Producto eliminado")

    # Del diccionario local

    localDb.pop(valueDelete)


def valueInventory():
    sumaTotal = 0
    products = (db.child("productos").get()).val()
    for product in products.values():
        sumaTotal = sumaTotal + (product["value"]) * int(product["quantity"])

    print("El valor total del inventario es : " + str(sumaTotal) + " soles ")
    return sumaTotal


if __name__ == '__main__':
    while True:
        print("Choose the next option:")
        print("1: Enter Web Version")
        print("2: Add Product")
        print("3: Remove Product")
        print("4: Show Inventary")
        print("5: Valor Total Inventario")
        print("6: Salir")
        print("######################################################################################################################################")
        print("Recuerda que si DESPUES de entrar a la OPCION 1 desea seguir en la consola. Tendrá que colocar Ctrl + C para salir de ejecucion del servidor y continuar con consola")
        print("######################################################################################################################################")
        valueEntered = input("Ingrese el valor a escoger : \n")
        print("Valor Ingresado es : " + valueEntered)
        # sincronizamos nuestro remoto con nuestro diccionario local
        localDb = (db.child("productos").get()).val()
        if valueEntered == "1":
            runWeb()
        elif valueEntered == "2":
            addProducts()
            input("Presione cualquier tecla para continuar")
        elif valueEntered == "3":
            RemoveProductByName()
            input("Presione cualquier tecla para continuar")
        elif valueEntered == "4":
            showDb()
            input("Presione cualquier tecla para continuar")
        elif valueEntered == "5":
            valueInventory()
            input("Presione cualquier tecla para continuar")
        elif valueEntered == "6":
            break
