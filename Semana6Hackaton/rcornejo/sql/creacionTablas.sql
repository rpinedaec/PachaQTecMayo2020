-- MySQL Workbench Synchronization
-- Generated: 2020-07-04 16:17
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: USER

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER TABLE `hackaton6rcornejo`.`facCabecera` 
DROP FOREIGN KEY `fk_facCabecera_clientes1`;

ALTER TABLE `hackaton6rcornejo`.`facCabecera` 
CHANGE COLUMN `idclientes` `idcliente` INT(11) NOT NULL ;

ALTER TABLE `hackaton6rcornejo`.`clientes` 
CHANGE COLUMN `idclientes` `idcliente` INT(11) NOT NULL AUTO_INCREMENT ;

ALTER TABLE `hackaton6rcornejo`.`facCabecera` 
ADD CONSTRAINT `fk_facCabecera_empresa1`
  FOREIGN KEY (`idempresa`)
  REFERENCES `hackaton6rcornejo`.`empresa` (`idempresa`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_facCabecera_tipoPago1`
  FOREIGN KEY (`idtipoPago`)
  REFERENCES `hackaton6rcornejo`.`tipoPago` (`idtipoPago`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_facCabecera_clientes1`
  FOREIGN KEY (`idcliente`)
  REFERENCES `hackaton6rcornejo`.`clientes` (`idcliente`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `hackaton6rcornejo`.`facDetalle` 
ADD CONSTRAINT `fk_facDetalle_facCabecera`
  FOREIGN KEY (`idfacCabecera`)
  REFERENCES `hackaton6rcornejo`.`facCabecera` (`idfacCabecera`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_facDetalle_productos1`
  FOREIGN KEY (`idproductos`)
  REFERENCES `hackaton6rcornejo`.`productos` (`idproductos`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
