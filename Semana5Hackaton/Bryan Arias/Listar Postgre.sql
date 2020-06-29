-- DETALLE DE LOS PROFESORES Y CURSOS QUE DICTAN
SELECT p.Nombre_Profesor, DATE_PART('YEAR', AGE(p.Fecha_Nacimiento) )
AS Edad_Actual, p.Correo_Profesor, c.Nombre_Curso FROM public."Detalle_curpro" dcp 
INNER JOIN public."Profesores" p ON p.Id_Profesores = dcp.Id_Profesor
INNER JOIN public."Cursos" c ON c.Id_Cursos = dcp.Id_Curso;

-- DETALLE DE LOS ALUMNOS (NOTAS)
SELECT a.Nombre_Alumno, DATE_PART('YEAR', AGE(a.Fecha_Nacimiento)) AS Edad_Alumno, 
s.Nombre_Salon, b.Des_Bimestre, p.Nombre_Profesor, c.Nombre_Curso, das.Nota
FROM public."Detalle_alusal" das 
INNER JOIN public."Alumno" a on a.Id_Alumno = das.Id_Alumno
INNER JOIN public."Salon" s on s.Id_Salon = das.Id_Salon
INNER JOIN public."Bimestre" b on b.Id_Bimestre = s.Id_Bimestre
INNER JOIN public."Profesores" p on p.Id_Profesores = s.Id_Profesores
INNER JOIN public."Detalle_curpro" dcp ON dcp.Id_Profesor = p.Id_Profesores
INNER JOIN public."Cursos" c ON c.Id_Cursos = dcp.Id_Curso;
