-- MySQL Workbench Synchronization
-- Generated: 2020-07-06 12:18
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: USUARIO

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE TABLE IF NOT EXISTS `jquispe`.`facCabecera` (
  `idfacCabecera` INT(11) NOT NULL AUTO_INCREMENT,
  `fechaFacCabecera` DATETIME NOT NULL DEFAULT NOW(),
  `igvFacCabecera` DECIMAL(18,2) NOT NULL,
  `subtotalFacCabecera` DECIMAL(18,2) NOT NULL,
  `totalFacCabecera` DECIMAL(18,2) NOT NULL,
  `estadoFactura` CHAR(1) NOT NULL,
  `idCliente` INT(11) NOT NULL,
  `idtipoPago` INT(11) NOT NULL,
  `idempresa` INT(11) NOT NULL,
  PRIMARY KEY (`idfacCabecera`),
  INDEX `fk_facCabecera_Clientes_idx` (`idCliente` ASC) VISIBLE,
  INDEX `fk_facCabecera_tipoPago1_idx` (`idtipoPago` ASC) VISIBLE,
  INDEX `fk_facCabecera_empresa1_idx` (`idempresa` ASC) VISIBLE,
  CONSTRAINT `fk_facCabecera_Clientes`
    FOREIGN KEY (`idCliente`)
    REFERENCES `jquispe`.`Clientes` (`idClientes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facCabecera_tipoPago1`
    FOREIGN KEY (`idtipoPago`)
    REFERENCES `jquispe`.`tipoPago` (`idtipoPago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facCabecera_empresa1`
    FOREIGN KEY (`idempresa`)
    REFERENCES `jquispe`.`empresa` (`idempresa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `jquispe`.`Clientes` (
  `idClientes` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreCliente` VARCHAR(45) NOT NULL,
  `nroIdentificacionCliente` VARCHAR(45) NOT NULL,
  `direccionCliente` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`idClientes`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `jquispe`.`tipoPago` (
  `idtipoPago` INT(11) NOT NULL AUTO_INCREMENT,
  `desctipoPago` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idtipoPago`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `jquispe`.`empresa` (
  `idempresa` INT(11) NOT NULL AUTO_INCREMENT,
  `rucEmpresa` VARCHAR(45) NOT NULL,
  `nombreEmpresa` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idempresa`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `jquispe`.`facDetalle` (
  `idfacDetalle` INT(11) NOT NULL AUTO_INCREMENT,
  `cantFacDetalle` INT(11) NOT NULL,
  `valorFacDetalle` DECIMAL(18,2) NOT NULL,
  `idfacCabecera` INT(11) NOT NULL,
  `idproductos` INT(11) NOT NULL,
  PRIMARY KEY (`idfacDetalle`),
  INDEX `fk_facDetalle_facCabecera1_idx` (`idfacCabecera` ASC) VISIBLE,
  INDEX `fk_facDetalle_productos1_idx` (`idproductos` ASC) VISIBLE,
  CONSTRAINT `fk_facDetalle_facCabecera1`
    FOREIGN KEY (`idfacCabecera`)
    REFERENCES `jquispe`.`facCabecera` (`idfacCabecera`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facDetalle_productos1`
    FOREIGN KEY (`idproductos`)
    REFERENCES `jquispe`.`productos` (`idproductos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `jquispe`.`productos` (
  `idproductos` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreProducto` VARCHAR(45) NOT NULL,
  `valorProducto` DECIMAL(18,2) NOT NULL,
  `igvProducto` TINYINT(4) NOT NULL,
  `productoscol` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idproductos`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
