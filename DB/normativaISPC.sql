CREATE DATABASE  IF NOT EXISTS `normativasispc` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `normativasispc`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: normativasispc
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorias` (
  `id_categoria` int NOT NULL,
  `nombre` varchar(20) NOT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (1,'LABORAL'),(2,'PENAL'),(3,'CIVIL'),(4,'COMERCIAL'),(5,'FAMILIA Y SUCESIONES'),(6,'AGRARIO Y AMBIENTAL'),(7,'MINERO'),(8,'DERECHO INFORMATICO');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jurisdicciones`
--

DROP TABLE IF EXISTS `jurisdicciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jurisdicciones` (
  `id_jurisdiccion` int NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `organo_legislativo` varchar(50) NOT NULL,
  PRIMARY KEY (`id_jurisdiccion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jurisdicciones`
--

LOCK TABLES `jurisdicciones` WRITE;
/*!40000 ALTER TABLE `jurisdicciones` DISABLE KEYS */;
INSERT INTO `jurisdicciones` VALUES (1,'NACIONAL','CONGRESO NACIONAL'),(2,'PROVINCIAL','LEGISLATURA PROVINCIAL');
/*!40000 ALTER TABLE `jurisdicciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leyes`
--

DROP TABLE IF EXISTS `leyes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leyes` (
  `id_leyes` int NOT NULL,
  `numero_registro` varchar(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `categoria` int DEFAULT NULL,
  `numero_normativa` varchar(50) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `jurisdiccion` int DEFAULT NULL,
  `tipo_normativa` int DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `palabra_clave` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_leyes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leyes`
--

LOCK TABLES `leyes` WRITE;
/*!40000 ALTER TABLE `leyes` DISABLE KEYS */;
INSERT INTO `leyes` VALUES (1,'1','Ley de Contrato de Trabajo',1,'20.744','2021-01-01',1,1,'Contrato, Trabajo','Contrato, Trabajo'),(2,'2','Ley De Teletrabajo',1,'27.555','2022-02-01',1,1,'Teletrabajo','Teletrabajo'),(3,'3','Ley de Ejercicio Prof.de la InformÃ¡tica en Cba.',8,'7642','2023-03-01',2,1,'InformÃ¡tica, Ejercicio Profesional','InformÃ¡tica, Ejercicio Profesional');
/*!40000 ALTER TABLE `leyes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipos`
--

DROP TABLE IF EXISTS `tipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipos` (
  `id_tipo` int NOT NULL,
  `nombre` varchar(20) NOT NULL,
  PRIMARY KEY (`id_tipo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos`
--

LOCK TABLES `tipos` WRITE;
/*!40000 ALTER TABLE `tipos` DISABLE KEYS */;
INSERT INTO `tipos` VALUES (1,'LEY'),(2,'DECRETO'),(3,'RESOLUCIÃ“N');
/*!40000 ALTER TABLE `tipos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

