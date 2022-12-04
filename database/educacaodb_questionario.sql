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
-- Table structure for table `questionario`
--

DROP TABLE IF EXISTS `questionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionario` (
  `idquestionario` int(11) NOT NULL AUTO_INCREMENT,
  `ordem` int(11) DEFAULT NULL,
  `pergunta` varchar(250) DEFAULT NULL,
  `idquestionario_grupo` int(11) DEFAULT NULL,
  PRIMARY KEY (`idquestionario`),
  KEY `fk_questionario_questio_grupo_idx` (`idquestionario_grupo`),
  CONSTRAINT `fk_questionario_questio_grupo` FOREIGN KEY (`idquestionario_grupo`) REFERENCES `questionario_grupo` (`idquestionario_grupo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionario`
--

LOCK TABLES `questionario` WRITE;
/*!40000 ALTER TABLE `questionario` DISABLE KEYS */;
INSERT INTO `questionario` VALUES (1,1,'O(a) Professor(a) procura lhe conhecer e o(a) incentiva no autoconhecimento, saber sobre seus projetos de vida, seus interesses, seus pontos fortes e no que eles precisam melhorar?',1),(2,2,'O(a) Professor(a) incentiva o  protagonismo em suas vidas, lhes ajudando, tanto em questões escolares, quanto em outras dimensões de suas vidas?',1),(3,3,'O(a) Professor(a) atua como um modelo a ser seguido?',2),(4,4,'O(a) Professor(a) é disponível para lhe atender e aos seus familiares ou responsáveis, incentivando a participação na aprendizagem e no desenvolvimento dos seus projetos de vida?',1),(5,5,'O(a) Professor(a) busca assuntos que se relacionem com aspectos de seus interesses para potencializar as aprendizagens?',3),(6,6,'O(a) Professor(a) é didático em suas orientações?',3),(7,7,'O(a) Professor(a) busca por novos saberes e práticas de forma a melhorar continuadamente seus fazeres como docente?',4),(8,8,'O(a) Professor(a) demonstra domínio do conteúdo que é apresentado em sala de aula?',3),(9,9,'O(a) Professor(a) executa com atençao suas dúvidas e ações?',2),(10,10,'O(a) Professor(a) se relaciona de forma positiva com os estudantes?',2),(11,11,'O(a) Professor(a) procura conhecer as experiências e conhecimentos dos estudantes, incentivando a melhoreia no aprendizado individual?',2),(12,12,'O(a) Professor(a) desenvolve estratégias inovadoras de ensino favorecendo as aprendizagens?',4),(13,13,'Você já reprovou alguma vez?',8),(14,14,'Você tem hábito de ler artigos na internet, jornais ou revistas?',5),(15,15,' Excetuando os livros escolares, quantos livros você lê por ano?',5),(16,16,'Que profissão você escolheu ou pretende seguir?',6),(17,17,'Sua sala possui uma boa ventilação?',7),(18,18,'Sua sala possui uma boa iluminação?',7),(19,19,'Dispõe de carteiras em número compatível com a quantidade de alunos?',7);
/*!40000 ALTER TABLE `questionario` ENABLE KEYS */;
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
