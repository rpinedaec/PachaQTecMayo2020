select * from apoderado;
insert into apoderado (nom_apoderado,correo_apoderado,telefono_apoderado) values('Juan','juan@gmail.com',999933101);
update apoderado set nom_apoderado = 'Maria', correo_apoderado = 'maria@gmail.com', telefono_apoderado = 932238456 where idapoderado = 1;
delete from apoderado where idapoderado = 1;