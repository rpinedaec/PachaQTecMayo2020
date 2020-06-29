select * from salon;
select * from profesor;
select * from alumno;
insert into profesor (nom_profesor,cod_profesor,edad_profesor,correo_profesor) values('Pepe',1234,45,'pepe@gmail.com');
insert into alumno (nom_alumno,cod_alumno,edad_alumno,correo_alumno,direccion_alumno,apoderado_idapoderado) values('Mario',1334,15,'mario@gmail.com','Av. Brasil,1023,Jesus Maria',2);
insert into salon (nom_salon,profesor_idprofesor,alumno_idalumno) values('Confraternidad',2,2);
update salon set nom_salon = 'Arte' where idsalon = 1;
delete from salon where idsalon = 1;