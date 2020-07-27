-- MySQL Workbench Synchronization
-- Generated: 2020-07-05 09:23
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: braul

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `Hackaton6Bberlanga` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `Hackaton6Bberlanga`.`metodo_pago` (
  `id_metodo_pago` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(25) NOT NULL,
  `producto_id_producto` INT(11) NOT NULL,
  PRIMARY KEY (`id_metodo_pago`),
  INDEX `fk_metodo_pago_producto1_idx` (`producto_id_producto` ASC) VISIBLE,
  CONSTRAINT `fk_metodo_pago_producto1`
    FOREIGN KEY (`producto_id_producto`)
    REFERENCES `Hackaton6Bberlanga`.`producto` (`id_producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Hackaton6Bberlanga`.`cliente` (
  `id_cliente` INT(11) NOT NULL AUTO_INCREMENT,
  `DNI_cliente` VARCHAR(45) NOT NULL,
  `nombre_cliente` VARCHAR(45) NOT NULL,
  `correo_cliente` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_cliente`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Hackaton6Bberlanga`.`producto` (
  `id_producto` INT(11) NOT NULL,
  `nombre_producto` VARCHAR(25) NOT NULL,
  `precio unitario` DECIMAL NOT NULL,
  PRIMARY KEY (`id_producto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Hackaton6Bberlanga`.`factura` (
  `id_factura` INT(11) NOT NULL AUTO_INCREMENT,
  `fecha_factura` DATE NOT NULL,
  `sub_total_factura` DECIMAL NOT NULL,
  `IGV_factura` DECIMAL NOT NULL,
  `total_factura` DECIMAL NOT NULL,
  `cliente_id_cliente` INT(11) NOT NULL,
  `metodo_pago_id_metodo_pago` INT(11) NOT NULL,
  `estado_factura` CHAR(1) NOT NULL,
  PRIMARY KEY (`id_factura`),
  INDEX `fk_factura_cliente_idx` (`cliente_id_cliente` ASC) VISIBLE,
  INDEX `fk_factura_metodo_pago1_idx` (`metodo_pago_id_metodo_pago` ASC) VISIBLE,
  CONSTRAINT `fk_factura_cliente`
    FOREIGN KEY (`cliente_id_cliente`)
    REFERENCES `Hackaton6Bberlanga`.`cliente` (`id_cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_factura_metodo_pago1`
    FOREIGN KEY (`metodo_pago_id_metodo_pago`)
    REFERENCES `Hackaton6Bberlanga`.`metodo_pago` (`id_metodo_pago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Hackaton6Bberlanga`.`detalle_factura` (
  `id_detalle_factura` INT(11) NOT NULL AUTO_INCREMENT,
  `factura_id_factura` INT(11) NOT NULL,
  `cantidad_detalle_factura` DECIMAL NOT NULL,
  `total_detalle_factura` DECIMAL NOT NULL,
  PRIMARY KEY (`id_detalle_factura`),
  INDEX `fk_detalle_factura_factura1_idx` (`factura_id_factura` ASC) VISIBLE,
  CONSTRAINT `fk_detalle_factura_factura1`
    FOREIGN KEY (`factura_id_factura`)
    REFERENCES `Hackaton6Bberlanga`.`factura` (`id_factura`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
