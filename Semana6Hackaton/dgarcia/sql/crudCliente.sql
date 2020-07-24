-- CRUD
-- create
insert into cliente (nombreCliente, nroIdentCliente, direccionCliente) values('Denisse Garcia','71756110','Lima');
select idcliente, nombreCliente as Nombre, nroIdentCliente as ID, direccionCliente as Direccion, created_at as creado, updated_at as actualizado from cliente;
select idcliente, nombreCliente as Nombre, nroIdentCliente as ID, direccionCliente as Direccion, created_at as creado, updated_at as actualizado from cliente where nroIdentCliente = '71756110';
update cliente set nombreCliente = 'David Lopez', nroIdentCliente = '001575293', direccionCliente = 'Santa Beatriz' where idcliente = 1;
delete from cliente where idcliente = 1 ;