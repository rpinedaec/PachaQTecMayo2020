-- MySQL Workbench Synchronization
-- Generated: 2020-06-29 18:52
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: aldo samaniego

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `asamaniego` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `asamaniego`.`alumno` (
  `idAlumno` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreAlumno` VARCHAR(45) NOT NULL,
  `edad` INT(11) NOT NULL,
  `correoAlumno` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idAlumno`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `asamaniego`.`profesor` (
  `idProfesor` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreProfesor` VARCHAR(45) NOT NULL,
  `edadProfesor` INT(11) NOT NULL,
  `correoProfesor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idProfesor`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `asamaniego`.`curso` (
  `idcurso` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreCurso` VARCHAR(45) NOT NULL,
  `idProfesor` INT(11) NOT NULL,
  `idsemestre` INT(11) NOT NULL,
  PRIMARY KEY (`idcurso`),
  INDEX `fk_curso_profesor_idx` (`idProfesor` ASC) VISIBLE,
  INDEX `fk_curso_semestre1_idx` (`idsemestre` ASC) VISIBLE,
  CONSTRAINT `fk_curso_profesor`
    FOREIGN KEY (`idProfesor`)
    REFERENCES `asamaniego`.`profesor` (`idProfesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_curso_semestre1`
    FOREIGN KEY (`idsemestre`)
    REFERENCES `asamaniego`.`semestre` (`idsemestre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `asamaniego`.`salon` (
  `idsalon` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreSalon` VARCHAR(45) NOT NULL,
  `idAlumno` INT(11) NOT NULL,
  `idProfesor` INT(11) NOT NULL,
  PRIMARY KEY (`idsalon`),
  INDEX `fk_salon_alumno1_idx` (`idAlumno` ASC) VISIBLE,
  INDEX `fk_salon_profesor1_idx` (`idProfesor` ASC) VISIBLE,
  CONSTRAINT `fk_salon_alumno1`
    FOREIGN KEY (`idAlumno`)
    REFERENCES `asamaniego`.`alumno` (`idAlumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_salon_profesor1`
    FOREIGN KEY (`idProfesor`)
    REFERENCES `asamaniego`.`profesor` (`idProfesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `asamaniego`.`nota` (
  `idnota` INT(11) NOT NULL AUTO_INCREMENT,
  `descNota` VARCHAR(45) NOT NULL,
  `idAlumno` INT(11) NOT NULL,
  `idcurso` INT(11) NOT NULL,
  PRIMARY KEY (`idnota`),
  INDEX `fk_nota_alumno1_idx` (`idAlumno` ASC) VISIBLE,
  INDEX `fk_nota_curso1_idx` (`idcurso` ASC) VISIBLE,
  CONSTRAINT `fk_nota_alumno1`
    FOREIGN KEY (`idAlumno`)
    REFERENCES `asamaniego`.`alumno` (`idAlumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_nota_curso1`
    FOREIGN KEY (`idcurso`)
    REFERENCES `asamaniego`.`curso` (`idcurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `asamaniego`.`semestre` (
  `idsemestre` INT(11) NOT NULL AUTO_INCREMENT,
  `descSemestre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idsemestre`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
