--POSTGRE
--MODIFICACION TABLA BIMESTRE
UPDATE "Bimestre" SET des_bimestre = 'PRIMER BIMESTRE', Fecha_modificacion = current_timestamp WHERE Id_Bimestre = 11;
UPDATE "Bimestre" SET des_bimestre = 'SEGUNDO BIMESTRE', Fecha_modificacion = current_timestamp WHERE Id_Bimestre = 12;
UPDATE "Bimestre" SET des_bimestre = 'TERCER BIMESTRE', Fecha_modificacion = current_timestamp WHERE Id_Bimestre = 13;
UPDATE "Bimestre" SET des_bimestre = 'CUARTO BIMESTRE', Fecha_modificacion = current_timestamp WHERE Id_Bimestre = 14;

-- MODIFICACION TABLA PROFESORES
UPDATE "Profesores" SET Nombre_Profesor = 'Elias Cordova', Dni_Profesor = '20548578', 
Correo_Profesor = 'eliascordova@hotmail.com', Fecha_Modificacion = current_timestamp WHERE Id_Profesores = 1;
UPDATE "Profesores" SET Nombre_Profesor = 'Luciana Alania', Dni_Profesor = '20142589', 
Correo_Profesor = 'lucialani@hotmail.com', Fecha_Modificacion = current_timestamp WHERE Id_Profesores = 2;

--MODIFICANDO TABLA SALON
UPDATE "Salon" SET Nombre_Salon = 'SALON A', Id_Bimestre = 11, Id_Profesores = 2, Fecha_Modificacion = current_timestamp
WHERE Id_Salon = 3;
UPDATE "Salon" SET Nombre_Salon = 'SALON C', Id_Bimestre = 12, Id_Profesores = 1, Fecha_Modificacion = current_timestamp
WHERE Id_Salon = 2;

--MODIFICACION TABLA CURSOS
UPDATE "Cursos" SET Nombre_Curso = 'Geometria', Fecha_Modificacion = current_timestamp WHERE Id_Cursos = 1;
UPDATE "Cursos" SET Nombre_Curso = 'Comunicacion', Fecha_Modificacion = current_timestamp WHERE Id_Cursos = 2;

--MODIFICACION TABLA DETALLE CURSO Y PROFESORES
UPDATE "Detalle_curpro" SET Id_Curso = 2, Id_Profesor = 2, Fecha_Modificacion = current_timestamp
WHERE Id_Detallecurpro = 1;
UPDATE "Detalle_curpro" SET Id_Curso = 1, Id_Profesor = 1, Fecha_Modificacion = current_timestamp
WHERE Id_Detallecurpro = 2;

--MODIFICACION TABLA ALUMNO
UPDATE "Alumno" SET Correo_Alumno = 'leydivaldez@hotmail.com', Fecha_Modificacion = current_timestamp WHERE Id_Alumno = 3;
UPDATE "Alumno" SET Dni_Alumno = '87654321', Fecha_Modificacion = current_timestamp WHERE Id_Alumno = 1;
UPDATE "Alumno" SET Fecha_Nacimiento = '1996/04/10', Fecha_Modificacion = current_timestamp WHERE Id_Alumno = 5;

--MODIFICAR TABLA DETALLE ALUMNO SALON (NOTAS)
UPDATE "Detalle_alusal" SET Id_Salon = 3, Nota = 15, Fecha_modificacion = current_timestamp WHERE Id_Detallealusal = 3;
UPDATE "Detalle_alusal" SET Id_Salon = 2, Fecha_modificacion = current_timestamp WHERE Id_Detallealusal = 1;
UPDATE "Detalle_alusal" SET Nota = 16, Fecha_modificacion = current_timestamp WHERE Id_Detallealusal = 5;