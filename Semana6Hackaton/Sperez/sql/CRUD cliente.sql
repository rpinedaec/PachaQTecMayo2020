-- CRUD
-- create
insert into clientes (nombreCliente, nroidentificacionCliente, direccionCliente) values ('sergio perez', 45249658, 'calle nelson guia');
select nombreCliente as Cliente, nroidentificacionCliente as DNI, direccionCliente as Direccion from clientes;
update clientes set nombreCliente='leonardo tafur', nroidentificacionCliente=58982445, direccionCliente='santiago de surco' where idcliente = 1;
delete from clientes where idCliente = 1;