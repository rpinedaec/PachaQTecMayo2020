 


CREATE TABLE productos (
  idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
  nombreProducto VARCHAR(45) NOT NULL,
  valorProducto DECIMAL(18,2) NOT NULL,
  igvProducto int NOT NULL
) 


CREATE TABLE empresa (
  idempresa INTEGER PRIMARY KEY AUTOINCREMENT,
  rucEmpresa VARCHAR(45) NOT NULL,
  nombreEmpresa VARCHAR(45) NOT NULL
  )


CREATE TABLE tipoPago (
  idtipoPago INTEGER PRIMARY KEY AUTOINCREMENT,
  descTipoPago VARCHAR(45) NOT NULL
  )


CREATE TABLE clientes (
  idcliente INTEGER PRIMARY KEY AUTOINCREMENT,
  nombreCliente VARCHAR(45) NOT NULL,
  nroIdentidicacionCliente VARCHAR(45) NOT NULL,
  direccionCliente VARCHAR(200) NOT NULL
)


CREATE TABLE facCabecera (
  idfacCabecera INTEGER PRIMARY KEY AUTOINCREMENT,
  idempresa INTEGER NOT NULL,
  idcliente INTEGER NOT NULL,
  idtipoPago INTEGER NOT NULL,
  fechaFacCabecera DATE NOT NULL,
  igvFacCabecera DECIMAL(18,2) NOT NULL,
  subtotalFacCabecera DECIMAL(18,2) NOT NULL,
  totalFacCabecera DECIMAL(18,2) NOT NULL,
  estadoFactura CHAR(1) NOT NULL,
  foreign key(idempresa) references empresa(idempresa),
  foreign key(idtipoPago) references tipoPago(idtipoPago),
  foreign key(idcliente) references clientes(idcliente)
 )

 
CREATE TABLE facDetalle (
  idfacDetalle INTEGER PRIMARY KEY AUTOINCREMENT,
  idfacCabecera INTEGER NOT NULL,
  idproducto INTEGER NOT NULL,
  cantFacDetalle INTEGER NOT NULL,
  valorFacDetalle DECIMAL(18,2) NOT NULL,
  foreign key(idproducto) references productos(idproducto),
  foreign key(idfacCabecera) references facCabecera(idfacCabecera)
)






