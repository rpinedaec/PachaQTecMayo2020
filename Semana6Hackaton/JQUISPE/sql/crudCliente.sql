-- CRUD
-- create
insert into clientes (nombreCliente, nroIdentificacionCliente,direccionCliente) values('Jorge Quispe','46934688','Lima');
select idClientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes;
select idClientes, nombreCliente as Nombre, nroIdentificacionCliente as ID, direccionCliente as Direccion from clientes where nroIdentidicacionCliente = '46934688';
update clientes set nombreCliente = 'Jorge Quispe', nroIdentidifacionCliente = '46934688',direccionCliente = 'Lima' where idCliente = 1;
delete from clientes where idCliente = 1 ;
