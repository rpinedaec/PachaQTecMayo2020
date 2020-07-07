SELECT * FROM alumno;
INSERT INTO alumno (nombreAlumno,edad,correoAlumno,idCreo,fechaCreo) VALUES ('Pepe Lucas',30,'pepe@hotmail.com',1000,now());
UPDATE alumno SET nombreAlumno = 'Lucas Perez', edad = 29, correoAlumno = 'lucas@yahoo.com', idModifico = 2000, fechaModifico = now() WHERE idAlumno = 1;
DELETE FROM alumno WHERE idAlumno = 1;