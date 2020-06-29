select * from bimestre;
insert into bimestre (desc_bimestre) values('2020-I');
update bimestre set desc_bimestre = '2020-SecuenciaI' where idbimestre = 1;
delete from bimestre where idbimestre = 1;