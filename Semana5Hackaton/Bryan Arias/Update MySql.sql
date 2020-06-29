--MYSQL
--MODIFICACION TABLA BIMESTRE
UPDATE registro.Bimestre SET Des_Bimestre = 'PRIMERBIMESTRE', Fecha_modificacion = sysdate() 
WHERE IdBimestre = 1;
UPDATE registro.Bimestre SET Des_Bimestre = 'SEGUNDO BIMESTRE', Fecha_modificacion = sysdate() 
WHERE IdBimestre = 2;
UPDATE registro.Bimestre SET Des_Bimestre = 'TERCER BIMESTRE', Fecha_modificacion = sysdate() 
WHERE IdBimestre = 3;
UPDATE registro.Bimestre SET Des_Bimestre = 'CUARTO BIMESTRE', Fecha_modificacion = sysdate() 
WHERE IdBimestre = 4;

-- MODIFICACION TABLA PROFESORES
UPDATE registro.Profesores SET Nombre_Profesor = 'Elias Cordova', Dni_Profesor = '20548578', 
Correo_Profesor = 'eliascordova@hotmail.com', Fecha_Modificacion = sysdate() WHERE IdProfesores = 1;
UPDATE registro.Profesores SET Nombre_Profesor = 'Luciana Alania', Dni_Profesor = '20142589', 
Correo_Profesor = 'lucialani@hotmail.com', Fecha_Modificacion = sysdate() WHERE IdProfesores = 2;

--MODIFICANDO TABLA SALON
UPDATE registro.Salon SET Nombre_Salon = 'SALON A', Bimestre_IdBimestre = 2, Profesores_IdProfesores = 2, Fecha_Modificacion = sysdate()
WHERE IdSalon = 1;
UPDATE registro.Salon SET Nombre_Salon = 'SALON C', Bimestre_IdBimestre = 4, Profesores_IdProfesores = 1, Fecha_Modificacion = sysdate()
WHERE IdSalon = 2;

--MODIFICACION TABLA CURSOS
UPDATE registro.Cursos SET Nombre_Curso = 'Geometria', Fecha_Modificacion = sysdate() WHERE IdCursos = 1;
UPDATE registro.Cursos SET Nombre_Curso = 'Comunicacion', Fecha_Modificacion = sysdate() WHERE IdCursos = 2;

--MODIFICACION TABLA DETALLE CURSO Y PROFESORES
UPDATE registro.cursos_has_profesores SET Cursos_IdCursos = 2, Profesores_IdProfesores = 2, Fecha_Modificacion = sysdate()
WHERE IdDetalle = 1;
UPDATE registro.cursos_has_profesores SET Cursos_IdCursos = 1, Profesores_IdProfesores = 1, Fecha_Modificacion = sysdate()
WHERE IdDetalle = 2;

--MODIFICACION TABLA ALUMNO
UPDATE registro.Alumno SET Correo_Alumno = 'leydivaldez@hotmail.com', Fecha_Modificacion = sysdate() WHERE IdAlumno = 3;
UPDATE registro.Alumno SET Dni_Alumno = '87654321', Fecha_Modificacion = sysdate() WHERE IdAlumno = 1;
UPDATE registro.Alumno SET Fecha_Nacimiento = '1996/04/10', Fecha_Modificacion = sysdate() WHERE IdAlumno = 5;

--MODIFICAR TABLA DETALLE ALUMNO SALON (NOTAS)
UPDATE registro.alumno_has_salon SET Salon_IdSalon = 1, Nota = 15, Fecha_Modificacion = sysdate() WHERE IdDetalle = 3;
UPDATE registro.alumno_has_salon SET Salon_IdSalon = 2, Fecha_Modificacion = sysdate() WHERE IdDetalle = 1;
UPDATE registro.alumno_has_salon SET Nota = 16, Fecha_Modificacion = sysdate() WHERE IdDetalle = 5;