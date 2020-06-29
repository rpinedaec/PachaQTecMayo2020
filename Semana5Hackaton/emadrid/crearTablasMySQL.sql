-- MySQL Workbench Synchronization
-- Generated: 2020-06-28 11:47
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: EMADRID

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `emadrid` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `emadrid`.`alumno` (
  `idalumno` INT(11) NOT NULL AUTO_INCREMENT,
  `nombresAlumno` VARCHAR(45) NOT NULL,
  `fNacimientoAlumno` DATE NOT NULL,
  `correoAlumno` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idalumno`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `emadrid`.`profesor` (
  `idprofesor` INT(11) NOT NULL AUTO_INCREMENT,
  `nombresProfesor` VARCHAR(45) NOT NULL,
  `fNacimientoProfesor` DATE NOT NULL,
  `correoProfesor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idprofesor`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `emadrid`.`salon` (
  `idsalon` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreSalon` VARCHAR(45) NOT NULL,
  `idalumno` INT(11) NOT NULL,
  `idprofesor` INT(11) NOT NULL,
  PRIMARY KEY (`idsalon`),
  INDEX `fk_salon_alumno1_idx` (`idalumno` ASC) VISIBLE,
  INDEX `fk_salon_profesor1_idx` (`idprofesor` ASC) VISIBLE,
  CONSTRAINT `fk_salon_alumno1`
    FOREIGN KEY (`idalumno`)
    REFERENCES `emadrid`.`alumno` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_salon_profesor1`
    FOREIGN KEY (`idprofesor`)
    REFERENCES `emadrid`.`profesor` (`idprofesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `emadrid`.`curso` (
  `idcurso` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreCurso` VARCHAR(45) NOT NULL,
  `idprofesor` INT(11) NOT NULL,
  `idsemestre` INT(11) NOT NULL,
  PRIMARY KEY (`idcurso`),
  INDEX `fk_curso_profesor_idx` (`idprofesor` ASC) VISIBLE,
  INDEX `fk_curso_semestre1_idx` (`idsemestre` ASC) VISIBLE,
  CONSTRAINT `fk_curso_profesor`
    FOREIGN KEY (`idprofesor`)
    REFERENCES `emadrid`.`profesor` (`idprofesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_curso_semestre1`
    FOREIGN KEY (`idsemestre`)
    REFERENCES `emadrid`.`semestre` (`idsemestre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `emadrid`.`notas` (
  `idnotas` INT(11) NOT NULL AUTO_INCREMENT,
  `idalumno` INT(11) NOT NULL,
  `idcurso` INT(11) NOT NULL,
  `descNota` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idnotas`),
  INDEX `fk_notas_alumno1_idx` (`idalumno` ASC) VISIBLE,
  INDEX `fk_notas_curso1_idx` (`idcurso` ASC) VISIBLE,
  CONSTRAINT `fk_notas_alumno1`
    FOREIGN KEY (`idalumno`)
    REFERENCES `emadrid`.`alumno` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_notas_curso1`
    FOREIGN KEY (`idcurso`)
    REFERENCES `emadrid`.`curso` (`idcurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `emadrid`.`semestre` (
  `idsemestre` INT(11) NOT NULL AUTO_INCREMENT,
  `descSemestre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idsemestre`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
