select * from facdetalle
insert into facdetalle (idFacCabecera,idProducto,cantFacDetalle,valorFacDetalle) values ('1','1','10','10');
select nombreProducto, cantFacDetalle,valorFacDetalle from facdetalle t1  inner join producto t2 on t1.idProducto = t2.idProducto where idFacCabecera=32;