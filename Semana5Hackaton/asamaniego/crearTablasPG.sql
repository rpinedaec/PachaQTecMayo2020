CREATE TABLE IF NOT EXISTS nota (
  idnota serial,
  descNota VARCHAR(45) NOT NULL,
  idAlumno INT NOT NULL,
  idcurso INT NOT NULL,
  PRIMARY KEY (idnota),
  CONSTRAINT fk_nota_alumno1
    FOREIGN KEY (idAlumno)
    REFERENCES alumno (idAlumno)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_nota_curso1
    FOREIGN KEY (idcurso)
    REFERENCES curso (idcurso)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)




CREATE TABLE IF NOT EXISTS salon (
  idsalon serial,
  nombreSalon VARCHAR(45) NOT NULL,
  idAlumno INT NOT NULL,
  idProfesor INT NOT NULL,
  PRIMARY KEY (idsalon),
  CONSTRAINT fk_salon_alumno1
    FOREIGN KEY (idAlumno)
    REFERENCES alumno (idAlumno)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_salon_profesor1
    FOREIGN KEY (idProfesor)
    REFERENCES profesor (idProfesor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)



CREATE TABLE IF NOT EXISTS curso (
  idcurso serial,
  nombreCurso VARCHAR(45) NOT NULL,
  idProfesor INT NOT NULL,
  idsemestre INT NOT NULL,
  idCreo INT NOT NULL,
  fechaCreo TIMESTAMP NOT NULL,
  idModifico INT  NULL DEFAULT NULL,
  fechaModifico TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (idcurso),
  CONSTRAINT fk_curso_profesor
    FOREIGN KEY (idProfesor)
    REFERENCES profesor (idProfesor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_curso_semestre1
    FOREIGN KEY (idsemestre)
    REFERENCES semestre (idsemestre)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)



CREATE TABLE IF NOT EXISTS semestre (
  idsemestre serial,
  descSemestre VARCHAR(45) NOT NULL,
  idCreo INT NOT NULL,
  fechaCreo TIMESTAMP NOT NULL,
  idModifico INT  NULL DEFAULT NULL,
  fechaModifico TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (idsemestre))


CREATE TABLE IF NOT EXISTS profesor (
  idProfesor serial,
  nombreProfesor VARCHAR(45) NOT NULL,
  edadProfesor INT NOT NULL,
  correoProfesor VARCHAR(45) NOT NULL,
  idCreo INT NOT NULL,
  fechaCreo TIMESTAMP NOT NULL,
  idModifico INT  NULL DEFAULT NULL,
  fechaModifico TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (idProfesor))




CREATE TABLE IF NOT EXISTS alumno (
  idAlumno  serial,
  nombreAlumno VARCHAR(45) NOT NULL,
  edad INT NOT NULL,
  correoAlumn VARCHAR(45) NOT NULL,
  idCreo INT NOT NULL,
  fechaCreo TIMESTAMP NOT NULL,
  idModifico INT  NULL DEFAULT NULL,
  fechaModifico TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (idAlumno))