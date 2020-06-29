-- MySQL Workbench Synchronization
-- Generated: 2020-06-28 18:18
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: MARTIN

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER SCHEMA `martinperez`  DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci ;

CREATE TABLE IF NOT EXISTS `martinperez`.`alumno` (
  `idalumno` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `edad` INT(11) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idalumno`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `martinperez`.`profesor` (
  `idprofesor` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `edad` INT(11) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idprofesor`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `martinperez`.`semestre` (
  `idsemestre` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idsemestre`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `martinperez`.`salon` (
  `idsalon` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `idalumno` INT(11) NOT NULL,
  `idprofesor` INT(11) NOT NULL,
  PRIMARY KEY (`idsalon`),
  INDEX `fk_salon_alumno_idx` (`idalumno` ASC) VISIBLE,
  INDEX `fk_salon_profesor1_idx` (`idprofesor` ASC) VISIBLE,
  CONSTRAINT `fk_salon_alumno`
    FOREIGN KEY (`idalumno`)
    REFERENCES `martinperez`.`alumno` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_salon_profesor1`
    FOREIGN KEY (`idprofesor`)
    REFERENCES `martinperez`.`profesor` (`idprofesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


CREATE TABLE IF NOT EXISTS `martinperez`.`curso` (
  `idcurso` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `idsemestre` INT(11) NOT NULL,
  `idprofesor` INT(11) NOT NULL,
  PRIMARY KEY (`idcurso`),
  INDEX `fk_curso_semestre1_idx` (`idsemestre` ASC) VISIBLE,
  INDEX `fk_curso_profesor1_idx` (`idprofesor` ASC) VISIBLE,
  CONSTRAINT `fk_curso_semestre1`
    FOREIGN KEY (`idsemestre`)
    REFERENCES `martinperez`.`semestre` (`idsemestre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_curso_profesor1`
    FOREIGN KEY (`idprofesor`)
    REFERENCES `martinperez`.`profesor` (`idprofesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;



CREATE TABLE IF NOT EXISTS `martinperez`.`nota` (
  `idnota` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(100) NOT NULL,
  `idalumno` INT(11) NOT NULL,
  `idcurso` INT(11) NOT NULL,
  PRIMARY KEY (`idnota`),
  INDEX `fk_nota_alumno1_idx` (`idalumno` ASC) VISIBLE,
  INDEX `fk_nota_curso1_idx` (`idcurso` ASC) VISIBLE,
  CONSTRAINT `fk_nota_alumno1`
    FOREIGN KEY (`idalumno`)
    REFERENCES `martinperez`.`alumno` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_nota_curso1`
    FOREIGN KEY (`idcurso`)
    REFERENCES `martinperez`.`curso` (`idcurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;



-- -----------------------------------------------------
-- Placeholder table for view `martinperez`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `martinperez`.`view1` (`idalumno` INT, `nombre` INT, `edad` INT, `correo` INT, `idsalon` INT, `idprofesor` INT);


USE `martinperez`;

-- -----------------------------------------------------
-- View `martinperez`.`view1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `martinperez`.`view1`;
USE `martinperez`;
CREATE  OR REPLACE VIEW `view1` AS
select
*
from alumno as A
inner join salon as S on A.idalumno = S.idalumno
inner join profesor as P on S.idprofesor = P.idprofesor;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
