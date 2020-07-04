select * from curso;
insert into curso (nombreCurso, idProfesor, idsemestre) values("matematicas",1,1);
update curso set nombreCurso = "Literatura" where idcurso = 1;
delete from curso where idcurso = 1;