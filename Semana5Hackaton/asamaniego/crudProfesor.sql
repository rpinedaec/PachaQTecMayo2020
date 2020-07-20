SELECT * FROM profesor;
INSERT INTO profesor (nombreProfesor,edadProfesor,correoProfesor,idCreo,fechaCreo) VALUES ('Roberto Pineda',36,'rpinedo@hotmail.com',1000,now());
UPDATE profesor SET nombreProfesor = 'Carlos Pinedo', edadProfesor = 37, correoProfesor = 'rpinedo@yahoo.com', idModifico = 2000, fechaModifico = now() WHERE idProfesor = 1;
DELETE FROM profesor WHERE idProfesor = 1;

