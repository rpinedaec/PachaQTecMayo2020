select * from producto
insert into producto (nombreProducto,valorProducto,igvProducto) values ('lapicero','1.0','1')
update producto set nombreProducto = 'Lapicero' where idProducto=1
delete from producto where idProducto = 1 