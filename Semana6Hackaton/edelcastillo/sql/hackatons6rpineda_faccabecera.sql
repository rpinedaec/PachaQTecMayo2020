CREATE DATABASE  IF NOT EXISTS `hackatons6rpineda` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hackatons6rpineda`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: hackatons6rpineda
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `faccabecera`
--

DROP TABLE IF EXISTS `faccabecera`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faccabecera` (
  `idfacCabecera` int NOT NULL AUTO_INCREMENT,
  `idempresa` int NOT NULL,
  `idcliente` int NOT NULL,
  `idtipoPago` int NOT NULL,
  `fechaFacCabecera` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `igvFacCabecera` decimal(18,2) NOT NULL,
  `subtotalFacCabecera` decimal(18,2) NOT NULL,
  `totalFacCabecera` decimal(18,2) NOT NULL,
  `estadoFactura` char(1) NOT NULL,
  PRIMARY KEY (`idfacCabecera`),
  KEY `fk_facCabecera_empresa1_idx` (`idempresa`),
  KEY `fk_facCabecera_tipoPago1_idx` (`idtipoPago`),
  KEY `fk_facCabecera_clientes1_idx` (`idcliente`),
  CONSTRAINT `fk_facCabecera_clientes1` FOREIGN KEY (`idcliente`) REFERENCES `clientes` (`idcliente`),
  CONSTRAINT `fk_facCabecera_empresa1` FOREIGN KEY (`idempresa`) REFERENCES `empresa` (`idempresa`),
  CONSTRAINT `fk_facCabecera_tipoPago1` FOREIGN KEY (`idtipoPago`) REFERENCES `tipopago` (`idtipoPago`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faccabecera`
--

LOCK TABLES `faccabecera` WRITE;
/*!40000 ALTER TABLE `faccabecera` DISABLE KEYS */;
INSERT INTO `faccabecera` VALUES (1,1,1,1,'0000-00-00 00:00:00',12.00,120.00,132.00,'1'),(2,1,1,1,'2020-07-06 00:00:00',12.00,120.00,132.00,'1'),(3,1,1,1,'2020-07-06 00:00:00',12.00,120.00,132.00,'1'),(4,1,1,1,'2007-07-20 00:00:00',21.60,120.00,141.60,'1'),(5,1,1,1,'2007-07-20 00:00:00',21.60,120.00,141.60,'1'),(6,1,1,1,'2007-07-20 00:00:00',21.60,120.00,141.60,'1'),(7,1,1,1,'2007-07-20 00:00:00',0.00,200.00,200.00,'1'),(8,1,1,1,'2020-07-06 00:00:00',12.00,120.00,132.00,'1'),(9,1,1,1,'2007-07-20 00:00:00',21.60,120.00,141.60,'1'),(10,1,1,1,'2007-07-20 00:00:00',21.60,120.00,141.60,'1'),(11,1,1,1,'2007-07-20 00:00:00',0.00,100.00,100.00,'1'),(12,1,1,1,'2007-07-20 00:00:00',0.00,100.00,100.00,'1');
/*!40000 ALTER TABLE `faccabecera` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-07  2:28:10
