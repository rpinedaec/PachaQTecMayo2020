-- MySQL Workbench Synchronization
-- Author: Fio

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `fmilla` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `fmilla`.`alumno` (
  `idalumno` INT(11) NOT NULL AUTO_INCREMENT,
  `nom_alumno` VARCHAR(45) NOT NULL,
  `cod_alumno` INT(11) NOT NULL,
  `edad_alumno` INT(11) NOT NULL,
  `correo_alumno` VARCHAR(50) NOT NULL,
  `direccion_alumno` VARCHAR(100) NOT NULL,
  `apoderado_idapoderado` INT(11) NOT NULL,
  PRIMARY KEY (`idalumno`))
  INDEX `fk_alumno_apoderado1_idx` (`apoderado_idapoderado` ASC) VISIBLE,
  CONSTRAINT `fk_alumno_apoderado1`
    FOREIGN KEY (`apoderado_idapoderado`)
    REFERENCES `fmilla`.`apoderado` (`idapoderado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `fmilla`.`apoderado` (
  `idapoderado` INT(11) NOT NULL AUTO_INCREMENT,
  `nom_apoderado` VARCHAR(45) NOT NULL,
  `correo_apoderado` VARCHAR(45) NOT NULL,
  `telefono_apoderado` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idapoderado`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `fmilla`.`profesor` (
  `idprofesor` INT(11) NOT NULL AUTO_INCREMENT,
  `nom_profesor` VARCHAR(45) NOT NULL,
  `cod_profesor` INT(11) NOT NULL,
  `edad_profesor` INT(11) NOT NULL,
  `correo_profesor` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`idprofesor`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `fmilla`.`salon` (
  `idsalon` INT(11) NOT NULL AUTO_INCREMENT,
  `nom_salon` VARCHAR(45) NOT NULL,
  `profesor_idprofesor` INT(11) NOT NULL,
  `alumno_idalumno` INT(11) NOT NULL,
  PRIMARY KEY (`idsalon`),
  INDEX `fk_salon_profesor_idx` (`profesor_idprofesor` ASC) VISIBLE,
  INDEX `fk_salon_alumno1_idx` (`alumno_idalumno` ASC) VISIBLE,
  CONSTRAINT `fk_salon_profesor`
    FOREIGN KEY (`profesor_idprofesor`)
    REFERENCES `fmilla`.`profesor` (`idprofesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_salon_alumno1`
    FOREIGN KEY (`alumno_idalumno`)
    REFERENCES `fmilla`.`alumno` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `fmilla`.`curso` (
  `idcurso` INT(11) NOT NULL AUTO_INCREMENT,
  `nom_curso` VARCHAR(45) NOT NULL,
  `profesor_idprofesor` INT(11) NOT NULL,
  `bimestre_idbimestre` INT(11) NOT NULL,
  PRIMARY KEY (`idcurso`),
  INDEX `fk_curso_profesor1_idx` (`profesor_idprofesor` ASC) VISIBLE,
  INDEX `fk_curso_bimestre1_idx` (`bimestre_idbimestre` ASC) VISIBLE,
  CONSTRAINT `fk_curso_profesor1`
    FOREIGN KEY (`profesor_idprofesor`)
    REFERENCES `fmilla`.`profesor` (`idprofesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_curso_bimestre1`
    FOREIGN KEY (`bimestre_idbimestre`)
    REFERENCES `fmilla`.`bimestre` (`idbimestre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `fmilla`.`nota` (
  `idnota` INT(11) NOT NULL AUTO_INCREMENT,
  `desc_nota` VARCHAR(45) NOT NULL,
  `alumno_idalumno` INT(11) NOT NULL,
  `curso_idcurso` INT(11) NOT NULL,
  PRIMARY KEY (`idnota`),
  INDEX `fk_nota_alumno1_idx` (`alumno_idalumno` ASC) VISIBLE,
  INDEX `fk_nota_curso1_idx` (`curso_idcurso` ASC) VISIBLE,
  CONSTRAINT `fk_nota_alumno1`
    FOREIGN KEY (`alumno_idalumno`)
    REFERENCES `fmilla`.`alumno` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_nota_curso1`
    FOREIGN KEY (`curso_idcurso`)
    REFERENCES `fmilla`.`curso` (`idcurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `fmilla`.`bimestre` (
  `idbimestre` INT(11) NOT NULL AUTO_INCREMENT,
  `desc_bimestre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idbimestre`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;