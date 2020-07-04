-- DETALLE DE LOS PROFESORES Y CURSOS QUE DICTAN
SELECT p.Nombre_Profesor, YEAR(CURDATE())-YEAR(p.Fecha_Nacimiento) + 
IF(DATE_FORMAT(CURDATE(),'%m-%d') > DATE_FORMAT(p.Fecha_Nacimiento,'%m-%d'), 0 , -1 ) 
AS Edad_Actual, p.Correo_Profesor, c.Nombre_Curso FROM registro.cursos_has_profesores dcp 
INNER JOIN registro.Profesores p ON p.IdProfesores = dcp.Profesores_IdProfesores
INNER JOIN registro.Cursos c ON c.IdCursos = dcp.Cursos_IdCursos;

-- DETALLE DE LOS ALUMNOS (NOTAS)
SELECT a.Nombre_Alumno, YEAR(CURDATE())-YEAR(a.Fecha_Nacimiento) + 
IF(DATE_FORMAT(CURDATE(),'%m-%d') > DATE_FORMAT(a.Fecha_Nacimiento,'%m-%d'), 0 , -1 ) 
AS Edad_Alumno, s.Nombre_Salon, b.Des_Bimestre, p.Nombre_Profesor, c.Nombre_Curso, das.Nota
FROM registro.alumno_has_salon das 
INNER JOIN registro.Alumno a on a.IdAlumno = das.Alumno_IdAlumno
INNER JOIN registro.Salon s on s.IdSalon = das.Salon_IdSalon
INNER JOIN registro.Bimestre b on b.IdBimestre = s.Bimestre_IdBimestre
INNER JOIN registro.Profesores p on p.IdProfesores = s.Profesores_IdProfesores
INNER JOIN registro.cursos_has_profesores dcp ON dcp.Profesores_IdProfesores = p.IdProfesores
INNER JOIN registro.Cursos c ON c.IdCursos = dcp.Cursos_IdCursos;