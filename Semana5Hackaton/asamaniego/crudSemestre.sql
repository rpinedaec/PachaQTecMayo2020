SELECT * FROM semestre;
INSERT INTO semestre (descSemestre,idCreo,fechaCreo) VALUES ('2020-1',1000,now());
UPDATE semestre SET descSemestre = '2020-2', idModifico = 2000, fechaModifico = now() WHERE idsemestre = 1;
DELETE FROM semestre WHERE idsemestre = 1;
