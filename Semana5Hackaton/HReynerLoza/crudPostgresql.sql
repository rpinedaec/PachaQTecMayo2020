SELECT *
FROM alumnos
INSERT INTO alumnos (alumno_nombre,alumno_apellido,alumno_fecha_nacimiento,alumno_email,alumno_pension,salon_id )
VALUES('Reyner','Loza','1995-03-19','hreloza@gmail.com',200.12,1);
UPDATE alumnos
SET alumno_apellido = 'Silva'
WHERE alumno_id = 1;
DELETE FROM alumnos
WHERE alumno_id = 1;


SELECT *
FROM salones
INSERT INTO salones (profesor_id, pabellon_id)
VALUES(1, 1);
UPDATE salones
SET profesor_id = 1
    AND pabellon_id = 2
WHERE salon_id = 1;
DELETE FROM salones
WHERE profesor_id = 1
    AND pabellon_id = 2;


SELECT *
FROM pabellones
INSERT INTO pabellones (pabellon_ubicacion)
VALUES('Segunda Planta');
UPDATE pabellones
SET pabellon_ubicacion = 'Tercera Planta'
WHERE pabellon_id = 1;
DELETE FROM pabellones
WHERE pabellon_id = 1


SELECT *
FROM profesores
INSERT INTO profesores (profesor_nombre,profesor_apellido,profesor_fecha_nacimiento,profesor_email,profesor_sueldo)
VALUES('Reyner','Loza','1995-03-19','hreloza@gmail.com',1000.01);
UPDATE profesores
SET profesor_email = 'rloza@pucp.pe'
WHERE profesor_id = 1;
DELETE FROM profesores
WHERE profesor_id = 1

SELECT *
FROM alumnos_profesores
INSERT INTO alumnos_profesores(alumno_id,profesor_id)
VALUES(1,2);
UPDATE alumnos_profesores
SET alumno_id = 2 AND profesor_id = 1
WHERE alumno_id = 1 AND profesor_id = 2;
DELETE FROM alumnos_profesores
WHERE alumno_id = 2 AND profesor_id = 1

SELECT *
FROM notas 
INSERT INTO notas(nota_valor,nota_fecha,alumno_id,curso_id)
VALUES(15.20,'2020-06-15',1,2);
UPDATE notas
SET nota_valor = 20.00
WHERE nota_id = 1 ;
DELETE FROM notas
WHERE nota_id = 1;


SELECT *
FROM cursos 
INSERT INTO cursos(curso_nombre,curso_grado,profesor_id)
VALUES('Aritmetica','Primero',2);
UPDATE cursos
SET  curso_nombre = 'Algebra'
WHERE curso_id = 1 ;
DELETE FROM cursos
WHERE curso_id = 1;