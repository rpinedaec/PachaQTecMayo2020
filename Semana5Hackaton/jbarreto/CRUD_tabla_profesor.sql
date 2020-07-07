--CRUD tabla profesor

--insertar datos en la tabla profesor
insert into profesor(nombreprofesor, edadprofesor, correoprofesor)
	values ('Ernesto',40,'ernerto1@gmail.com'),
			('Mariana',30,'mariana@gmail.com')

--leer datos de la tabla profesor
select * from profesor

--actualizar datos de tabla profesor
UPDATE profesor SET nombreprofesor = 'Ernesto Padilla' 
	WHERE nombreprofesor= 'Ernesto';


--eliminar datos de tabla
DELETE FROM profesor WHERE nombreprofesor = 'Ernesto Padilla';

