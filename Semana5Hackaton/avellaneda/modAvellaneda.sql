-- MySQL Workbench Synchronization
-- Generated: 2020-06-29 22:37
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: Ricardo Avellaneda

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `avellaneda` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `avellaneda`.`alumno` (
  `idalumno` INT(11) NOT NULL AUTO_INCREMENT,
  `aliasAlumno` VARCHAR(45) NOT NULL,
  `edadAlumno` INT(11) NOT NULL,
  `mailAlumno` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idalumno`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `avellaneda`.`profesores` (
  `idprofesores` INT(11) NOT NULL AUTO_INCREMENT,
  `aliasProfesor` VARCHAR(45) NOT NULL,
  `edadProfesor` INT(11) NOT NULL,
  `mailProfesor` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idprofesores`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `avellaneda`.`asignaturas` (
  `idasignaturas` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreCurso` VARCHAR(45) NOT NULL,
  `idprofesores` INT(11) NOT NULL,
  `idsemestre` INT(11) NOT NULL,
  PRIMARY KEY (`idasignaturas`),
  INDEX `fk_asignaturas_profesores_idx` (`idprofesores` ASC) VISIBLE,
  INDEX `fk_asignaturas_semestre1_idx` (`idsemestre` ASC) VISIBLE,
  CONSTRAINT `fk_asignaturas_profesores`
    FOREIGN KEY (`idprofesores`)
    REFERENCES `avellaneda`.`profesores` (`idprofesores`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_asignaturas_semestre1`
    FOREIGN KEY (`idsemestre`)
    REFERENCES `avellaneda`.`semestre` (`idsemestre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `avellaneda`.`aula` (
  `idaula` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreAula` VARCHAR(45) NOT NULL,
  `idprofesores` INT(11) NOT NULL,
  `idalumno` INT(11) NOT NULL,
  PRIMARY KEY (`idaula`),
  INDEX `fk_aula_profesores1_idx` (`idprofesores` ASC) VISIBLE,
  INDEX `fk_aula_alumno1_idx` (`idalumno` ASC) VISIBLE,
  CONSTRAINT `fk_aula_profesores1`
    FOREIGN KEY (`idprofesores`)
    REFERENCES `avellaneda`.`profesores` (`idprofesores`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_aula_alumno1`
    FOREIGN KEY (`idalumno`)
    REFERENCES `avellaneda`.`alumno` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `avellaneda`.`notas` (
  `idnotas` INT(11) NOT NULL AUTO_INCREMENT,
  `descNotas` VARCHAR(45) NOT NULL,
  `idalumno` INT(11) NOT NULL,
  `idasignaturas` INT(11) NOT NULL,
  PRIMARY KEY (`idnotas`),
  INDEX `fk_notas_alumno1_idx` (`idalumno` ASC) VISIBLE,
  INDEX `fk_notas_asignaturas1_idx` (`idasignaturas` ASC) VISIBLE,
  CONSTRAINT `fk_notas_alumno1`
    FOREIGN KEY (`idalumno`)
    REFERENCES `avellaneda`.`alumno` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_notas_asignaturas1`
    FOREIGN KEY (`idasignaturas`)
    REFERENCES `avellaneda`.`asignaturas` (`idasignaturas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `avellaneda`.`semestre` (
  `idsemestre` INT(11) NOT NULL AUTO_INCREMENT,
  `descSemestre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idsemestre`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
