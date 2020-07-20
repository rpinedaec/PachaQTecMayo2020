-- MySQL Workbench Synchronization
-- Generated: 2020-06-28 19:57
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: Usuario

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `Sperez` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `Sperez`.`Alumno` (
  `idAlumno` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreAlumno` VARCHAR(45) NOT NULL,
  `edadAlumno` INT(11) NOT NULL,
  `correoAlumno` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idAlumno`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Sperez`.`Profesor` (
  `idProfesor` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreProfesor` VARCHAR(45) NOT NULL,
  `edadProfesor` INT(11) NOT NULL,
  `correoProfesor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idProfesor`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Sperez`.`curso` (
  `idcurso` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreCurso` VARCHAR(45) NOT NULL,
  `idProfesor` INT(11) NOT NULL,
  `idsemestre` INT(11) NOT NULL,
  PRIMARY KEY (`idcurso`),
  INDEX `fk_curso_Profesor_idx` (`idProfesor` ASC) VISIBLE,
  INDEX `fk_curso_semestre1_idx` (`idsemestre` ASC) VISIBLE,
  CONSTRAINT `fk_curso_Profesor`
    FOREIGN KEY (`idProfesor`)
    REFERENCES `Sperez`.`Profesor` (`idProfesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_curso_semestre1`
    FOREIGN KEY (`idsemestre`)
    REFERENCES `Sperez`.`semestre` (`idsemestre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Sperez`.`salon` (
  `idsalon` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreSalon` VARCHAR(45) NOT NULL,
  `idAlumno` INT(11) NOT NULL,
  `idProfesor` INT(11) NOT NULL,
  PRIMARY KEY (`idsalon`),
  INDEX `fk_salon_Alumno1_idx` (`idAlumno` ASC) VISIBLE,
  INDEX `fk_salon_Profesor1_idx` (`idProfesor` ASC) VISIBLE,
  CONSTRAINT `fk_salon_Alumno1`
    FOREIGN KEY (`idAlumno`)
    REFERENCES `Sperez`.`Alumno` (`idAlumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_salon_Profesor1`
    FOREIGN KEY (`idProfesor`)
    REFERENCES `Sperez`.`Profesor` (`idProfesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Sperez`.`notas` (
  `idnotas` INT(11) NOT NULL AUTO_INCREMENT,
  `descNotas` VARCHAR(45) NOT NULL,
  `idAlumno` INT(11) NOT NULL,
  `idcurso` INT(11) NOT NULL,
  PRIMARY KEY (`idnotas`),
  INDEX `fk_notas_Alumno1_idx` (`idAlumno` ASC) VISIBLE,
  INDEX `fk_notas_curso1_idx` (`idcurso` ASC) VISIBLE,
  CONSTRAINT `fk_notas_Alumno1`
    FOREIGN KEY (`idAlumno`)
    REFERENCES `Sperez`.`Alumno` (`idAlumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_notas_curso1`
    FOREIGN KEY (`idcurso`)
    REFERENCES `Sperez`.`curso` (`idcurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Sperez`.`semestre` (
  `idsemestre` INT(11) NOT NULL AUTO_INCREMENT,
  `descSemestre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idsemestre`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
