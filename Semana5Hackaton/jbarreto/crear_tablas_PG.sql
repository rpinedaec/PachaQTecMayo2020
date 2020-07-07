--crear bd jbarreto
  CREATE DATABASE jbarreto;

-- crear tabla 	ALUMNO
  CREATE TABLE IF NOT EXISTS alumno(
  idalumno serial,
  nombreAlumno VARCHAR(45) NOT NULL,
  edadAlumno VARCHAR(45) NOT NULL,
  correoAlumno VARCHAR(45) NOT NULL,
  PRIMARY KEY (idalumno))


-- CREAR TABLA PROFESOR--
  create TABLE IF NOT EXISTS profesor (
  idProfesor serial,
  nombreProfesor VARCHAR(45) NOT NULL,
  edadProfesor INT NOT NULL,
  correoProfesor VARCHAR(45) NOT NULL,
  PRIMARY KEY (idProfesor))


--CREAR TABLA SEMESTRE--
  CREATE TABLE IF NOT EXISTS semestre (
  idsemestre serial,
  descsemestre VARCHAR(45) NOT NULL,
  PRIMARY KEY (idsemestre))


--CREAR TABLA CURSO-----
CREATE TABLE IF NOT EXISTS curso (
  idcurso serial,
  nombreCurso VARCHAR(45) NOT NULL,
  idprofesor INT NOT NULL,
  idsemestre INT NOT NULL,
  PRIMARY KEY (idcurso))
 
--crear clave foranea idprofesor	 
	alter table curso
	add foreign key (idprofesor) references profesor;

--crear clave foranea idsemestre	
	alter table curso
	add foreign key (idsemestre) references semestre;

-- 	crear indice idprofesor
	create index fk_curso_profesor_idx ON profesor(idprofesor)

-- crear indice idsemestre
    create INDEX fk_curso_semestre1_idx ON curso(idsemestre)

-- crear constraint(restricci�n) fk_curso_profesor
    alter table curso
    add CONSTRAINT fk_curso_profesor
    FOREIGN KEY (idprofesor)
    REFERENCES profesor (idprofesor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION

-- crear constraint(restricci�n) fk_curso_semestre1
    alter table curso
	add	CONSTRAINT fk_curso_semestre1
    FOREIGN KEY (idsemestre)
    REFERENCES semestre (idsemestre)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION


--CREAR TABLA SALON---
CREATE TABLE IF NOT EXISTS salon(
  idsalon serial,
  nombreSalon VARCHAR(45) NOT NULL,
  idprofesor INT NOT NULL,
  idalumno INT NOT NULL,
  PRIMARY KEY (idsalon, idalumno))
  
-- crear clave foranea idprofesor
  alter table salon
  add foreign key (idprofesor) references profesor;
  
-- crear clave foranea idalumno 
  alter table salon
  add foreign key (idalumno) references alumno;

-- crear indice idprofesor
  create INDEX fk_salon_profesor1_idx ON profesor(idprofesor)
  
-- crear indice idalumno
  create INDEX fk_salon_alumno1_idx ON alumno(idalumno)

-- crear constraint(restricci�n) fk_curso_profesor1
   alter table salon
   add CONSTRAINT fk_salon_profesor1
   FOREIGN KEY (idprofesor)
   REFERENCES profesor (idprofesor)
   ON DELETE NO ACTION
   ON UPDATE NO ACTION
    
-- crear constraint(restricci�n) fk_salon_alumno1   
   alter table salon
   add CONSTRAINT fk_salon_alumno1
   FOREIGN KEY (idalumno)
   REFERENCES alumno (idalumno)
   ON DELETE NO ACTION
   ON UPDATE NO ACTION


--CREAR TABLA NOTAS--
  CREATE TABLE IF NOT EXISTS notas (
  idnotas serial,
  descNotas VARCHAR(45) NOT NULL,
  idcurso INT NOT NULL,
  idalumno INT NOT NULL,
  PRIMARY KEY (idnotas))
	
-- crear clave foranea idcurso
  alter table notas
  add foreign key (idcurso) references curso;
	
-- crear clave foranea idalumno
  alter table notas
  add foreign key (idalumno) references alumno;

-- crear indice idcurso
  create INDEX fk_notas_curso1_idx ON curso(idcurso)
  
-- crear indice idalumno
   create INDEX fk_notas_Alumno1_idx ON alumno(idalumno)
  
-- crear constraint(restricci�n) fk_notas_curso1
   alter table notas
   add CONSTRAINT fk_notas_curso1
   FOREIGN KEY (idcurso)
   REFERENCES curso (idcurso)
   ON DELETE NO ACTION
   ON UPDATE NO ACTION
   
   
-- crear constraint(restricci�n) fk_notas_Alumno1
   alter table notas
   add CONSTRAINT fk_notas_Alumno1
   FOREIGN KEY (idalumno)
   REFERENCES alumno (idalumno)
   ON DELETE NO ACTION
   ON UPDATE NO ACTION

