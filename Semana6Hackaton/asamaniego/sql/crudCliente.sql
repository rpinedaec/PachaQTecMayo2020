-- CRUD
-- create
insert into clientes (nombreCliente, nroIdentidicacionCliente,direccionCliente) values('Roberto Pineda','001575294','Lima');
select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;
select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes where nroIdentidicacionCliente = '001575294';
update clientes set nombreCliente = 'David Lopez', nroIdentidicacionCliente = '001575293',direccionCliente = 'Santa Beatriz' where idCliente = 1;
delete from clientes where idCliente = 1 ;