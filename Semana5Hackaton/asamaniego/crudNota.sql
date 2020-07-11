SELECT * FROM nota;
INSERT INTO nota (descNota,idAlumno,idCreo,fechaCreo) VALUES ('11',2,1000,now());
UPDATE nota SET descNota = '10', idAlumno = 2, idCurso =3, idModifico = 2000, fechaModifico = now() WHERE idnota = '10';
DELETE FROM nota  WHERE idnota = 3;