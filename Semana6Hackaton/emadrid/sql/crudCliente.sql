-- CRUD
-- create
insert into clientes (nombreCliente, nroIdentidicacionCliente,direccionCliente) values('Santiago Rugel','02051478','Tumbes');
select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;
select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes where nroIdentidicacionCliente = '001575294';
update clientes set nombreCliente = 'Juan Perez', nroIdentidicacionCliente = '01020507',direccionCliente = 'Lima' where idCliente = 1;
delete from clientes where idCliente = 1 ;