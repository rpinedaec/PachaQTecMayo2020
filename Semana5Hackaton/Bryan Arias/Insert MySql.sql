-- MYSQL
-- TABLA SEMESTRE
INSERT INTO registro.Semestre (Des_Semestre, Fecha_Registro) VALUES ('2020-I', sysdate());
INSERT INTO registro.Semestre (Des_Semestre, Fecha_Registro) VALUES ('2020-II', sysdate());
INSERT INTO registro.Semestre (Des_Semestre, Fecha_Registro) VALUES ('2020-III', sysdate());
INSERT INTO registro.Semestre (Des_Semestre, Fecha_Registro) VALUES ('2020-IV', sysdate());

-- TABLA PROFESORES
INSERT INTO registro.Profesores (Nombre_Profesor, Dni_Profesor, Fecha_Nacimiento, Correo_Profesor, Fecha_Registro) 
VALUES ('Kevin Arias', '25748568', '1964/05/24', 'kevinarias@gmail.com', sysdate());
INSERT INTO registro.Profesores (Nombre_Profesor, Dni_Profesor, Fecha_Nacimiento, Correo_Profesor, Fecha_Registro)
VALUES ('Miguel Arias', '48574257', '1978/02/17', 'miguelarias@gmail.com', sysdate());

-- TABLA SALON
INSERT INTO registro.Salon (Nombre_Salon, Semestre_IdSemestre, Profesores_IdProfesores, Fecha_Registro) 
VALUES ('SALON 1', 1, 1, sysdate());
INSERT INTO registro.Salon (Nombre_Salon, Semestre_IdSemestre, Profesores_IdProfesores, Fecha_Registro) 
VALUES ('SALON 2', 1, 2, sysdate());

-- TABLA CURSOS
INSERT INTO registro.Cursos (Nombre_Curso, Fecha_Registro) VALUES ('Matematica', sysdate());
INSERT INTO registro.Cursos (Nombre_Curso, Fecha_Registro) VALUES ('Lenguaje', sysdate());

-- TABLA DETALLE CURSOS Y PROFESORES
INSERT INTO registro.cursos_has_profesores (Cursos_IdCursos, Profesores_IdProfesores, Fecha_Registro) 
VALUES (1, 1, sysdate());
INSERT INTO registro.cursos_has_profesores (Cursos_IdCursos, Profesores_IdProfesores, Fecha_Registro) 
VALUES (2, 2, sysdate());

-- TABLA ALUMNO
INSERT INTO registro.Alumno (Nombre_Alumno, Dni_Alumno, Fecha_Nacimiento, Correo_Alumno, Fecha_Registro) 
VALUES ('Bryan Arias Canchihuaman', '87541236', '1998/02/25', 'bryanarias@gmail.com', sysdate());
INSERT INTO registro.Alumno (Nombre_Alumno, Dni_Alumno, Fecha_Nacimiento, Correo_Alumno, Fecha_Registro) 
VALUES ('Javier Arce Arenas', '45751548', '1999/07/18', 'javierarenas@gmail.com', sysdate());
INSERT INTO registro.Alumno (Nombre_Alumno, Dni_Alumno, Fecha_Nacimiento, Correo_Alumno, Fecha_Registro) 
VALUES ('Leydi Camarena Valdez', '48751235', '1997/10/11', 'Leydivaldez@gmail.com', sysdate());
INSERT INTO registro.Alumno (Nombre_Alumno, Dni_Alumno, Fecha_Nacimiento, Correo_Alumno, Fecha_Registro) 
VALUES ('Mirian Cordova Alania', '75412570', '1997/01/14', 'mirianalania@gmail.com', sysdate());
INSERT INTO registro.Alumno (Nombre_Alumno, Dni_Alumno, Fecha_Nacimiento, Correo_Alumno, Fecha_Registro) 
VALUES ('Miguel Vargas Sanchez', '74515247', '1999/07/20', 'miguelsanchez@gmail.com', sysdate());

--TABLA DETALLE ALUMNO Y SALON (NOTAS)
INSERT INTO registro.alumno_has_salon (Alumno_IdAlumno, Salon_IdSalon, Nota, Fecha_Registro) 
VALUES (1, 1, 18,sysdate());
INSERT INTO registro.alumno_has_salon (Alumno_IdAlumno, Salon_IdSalon, Nota, Fecha_Registro) 
VALUES (2, 1, 15,sysdate());
INSERT INTO registro.alumno_has_salon (Alumno_IdAlumno, Salon_IdSalon, Nota, Fecha_Registro) 
VALUES (3, 2, 12,sysdate());
INSERT INTO registro.alumno_has_salon (Alumno_IdAlumno, Salon_IdSalon, Nota, Fecha_Registro) 
VALUES (4, 1, 19,sysdate());
INSERT INTO registro.alumno_has_salon (Alumno_IdAlumno, Salon_IdSalon, Nota, Fecha_Registro) 
VALUES (5, 2, 14,sysdate());

