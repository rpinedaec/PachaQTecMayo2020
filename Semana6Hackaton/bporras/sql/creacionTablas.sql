-- MySQL Workbench Synchronization
-- Generated: 2020-07-05 11:23
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: Bruce Porras

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `Hackathon6_bporras` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `Hackathon6_bporras`.`FacCabecera` (
  `idFacCabecera` INT(11) NOT NULL AUTO_INCREMENT,
  `idCliente` INT(11) NOT NULL,
  `igvFacCabecera` DECIMAL(18,2) NOT NULL,
  `subtotalFacCabecera` DECIMAL(18,2) NOT NULL,
  `totalFacCabecera` DECIMAL(18,2) NOT NULL,
  `fechaFacCabecera` DATETIME NOT NULL,
  `estadoFacCabecera` CHAR(1) NOT NULL,
  PRIMARY KEY (`idFacCabecera`),
  INDEX `fk_FacCabecera_Cliente1_idx` (`idCliente` ASC) VISIBLE,
  CONSTRAINT `fk_FacCabecera_Cliente1`
    FOREIGN KEY (`idCliente`)
    REFERENCES `Hackathon6_bporras`.`Cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Hackathon6_bporras`.`Producto` (
  `idProducto` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreProducto` VARCHAR(45) NOT NULL,
  `valorProducto` DECIMAL(18,2) NULL DEFAULT NULL,
  `igvProducto` TINYINT(4) NOT NULL,
  PRIMARY KEY (`idProducto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Hackathon6_bporras`.`FacDetalle` (
  `idFacDetalle` INT(11) NOT NULL AUTO_INCREMENT,
  `idFacCabecera` INT(11) NOT NULL,
  `idProducto` INT(11) NOT NULL,
  `cantFacDetalle` VARCHAR(45) NOT NULL,
  `valorFacDetalle` DECIMAL(18,2) NOT NULL,
  PRIMARY KEY (`idFacDetalle`),
  INDEX `fk_FacDetalle_FacCabecera_idx` (`idFacCabecera` ASC) VISIBLE,
  INDEX `fk_FacDetalle_Producto1_idx` (`idProducto` ASC) VISIBLE,
  CONSTRAINT `fk_FacDetalle_FacCabecera`
    FOREIGN KEY (`idFacCabecera`)
    REFERENCES `Hackathon6_bporras`.`FacCabecera` (`idFacCabecera`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FacDetalle_Producto1`
    FOREIGN KEY (`idProducto`)
    REFERENCES `Hackathon6_bporras`.`Producto` (`idProducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Hackathon6_bporras`.`Cliente` (
  `idCliente` INT(11) NOT NULL AUTO_INCREMENT,
  `dniCliente` INT(11) NOT NULL,
  `nombreCliente` VARCHAR(45) NOT NULL,
  `apellidoCliente` VARCHAR(45) NOT NULL,
  `correoCliente` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCliente`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
