-- Consulta ingresando cada atributo de la Tabla
SELECT idprofesor, nombresprofesor, edadprofesor, correoprofesor
	FROM emadrid.profesor;

-- Select con comodin * para seleccionar todos los campos
SELECT * FROM emadrid.profesor;

--Insert --
INSERT INTO emadrid.profesor(
	nombresprofesor, edadprofesor, correoprofesor)
	VALUES ('Luis Rojas','38', 'lrojas@uni.com');

--Update --
UPDATE emadrid.profesor
	SET nombresprofesor='Pedro Martinez', edadprofesor='39', correoprofesor='pmartinez@uni.com'
	WHERE idprofesor=1;

-- Delete --
DELETE FROM emadrid.profesor
	WHERE idprofesor=1;