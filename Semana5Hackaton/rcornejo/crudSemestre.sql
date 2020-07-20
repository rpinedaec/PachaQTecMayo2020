Select * from semestre;
update semestre set desSemestre = '2020-Secuencial' where idsemestre = 0;
update semestre set idsemestre = '1' where idsemestre = 0;
Select * from semestre;
delete from semestre where idsemestre = 1