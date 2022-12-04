-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: educacaodb
-- ------------------------------------------------------
-- Server version	5.7.40-log

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
-- Table structure for table `opcoes`
--

DROP TABLE IF EXISTS `opcoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `opcoes` (
  `idopcoes` int(11) NOT NULL AUTO_INCREMENT,
  `idquestionario` int(11) NOT NULL,
  `ordem` int(11) DEFAULT NULL,
  `letra` varchar(1) DEFAULT NULL,
  `item` varchar(250) DEFAULT NULL,
  `item_resultado` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`idopcoes`),
  KEY `fk_quest_ops_idx` (`idquestionario`),
  CONSTRAINT `fk_quest_ops` FOREIGN KEY (`idquestionario`) REFERENCES `questionario` (`idquestionario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=317 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opcoes`
--

LOCK TABLES `opcoes` WRITE;
/*!40000 ALTER TABLE `opcoes` DISABLE KEYS */;
INSERT INTO `opcoes` VALUES (246,1,1,'A','SEMPRE',NULL),(247,1,2,'B','QUASE SEMPRE',NULL),(248,1,3,'C','ÀS VEZES',NULL),(249,1,4,'D','RARAMENTE',NULL),(250,2,1,'A','SEMPRE',NULL),(251,2,2,'B','QUASE SEMPRE',NULL),(252,2,3,'C','ÀS VEZES',NULL),(253,2,4,'D','RARAMENTE',NULL),(254,3,1,'A','SEMPRE',NULL),(255,3,2,'B','QUASE SEMPRE',NULL),(256,3,3,'C','ÀS VEZES',NULL),(257,3,4,'D','RARAMENTE',NULL),(258,4,1,'A','SEMPRE',NULL),(259,4,2,'B','QUASE SEMPRE',NULL),(260,4,3,'C','ÀS VEZES',NULL),(261,4,4,'D','RARAMENTE',NULL),(262,5,1,'A','SEMPRE',NULL),(263,5,2,'B','QUASE SEMPRE',NULL),(264,5,3,'C','ÀS VEZES',NULL),(265,5,4,'D','RARAMENTE',NULL),(266,6,1,'A','SEMPRE',NULL),(267,6,2,'B','QUASE SEMPRE',NULL),(268,6,3,'C','ÀS VEZES',NULL),(269,6,4,'D','RARAMENTE',NULL),(270,7,1,'A','SEMPRE',NULL),(271,7,2,'B','QUASE SEMPRE',NULL),(272,7,3,'C','ÀS VEZES',NULL),(273,7,4,'D','RARAMENTE',NULL),(274,8,1,'A','SEMPRE',NULL),(275,8,2,'B','QUASE SEMPRE',NULL),(276,8,3,'C','ÀS VEZES',NULL),(277,8,4,'D','RARAMENTE',NULL),(278,9,1,'A','SEMPRE',NULL),(279,9,2,'B','QUASE SEMPRE',NULL),(280,9,3,'C','ÀS VEZES',NULL),(281,9,4,'D','RARAMENTE',NULL),(282,10,1,'A','SEMPRE',NULL),(283,10,2,'B','QUASE SEMPRE',NULL),(284,10,3,'C','ÀS VEZES',NULL),(285,10,4,'D','RARAMENTE',NULL),(286,11,1,'A','SEMPRE',NULL),(287,11,2,'B','QUASE SEMPRE',NULL),(288,11,3,'C','ÀS VEZES',NULL),(289,11,4,'D','RARAMENTE',NULL),(290,12,1,'A','SEMPRE',NULL),(291,12,2,'B','QUASE SEMPRE',NULL),(292,12,3,'C','ÀS VEZES',NULL),(293,12,4,'D','RARAMENTE',NULL),(294,13,1,'A','Nunca ','Pouca defasagem'),(295,13,2,'B','Sim, uma vez.','Pouca defasagem'),(296,13,3,'C','Sim, duas vezes.','Defasagem significativa  '),(297,13,4,'D','Sim, três vezes ou mais','Defasagem significativa  '),(298,14,1,'A','Não','NÃO'),(299,14,2,'B','Ocasionalmente','NÃO'),(300,14,3,'C','Semanalmente','SIM'),(301,14,4,'D','Diariamente','SIM'),(302,15,1,'A','Nenhum','NÃO'),(303,15,2,'B','01 a 02 livros','NÃO'),(304,15,3,'C','03 a 05 livros','SIM'),(305,15,4,'D','Mais de 05 livros','SIM'),(306,16,1,'A','Ainda não escolhi',NULL),(307,16,2,'B','Profissão ligada às Engenharias / Ciências Tecnológicas / Matemáticas',NULL),(308,16,3,'C','Profissão ligada às Ciências Humanas.',NULL),(309,16,4,'D','Profissão ligada às Artes',NULL),(310,16,5,'E','Profissão ligada às Ciências Biológicas e da Saúde',NULL),(311,17,1,'A','SIM',NULL),(312,17,2,'B','NÃO',NULL),(313,18,1,'A','SIM',NULL),(314,18,2,'B','NÃO',NULL),(315,19,1,'A','SIM',NULL),(316,19,2,'B','NÃO',NULL);
/*!40000 ALTER TABLE `opcoes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-03 23:16:59
