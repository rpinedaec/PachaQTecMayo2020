select * from Alumno;
insert into Alumno (nameAlumno,ageAlumno,emailAlumno) values("Jorge Quispe Guzman","29","wilianders.uni@gmail.com");
update Alumno set nameAlumno = "Jorge Quispe Guzman" where idAlumno = 1;
delete from Alumno where idAlumno = 1;

select * from Salon;
insert into Salon (nameSalon) values("BACKEND001");
update Salon set nameSalon = "BACKEND001" where idSalon = 1;
delete from Salon where idSalon = 1;

select * from Profesor;
insert into Profesor (nameProfesor,ageProfesor,emailProfesor) values("Roberto","35","rpineda@pachaqutec.com");
update Profesor set emailProfesor = "rpineda@pachaqutec.com" where idProfesor = 1;
delete from Profesor where idProfesor = 1;

select * from Curso;
insert into Curso (nameCurso) values("BACK-END MAYO 2020-1");
update Curso set nameCurso = "BACK-END MAYO 2020-1" where idCurso = 1;
delete from Curso where idCurso = 1;

select * from Notas;
insert into Notas (descNotas) values("16");
update Notas set descNotas = "16" where idNotas = 1;
delete from Notas where idNotas = 1;

select * from Semestre;
insert into Semestre (descSemestre) values("1erSemestre2020");
update Semestre set descSemestre = "1erSemestre2020" where idSemestre = 1;
delete from Semestre where idSemestre = 1;
