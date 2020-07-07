CREATE TABLE IF NOT EXISTS dbcolegio.alumno
(
    idalumno INT AUTO_INCREMENT NOT NULL,
    nombreAlumno VARCHAR(45)  NOT NULL,
    edadAlumno int NOT NULL,
    correoAlumno VARCHAR(45) NOT NULL,
    PRIMARY KEY (idalumno)
)


CREATE TABLE IF NOT EXISTS dbcolegio.profesor
(
    idprofesor INT AUTO_INCREMENT NOT NULL,
    nombreProfesor VARCHAR(45)  NOT NULL,
    edadProfesor int NOT NULL,
    correoProfesor VARCHAR(45) NOT NULL,
    PRIMARY KEY (idprofesor)
)

CREATE TABLE IF NOT EXISTS  dbcolegio.salon (
  idsalon INT NOT NULL AUTO_INCREMENT ,
  nombreSalon VARCHAR(45)  NOT NULL,
  idalumno INT NOT NULL,
  idprofesor INT NOT NULL,
  PRIMARY KEY (idsalon),
CONSTRAINT fkidalumno
  FOREIGN KEY (idalumno)
  REFERENCES dbcolegio.alumno (idalumno)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
CONSTRAINT fkidprofesor
  FOREIGN KEY (idprofesor)
  REFERENCES dbcolegio.profesor (idprofesor)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION
);



CREATE TABLE IF NOT EXISTS dbcolegio.semestre
(
    idsemestre INT NOT NULL AUTO_INCREMENT ,
    descSemestre VARCHAR(45)  NOT NULL,
    PRIMARY KEY (idsemestre)
)



CREATE TABLE IF NOT EXISTS  dbcolegio.curso (
  idcurso INT NOT NULL AUTO_INCREMENT ,
  nombreCurso VARCHAR(45)  NOT NULL,
  idprofesor INT NOT NULL,
  idsemestre INT NOT NULL,
  PRIMARY KEY (idcurso),
CONSTRAINT fk_idprofesor
  FOREIGN KEY (idprofesor)
  REFERENCES dbcolegio.profesor (idprofesor)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
CONSTRAINT fk_idsemestre
  FOREIGN KEY (idsemestre)
  REFERENCES dbcolegio.semestre (idsemestre)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION
);




CREATE TABLE IF NOT EXISTS  dbcolegio.notas (
  idnotas INT NOT NULL AUTO_INCREMENT ,
  idalumno INT NOT NULL,
  idcurso INT NOT NULL,
  descNota VARCHAR(45)  NOT NULL,
  PRIMARY KEY (idnotas),
CONSTRAINT fk_idalumno
  FOREIGN KEY (idalumno)
  REFERENCES dbcolegio.alumno (idalumno)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
CONSTRAINT fk_idcurso
  FOREIGN KEY (idcurso)
  REFERENCES dbcolegio.curso (idcurso)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION
);
