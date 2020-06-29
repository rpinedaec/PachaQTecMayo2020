-- MYSQL
-- TABLA SEMESTRE
INSERT INTO public."Bimestre"(des_bimestre, fecha_registro)	VALUES ('2020-I', current_date);
INSERT INTO public."Bimestre"(des_bimestre, fecha_registro)	VALUES ('2020-II', current_date);
INSERT INTO public."Bimestre"(des_bimestre, fecha_registro)	VALUES ('2020-III', current_date);
INSERT INTO public."Bimestre"(des_bimestre, fecha_registro) VALUES ('2020-IV', current_date);

-- TABLA PROFESORES
INSERT INTO "Profesores" (Nombre_Profesor, Dni_Profesor, Fecha_Nacimiento, Correo_Profesor, Fecha_Registro) 
VALUES ('Kevin Arias', '25748568', '1964/05/24', 'kevinarias@gmail.com', current_timestamp);
INSERT INTO "Profesores" (Nombre_Profesor, Dni_Profesor, Fecha_Nacimiento, Correo_Profesor, Fecha_Registro)
VALUES ('Miguel Arias', '48574257', '1978/02/17', 'miguelarias@gmail.com', current_timestamp);

-- TABLA SALON
INSERT INTO "Salon" (Nombre_Salon, Id_Bimestre, Id_Profesores, Fecha_Registro) 
VALUES ('SALON 1', 11, 1, current_timestamp);
INSERT INTO "Salon" (Nombre_Salon, Id_Bimestre, Id_Profesores, Fecha_Registro) 
VALUES ('SALON 2', 12, 2, current_timestamp);

-- TABLA CURSOS
INSERT INTO "Cursos" (Nombre_Curso, Fecha_Registro) VALUES ('Matematica', current_timestamp);
INSERT INTO "Cursos" (Nombre_Curso, Fecha_Registro) VALUES ('Lenguaje', current_timestamp);

-- TABLA DETALLE CURSOS Y PROFESORES
INSERT INTO "Detalle_curpro" (Id_Curso, Id_Profesor, Fecha_Registro) VALUES (1, 1, current_timestamp);
INSERT INTO "Detalle_curpro" (Id_Curso, Id_Profesor, Fecha_Registro) VALUES (2, 2, current_timestamp);

-- TABLA ALUMNO
INSERT INTO "Alumno" (Nombre_Alumno, Dni_Alumno, Fecha_Nacimiento, Correo_Alumno, Fecha_Registro) 
VALUES ('Bryan Arias Canchihuaman', '87541236', '1998/02/25', 'bryanarias@gmail.com', current_timestamp);
INSERT INTO "Alumno" (Nombre_Alumno, Dni_Alumno, Fecha_Nacimiento, Correo_Alumno, Fecha_Registro) 
VALUES ('Javier Arce Arenas', '45751548', '1999/07/18', 'javierarenas@gmail.com', current_timestamp);
INSERT INTO "Alumno" (Nombre_Alumno, Dni_Alumno, Fecha_Nacimiento, Correo_Alumno, Fecha_Registro) 
VALUES ('Leydi Camarena Valdez', '48751235', '1997/10/11', 'Leydivaldez@gmail.com', current_timestamp);
INSERT INTO "Alumno" (Nombre_Alumno, Dni_Alumno, Fecha_Nacimiento, Correo_Alumno, Fecha_Registro) 
VALUES ('Mirian Cordova Alania', '75412570', '1997/01/14', 'mirianalania@gmail.com', current_timestamp);
INSERT INTO "Alumno" (Nombre_Alumno, Dni_Alumno, Fecha_Nacimiento, Correo_Alumno, Fecha_Registro) 
VALUES ('Miguel Vargas Sanchez', '74515247', '1999/07/20', 'miguelsanchez@gmail.com', current_timestamp);

--TABLA DETALLE ALUMNO Y SALON (NOTAS)
INSERT INTO "Detalle_alusal" (Id_Alumno, Id_Salon, Nota, Fecha_Registro) VALUES (1, 3, 18,current_timestamp);
INSERT INTO "Detalle_alusal" (Id_Alumno, Id_Salon, Nota, Fecha_Registro) VALUES (2, 3, 15,current_timestamp);
INSERT INTO "Detalle_alusal" (Id_Alumno, Id_Salon, Nota, Fecha_Registro) VALUES (3, 2, 12,current_timestamp);
INSERT INTO "Detalle_alusal" (Id_Alumno, Id_Salon, Nota, Fecha_Registro) VALUES (4, 3, 19,current_timestamp);
INSERT INTO "Detalle_alusal" (Id_Alumno, Id_Salon, Nota, Fecha_Registro) VALUES (5, 2, 14,current_timestamp);

