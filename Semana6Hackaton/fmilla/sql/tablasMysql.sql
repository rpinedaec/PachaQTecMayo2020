
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `Hackatons6fmilla` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `Hackatons6fmilla`.`facCabecera` (
  `idfacCabecera` INT(11) NOT NULL AUTO_INCREMENT,
  `fechaFacCabecera` DATETIME NOT NULL,
  `igvFacturaCabecera` DECIMAL(18,2) NOT NULL,
  `subtotalFacCabecera` DECIMAL(18,2) NOT NULL,
  `totalFacCabecera` DECIMAL(18,2) NOT NULL,
  `empresa_idempresa` INT(11) NOT NULL,
  `tipoPago_idtipoPago` INT(11) NOT NULL,
  `clientes_idclientes` INT(11) NOT NULL,
  `estadoFactura` CHAR(1) NOT NULL,
  PRIMARY KEY (`idfacCabecera`),
  INDEX `fk_facCabecera_empresa1_idx` (`empresa_idempresa` ASC) VISIBLE,
  INDEX `fk_facCabecera_tipoPago1_idx` (`tipoPago_idtipoPago` ASC) VISIBLE,
  INDEX `fk_facCabecera_clientes1_idx` (`clientes_idclientes` ASC) VISIBLE,
  CONSTRAINT `fk_facCabecera_empresa1`
    FOREIGN KEY (`empresa_idempresa`)
    REFERENCES `Hackatons6fmilla`.`empresa` (`idempresa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facCabecera_tipoPago1`
    FOREIGN KEY (`tipoPago_idtipoPago`)
    REFERENCES `Hackatons6fmilla`.`tipoPago` (`idtipoPago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facCabecera_clientes1`
    FOREIGN KEY (`clientes_idclientes`)
    REFERENCES `Hackatons6fmilla`.`clientes` (`idclientes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Hackatons6fmilla`.`productos` (
  `idproductos` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreProducto` VARCHAR(45) NOT NULL,
  `valorProducto` DECIMAL(18,2) NOT NULL,
  `igvProducto` TINYINT(4) NOT NULL,
  PRIMARY KEY (`idproductos`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Hackatons6fmilla`.`facDetalle` (
  `idfacDetalle` INT(11) NOT NULL AUTO_INCREMENT,
  `cantFacDetalle` INT(11) NOT NULL,
  `facCabecera_idfacCabecera` INT(11) NOT NULL,
  `productos_idproductos` INT(11) NOT NULL,
  `valorProducto` DECIMAL(18,2) NOT NULL,
  PRIMARY KEY (`idfacDetalle`),
  INDEX `fk_facDetalle_facCabecera_idx` (`facCabecera_idfacCabecera` ASC) VISIBLE,
  INDEX `fk_facDetalle_productos1_idx` (`productos_idproductos` ASC) VISIBLE,
  CONSTRAINT `fk_facDetalle_facCabecera`
    FOREIGN KEY (`facCabecera_idfacCabecera`)
    REFERENCES `Hackatons6fmilla`.`facCabecera` (`idfacCabecera`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facDetalle_productos1`
    FOREIGN KEY (`productos_idproductos`)
    REFERENCES `Hackatons6fmilla`.`productos` (`idproductos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Hackatons6fmilla`.`empresa` (
  `idempresa` INT(11) NOT NULL AUTO_INCREMENT,
  `rucEmpresa` VARCHAR(45) NOT NULL,
  `nombreEmpresa` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idempresa`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Hackatons6fmilla`.`tipoPago` (
  `idtipoPago` INT(11) NOT NULL AUTO_INCREMENT,
  `tipoPagocol` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idtipoPago`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Hackatons6fmilla`.`clientes` (
  `idclientes` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreCliente` VARCHAR(45) NOT NULL,
  `nroIdentificacionCliente` VARCHAR(45) NOT NULL,
  `direccionCliente` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`idclientes`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;