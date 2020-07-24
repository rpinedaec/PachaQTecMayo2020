select * from faccabecera;
insert into faccabecera (idCliente,igvFacCabecera,subtotalFacCabecera,totalFacCabecera,fechaFacCabecera,estadoFacCabecera) values ('1', '18','0','0','2020-07-06 17:54:00','0');
SELECT idFacCabecera FROM faccabecera WHERE idFacCabecera = @@Identity;
SELECT LAST_INSERT_ID();
SELECT idFacCabecera from faccabecera where fechaFacCabecera='2020-07-06 17:54:00';
update faccabecera set subtotalFacCabecera = 10, totalFacCabecera=100 where idFacCabecera=44;
