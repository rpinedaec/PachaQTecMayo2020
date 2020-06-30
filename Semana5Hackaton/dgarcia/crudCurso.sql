select * from curso;
insert into curso (nombreCurso, idProfesor, idSemestre) 
values("Base de Datos", "3", "2");
update curso 
set  nombreCurso = "Python" where idCurso = 3; 
delete from curso where idCurso = 3;

