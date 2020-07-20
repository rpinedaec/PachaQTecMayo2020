select * from salon;
insert into salon (nombreSalron, idAlumno, idProfesor) 
values("Seccion 1", "2", "2");
update salon 
set  nombreSalron = "Seccion A", idAlumno = "3",  idProfesor = "3" where idsalon = 5; 
delete from salon where idsalon = 5;