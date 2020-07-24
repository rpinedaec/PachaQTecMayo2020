-- CRUD
-- create
insert into clientes (nombreCliente, nroIdentificacionCliente,direccionCliente) values('Roberto Pineda','001575294','Lima');
select idCliente, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;
select idCliente, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes where nroIdentificacionCliente = '001575294';
update clientes set nombreCliente = 'David Lopez', nroIdentificacionCliente = '001575293',direccionCliente = 'Santa Beatriz' where idCliente = 1;
delete from clientes where idCliente = 1 ;