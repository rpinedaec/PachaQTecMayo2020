1. Vamos a la carpeta de trabajo

2. Creamos entorno virtual
    python -m venv venv
3. Activamos entorno virtual
    . venv/Scripts/activate
4. Instalamos dependencias
    pip install flask
    pip install python-dotenv
    pip install twilio==6
    pip install psycopg2
    pip install flask-orator
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

9.  CONSULTA: orator migrate:status -c db.py
9.  MIGRAR: orator migrate -c db.py
9.  SUBIR SEEDS: orator migrate:refresh --seed -c db.py

10. Creamos los modelos
    orator make:model Cliente
    orator make:model Producto
    orator make:model Pedido
11. Creamos las rutas
    
11. CONSULTAR NGROK: ./ngrok.exe http 5000
