--CRUD tabla salon

/*insertar datos en la tabla salon, antes se debe insertar datos en la
tabla profesor y alumno*/
insert into salon(nombresalon, idprofesor, idalumno) 
select 'salon ciclo 1' AS nombresalon, idprofesor, idalumno from profesor, alumno
	where idprofesor = profesor.idprofesor and
		  idalumno = alumno.idalumno	

--leer datos de la tabla salon
select idsalon, nombresalon, salon.idprofesor, nombreprofesor, salon.idalumno, nombrealumno 
	from salon inner join profesor on salon.idprofesor = profesor.idprofesor 
			   inner join alumno on salon.idalumno = alumno.idalumno;	

--actualizar datos de tabla salon
UPDATE salon SET nombresalon = 'salon ciclo 2' 
	WHERE nombresalon = 'salon ciclo 1';


--eliminar datos de tabla
DELETE FROM salon WHERE nombresalon = 'salon ciclo 2';