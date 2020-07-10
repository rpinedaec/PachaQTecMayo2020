select * from cliente
insert into cliente (dniCliente,nombreCliente,apellidoCliente,correoCliente) values ('71206364','Bruce','Porras','bruce.porras@corre.com')
update cliente set correoCliente = 'bruce.porras@correo.com' where idCliente=1
delete from cliente where idCliente = 1 