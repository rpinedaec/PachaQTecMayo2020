-- crud
-- crear cliente
insert into clientes (nombreCliente, nroIdentificacionCliente, direccionCliente) values('Ricardo Cornejo', '46247351', 'Lima');
select idcliente, nombreCliente as Nombre, nroIclientesclientesdentificacionCliente as ID, direccionCliente as Direccion from clientes;
select idcliente, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes where nroIdentificacionCliente = '46247351';
update clientes set nombreCliente = 'Juan Perez', nroIdentificacionCliente = '12345678', direccionCliente = 'San Borja' where idcliente = 1;
delete from clientes where idcliente ORDER BY 'root' LIMIT 20



