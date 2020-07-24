-- MySQL Workbench Synchronization
-- Generated: 2020-07-06 01:36
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: CARLOS

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `hackaton6_dgarcia` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `hackaton6_dgarcia`.`cliente` (
  `idcliente` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreCliente` VARCHAR(45) NOT NULL,
  `nroIdentCliente` VARCHAR(45) NOT NULL,
  `direccionCliente` VARCHAR(200) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`idcliente`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `hackaton6_dgarcia`.`producto` (
  `idproducto` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreProducto` VARCHAR(45) NOT NULL,
  `precioProducto` DECIMAL(18,2) NOT NULL,
  `igvProducto` TINYINT(4) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`idproducto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `hackaton6_dgarcia`.`facCabecera` (
  `idfacCabecera` INT(11) NOT NULL AUTO_INCREMENT,
  `idempresa` INT(11) NOT NULL,
  `idtipoPago` INT(11) NOT NULL,
  `idcliente` INT(11) NOT NULL,
  `fechaFacCabecera` DATETIME NOT NULL DEFAULT NOW(),
  `igvFacCabecera` DECIMAL(18,2) NOT NULL,
  `subtotalFacCabecera` DECIMAL(18,2) NOT NULL,
  `totalFacCabecera` DECIMAL(18,2) NOT NULL,
  `estadoFactura` CHAR(1) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`idfacCabecera`),
  INDEX `fk_facCabecera_empresa1_idx` (`idempresa` ASC) VISIBLE,
  INDEX `fk_facCabecera_tipoPago1_idx` (`idtipoPago` ASC) VISIBLE,
  INDEX `fk_facCabecera_cliente1_idx` (`idcliente` ASC) VISIBLE,
  CONSTRAINT `fk_facCabecera_empresa1`
    FOREIGN KEY (`idempresa`)
    REFERENCES `hackaton6_dgarcia`.`empresa` (`idempresa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facCabecera_tipoPago1`
    FOREIGN KEY (`idtipoPago`)
    REFERENCES `hackaton6_dgarcia`.`tipoPago` (`idtipoPago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facCabecera_cliente1`
    FOREIGN KEY (`idcliente`)
    REFERENCES `hackaton6_dgarcia`.`cliente` (`idcliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `hackaton6_dgarcia`.`facDetalle` (
  `idfacDetalle` INT(11) NOT NULL AUTO_INCREMENT,
  `idfacCabecera` INT(11) NOT NULL,
  `idproducto` INT(11) NOT NULL,
  `cantFacDetalle` INT(11) NOT NULL,
  `valorFacDetalle` DECIMAL(18,2) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`idfacDetalle`),
  INDEX `fk_facDetalle_facCabecera_idx` (`idfacCabecera` ASC) VISIBLE,
  INDEX `fk_facDetalle_producto1_idx` (`idproducto` ASC) VISIBLE,
  CONSTRAINT `fk_facDetalle_facCabecera`
    FOREIGN KEY (`idfacCabecera`)
    REFERENCES `hackaton6_dgarcia`.`facCabecera` (`idfacCabecera`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facDetalle_producto1`
    FOREIGN KEY (`idproducto`)
    REFERENCES `hackaton6_dgarcia`.`producto` (`idproducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `hackaton6_dgarcia`.`empresa` (
  `idempresa` INT(11) NOT NULL AUTO_INCREMENT,
  `rucEmpresa` VARCHAR(45) NOT NULL,
  `nombreEmpresa` VARCHAR(45) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT 'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP',
  PRIMARY KEY (`idempresa`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `hackaton6_dgarcia`.`tipoPago` (
  `idtipoPago` INT(11) NOT NULL AUTO_INCREMENT,
  `descTipoPago` VARCHAR(45) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`idtipoPago`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
