Select * from semestre;
insert into semestre (descSemestre) values('2020-I');
update semestre set descSemestre = '2020-Secuencial' where idsemestre = 1;
delete from semestre where idsemestre = 1