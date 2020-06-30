-- MySQL Workbench Synchronization
-- Generated: 2020-06-29 10:20
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: Bruce Porras

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE TABLE IF NOT EXISTS `bporras`.`Alumno` (
  `idAlumno` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreAlumno` VARCHAR(45) NOT NULL,
  `edadAlumno` INT(11) NOT NULL,
  `correoAlumno` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idAlumno`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `bporras`.`Profesor` (
  `idProfesor` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreProfesor` VARCHAR(45) NOT NULL,
  `edadProfesor` INT(11) NOT NULL,
  `correoProfesor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idProfesor`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `bporras`.`Salon` (
  `idSalon` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreSalon` VARCHAR(45) NOT NULL,
  `añoescolarSalon` INT(11) NOT NULL,
  `idAlumno` INT(11) NOT NULL,
  `idProfesor` INT(11) NOT NULL,
  PRIMARY KEY (`idSalon`),
  INDEX `fk_Salon_Alumno1_idx` (`idAlumno` ASC) VISIBLE,
  INDEX `fk_Salon_Profesor1_idx` (`idProfesor` ASC) VISIBLE,
  CONSTRAINT `fk_Salon_Alumno1`
    FOREIGN KEY (`idAlumno`)
    REFERENCES `bporras`.`Alumno` (`idAlumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Salon_Profesor1`
    FOREIGN KEY (`idProfesor`)
    REFERENCES `bporras`.`Profesor` (`idProfesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `bporras`.`Curso` (
  `idCurso` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreCurso` VARCHAR(45) NOT NULL,
  `idProfesor` INT(11) NOT NULL,
  `idSalon` INT(11) NOT NULL,
  `idSemestre` INT(11) NOT NULL,
  PRIMARY KEY (`idCurso`),
  INDEX `fk_Curso_Profesor1_idx` (`idProfesor` ASC) VISIBLE,
  INDEX `fk_Curso_Salon1_idx` (`idSalon` ASC) VISIBLE,
  INDEX `fk_Curso_Semestre1_idx` (`idSemestre` ASC) VISIBLE,
  CONSTRAINT `fk_Curso_Profesor1`
    FOREIGN KEY (`idProfesor`)
    REFERENCES `bporras`.`Profesor` (`idProfesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Curso_Salon1`
    FOREIGN KEY (`idSalon`)
    REFERENCES `bporras`.`Salon` (`idSalon`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Curso_Semestre1`
    FOREIGN KEY (`idSemestre`)
    REFERENCES `bporras`.`Semestre` (`idSemestre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `bporras`.`Notas` (
  `idNotas` INT(11) NOT NULL AUTO_INCREMENT,
  `descNota` VARCHAR(45) NOT NULL,
  `idAlumno` INT(11) NOT NULL,
  `idCurso` INT(11) NOT NULL,
  PRIMARY KEY (`idNotas`),
  INDEX `fk_Notas_Alumno1_idx` (`idAlumno` ASC) VISIBLE,
  INDEX `fk_Notas_Curso1_idx` (`idCurso` ASC) VISIBLE,
  CONSTRAINT `fk_Notas_Alumno1`
    FOREIGN KEY (`idAlumno`)
    REFERENCES `bporras`.`Alumno` (`idAlumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Notas_Curso1`
    FOREIGN KEY (`idCurso`)
    REFERENCES `bporras`.`Curso` (`idCurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `bporras`.`Semestre` (
  `idSemestre` INT(11) NOT NULL AUTO_INCREMENT,
  `descSemestre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idSemestre`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
