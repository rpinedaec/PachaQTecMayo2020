select * from alumno;
select * from apoderado;
insert into apoderado (nom_apoderado,correo_apoderado,telefono_apoderado) values('Juan','juan@gmail.com',999933101);
insert into alumno (nom_alumno,cod_alumno,edad_alumno,correo_alumno,direccion_alumno,apoderado_idapoderado) values('Mario',1334,15,'mario@gmail.com','Av. Brasil,1023,Jesus Maria',2);
update alumno set nom_alumno = 'Jimena', cod_alumno = 3335, edad_alumno = 17, correo_alumno = 'jimena@gmail.com', direccion_alumno = 'Av. Profecia,666,averno' where idalumno = 1;
delete from alumno where idalumno = 1;
