SELECT * FROM salon;
INSERT INTO salon (nombreSalon,idAlumno,idProfesor,idCreo,fechaCreo) VALUES ('A201',2,2,1000,now());
UPDATE salon SET nombreSalon = 'A202', idAlumno = 2, idModifico = 2000, fechaModifico = now() WHERE idsalon = 3;
DELETE FROM salon  WHERE idsalon = 3;