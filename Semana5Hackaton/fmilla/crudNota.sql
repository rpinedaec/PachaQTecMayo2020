select * from nota;
select * from alumno;
select * from curso;
insert into alumno (nom_alumno,cod_alumno,edad_alumno,correo_alumno,direccion_alumno,apoderado_idapoderado) values('Mario',1334,15,'mario@gmail.com','Av. Brasil,1023,Jesus Maria',2);
insert into curso (nom_curso,profesor_idprofesor,bimestre_idbimestre) values('Biologia',3,3);
insert into nota (desc_nota,alumno_idalumno,curso_idcurso) values('Aprobado',2,2);
update nota set desc_nota = 'Desaprobado' where idnota = 1;
delete from nota where idnota = 1;