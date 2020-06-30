--INSERT
insert into alumno (nombreAlumno,edadAlumno,correoAlumno) values("Bruce Porras","16","bruce@gmail.com");

-- UPDATE
update alumno set edadAlumno = "20" where idAlumno = 1;

-- SELECT
select * from alumno where nombreAlumno = "Bruce Porras";

--DELETE 

delete from alumno where idAlumno = 1;
