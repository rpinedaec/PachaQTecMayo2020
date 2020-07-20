-- CRUD
-- create
insert into clientes (nombreCliente, nroIdentidicacionCliente,direccionCliente) 
    values('martin perez','012345678','Lima');

select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes;

select idCliente, nombreCliente as Nombre, nroIdentidicacionCliente as ID, direccionCliente as Direccion from clientes
    where nroIdentidicacionCliente = '012345678';

update clientes set
    nombreCliente = 'perez martin',
    nroIdentidicacionCliente = '012345999',
    direccionCliente = 'Comas'
    where idCliente = 1;


delete from clientes
    where idCliente = 1;


