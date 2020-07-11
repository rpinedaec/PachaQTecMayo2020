-- MySQL Workbench Synchronization
-- Generated: 2020-06-30 11:28
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: aldo samaniego

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER TABLE `asamaniego`.`curso` 
DROP FOREIGN KEY `fk_curso_profesor`,
DROP FOREIGN KEY `fk_curso_semestre1`;

ALTER TABLE `asamaniego`.`salon` 
DROP FOREIGN KEY `fk_salon_alumno1`,
DROP FOREIGN KEY `fk_salon_profesor1`;

ALTER TABLE `asamaniego`.`nota` 
DROP FOREIGN KEY `fk_nota_alumno1`,
DROP FOREIGN KEY `fk_nota_curso1`;

ALTER TABLE `asamaniego`.`alumno` 
ADD COLUMN `idCreo` INT(11) NOT NULL AFTER `correoAlumno`,
ADD COLUMN `fechaCreo` DATETIME NOT NULL AFTER `idCreo`,
ADD COLUMN `idModifico` INT(11) NULL DEFAULT NULL AFTER `fechaCreo`,
ADD COLUMN `fechaModifico` DATETIME NULL DEFAULT NULL AFTER `idModifico`;

ALTER TABLE `asamaniego`.`profesor` 
ADD COLUMN `idCreo` INT(11) NOT NULL AFTER `correoProfesor`,
ADD COLUMN `fechaCreo` DATETIME NOT NULL AFTER `idCreo`,
ADD COLUMN `idModifico` INT(11) NULL DEFAULT NULL AFTER `fechaCreo`,
ADD COLUMN `fechaModifico` DATETIME NULL DEFAULT NULL AFTER `idModifico`;

ALTER TABLE `asamaniego`.`curso` 
ADD COLUMN `idCreo` INT(11) NOT NULL AFTER `idsemestre`,
ADD COLUMN `fechaCreo` DATETIME NOT NULL AFTER `idCreo`,
ADD COLUMN `idModifico` INT(11) NULL DEFAULT NULL AFTER `fechaCreo`,
ADD COLUMN `fechaModifico` DATETIME NULL DEFAULT NULL AFTER `idModifico`;

ALTER TABLE `asamaniego`.`salon` 
ADD COLUMN `idCreo` INT(11) NOT NULL AFTER `idProfesor`,
ADD COLUMN `fechaCreo` DATETIME NOT NULL AFTER `idCreo`,
ADD COLUMN `idModifico` INT(11) NULL DEFAULT NULL AFTER `fechaCreo`,
ADD COLUMN `fechaModifico` DATETIME NULL DEFAULT NULL AFTER `idModifico`;

ALTER TABLE `asamaniego`.`nota` 
ADD COLUMN `idCreo` INT(11) NOT NULL AFTER `idcurso`,
ADD COLUMN `fechaCreo` DATETIME NOT NULL AFTER `idCreo`,
ADD COLUMN `idModifico` INT(11) NULL DEFAULT NULL AFTER `fechaCreo`,
ADD COLUMN `fechaModifico` DATETIME NULL DEFAULT NULL AFTER `idModifico`;

ALTER TABLE `asamaniego`.`semestre` 
ADD COLUMN `idCreo` INT(11) NOT NULL AFTER `descSemestre`,
ADD COLUMN `fechaCreo` DATETIME NOT NULL AFTER `idCreo`,
ADD COLUMN `idModifico` INT(11) NULL DEFAULT NULL AFTER `fechaCreo`,
ADD COLUMN `fechaModifico` DATETIME NULL DEFAULT NULL AFTER `idModifico`;

ALTER TABLE `asamaniego`.`curso` 
ADD CONSTRAINT `fk_curso_profesor`
  FOREIGN KEY (`idProfesor`)
  REFERENCES `asamaniego`.`profesor` (`idProfesor`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_curso_semestre1`
  FOREIGN KEY (`idsemestre`)
  REFERENCES `asamaniego`.`semestre` (`idsemestre`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `asamaniego`.`salon` 
ADD CONSTRAINT `fk_salon_alumno1`
  FOREIGN KEY (`idAlumno`)
  REFERENCES `asamaniego`.`alumno` (`idAlumno`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_salon_profesor1`
  FOREIGN KEY (`idProfesor`)
  REFERENCES `asamaniego`.`profesor` (`idProfesor`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `asamaniego`.`nota` 
ADD CONSTRAINT `fk_nota_alumno1`
  FOREIGN KEY (`idAlumno`)
  REFERENCES `asamaniego`.`alumno` (`idAlumno`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_nota_curso1`
  FOREIGN KEY (`idcurso`)
  REFERENCES `asamaniego`.`curso` (`idcurso`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
