-- MySQL Workbench Synchronization
-- Generated: 2020-07-03 20:15
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: CARLOS

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `hackatonsemana6_dgarcia` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `hackatonsemana6_dgarcia`.`facturaCabecera` (
  `idFacCabecera` INT(11) NOT NULL AUTO_INCREMENT,
  `fechaFacCabeceracol` DATETIME NOT NULL,
  `igvFacCabecera` DECIMAL(18,2) NOT NULL,
  `subtotalFacCabecera` DECIMAL(18,2) NOT NULL,
  `totalFacCabecera` DECIMAL(18,2) NOT NULL,
  `empresa_idempresa` INT(11) NOT NULL,
  `tipoPago_idtipoPago` INT(11) NOT NULL,
  `clientes_idcliente` INT(11) NOT NULL,
  PRIMARY KEY (`idFacCabecera`),
  INDEX `fk_facturaCabecera_empresa_idx` (`empresa_idempresa` ASC) VISIBLE,
  INDEX `fk_facturaCabecera_tipoPago1_idx` (`tipoPago_idtipoPago` ASC) VISIBLE,
  INDEX `fk_facturaCabecera_clientes1_idx` (`clientes_idcliente` ASC) VISIBLE,
  CONSTRAINT `fk_facturaCabecera_empresa`
    FOREIGN KEY (`empresa_idempresa`)
    REFERENCES `hackatonsemana6_dgarcia`.`empresa` (`idempresa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facturaCabecera_tipoPago1`
    FOREIGN KEY (`tipoPago_idtipoPago`)
    REFERENCES `hackatonsemana6_dgarcia`.`tipoPago` (`idtipoPago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facturaCabecera_clientes1`
    FOREIGN KEY (`clientes_idcliente`)
    REFERENCES `hackatonsemana6_dgarcia`.`clientes` (`idcliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `hackatonsemana6_dgarcia`.`productos` (
  `idproductos` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreProducto` VARCHAR(45) NOT NULL,
  `valorProducto` DECIMAL NOT NULL,
  `nombreProducto` VARCHAR(45) NOT NULL,
  `valorProducto` DECIMAL(18,2) NOT NULL,
  `igvProducto` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idproductos`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `hackatonsemana6_dgarcia`.`facDetalle` (
  `idfacDetalle` INT(11) NOT NULL AUTO_INCREMENT,
  `cantFacDetalle` INT(11) NOT NULL,
  `valorFacDetalle` DECIMAL(18,2) NOT NULL,
  `productos_idproductos` INT(11) NOT NULL,
  `facturaCabecera_idFacCabecera` INT(11) NOT NULL,
  PRIMARY KEY (`idfacDetalle`),
  INDEX `fk_facDetalle_productos1_idx` (`productos_idproductos` ASC) VISIBLE,
  INDEX `fk_facDetalle_facturaCabecera1_idx` (`facturaCabecera_idFacCabecera` ASC) VISIBLE,
  CONSTRAINT `fk_facDetalle_productos1`
    FOREIGN KEY (`productos_idproductos`)
    REFERENCES `hackatonsemana6_dgarcia`.`productos` (`idproductos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facDetalle_facturaCabecera1`
    FOREIGN KEY (`facturaCabecera_idFacCabecera`)
    REFERENCES `hackatonsemana6_dgarcia`.`facturaCabecera` (`idFacCabecera`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `hackatonsemana6_dgarcia`.`empresa` (
  `idempresa` INT(11) NOT NULL AUTO_INCREMENT,
  `rucEmpresa` VARCHAR(45) NOT NULL,
  `nombreEmpresa` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idempresa`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `hackatonsemana6_dgarcia`.`tipoPago` (
  `idtipoPago` INT(11) NOT NULL AUTO_INCREMENT,
  `descTIpoPago` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idtipoPago`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `hackatonsemana6_dgarcia`.`clientes` (
  `idcliente` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreCliente` VARCHAR(45) NOT NULL,
  `direccionCliente` VARCHAR(200) NOT NULL,
  `nroIdentificacionCliente` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idcliente`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
