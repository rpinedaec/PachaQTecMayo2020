SELECT * FROM curso;
INSERT INTO curso (nombreCurso,idProfesor,idSemestre,idCreo,fechaCreo) VALUES ('Python',1,1,1000,now());
UPDATE curso SET nombreCurso = 'Backend con Python', idSemestre = 2, idModifico = 2000, fechaModifico = now() WHERE idcurso = 1;
DELETE FROM curso WHERE idCurso = 1;