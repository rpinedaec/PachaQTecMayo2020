select * from profesor;
insert into profesor (nombreProfesor, edadProfesor, correoProfesor) values("Jirafales", 40, "pro_jirafales@hotmail.com");
update profesor set correoProfesor = "jirafales@gmail.com" where idprofesor = 1;
delete from profesor where idProfesor = 2 ;