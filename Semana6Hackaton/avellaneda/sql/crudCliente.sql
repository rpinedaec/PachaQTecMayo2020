-- CRUD
-- cliente
INSERT INTO clientes (nombreCliente, numeroIdCliente, direccionCliente) VALUES ('ric', '42458831', 'Lima');
SELECT idclientes, nombreCliente AS Nombre, numeroIdCliente AS ID, direccionCliente AS Direccion FROM clientes;
SELECT idclientes, nombreCliente AS Nombre, numeroIdCliente AS ID, direccionCliente AS Direccion FROM clientes WHERE numeroIdCliente = '42458831';
UPDATE clientes SET  nombreCliente = 'Asu', numeroIdCliente = '42458831', direccionCliente = 'Ate' WHERE idclientes = 1;
DELETE FROM clientes WHERE idclientes = 1;