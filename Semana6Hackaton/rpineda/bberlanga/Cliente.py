import Connection

# Read: select por DNI
def select_cliente(dni):
    query="SELECT * FROM cliente WHERE DNI_cliente="+dni
    Connection.mycursor.execute(query)
    reg=Connection.mycursor.fetchall()
    print(reg)

# Create: insert cliente
def insert_cliente(DNI_cliente,nombre_cliente,correo_cliente):
    query="INSERT INTO cliente (DNI_cliente,nombre_cliente,correo_cliente) VALUES (%s,%s,%s)"
    reg=(DNI_cliente,nombre_cliente,correo_cliente)
    Connection.mycursor.execute(query,reg)
    Connection.mydb.commit()

# Delete: delete cliente
def delete_cliente(DNI):
    query="DELETE FROM cliente WHERE DNI_cliente="+DNI
    Connection.mycursor.execute(query)
    Connection.mydb.commit()

# Update: update cliente
def update_cliente(field,new_value,DNI):
    query="UPDATE cliente SET {}='{}' WHERE DNI_cliente='{}'"\
        .format(field,new_value,DNI)
    Connection.mycursor.execute(query)
    Connection.mydb.commit()


