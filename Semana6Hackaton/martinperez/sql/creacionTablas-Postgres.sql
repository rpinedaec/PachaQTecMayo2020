
CREATE TABLE IF NOT EXISTS "productos" (
  "idproducto" SERIAL NOT NULL ,
  "nombreProducto" VARCHAR(45) NOT NULL,
  "valorProducto" DECIMAL(18,2) NOT NULL,
  "igvProducto" INT NOT NULL,
  PRIMARY KEY ("idproducto"))



CREATE TABLE IF NOT EXISTS "empresa" (
  "idempresa" SERIAL NOT NULL ,
  "rucEmpresa" VARCHAR(45) NOT NULL,
  "nombreEmpresa" VARCHAR(45) NOT NULL,
  PRIMARY KEY ("idempresa"))



CREATE TABLE IF NOT EXISTS "tipoPago" (
  "idtipoPago" SERIAL NOT NULL ,
  "descTipoPago" VARCHAR(45) NOT NULL,
  PRIMARY KEY ("idtipoPago"))



CREATE TABLE IF NOT EXISTS "clientes" (
  "idcliente" SERIAL NOT NULL ,
  "nombreCliente" VARCHAR(45) NOT NULL,
  "nroIdentidicacionCliente" VARCHAR(45) NOT NULL,
  "direccionCliente" VARCHAR(200) NOT NULL,
  PRIMARY KEY ("idcliente"))







  

CREATE TABLE IF NOT EXISTS "facCabecera" (
  "idfacCabecera" SERIAL NOT NULL ,
  "idempresa" INT NOT NULL,
  "idcliente" INT NOT NULL,
  "idtipoPago" INT NOT NULL,
  "fechaFacCabecera" DATE NOT NULL DEFAULT NOW(),
  "igvFacCabecera" DECIMAL(18,2) NOT NULL,
  "subtotalFacCabecera" DECIMAL(18,2) NOT NULL,
  "totalFacCabecera" DECIMAL(18,2) NOT NULL,
  "estadoFactura" CHAR(1) NOT NULL,
  PRIMARY KEY ("idfacCabecera")
)


ALTER TABLE "facCabecera"
  ADD CONSTRAINT "fk_facCabecera_empresa1"
    FOREIGN KEY ("idempresa")
    REFERENCES "empresa" ("idempresa")

ALTER TABLE "facCabecera"
  ADD CONSTRAINT "fk_facCabecera_tipoPago1"
    FOREIGN KEY ("idtipoPago")
    REFERENCES "tipoPago" ("idtipoPago")

ALTER TABLE "facCabecera"
  ADD CONSTRAINT "fk_facCabecera_clientes1"
    FOREIGN KEY ("idcliente")
    REFERENCES "clientes" ("idcliente")
	 



CREATE TABLE IF NOT EXISTS "facDetalle" (
  "idfacDetalle" SERIAL NOT NULL ,
  "idfacCabecera" INT NOT NULL,
  "idproducto" INT NOT NULL,
  "cantFacDetalle" INT NOT NULL,
  "valorFacDetalle" DECIMAL(18,2) NOT NULL,
  PRIMARY KEY ("idfacDetalle")
)

ALTER TABLE "facDetalle"
  ADD CONSTRAINT "fk_facDetalle_facCabecera"
    FOREIGN KEY ("idfacCabecera")
    REFERENCES "facCabecera" ("idfacCabecera")

ALTER TABLE "facDetalle"
  ADD CONSTRAINT "fk_facDetalle_productos1"
    FOREIGN KEY ("idproducto")
    REFERENCES "productos" ("idproducto")

	
	



