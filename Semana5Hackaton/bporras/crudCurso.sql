--INSERT
insert into curso (nombreCurso,idProfesor,idSalon,idSemestre) values("Programacion II",1,1,1);

--SELECT
select * from curso where idProfesor=1;

--UPDATE
update curso set idProfesor = 2 where nombreCurso = "Programacion I";

--DELETE
delete from curso where idProfesor = 2;