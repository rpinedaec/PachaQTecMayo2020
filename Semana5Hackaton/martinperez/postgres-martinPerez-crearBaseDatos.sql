CREATE DATABASE martinperez
    WITH 
    OWNER = postgres
    ENCODING = "UTF8"
    LC_COLLATE = "Spanish_Spain.1252"
    LC_CTYPE = "Spanish_Spain.1252"
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

	
CREATE TABLE IF NOT EXISTS "alumno" (
  "idalumno" SERIAL NOT NULL PRIMARY KEY,
  "nombre" VARCHAR(100) NOT NULL,
  "edad" INT NOT NULL,
  "correo" VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS "profesor" (
  "idprofesor" SERIAL NOT NULL PRIMARY KEY,
  "nombre" VARCHAR(100) NOT NULL,
  "edad" INT NOT NULL,
  "correo" VARCHAR(100) NOT NULL
  );

CREATE TABLE IF NOT EXISTS "semestre" (
  "idsemestre" SERIAL NOT NULL PRIMARY KEY,
  "descripcion" VARCHAR(100) NOT NULL
  );

CREATE TABLE IF NOT EXISTS "salon" (
  "idsalon" SERIAL NOT NULL PRIMARY KEY,
  "nombre" VARCHAR(100) NOT NULL,
  "idalumno" INT NOT NULL,
  "idprofesor" INT NOT NULL
  );
 
 ALTER TABLE salon 
 ADD CONSTRAINT salon_alumno 
 FOREIGN KEY (idalumno)
 REFERENCES alumno (idalumno) MATCH FULL;
 
 ALTER TABLE salon 
 ADD CONSTRAINT salon_profesor 
 FOREIGN KEY (idprofesor)
 REFERENCES profesor (idprofesor) MATCH FULL;
 
 
CREATE TABLE IF NOT EXISTS "curso" (
  "idcurso" SERIAL NOT NULL PRIMARY KEY,
  "nombre" VARCHAR(100) NOT NULL,
  "idsemestre" INT NOT NULL,
  "idprofesor" INT NOT NULL
  );
  
 ALTER TABLE curso 
 ADD CONSTRAINT curso_semestre
 FOREIGN KEY (idsemestre)
 REFERENCES semestre(idsemestre) MATCH FULL;
 
 ALTER TABLE curso
 ADD CONSTRAINT curso_profesor
 FOREIGN KEY (idprofesor)
 REFERENCES profesor (idprofesor) MATCH FULL;
 
 

CREATE TABLE IF NOT EXISTS "nota" (
  "idnota" SERIAL NOT NULL PRIMARY KEY,
  "descripcion" VARCHAR(100) NOT NULL,
  "idalumno" INT NOT NULL,
  "idcurso" INT NOT NULL
  );

  
 ALTER TABLE nota 
 ADD CONSTRAINT nota_alumno
 FOREIGN KEY (idalumno)
 REFERENCES alumno(idalumno) MATCH FULL;
 
 ALTER TABLE nota
 ADD CONSTRAINT nota_curso
 FOREIGN KEY (idcurso)
 REFERENCES curso (idcurso) MATCH FULL;
 
 
 
