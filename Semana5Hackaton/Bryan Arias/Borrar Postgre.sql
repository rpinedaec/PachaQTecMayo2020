--ELIMIAR O CAMBIAR DE ESTADO TABLA BIMESTRE
UPDATE "Bimestre" SET Estado = '0', Fecha_baja = current_timestamp WHERE Id_Bimestre = 11;

--ELIMINAR O CAMBIAR DE ESTADO TABLA PROFESORES
UPDATE "Profesores" SET Estado = '0', Fecha_Baja = current_timestamp WHERE Id_Profesores = 2;

--ELIMINAR O CAMBIAR DE ESTADO TABLA SALON
UPDATE "Salon" SET Estado = '0', Fecha_Baja = current_timestamp WHERE Id_Salon = 2;

--ELIMINAR O CAMBIAR DE ESTADO TABLA CURSOS
UPDATE "Cursos" SET Estado = '0', Fecha_Baja = current_timestamp WHERE Id_Cursos = 1;

--ELIMINAR O CAMBIAR DE ESTADO TABLA DETALLE DEL CURSO QUE DICTA EL PROFESOR
UPDATE "Detalle_curpro" SET Estado = '0', Fecha_baja = current_timestamp WHERE Id_Detallecurpro = 1;

--ELIMINAR O CAMBIAR DE ESTADO TABLA ALUMNO
UPDATE "Alumno" SET Estado = '0', Fecha_Baja = current_timestamp WHERE Id_Alumno = 3;

--ELIMINAR O CAMBIAR DE ESTADO TABLA
UPDATE "Detalle_alusal" SET Estado = '0', Fecha_Baja = current_timestamp WHERE Id_Detallealusal = 4;
