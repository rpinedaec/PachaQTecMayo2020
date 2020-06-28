select * from profesor;
insert into profesor (nom_profesor,cod_profesor,edad_profesor,correo_profesor) values('Pepe',1234,45,'pepe@gmail.com');
update profesor set nom_profesor = 'Maria', cod_profesor = 1235, edad_profesor = 30, correo_profesor = 'maria@gmail.com' where idprofesor = 1;
delete from profesor where idprofesor = 1;