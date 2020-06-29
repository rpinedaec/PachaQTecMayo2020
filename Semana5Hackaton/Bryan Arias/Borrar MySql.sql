--ELIMIAR O CAMBIAR DE ESTADO TABLA BIMESTRE
UPDATE registro.Bimestre SET Estado = '0', Fecha_baja = sysdate() WHERE IdBimestre = 1;
DELETE FROM registro.Bimestre WHERE IdBimestre = 1;

--ELIMINAR O CAMBIAR DE ESTADO TABLA PROFESORES
UPDATE registro.Profesores SET Estado = '0', Fecha_Baja = sysdate() WHERE IdProfesores = 2;
DELETE FROM registro.Profesores WHERE IdProfesores = 2;

--ELIMINAR O CAMBIAR DE ESTADO TABLA SALON
UPDATE registro.Salon SET Estado = '0', Fecha_Baja = sysdate() WHERE IdSalon = 2;
DELETE FROM registro.Salon WHERE IdSalon = 2;

--ELIMINAR O CAMBIAR DE ESTADO TABLA CURSOS
UPDATE registro.Cursos SET Estado = '0', Fecha_Baja = sysdate() WHERE IdCursos = 1;
DELETE FROM registro.Cursos WHERE IdCursos = 1;

--ELIMINAR O CAMBIAR DE ESTADO TABLA DETALLE DEL CURSO QUE DICTA EL PROFESOR
UPDATE registro.cursos_has_profesores SET Estado = '0', Fecha_Baja = sysdate() WHERE IdDetalle = 1;
DELETE FROM registro.cursos_has_profesores WHERE IdDetalle = 1;

--ELIMINAR O CAMBIAR DE ESTADO TABLA ALUMNO
UPDATE registro.Alumno SET Estado = '0', Fecha_Baja = sysdate() WHERE IdAlumno = 3;
DELETE FROM registro.Alumno WHERE IdAlumno = 3;

--ELIMINAR O CAMBIAR DE ESTADO TABLA
UPDATE registro.alumno_has_salon SET Estado = '0', Fecha_Baja = sysdate() WHERE IdDetalle = 4;
DELETE FROM registro.alumno_has_salon WHERE IdDetalle = 4;