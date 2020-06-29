
-- Inner Join -- Consulta Profesor y Salon -- 
SELECT idsalon, nombresalon, nombresprofesor
FROM emadrid.salon ss inner join emadrid.alumno aa on ss.idalumno = aa.idalumno
						inner join emadrid.profesor pp on ss.idprofesor = pp.idprofesor;
-- Inner Join -- Consulta Alummo y Salon -- 	
SELECT idsalon, nombresalon, "nombresAlumno"
FROM emadrid.salon ss inner join emadrid.alumno aa on ss.idalumno = aa.idalumno
						inner join emadrid.profesor pp on ss.idprofesor = pp.idprofesor;	

-- SELECT -- 
SELECT idsalon, nombresalon, idalumno, idprofesor
	FROM emadrid.salon;

-- INSERT -- 	
INSERT INTO emadrid.salon(
	nombresalon, idalumno, idprofesor)
	VALUES ('S-401', 2, 1);

-- UPDATE -- 	
UPDATE emadrid.salon
	SET nombresalon='S-402', idalumno=3, idprofesor=2
	WHERE idsalon=1;

-- DELETE --	
DELETE FROM emadrid.salon
	WHERE idsalon=1;