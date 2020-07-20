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
-- Table structure for table `facdetalle`
--

DROP TABLE IF EXISTS `facdetalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facdetalle` (
  `idfacDetalle` int NOT NULL AUTO_INCREMENT,
  `idfacCabecera` int NOT NULL,
  `idproducto` int NOT NULL,
  `cantFacDetalle` int NOT NULL,
  `valorFacDetalle` decimal(18,2) NOT NULL,
  PRIMARY KEY (`idfacDetalle`),
  KEY `fk_facDetalle_facCabecera_idx` (`idfacCabecera`),
  KEY `fk_facDetalle_productos1_idx` (`idproducto`),
  CONSTRAINT `fk_facDetalle_facCabecera` FOREIGN KEY (`idfacCabecera`) REFERENCES `faccabecera` (`idfacCabecera`),
  CONSTRAINT `fk_facDetalle_productos1` FOREIGN KEY (`idproducto`) REFERENCES `productos` (`idproducto`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facdetalle`
--

LOCK TABLES `facdetalle` WRITE;
/*!40000 ALTER TABLE `facdetalle` DISABLE KEYS */;
INSERT INTO `facdetalle` VALUES (1,1,1,1,100.00),(2,2,1,1,100.00),(5,3,1,1,100.00),(8,5,1,1,100.00),(19,12,1,1,100.00);
/*!40000 ALTER TABLE `facdetalle` ENABLE KEYS */;
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
