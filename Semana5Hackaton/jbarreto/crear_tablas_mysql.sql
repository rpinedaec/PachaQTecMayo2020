-- MySQL Workbench Synchronization
-- Generated: 2020-06-27 12:06
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: JACQUELINE

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `jbarreto` DEFAULT CHARACTER SET utf8 ;


CREATE TABLE IF NOT EXISTS `jbarreto`.`Alumno` (
  `idalumno` INT(11) NOT NULL,
  `nombreAlumno` VARCHAR(45) NOT NULL,
  `edadAlumno` VARCHAR(45) NOT NULL,
  `correoAlumno` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idalumno`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `jbarreto`.`Profesor` (
  `idProfesor` INT(11) NOT NULL,
  `nombreProfesor` VARCHAR(45) NOT NULL,
  `edadProfesor` INT(11) NOT NULL,
  `correoProfesor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idProfesor`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `jbarreto`.`curso` (
  `idcurso` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreCurso` VARCHAR(45) NOT NULL,
  `Profesor_idProfesor` INT(11) NOT NULL,
  `semestre_idsemestre` INT(11) NOT NULL,
  PRIMARY KEY (`idcurso`),
  INDEX `fk_curso_Profesor_idx` (`Profesor_idProfesor` ASC) VISIBLE,
  INDEX `fk_curso_semestre1_idx` (`semestre_idsemestre` ASC) VISIBLE,
  CONSTRAINT `fk_curso_Profesor`
    FOREIGN KEY (`Profesor_idProfesor`)
    REFERENCES `jbarreto`.`Profesor` (`idProfesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_curso_semestre1`
    FOREIGN KEY (`semestre_idsemestre`)
    REFERENCES `jbarreto`.`semestre` (`idsemestre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `jbarreto`.`salon` (
  `idsalon` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreSalon` VARCHAR(45) NOT NULL,
  `Profesor_idProfesor` INT(11) NOT NULL,
  `Alumno_idalumno` INT(11) NOT NULL,
  PRIMARY KEY (`idsalon`, `Alumno_idalumno`),
  INDEX `fk_salon_Profesor1_idx` (`Profesor_idProfesor` ASC) VISIBLE,
  INDEX `fk_salon_Alumno1_idx` (`Alumno_idalumno` ASC) VISIBLE,
  CONSTRAINT `fk_salon_Profesor1`
    FOREIGN KEY (`Profesor_idProfesor`)
    REFERENCES `jbarreto`.`Profesor` (`idProfesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_salon_Alumno1`
    FOREIGN KEY (`Alumno_idalumno`)
    REFERENCES `jbarreto`.`Alumno` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `jbarreto`.`notas` (
  `idnotas` INT(11) NOT NULL AUTO_INCREMENT,
  `descNotas` VARCHAR(45) NOT NULL,
  `curso_idcurso` INT(11) NOT NULL,
  `Alumno_idalumno` INT(11) NOT NULL,
  PRIMARY KEY (`idnotas`),
  INDEX `fk_notas_curso1_idx` (`curso_idcurso` ASC) VISIBLE,
  INDEX `fk_notas_Alumno1_idx` (`Alumno_idalumno` ASC) VISIBLE,
  CONSTRAINT `fk_notas_curso1`
    FOREIGN KEY (`curso_idcurso`)
    REFERENCES `jbarreto`.`curso` (`idcurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_notas_Alumno1`
    FOREIGN KEY (`Alumno_idalumno`)
    REFERENCES `jbarreto`.`Alumno` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `jbarreto`.`semestre` (
  `idsemestre` INT(11) NOT NULL,
  `descsemestre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idsemestre`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
