
CREATE TABLE IF NOT EXISTS Alumno (
  idAlumno INT(11) NOT NULL,
  nameAlumno VARCHAR(45) NOT NULL,
  ageAlumno VARCHAR(45) NOT NULL,
  emailAlumno VARCHAR(45) NOT NULL,
  PRIMARY KEY (idAlumno))

CREATE TABLE IF NOT EXISTS Salon (
  idSalon INT(11) NOT NULL,
  nameSalon VARCHAR(45) NULL DEFAULT NULL,
  Profesor_idProfesor INT(11) NOT NULL,
  Alumno_idAlumno INT(11) NOT NULL,
  PRIMARY KEY (idSalon),
  CONSTRAINT fk_Salon_Profesor
    FOREIGN KEY (Profesor_idProfesor)
    REFERENCES Profesor (idProfesor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Salon_Alumno1
    FOREIGN KEY (Alumno_idAlumno)
    REFERENCES Alumno (idAlumno)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)

CREATE TABLE IF NOT EXISTS Profesor (
  idProfesor INT(11) NOT NULL,
  nameProfesor VARCHAR(45) NOT NULL,
  ageProfesor VARCHAR(45) NOT NULL,
  emailProfesor VARCHAR(45) NOT NULL,
  PRIMARY KEY (idProfesor))

CREATE TABLE IF NOT EXISTS Curso (
  idCurso INT(11) NOT NULL,
  nameCurso VARCHAR(45) NULL DEFAULT NULL,
  Profesor_idProfesor INT(11) NOT NULL,
  Semestre_idSemestre INT(11) NOT NULL,
  PRIMARY KEY (idCurso),
  CONSTRAINT fk_Curso_Profesor1
    FOREIGN KEY (Profesor_idProfesor)
    REFERENCES Profesor (idProfesor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Curso_Semestre1
    FOREIGN KEY (Semestre_idSemestre)
    REFERENCES Semestre (idSemestre)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)

CREATE TABLE IF NOT EXISTS Notas (
  idNotas INT(11) NOT NULL,
  descNotas VARCHAR(45) NOT NULL,
  Alumno_idAlumno INT(11) NOT NULL,
  Curso_idCurso INT(11) NOT NULL,
  PRIMARY KEY (idNotas),
  CONSTRAINT fk_Notas_Alumno1
    FOREIGN KEY (Alumno_idAlumno)
    REFERENCES Alumno (idAlumno)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Notas_Curso1
    FOREIGN KEY (Curso_idCurso)
    REFERENCES Curso (idCurso)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)

CREATE TABLE IF NOT EXISTS Semestre (
  idSemestre INT(11) NOT NULL,
  descSemestre VARCHAR(45) NOT NULL,
  PRIMARY KEY (idSemestre))
