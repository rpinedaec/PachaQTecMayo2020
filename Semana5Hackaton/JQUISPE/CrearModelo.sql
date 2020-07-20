-- MySQL Workbench Synchronization
-- Generated: 2020-06-28 21:47
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: USUARIO

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE TABLE IF NOT EXISTS `jquispe`.`Alumno` (
  `idAlumno` INT(11) NOT NULL,
  `nameAlumno` VARCHAR(45) NOT NULL,
  `ageAlumno` VARCHAR(45) NOT NULL,
  `emailAlumno` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idAlumno`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `jquispe`.`Salon` (
  `idSalon` INT(11) NOT NULL,
  `nameSalon` VARCHAR(45) NULL DEFAULT NULL,
  `Profesor_idProfesor` INT(11) NOT NULL,
  `Alumno_idAlumno` INT(11) NOT NULL,
  PRIMARY KEY (`idSalon`),
  INDEX `fk_Salon_Profesor_idx` (`Profesor_idProfesor` ASC) VISIBLE,
  INDEX `fk_Salon_Alumno1_idx` (`Alumno_idAlumno` ASC) VISIBLE,
  CONSTRAINT `fk_Salon_Profesor`
    FOREIGN KEY (`Profesor_idProfesor`)
    REFERENCES `jquispe`.`Profesor` (`idProfesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Salon_Alumno1`
    FOREIGN KEY (`Alumno_idAlumno`)
    REFERENCES `jquispe`.`Alumno` (`idAlumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `jquispe`.`Profesor` (
  `idProfesor` INT(11) NOT NULL,
  `nameProfesor` VARCHAR(45) NOT NULL,
  `ageProfesor` VARCHAR(45) NOT NULL,
  `emailProfesor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idProfesor`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `jquispe`.`Curso` (
  `idCurso` INT(11) NOT NULL,
  `nameCurso` VARCHAR(45) NULL DEFAULT NULL,
  `Profesor_idProfesor` INT(11) NOT NULL,
  `Semestre_idSemestre` INT(11) NOT NULL,
  PRIMARY KEY (`idCurso`),
  INDEX `fk_Curso_Profesor1_idx` (`Profesor_idProfesor` ASC) VISIBLE,
  INDEX `fk_Curso_Semestre1_idx` (`Semestre_idSemestre` ASC) VISIBLE,
  CONSTRAINT `fk_Curso_Profesor1`
    FOREIGN KEY (`Profesor_idProfesor`)
    REFERENCES `jquispe`.`Profesor` (`idProfesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Curso_Semestre1`
    FOREIGN KEY (`Semestre_idSemestre`)
    REFERENCES `jquispe`.`Semestre` (`idSemestre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `jquispe`.`Notas` (
  `idNotas` INT(11) NOT NULL,
  `descNotas` VARCHAR(45) NOT NULL,
  `Alumno_idAlumno` INT(11) NOT NULL,
  `Curso_idCurso` INT(11) NOT NULL,
  PRIMARY KEY (`idNotas`),
  INDEX `fk_Notas_Alumno1_idx` (`Alumno_idAlumno` ASC) VISIBLE,
  INDEX `fk_Notas_Curso1_idx` (`Curso_idCurso` ASC) VISIBLE,
  CONSTRAINT `fk_Notas_Alumno1`
    FOREIGN KEY (`Alumno_idAlumno`)
    REFERENCES `jquispe`.`Alumno` (`idAlumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Notas_Curso1`
    FOREIGN KEY (`Curso_idCurso`)
    REFERENCES `jquispe`.`Curso` (`idCurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `jquispe`.`Semestre` (
  `idSemestre` INT(11) NOT NULL,
  `descSemestre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idSemestre`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
