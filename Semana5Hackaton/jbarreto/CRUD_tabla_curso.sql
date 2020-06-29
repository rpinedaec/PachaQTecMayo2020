--CRUD tabla curso

/*insertar datos en la tabla curso, antes se debe insertar datos en la
tabla profesor y semestre*/
insert into curso(nombrecurso,idprofesor,idsemestre)
select 'programacion 1' as nombrecurso, idprofesor, idsemestre from profesor, semestre
	where idprofesor = profesor.idprofesor and
		  idsemestre = semestre.idsemestre
		  
--leer datos de la tabla curso
select idcurso, nombrecurso, curso.idprofesor, curso.idsemestre
	from curso inner join profesor on curso.idprofesor = profesor.idprofesor
			   inner join semestre on curso.idsemestre = semestre.idsemestre;	

--actualizar datos de tabla curso
UPDATE curso SET nombrecurso = 'Algoritmos'
	where nombrecurso = 'programacion 1'


--eliminar datos de tabla
delete from curso where nombrecurso = 'Algoritmos';