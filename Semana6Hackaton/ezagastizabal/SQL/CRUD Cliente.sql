INSERT INTO cliente (nombreCliente, nroIdentificacion) values ('Edwin Zagastizabal','72854813');
SELECT * FROM cliente
UPDATE cliente SET nombreCliente = 'Edwin Alberto Zagastizabal' WHERE idCliente = 1;
DELETE FROM cliente WHERE idCliente = 1;

INSERT INTO productos (nombreProducto, valorProducto, igvProducto) values ('Cuchillos','50.49',1);
SELECT * FROM productos
UPDATE productos SET nombreProducto = 'Tenedores' WHERE idProductos = 1;
DELETE FROM productos WHERE idProductos= 1;

INSERT INTO tipopago (descTipoPago) values ('Efectivo');
SELECT * FROM tipopago
UPDATE tipopago SET descTipoPago = 'Crédito' WHERE idtipoPago = 1;
DELETE FROM tipopago WHERE idtipoPago= 1;