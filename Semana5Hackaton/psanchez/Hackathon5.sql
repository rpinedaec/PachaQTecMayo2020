	--Busquedas
    --Lista de alumnos desaprobados por curso
select * 
from alumnos
where alumnonota <11
order by alumnocurso desc
    
    
    --Ingreso de datos a la DB
    --Data de Salon
     insert into salon (salonid, salondesc) values ('11','Gimnasio');
	 insert into salon (salonid, salondesc) values ('12','Teatro');
	 insert into salon (salonid, salondesc) values ('13','Piscina');
	 insert into salon (salonid, salondesc) values ('101','Primero');
	 insert into salon (salonid, salondesc) values ('201','Segundo');
	 insert into salon (salonid, salondesc) values ('301','Tercero');
	 insert into salon (salonid, salondesc) values ('401','Cuarto');
	 insert into salon (salonid, salondesc) values ('501','Quinto');
	 insert into salon (salonid, salondesc) values ('14','Lab Ingles');
	 insert into salon (salonid, salondesc) values ('15','Lab PC'); 
    --Data de Notas
	 insert into notas (notaid, notadesc) values ('00','Desaprobado');
	 insert into notas (notaid, notadesc) values ('01','Desaprobado');
	 insert into notas (notaid, notadesc) values ('02','Desaprobado');
	 insert into notas (notaid, notadesc) values ('03','Desaprobado');
	 insert into notas (notaid, notadesc) values ('04','Desaprobado');
	 insert into notas (notaid, notadesc) values ('05','Desaprobado');
	 insert into notas (notaid, notadesc) values ('06','Desaprobado');
	 insert into notas (notaid, notadesc) values ('07','Desaprobado');
	 insert into notas (notaid, notadesc) values ('08','Desaprobado');
	 insert into notas (notaid, notadesc) values ('09','Desaprobado');
	 insert into notas (notaid, notadesc) values ('10','Desaprobado');
	 insert into notas (notaid, notadesc) values ('11','Aprobado');
	 insert into notas (notaid, notadesc) values ('12','Aprobado');
	 insert into notas (notaid, notadesc) values ('13','Aprobado');
	 insert into notas (notaid, notadesc) values ('14','Aprobado');
	 insert into notas (notaid, notadesc) values ('15','Aprobado');
	 insert into notas (notaid, notadesc) values ('16','Aprobado');
	 insert into notas (notaid, notadesc) values ('17','Aprobado');
	 insert into notas (notaid, notadesc) values ('18','Aprobado');
	 insert into notas (notaid, notadesc) values ('19','Aprobado');
	 insert into notas (notaid, notadesc) values ('20','Aprobado');
    --Data de Profesores
	insert into profesores (profesorid, profesornombre, profesoredad, profesorcorreo) values ('800001','Benito Juarez','45','benito.juarez@elcolegio.com');
	insert into profesores (profesorid, profesornombre, profesoredad, profesorcorreo) values ('800002','Mala Rodriguez','35','mala.rodriguez@elcolegio.com');
	insert into profesores (profesorid, profesornombre, profesoredad, profesorcorreo) values ('800003','Leo Dan','40','leo.dan@elcolegio.com');
	insert into profesores (profesorid, profesornombre, profesoredad, profesorcorreo) values ('800004','Carlos Cacho Juarez','54','carlos.cacho@elcolegio.com');
	insert into profesores (profesorid, profesornombre, profesoredad, profesorcorreo) values ('800005','Simon Bolivar','28','simon.bolivar@elcolegio.com');
	insert into profesores (profesorid, profesornombre, profesoredad, profesorcorreo) values ('800006','Nolberto Nolasco','38','nolberto.nolasco@elcolegio.com');
	insert into profesores (profesorid, profesornombre, profesoredad, profesorcorreo) values ('800007','Gilberto La Rosa','31','gilberto.larosa@elcolegio.com');
	--Data de Cursos
	insert into cursos (cursoid, curspdesc) values ('900','Ciencia y Ambiente');
	insert into cursos (cursoid, curspdesc) values ('901','Matematicas');
	insert into cursos (cursoid, curspdesc) values ('902','Comunicacion');
	insert into cursos (cursoid, curspdesc) values ('903','Ciencias Sociales');
	insert into cursos (cursoid, curspdesc) values ('904','Educacion Fisica');
	insert into cursos (cursoid, curspdesc) values ('905','Geografia');
	insert into cursos (cursoid, curspdesc) values ('906','Arte');
	--Data de Semestres
	insert into semestre (semid,semdesc) values ('1','M-J');
	insert into semestre (semid,semdesc) values ('2','A-D');
    --Data de Alumnos
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('1010001','Javier Cuadros','12','javier.cuadros@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('1010002','Jose Lopez','11','jose.lopez@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('1010003','Maria Zanelli','12','maria.zanelli@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('1010004','Fiorella Gomez','12','fiorella.gomez@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('1010005','Tomas Rebagliati','11','tomas.rebagliati@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('1010006','Valentina Montes','13','valentina.montes@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('1010007','Marjorie Espejos','11','marjorie.espejos@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('1010008','Belisario Ramirez','12','belisario.ramirez@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('1010009','Luis Breadt','13','luis.breadt@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('1010010','David Iten','12','david.iten@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('2010001','Javier Vega','12','javier.vega@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('2010002','Jose Bardellini','11','jose.bardellini@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('2010003','Maria Sanchez','12','maria.sanchez@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('2010004','Fiorella Apolaya','12','fiorella.apolaya@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('2010005','Tomas Huertas','11','tomas.huertas@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('2010006','Valentina Godenzi','13','valentina.godenzi@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('2010007','Marjorie Maunders','11','marjorie.maunders@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('2010008','Belisario Razetto','12','belisario.razetto@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('2010009','Luis Gonzales','13','luis.gonzales@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('2010010','David Cuzco','12','david.cuzco@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('3010001','Javier Balta','12','javier.balta@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('3010002','Jose Huarcaya','11','jose.huarcaya@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('3010003','Maria Pozas','12','maria.pozas@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('3010004','Fiorella Del Toro','12','fiorella.deltoro@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('3010005','Tomas Tusa','11','tomas.tusa@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('3010006','Valentina Ozuna','13','valentina.ozuna@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('3010007','Marjorie Maria','11','marjorie.maria@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('3010008','Belisario Mohammed','12','belisario.mohammed@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('3010009','Luis pinchi','13','luis.pinchi@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('3010010','David Huapaya','12','david.huapaya@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('4010001','Javier Leey','12','javier.leey@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('4010002','Jose Chong','11','jose.chong@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('4010003','Maria Maita','12','maria.maita@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('4010004','Fiorella Vandemeyer','12','fiorella.vandemeyer@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('4010005','Tomas Bisbal','11','tomas.bisbal@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('4010006','Valentina Maltese','13','valentina.maltese@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('4010007','Marjorie Zapata','11','marjorie.zapata@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('4010008','Belisario Cuarzo','12','belisario.cuarzo@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('4010009','Luis Benedetti','13','luis.benedetti@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('4010010','David Ramirez','12','david.ramirez@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('5010001','Javier Torreani','12','javier.torreani@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('5010002','Jose Nielsen','11','jose.nielsen@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('5010003','Maria Kahnwald','12','maria.kahnwald@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('5010004','Fiorella Woller','12','fiorella.woller@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('5010005','Tomas Kuhn','11','tomas.kuhn@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('5010006','Valentina Baeni','13','valentina.baeni@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('5010007','Marjorie Castellanos','11','marjorie.castellanos@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('5010008','Belisario Pomacaja','12','belisario.pomacaja@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('5010009','Luis Aliaga','13','luis.aliaga@elcolegio.com');
	 insert into alumnos (alumnoid, alumnonombre, alumnoedad, alumnocorreo) values ('5010010','David Castaneda','12','david.castaneda@elcolegio.com');

--Se crea la columna profesor curso con un FK
ALTER TABLE public.profesores
    ADD COLUMN profesorcurso integer;
ALTER TABLE public.profesores
    ADD CONSTRAINT profesorcurso FOREIGN KEY (profesorcurso)
    REFERENCES public.cursos (cursoid) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
CREATE INDEX fki_profesorcurso
    ON public.profesores(profesorcurso);

--Ingreso la información a la nueva columna relacionada	
	update profesores set profesorcurso = '900'
	where profesornombre = 'Benito Juarez'
	update profesores set profesorcurso = '901'
	where profesornombre = 'Mala Rodriguez'
	update profesores set profesorcurso = '902'
	where profesornombre = 'Simon Bolivar'
	update profesores set profesorcurso = '903'
	where profesornombre = 'Leo Dan'
	update profesores set profesorcurso = '904'
	where profesornombre = 'Gilberto La Rosa'
	update profesores set profesorcurso = '905'
	where profesornombre = 'Nolberto Nolasco'
	update profesores set profesorcurso = '906'
	where profesornombre = 'Carlos Cacho'

--Se relaciona el salon con el curso
ALTER TABLE public.salon
    ADD COLUMN salondelcurso integer;

ALTER TABLE public.salon
    ADD CONSTRAINT salondelcurso FOREIGN KEY (salondelcurso)
    REFERENCES public.cursos (cursoid) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
CREATE INDEX fki_salondelcurso
    ON public.salon(salondelcurso);

	update salon set salondelcurso = '904'
	where salonid = '11'
	update salon set salondelcurso = '906'
	where salonid = '12'
	update salon set salondelcurso = '904'
	where salonid = '13'
	update salon set salondelcurso = '900'
	where salonid = '101'
	update salon set salondelcurso = '902'
	where salonid = '201'
	update salon set salondelcurso = '903'
	where salonid = '301'
	update salon set salondelcurso = '905'
	where salonid = '401'
	update salon set salondelcurso = '901'
	where salonid = '501'
	update salon set salondelcurso = '902'
	where salonid = '14'
	update salon set salondelcurso = '902'
	where salonid = '15'

--Se relaciona alumno curso
ALTER TABLE public.alumnos
    ADD COLUMN alumnocurso integer;

ALTER TABLE public.alumnos
    ADD CONSTRAINT alumnocurso FOREIGN KEY (alumnocurso)
    REFERENCES public.cursos (cursoid) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
CREATE INDEX fki_alumnocurso
    ON public.alumnos(alumnocurso);

    update alumnos set alumnocurso = '900'
	where alumnoid = '1010002'
	update alumnos set alumnocurso = '901'
	where alumnoid = '1010003'
	update alumnos set alumnocurso = '902'
	where alumnoid = '1010004'
	update alumnos set alumnocurso = '903'
	where alumnoid = '1010005'
	update alumnos set alumnocurso = '904'
	where alumnoid = '1010006'
	update alumnos set alumnocurso = '905'
	where alumnoid = '1010007'
	update alumnos set alumnocurso = '906'
	where alumnoid = '1010008'
	update alumnos set alumnocurso = '900'
	where alumnoid = '1010009'
	update alumnos set alumnocurso = '901'
	where alumnoid = '1010010'
	update alumnos set alumnocurso = '902'
	where alumnoid = '2010001'
	update alumnos set alumnocurso = '903'
	where alumnoid = '2010002'
	update alumnos set alumnocurso = '904'
	where alumnoid = '2010003'
	update alumnos set alumnocurso = '905'
	where alumnoid = '2010004'
	update alumnos set alumnocurso = '906'
	where alumnoid = '2010005'
	update alumnos set alumnocurso = '900'
	where alumnoid = '2010006'
	update alumnos set alumnocurso = '901'
	where alumnoid = '2010007'
	update alumnos set alumnocurso = '902'
	where alumnoid = '2010008'
	update alumnos set alumnocurso = '903'
	where alumnoid = '2010009'
	update alumnos set alumnocurso = '904'
	where alumnoid = '2010010'
    update alumnos set alumnocurso = '905'
	where alumnoid = '3010002'
	update alumnos set alumnocurso = '906'
	where alumnoid = '3010003'
	update alumnos set alumnocurso = '900'
	where alumnoid = '3010004'
	update alumnos set alumnocurso = '901'
	where alumnoid = '3010005'
	update alumnos set alumnocurso = '902'
	where alumnoid = '3010006'
	update alumnos set alumnocurso = '903'
	where alumnoid = '3010007'
	update alumnos set alumnocurso = '904'
	where alumnoid = '3010008'
	update alumnos set alumnocurso = '905'
	where alumnoid = '3010009'
	update alumnos set alumnocurso = '906'
	where alumnoid = '3010010'
	update alumnos set alumnocurso = '900'
	where alumnoid = '4010001'
	update alumnos set alumnocurso = '901'
	where alumnoid = '4010002'
	update alumnos set alumnocurso = '902'
	where alumnoid = '4010003'
	update alumnos set alumnocurso = '903'
	where alumnoid = '4010004'
	update alumnos set alumnocurso = '904'
	where alumnoid = '4010005'
	update alumnos set alumnocurso = '905'
	where alumnoid = '4010006'
	update alumnos set alumnocurso = '906'
	where alumnoid = '4010007'
	update alumnos set alumnocurso = '900'
	where alumnoid = '4010008'
	update alumnos set alumnocurso = '901'
	where alumnoid = '4010009'
	update alumnos set alumnocurso = '902'
	where alumnoid = '4010010'
    update alumnos set alumnocurso = '903'
	where alumnoid = '5010001'
	update alumnos set alumnocurso = '904'
	where alumnoid = '5010003'
	update alumnos set alumnocurso = '905'
	where alumnoid = '5010004'
	update alumnos set alumnocurso = '906'
	where alumnoid = '5010005'
	update alumnos set alumnocurso = '900'
	where alumnoid = '5010006'
	update alumnos set alumnocurso = '901'
	where alumnoid = '5010007'
	update alumnos set alumnocurso = '902'
	where alumnoid = '5010008'
	update alumnos set alumnocurso = '903'
	where alumnoid = '5010009'
	update alumnos set alumnocurso = '904'
	where alumnoid = '5010010'
    update alumnos set alumnocurso = '905'
	where alumnoid = '3010001'
	update alumnos set alumnocurso = '906'
	where alumnoid = '5010002'

--Relacion alumno nota
ALTER TABLE public.alumnos
    ADD COLUMN alumnonota integer;

ALTER TABLE public.alumnos
    ADD CONSTRAINT alumnonota FOREIGN KEY (alumnonota)
    REFERENCES public.notas (notaid) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
CREATE INDEX fki_alumnonota
    ON public.alumnos(alumnonota);

    update alumnos set alumnonota = '20'
	where alumnoid = '1010002'
	update alumnos set alumnonota = '05'
	where alumnoid = '1010003'
	update alumnos set alumnonota = '19'
	where alumnoid = '1010004'
	update alumnos set alumnonota = '01'
	where alumnoid = '1010005'
	update alumnos set alumnonota = '18'
	where alumnoid = '1010006'
	update alumnos set alumnonota = '02'
	where alumnoid = '1010007'
	update alumnos set alumnonota = '03'
	where alumnoid = '1010008'
	update alumnos set alumnonota = '17'
	where alumnoid = '1010009'
	update alumnos set alumnonota = '16'
	where alumnoid = '1010010'
	update alumnos set alumnonota = '15'
	where alumnoid = '2010001'
	update alumnos set alumnonota = '14'
	where alumnoid = '2010002'
	update alumnos set alumnonota = '11'
	where alumnoid = '2010003'
	update alumnos set alumnonota = '11'
	where alumnoid = '2010004'
	update alumnos set alumnonota = '14'
	where alumnoid = '2010005'
	update alumnos set alumnonota = '18'
	where alumnoid = '2010006'
	update alumnos set alumnonota = '07'
	where alumnoid = '2010007'
	update alumnos set alumnonota = '09'
	where alumnoid = '2010008'
	update alumnos set alumnonota = '01'
	where alumnoid = '2010009'
	update alumnos set alumnonota = '16'
	where alumnoid = '2010010'
    update alumnos set alumnonota = '15'
	where alumnoid = '3010002'
	update alumnos set alumnonota = '15'
	where alumnoid = '3010003'
	update alumnos set alumnonota = '17'
	where alumnoid = '3010004'
	update alumnos set alumnonota = '18'
	where alumnoid = '3010005'
	update alumnos set alumnonota = '20'
	where alumnoid = '3010006'
	update alumnos set alumnonota = '11'
	where alumnoid = '3010007'
	update alumnos set alumnonota = '11'
	where alumnoid = '3010008'
	update alumnos set alumnonota = '13'
	where alumnoid = '3010009'
	update alumnos set alumnonota = '08'
	where alumnoid = '3010010'
	update alumnos set alumnonota = '06'
	where alumnoid = '4010001'
	update alumnos set alumnonota = '17'
	where alumnoid = '4010002'
	update alumnos set alumnonota = '19'
	where alumnoid = '4010003'
	update alumnos set alumnonota = '04'
	where alumnoid = '4010004'
	update alumnos set alumnonota = '20'
	where alumnoid = '4010005'
	update alumnos set alumnonota = '11'
	where alumnoid = '4010006'
	update alumnos set alumnonota = '12'
	where alumnoid = '4010007'
	update alumnos set alumnonota = '13'
	where alumnoid = '4010008'
	update alumnos set alumnonota = '14'
	where alumnoid = '4010009'
	update alumnos set alumnonota = '15'
	where alumnoid = '4010010'
    update alumnos set alumnonota = '18'
	where alumnoid = '5010001'
	update alumnos set alumnonota = '10'
	where alumnoid = '5010003'
	update alumnos set alumnonota = '10'
	where alumnoid = '5010004'
	update alumnos set alumnonota = '10'
	where alumnoid = '5010005'
	update alumnos set alumnonota = '15'
	where alumnoid = '5010006'
	update alumnos set alumnonota = '14'
	where alumnoid = '5010007'
	update alumnos set alumnonota = '02'
	where alumnoid = '5010008'
	update alumnos set alumnonota = '11'
	where alumnoid = '5010009'
	update alumnos set alumnonota = '12'
	where alumnoid = '5010010'
    update alumnos set alumnonota = '16'
	where alumnoid = '3010001'
	update alumnos set alumnonota = '15'
	where alumnoid = '5010002'
    update alumnos set alumnonota = '15'
	where alumnoid = '1010001'
