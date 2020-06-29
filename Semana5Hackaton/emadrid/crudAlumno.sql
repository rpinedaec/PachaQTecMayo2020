-- Generated: 2020-06-28
-- Model: Colegio
-- Version: 1.0
-- Project: BD Colegio
-- Author: EMADRID

-- SELECT --
SELECT idalumno, "nombresAlumno", "correoAlumno", "edadAlumno", "ultimaActualizacionAlumno"
	FROM emadrid.alumno;

-- INSERT --
INSERT INTO emadrid.alumno(
	"nombresAlumno", "correoAlumno", "edadAlumno", "ultimaActualizacionAlumno")
	VALUES ('Erin Madrid', 'emadrid@prueba.com', 32, current_time);

-- UPDATE --
UPDATE emadrid.alumno
	SET "nombresAlumno"='Juan Perez', "correoAlumno"='jperez@prueba.com', "edadAlumno"=30, "ultimaActualizacionAlumno"=now()
	WHERE idalumno=1;

-- DELETE --
DELETE FROM emadrid.alumno
	WHERE idalumno=1;