select * from notas;
insert into notas (idAlumno, idCurso, descNota) 
values(2, 4, "Aprobado");
update notas 
set  descNota = "Desaprobado" where idNotas = 3; 
delete from notas where idNotas = 3;