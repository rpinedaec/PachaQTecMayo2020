--INSERT
insert into salon (nombreSalon,añoescolarSalon,idAlumno,idProfesor) values("Salon 1",2,1,1);

--SELECT
select * from salon where idAlumno=1;

--UPDATE
update salon set añoescolarSalon = 3 where idSalon = 2;

--DELETE
delete from salon where idSalon = 1;