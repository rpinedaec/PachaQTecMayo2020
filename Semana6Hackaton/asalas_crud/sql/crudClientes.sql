Select nomcliente as Nombre, docidentidad as NroIdentidad, direccion as Direccion from clientes;
INSERT INTO clientes(nomcliente,docidentidad,direccion) VALUES('Roberto Pineda','001575294','lima');
UPDATE clientes SET nomcliente = 'David Loopez', docidentidad = '123456', direccion = 'San Miguel' WHERE idcliente = 1;
DELETE	FROM clientes WHERE idcliente = 1;