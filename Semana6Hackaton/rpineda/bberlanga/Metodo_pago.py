import Connection

# Read: select por id
def select_metodo_pago(id):
    query="SELECT * FROM metodo_pago WHERE id_metodo_pago="+id
    Connection.mycursor.execute(query)
    reg=Connection.mycursor.fetchall()
    print(reg)

# Create: insert metodo_pago
def insert_metodo_pago(metodo_pago_descripcion):
    query="INSERT INTO metodo_pago (descripcion_metodo_pago) VALUES (%s)"
    reg=(metodo_pago_descripcion,)
    Connection.mycursor.execute(query,reg)
    Connection.mydb.commit()

# Delete: delete metodo_pago
def delete_metodo_pago(id):
    query="DELETE FROM metodo_pago WHERE id_metodo_pago="+id
    Connection.mycursor.execute(query)
    Connection.mydb.commit()

# Update: update metodo_pago
def update_metodo_pago(new_value,id):
    query="UPDATE metodo_pago SET descripcion_metodo_pago='{}' WHERE id_metodo_pago='{}'"\
        .format(new_value,id)
    Connection.mycursor.execute(query)
    Connection.mydb.commit()
