
CREATE SCHEMA IF NOT EXISTS bporras

CREATE TABLE IF NOT EXISTS alumno (
  idalumno serial NOT NULL,
  nombresAlumno VARCHAR(60) NOT NULL,
  apellidosAlumno VARCHAR(60) NOT NULL,
  fechaNacimientoAlumno DATE NOT NULL,
  edadAlumno INT NOT NULL,
  correoAlumno VARCHAR(45) NOT NULL,
  PRIMARY KEY (idalumno))


CREATE TABLE IF NOT EXISTS profesor (
  idprofesor serial NOT NULL,
  nombresProfesor VARCHAR(45) NOT NULL,
  apellidosProfesor VARCHAR(60) NOT NULL,
  fechaNacimientoProfesor DATE NOT NULL,
  edadProfesor INT NOT NULL,
  correoProfesor VARCHAR(45) NOT NULL,
  PRIMARY KEY (idprofesor))


CREATE TABLE IF NOT EXISTS semestre (
  idsemestre serial NOT NULL,
  descSemestre VARCHAR(45) NOT NULL,
  PRIMARY KEY (idsemestre))


CREATE TABLE IF NOT EXISTS salon (
  idsalon serial NOT NULL,
  nombreSalon VARCHAR(45) NOT NULL,
  idalumno INT NOT NULL,
  idprofesor INT NOT NULL,
  PRIMARY KEY (idsalon),
  CONSTRAINT fk_salon_alumno1
    FOREIGN KEY (idalumno)
    REFERENCES alumno (idalumno)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_salon_profesor1
    FOREIGN KEY (idprofesor)
    REFERENCES profesor (idprofesor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)


CREATE TABLE IF NOT EXISTS curso (
  idcurso serial NOT NULL,
  nombreCurso VARCHAR(45) NOT NULL,
  idprofesor INT NOT NULL,
  idsemestre INT NOT NULL,
  PRIMARY KEY (idcurso),
  CONSTRAINT fk_curso_profesor
    FOREIGN KEY (idprofesor)
    REFERENCES profesor (idprofesor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_curso_semestre1
    FOREIGN KEY (idsemestre)
    REFERENCES semestre (idsemestre)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)


CREATE TABLE IF NOT EXISTS notas (
  idnotas serial NOT NULL,
  idalumno INT NOT NULL,
  idcurso INT NOT NULL,
  descNota VARCHAR(45) NOT NULL,
  PRIMARY KEY (idnotas),
  CONSTRAINT fk_notas_alumno1
    FOREIGN KEY (idalumno)
    REFERENCES alumno (idalumno)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_notas_curso1
    FOREIGN KEY (idcurso)
    REFERENCES curso (idcurso)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)

