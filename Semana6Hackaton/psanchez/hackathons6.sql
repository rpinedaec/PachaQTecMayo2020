-- ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'pachaqtec'
-- flush privileges;faccabeceraclientes
insert into clientes (nombrecliente, nroidentificacioncliente, direccioncliente) values ('Manuel Ramos','1010002','San Borja');
insert into empresa (idempresa, rucempresa, nombreempresa) values ('1','20508891178','El Negocio SA');
insert into empresa (idempresa, rucempresa, nombreempresa) values ('2','20607889451','PYME SAC');
insert into productos (idproductos, nombreproducto, valorproducto, igvproducto) values ('101','Escritorio','175.00','31.50');
insert into productos (idproductos, nombreproducto, valorproducto, igvproducto) values ('102','Alcohol en Gel','5.00','0.90');
insert into productos (idproductos, nombreproducto, valorproducto, igvproducto) values ('103','Lapicero','2.50','0');
insert into productos (idproductos, nombreproducto, valorproducto, igvproducto) values ('201','paq x100 Hojas Bond','27.50','4.95');
insert into productos (idproductos, nombreproducto, valorproducto, igvproducto) values ('301','Borrador','0.70','0');
insert into productos (idproductos, nombreproducto, valorproducto, igvproducto) values ('401','Silla','72.00','12.96');
insert into tipodepago (idtipodepago, desctipopago) values ('1001','Transferencia');
insert into tipodepago (idtipodepago, desctipopago) values ('1002','Efectivo');
insert into tipodepago (idtipodepago, desctipopago) values ('1003','Credito');
insert into facdetalle (idfacdetalle, idfaccabecera, idproducto, cantfacdetalle, valorfacdetalle) values ('1','001','103','1','2.50');
select * from facdetalle;
select idclientes, nombrecliente as Nombre, nroIdentidicacioncliente as ID, direccioncliente as Direccion from clientes;
SELECT idclientes, nroidentificacioncliente, nombrecliente, direccioncliente from clientes where nroidentificacioncliente = '1010001';
update clientes set nombrecliente = 'Roberto', nroidentificacioncliente = '70040071',direccioncliente = 'Lince' where idclientes = "1";