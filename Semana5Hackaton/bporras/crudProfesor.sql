--INSERT
insert into profesor (nombreProfesor,edadProfesor,correoProfesor) values("Jose Rivas","50","JoseR@gmail.com");

-- UPDATE
update profesor set nombreAlumno = "Pier Caceres" where idProfesor = 1;

-- SELECT
select * from profesor where idProfesor = 2;

--DELETE 

delete from profesor where idProfesor = 1;
