-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema bberlangas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bberlangas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bberlangas` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema bberlanga
-- -----------------------------------------------------
USE `bberlangas` ;

-- -----------------------------------------------------
-- Table `bberlangas`.`profesor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bberlangas`.`profesor` (
  `id_profesor` INT NOT NULL AUTO_INCREMENT,
  `nombre_profesor` VARCHAR(45) NOT NULL,
  `edad_profesor` INT NOT NULL,
  `correo_profesor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_profesor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bberlangas`.`salon`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bberlangas`.`salon` (
  `id_salon` INT NOT NULL AUTO_INCREMENT,
  `nombre_salon` VARCHAR(45) NOT NULL,
  `año_escolar_salon` VARCHAR(45) NOT NULL,
  `profesor_id_profesor` INT NOT NULL,
  PRIMARY KEY (`id_salon`),
  INDEX `fk_salon_profesor1_idx` (`profesor_id_profesor` ASC) VISIBLE,
  CONSTRAINT `fk_salon_profesor1`
    FOREIGN KEY (`profesor_id_profesor`)
    REFERENCES `bberlangas`.`profesor` (`id_profesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bberlangas`.`alumno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bberlangas`.`alumno` (
  `id_alumno` INT NOT NULL AUTO_INCREMENT,
  `nombre_alumno` VARCHAR(45) NOT NULL,
  `edad_alumno` INT NOT NULL,
  `correo_alumno` VARCHAR(45) NOT NULL,
  `salon_id_salon` INT NOT NULL,
  PRIMARY KEY (`id_alumno`),
  INDEX `fk_alumno_salon1_idx` (`salon_id_salon` ASC) VISIBLE,
  CONSTRAINT `fk_alumno_salon1`
    FOREIGN KEY (`salon_id_salon`)
    REFERENCES `bberlangas`.`salon` (`id_salon`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bberlangas`.`curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bberlangas`.`curso` (
  `id_curso` INT NOT NULL AUTO_INCREMENT,
  `nombre_curso` VARCHAR(45) NOT NULL,
  `profesor_id_profesor` INT NOT NULL,
  PRIMARY KEY (`id_curso`),
  INDEX `fk_curso_profesor_idx` (`profesor_id_profesor` ASC) VISIBLE,
  CONSTRAINT `fk_curso_profesor`
    FOREIGN KEY (`profesor_id_profesor`)
    REFERENCES `bberlangas`.`profesor` (`id_profesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bberlangas`.`Año`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bberlangas`.`Año` (
  `id_año` INT NOT NULL AUTO_INCREMENT,
  `nombre_año` INT NOT NULL,
  PRIMARY KEY (`id_año`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bberlangas`.`bimestres`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bberlangas`.`bimestres` (
  `id_bimestre` INT NOT NULL AUTO_INCREMENT,
  `nombre_bimestre` VARCHAR(45) NOT NULL,
  `fecha_inicio` DATE NOT NULL,
  `fecha_final` DATE NOT NULL,
  `Año_id_año` INT NOT NULL,
  PRIMARY KEY (`id_bimestre`),
  INDEX `fk_bimestres_Año1_idx` (`Año_id_año` ASC) VISIBLE,
  CONSTRAINT `fk_bimestres_Año1`
    FOREIGN KEY (`Año_id_año`)
    REFERENCES `bberlangas`.`Año` (`id_año`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bberlangas`.`notas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bberlangas`.`notas` (
  `id_notas` INT NOT NULL AUTO_INCREMENT,
  `valor_nota` INT NOT NULL,
  `bimestres_id_bimestre` INT NOT NULL,
  `Año_id_año` INT NOT NULL,
  `alumno_id_alumno` INT NOT NULL,
  `curso_id_curso` INT NOT NULL,
  PRIMARY KEY (`id_notas`),
  INDEX `fk_Notas_bimestres1_idx` (`bimestres_id_bimestre` ASC) VISIBLE,
  INDEX `fk_Notas_Año1_idx` (`Año_id_año` ASC) VISIBLE,
  INDEX `fk_Notas_alumno1_idx` (`alumno_id_alumno` ASC) VISIBLE,
  INDEX `fk_Notas_curso1_idx` (`curso_id_curso` ASC) VISIBLE,
  CONSTRAINT `fk_Notas_bimestres1`
    FOREIGN KEY (`bimestres_id_bimestre`)
    REFERENCES `bberlangas`.`bimestres` (`id_bimestre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Notas_Año1`
    FOREIGN KEY (`Año_id_año`)
    REFERENCES `bberlangas`.`Año` (`id_año`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Notas_alumno1`
    FOREIGN KEY (`alumno_id_alumno`)
    REFERENCES `bberlangas`.`alumno` (`id_alumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Notas_curso1`
    FOREIGN KEY (`curso_id_curso`)
    REFERENCES `bberlangas`.`curso` (`id_curso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
