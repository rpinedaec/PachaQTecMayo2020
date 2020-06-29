select * from semestre;
insert into semestre (descSemestre) values("2020-I");
insert into semestre (descSemestre) values("2020");
update semestre set descSemestre = "2020 - verano" where idsemestre = 2;
delete from semestre where idsemestre = 2 ;

