--CRUD tabla notas

/*insertar datos en la tabla notas, antes se debe insertar datos en la
tabla alumno y curso*/
insert into notas(descnotas, idcurso, idalumno)
select '12' as descnotas, idcurso, idalumno from curso, alumno
	where idcurso = curso.idcurso and
		  idalumno = 6 --alumno.idalumno 	
 
--leer datos de la tabla notas
select idnotas, descnotas, notas.idcurso, curso.nombrecurso, notas.idalumno, alumno.nombrealumno
	from notas inner join curso on notas.idcurso = curso.idcurso
			   inner join alumno on notas.idalumno = alumno.idalumno;
			   
--actualizar datos de tabla notas
UPDATE notas SET descnotas = '16' 
	where idnotas = 5
	--verificar
	select * from notas
	
	
--eliminar datos de tabla notas
delete from notas where idnotas = 3


