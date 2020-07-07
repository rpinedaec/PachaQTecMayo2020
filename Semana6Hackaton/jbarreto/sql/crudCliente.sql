-- CRUD
-- create
insert into clientes (nombreCliente, nroIdentidicacionCliente,direccionCliente) values('july pinedo ','12345678','Lima');
select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;
select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes where nroIdentidicacionCliente = '12345678';
update clientes set nombreCliente = 'juanita', nroIdentidicacionCliente = '987654321',direccionCliente = 'jesus maria' where idCliente = 1;
delete from clientes where idCliente = 1 ;