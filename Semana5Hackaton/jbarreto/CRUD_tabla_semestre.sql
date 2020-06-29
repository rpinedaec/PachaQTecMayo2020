--CRUD tabla semestre

--insertar datos en la tabla semestre
insert into semestre(descsemestre) values('semestre1')

--leer datos de la tabla semestre
select * from semestre

--actualizar datos de tabla semestre
UPDATE semestre SET descsemestre = 'semestre II' 
	WHERE descsemestre= 'semestre1';


--eliminar datos de tabla semestre
DELETE FROM semestre WHERE descsemestre = 'semestre II';