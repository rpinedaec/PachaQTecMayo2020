Select * from alumno;
insert into alumno (nombreAlumno, edadAlumno, correoAlumno) values("Denisse Garcia", "24", "denisse@pachaqtec.pe");
update alumno set  nombreAlumno = 'Pepito', edadAlumno = '30',  correoAlumno = 'pepito@pachaqtec.pe' where idAlumno = 2; 
delete from alumno where idAlumno = 1;
