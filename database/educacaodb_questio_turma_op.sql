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
-- Table structure for table `questio_turma_op`
--

DROP TABLE IF EXISTS `questio_turma_op`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questio_turma_op` (
  `idquestio_turma_op` int(11) NOT NULL AUTO_INCREMENT,
  `idquestionario_turma` int(11) DEFAULT NULL,
  `idquestionario` int(11) DEFAULT NULL,
  `idopcoes` int(11) DEFAULT NULL,
  PRIMARY KEY (`idquestio_turma_op`),
  KEY `fk_quest_turma_op_turma_idx` (`idquestionario_turma`),
  KEY `fk_quest_turma_op_opcoes_idx` (`idopcoes`),
  KEY `fk_quest_turma_op_questionario_idx` (`idquestionario`),
  CONSTRAINT `fk_quest_turma_op_opcoes` FOREIGN KEY (`idopcoes`) REFERENCES `opcoes` (`idopcoes`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_quest_turma_op_questionario` FOREIGN KEY (`idquestionario`) REFERENCES `questionario` (`idquestionario`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_quest_turma_op_turma` FOREIGN KEY (`idquestionario_turma`) REFERENCES `questionario_turma` (`idquestionario_turma`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=685 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-03 23:17:00
