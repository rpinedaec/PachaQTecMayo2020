--CRUD tabla alumno
-- crear tabla 	alumno
  CREATE TABLE IF NOT EXISTS alumno(
  idalumno serial,
  nombreAlumno VARCHAR(45) NOT NULL,
  edadAlumno VARCHAR(45) NOT NULL,
  correoAlumno VARCHAR(45) NOT NULL,
  PRIMARY KEY (idalumno))



--insertar datos en la tabla
insert into alumno(nombrealumno, edadalumno,correoalumno) 
	values ('Sebastian', 20, 'sebas@hotmail.com'),
			('lucia', 17, 'lucia@hotmail.com');
	
  		
--leer datos de la tabla
select * from alumno

--actualizar datos de tabla 
UPDATE alumno SET nombrealumno = 'lucia camila' 
	WHERE nombrealumno = 'lucia';

--eliminar datos de tabla
DELETE FROM alumno WHERE nombrealumno = 'lucia camila';
-- mas de un registro
DELETE FROM alumno WHERE nombrealumno in ('lucia','Sebastian')

