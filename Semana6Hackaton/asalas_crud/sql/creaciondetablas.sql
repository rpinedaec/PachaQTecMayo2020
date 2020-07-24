-- MySQL Workbench Synchronization
-- Generated: 2020-07-05 15:01
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: salas

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER TABLE `asalas`.`facdetalle` 
DROP COLUMN `idcliente`,
DROP COLUMN `idtipopago`,
DROP COLUMN `idproducto`,
DROP COLUMN `idfacab`,
ADD COLUMN `idfacab` INT(11) NOT NULL AFTER `idfacdetalle`,
ADD COLUMN `idproducto` INT(11) NOT NULL AFTER `idfacab`,
ADD COLUMN `idtipopago` INT(11) NOT NULL AFTER `idproducto`,
ADD COLUMN `idcliente` INT(11) NOT NULL AFTER `idtipopago`,
ADD INDEX `fk_facdetalle_facturacabecera_idx` (`idfacab` ASC) VISIBLE,
ADD INDEX `fk_facdetalle_productos1_idx` (`idproducto` ASC) VISIBLE,
ADD INDEX `fk_facdetalle_tipopago1_idx` (`idtipopago` ASC) VISIBLE,
ADD INDEX `fk_facdetalle_clientes1_idx` (`idcliente` ASC) VISIBLE,
DROP INDEX `fk_facdetalle_clientes1_idx` ,
DROP INDEX `fk_facdetalle_tipopago1_idx` ,
DROP INDEX `fk_facdetalle_productos1_idx` ,
DROP INDEX `fk_facdetalle_facturacabecera_idx` ;
;

ALTER TABLE `asalas`.`facturacabecera` 
DROP COLUMN `idempresa`,
ADD COLUMN `idempresa` INT(11) NOT NULL AFTER `idfacab`,
ADD INDEX `fk_facturacabecera_empresa1_idx` (`idempresa` ASC) VISIBLE,
DROP INDEX `fk_facturacabecera_empresa1_idx` ;
;

CREATE TABLE IF NOT EXISTS `asalas`.`empresa` (
  `idempresa` INT(11) NOT NULL AUTO_INCREMENT,
  `rucempresa` VARCHAR(45) NOT NULL,
  `nomempresa` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idempresa`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `asalas`.`tipopago` (
  `idtipopago` INT(11) NOT NULL AUTO_INCREMENT,
  `desctipopago` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idtipopago`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `asalas`.`clientes` (
  `idcliente` INT(11) NOT NULL AUTO_INCREMENT,
  `nomcliente` VARCHAR(45) NOT NULL,
  `docidentidad` VARCHAR(45) NOT NULL,
  `direccion` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idcliente`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

ALTER TABLE `asalas`.`facdetalle` 
ADD CONSTRAINT `fk_facdetalle_facturacabecera`
  FOREIGN KEY (`idfacab`)
  REFERENCES `asalas`.`facturacabecera` (`idfacab`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_facdetalle_productos1`
  FOREIGN KEY (`idproducto`)
  REFERENCES `asalas`.`productos` (`idproducto`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_facdetalle_tipopago1`
  FOREIGN KEY (`idtipopago`)
  REFERENCES `asalas`.`tipopago` (`idtipopago`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_facdetalle_clientes1`
  FOREIGN KEY (`idcliente`)
  REFERENCES `asalas`.`clientes` (`idcliente`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `asalas`.`facturacabecera` 
ADD CONSTRAINT `fk_facturacabecera_empresa1`
  FOREIGN KEY (`idempresa`)
  REFERENCES `asalas`.`empresa` (`idempresa`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
