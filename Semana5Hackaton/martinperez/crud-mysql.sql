use martinperez;
select idalumno,nombre,edad,correo from alumno;

insert into alumno(nombre,edad,correo)
select 'martin' nombre,30 edad,'martin.perez@pachaqtec.edu.pe' correo;

insert into alumno(nombre,edad,correo)
select 'martin' nombre,30 edad,'martin.perez@pachaqtec.edu.pe' correo union all
select 'juan',31,'juan@pachaqtec.edu.pe' union all
select 'andres',21,'andres@pachaqtec.edu.pe' union all
select 'fidel',47,'fidel@pachaqtec.edu.pe' union all
select 'andrea',42,'andrea@pachaqtec.edu.pe' union all
select 'luis',33,'luis@pachaqtec.edu.pe' union all
select 'pedro',27,'pedro@pachaqtec.edu.pe' union all
select 'luis',26,'luis@pachaqtec.edu.pe' union all
select 'juana',45,'juana@pachaqtec.edu.pe' union all
select 'karen',40,'karen@pachaqtec.edu.pe' union all
select 'carlos',32,'carlos@pachaqtec.edu.pe' union all
select 'kalin',24,'kalin@pachaqtec.edu.pe' union all
select 'pachaq',28,'pachaq@pachaqtec.edu.pe' union all
select 'peru',32,'peru@pachaqtec.edu.pe' union all
select 'lima',38,'lima@pachaqtec.edu.pe';

update alumno
set nombre = 'administracion'
, correo='administracion@pachaqtec.edu.pe'
, edad = 27
where idalumno = 1;

delete from alumno where idalumno = 16;








select idprofesor,nombre,edad,correo from profesor;

insert into profesor (nombre,edad,correo)
select 'Richard',50,'profesor_richard@pachaqtec.edu.pe' union all
select 'Juan',46,'profesor_juan@pachaqtec.edu.pe' union all
select 'Pablo',39,'profesor_pablo@pachaqtec.edu.pe' union all
select 'Luis',40,'profesor_luis@pachaqtec.edu.pe' union all
select 'eliminar',30,'profesor_elim@pachaqtec.edu.pe';

update profesor
set nombre ='Javier'
,edad = 40
,correo ='profesor_javier@pachaqtec.edu.pe'
where idprofesor = 4;

delete from profesor
where idprofesor = 8;








select idsalon,nombre,idalumno,idprofesor from salon;
select s.idsalon IDSALON,s.nombre SALON
,a.nombre ALUMNO,a.edad EDAD_ALUMNO, a.correo CORREO_ALUMNO
,p.nombre PROFESOR,p.edad EDAD_PROFESOR,p.correo CORREO_PROFESOR
from salon s
inner join alumno a on s.idalumno=a.idalumno
inner join profesor p on s.idprofesor = p.idprofesor;

 
insert into salon (nombre,idalumno,idprofesor)
select salon,idalumno,idprofesor from 
(
select 
ltrim(rtrim(cast((case when p.idprofesor = 1 and a.idalumno<8 then 'SALON-1'
	   when p.idprofesor = 2 and a.idalumno<8 then 'SALON-2'
	   when p.idprofesor = 3 and a.idalumno>7 then 'SALON-3'
	   when p.idprofesor = 4 and a.idalumno>7 then 'SALON-4'
	   else '' end) as CHAR(50)))) as salon
,a.idalumno,p.idprofesor
  from alumno a 
inner join profesor p on a.idalumno=a.idalumno
) tablaTotal where salon <> '' ORDER BY 1,3,2;

update SALON
set NOMBRE = CONCAT('SALON-0',RIGHT(NOMBRE,1))
WHERE idsalon >0;

delete from SALON WHERE idsalon =9999;

 


 
select idsemestre ID,descripcion SEMESTRE from semestre;

insert into semestre (descripcion)
select 'SEMESTRE-2020-I' DESCRIPCION UNION ALL
select 'SEMESTRE-2020-II'; 

update semestre
set descripcion = concat('SEM',RIGHT(descripcion,7))
where idsemestre>0;

DELETE FROM SEMESTRE WHERE IDSEMESTRE = 4;




SELECT IDCURSO,NOMBRE,IDSEMESTRE,IDPROFESOR FROM CURSO;

INSERT INTO CURSO (NOMBRE,IDPROFESOR,IDSEMESTRE)
SELECT 'PROGRAMACION BASICA',1,1  UNION ALL
SELECT 'PROGRAMACION MEDIA',1,1  UNION ALL
SELECT 'PROGRAMACION AVANZADA',1,1  UNION ALL
SELECT 'EXCEL BASICA',2,1  UNION ALL
SELECT 'EXCEL MEDIA',2,1  UNION ALL
SELECT 'EXCEL AVANZADA',2,1  UNION ALL
SELECT 'PYTHON BASICO',3,1  UNION ALL
SELECT 'PYTHON MEDIO',3,1  UNION ALL
SELECT 'PYTHON AVANZADO',3,1  UNION ALL
SELECT 'WEB BASICA',4,1  UNION ALL
SELECT 'WEB MEDIA',4,1  UNION ALL
SELECT 'WEB AVANZADA',4,1;

UPDATE CURSO
SET NOMBRE = 'EXCEL BASICO'
WHERE IDCURSO = 4;

DELETE FROM CURSO WHERE IDCURSO = 999;




SELECT IDNOTA,DESCRIPCION NOTA,IDALUMNO,IDCURSO FROM NOTA;


INSERT NOTA (DESCRIPCION,IDALUMNO,IDCURSO)
SELECT FLOOR(11 + (RAND() * 10)) NOTA,A.IDALUMNO,C.IDCURSO
FROM ALUMNO A
INNER JOIN CURSO C ON A.IDALUMNO = A.IDALUMNO
WHERE IDCURSO IN (1,2,3,10,11,12);

INSERT NOTA (DESCRIPCION,IDALUMNO,IDCURSO)
SELECT FLOOR(11 + (RAND() * 10)) NOTA,A.IDALUMNO,C.IDCURSO
FROM ALUMNO A
INNER JOIN CURSO C ON A.IDALUMNO = A.IDALUMNO
WHERE IDCURSO IN (4,5,6,7,8,9)
AND IDALUMNO IN (1,3,5,7,8,9,11,13,15);

UPDATE NOTA
SET DESCRIPCION = 15
WHERE IDNOTA = 167;

DELETE FROM NOTA WHERE IDNOTA=999;












