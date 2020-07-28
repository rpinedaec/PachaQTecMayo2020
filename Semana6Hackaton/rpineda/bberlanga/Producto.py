import Connection

# Read: select por id
def select_producto(id):
    query="SELECT * FROM producto WHERE id_producto="+id
    Connection.mycursor.execute(query)
    reg=Connection.mycursor.fetchall()
    print(reg)

# Create: insert producto
def insert_producto(nombre_producto,precio_producto):
    query="INSERT INTO producto (nombre_producto,precio_unitario_producto) VALUES (%s,%s)"
    reg=(nombre_producto,precio_producto)
    Connection.mycursor.execute(query,reg)
    Connection.mydb.commit()

# Delete: delete producto
def delete_producto(id):
    query="DELETE FROM producto WHERE id_producto="+id
    Connection.mycursor.execute(query)
    Connection.mydb.commit()

# Update: update producto
def update_producto(field,new_value,id):
    query="UPDATE producto SET {}='{}' WHERE id_producto='{}'"\
        .format(field,new_value,id)
    Connection.mycursor.execute(query)
    Connection.mydb.commit()
