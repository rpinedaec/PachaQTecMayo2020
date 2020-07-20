Select * from profesor;
insert into profesor (nombreProfesor, edadProfeor, correoProfesor) 
values("Juan Perez", "50", "juan@pachaqtec.pe");
update profesor 
set  nombreProfesor = "Pablo", edadProfeor = "30",  correoProfesor = "pablo@pachaqtec.pe" where idProfesor = 1; 
delete from profesor where idProfesor = 1;