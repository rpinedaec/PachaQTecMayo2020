--INSERT
insert into notas (descNota,idAlumno,idCurso) values("Nota primer Trimestre",2,1);

--SELECT
select * from notas where idNota = 1;

--UPDATE
update notas set idAlumno = 2 where idNota = 1;

--DELETE
delete from notas where idAlumno = 1;