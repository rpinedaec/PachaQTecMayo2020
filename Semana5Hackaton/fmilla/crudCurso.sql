select * from curso;
select * from profesor;
select * from bimestre;
insert into profesor (nom_profesor,cod_profesor,edad_profesor,correo_profesor) values('Lucho',1434,43,'lucho@gmail.com');
insert into bimestre (desc_bimestre) values('2020-II');
insert into curso (nom_curso,profesor_idprofesor,bimestre_idbimestre) values('Biologia',3,3);
update curso set nom_curso = 'Matematica' where idcurso = 1;
delete from curso where idcurso = 1;