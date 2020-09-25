1. Vamos a la carpeta de trabajo

2. Creamos entorno virtual
    python -m venv venv
3. Activamos entorno virtual
    . venv/Scripts/activate
4. Instalamos dependencias
    flask, python-dotenv, twilio, psycopg2, flask-orator
5. Creamos el .env de configuracion
6. Creamos la aplicacion
7. Creamos el db.py
8. Creamos las migraciones
    orator make:migration create_clientes_table --table clientes --create
    orator make:migration create_productos_table --table productos --create
    orator make:migration create_pedidos_table --table pedidos --create
9. Creamos los seeeders
    orator make:seed cliente_table_seeder
    orator make:seed producto_table_seeder
    orator make:seed pedido_table_seeder
10. Creamos los modelos
    orator make:model Cliente
    orator make:model Producto
    orator make:model Pedido
11. Creamos las rutas
    

