-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema rcornejo
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema rcornejo
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS rcornejo DEFAULT CHARACTER SET utf8 ;
USE rcornejo ;

-- -----------------------------------------------------
-- Table rcornejo.alumno
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS alumno (
  idalumno serial,
  nombreAlumno VARCHAR(45) NOT NULL,
  edadAlumno INT NOT NULL,
  correoAlumno VARCHAR(45) NOT NULL,
  PRIMARY KEY (idalumno))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table rcornejo.profesor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS profesor (
  idprofesor serial,
  nombreProfesor VARCHAR(45) NOT NULL,
  edadProfesor INT NOT NULL,
  correoProfesor VARCHAR(45) NOT NULL,
  PRIMARY KEY (idprofesor))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table rcornejo.semestre
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS semestre (
  idsemestre serial,
  desSemestre VARCHAR(45) NOT NULL,
  PRIMARY KEY (idsemestre))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table rcornejo.curso
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS curso (
  idcurso serial,
  nombreCurso VARCHAR(45) NOT NULL,
  idprofesor INT NOT NULL,
  idsemestre INT NOT NULL,
  PRIMARY KEY (idcurso),
  CONSTRAINT fk_curso_profesor1
    FOREIGN KEY (idprofesor)
    REFERENCES profesor (idprofesor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_curso_semestre1
    FOREIGN KEY (idsemestre)
    REFERENCES semestre (idsemestre)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table rcornejo.salon
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS salon (
  idsalon serial,
  nombreSalon VARCHAR(45) NOT NULL,
  idprofesor INT NOT NULL,
  idalumno INT NOT NULL,
  PRIMARY KEY (idsalon),
  CONSTRAINT fk_salon_profesor
    FOREIGN KEY (idprofesor)
    REFERENCES profesor (idprofesor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_salon_alumno1
    FOREIGN KEY (idalumno)
    REFERENCES alumno (idalumno)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table rcornejo.notas
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS notas (
  idnotas serial,
  descNota VARCHAR(45) NOT NULL,
  idalumno INT NOT NULL,
  idcurso INT NOT NULL,
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
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
