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
-- Table structure for table `questionario_grupo`
--

DROP TABLE IF EXISTS `questionario_grupo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionario_grupo` (
  `idquestionario_grupo` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(250) DEFAULT NULL,
  `detalhamento` varchar(4000) DEFAULT NULL,
  PRIMARY KEY (`idquestionario_grupo`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionario_grupo`
--

LOCK TABLES `questionario_grupo` WRITE;
/*!40000 ALTER TABLE `questionario_grupo` DISABLE KEYS */;
INSERT INTO `questionario_grupo` VALUES (1,'Professor incentiva o protagonismo juvenil?','Estudantes que são estimulados a desenvolver o protagonismo enfrentam melhor problemas do cotidiano e de sua vida, estão mais preparados para enfrentar o futuro e serem protagonistas da sua própria história, atuando em papéis fundamentais dentro da sociedade. Conhecer a sua identidade contribui na construção do seu Projeto de Vida e apoiar o autoconhecimento é a chave para a concretização do projeto.'),(2,'Professor possui bom relacionamento com a turma?','Quando há uma boa relação de professor e aluno, ambos os lados estão em sintonia e motivados, o aluno também motiva o professor quando é desafiado a investigar e buscar novas soluções para a aula e o professor traz novas experiências que desafia e estimula a turma, criando um laço e uma sintonia de aprendizagem, é preciso estabelecer um bom relacionamento de professor e aluno, em que todos tenham vez e voz, todos sejam ouvidos para contribuir no crescente aprendizado.  '),(3,'Professor domina a matéria que atua','É fundamental que o professor conheça a sua turma e elabore um plano de trabalho no intuito de facilitar as dificuldades encontradas no dia-a-dia da sala de aula, apresentar um bom domínio da matéria facilita a transmitir o conteúdo a ser trabalhado, fundamentar um bom plano que realmente possa apoiar o professor na tomada de decisão pode proporcionar melhor desempenho dos alunos.'),(4,'Oferece aulas diversificadas','Novas abordagens podem preparar o aluno para o futuro pois ele passa a se adaptar a novas situações de maneira criativa, abordar o mesmo assunto em diferentes linguagens combinados com inovação contribui para uma melhor compreensão podendo atrair a atenção dos alunos em sala de aula. '),(5,'Possui hábitos de leitura','O hábito da leitura pode ser benéfico não apenas para estudos de textos e palavras, o benefício pode ser estendido também a outras áreas que não tem relação com a literatura, pois este hábito auxilia na concentração, compreensão e outras habilidades que podem ser adquiridas através da leitura. Diversificar formas de informação e práticas de leitura auxiliam construtivamente e complementam o ensino e aprendizado. Adquirir novos hábitos estimulam e favorecem o desenvolvimento de habilidades ou as aprimora. Incentivar essas práticas ajuda no desenvolvimento cognitivo ao aluno, com percepção mais ampla, memória e raciocínio, tornando mais fácil a absorção das demais informações passadas tanto em sala de aula como em hábitos de leituras e pesquisas.'),(6,'Afinidade com matéria relacionada a área de:','Um bom desempenho dos alunos em algumas áreas pode ser devido combinação dos fatores de afinidade e prazer, pois a aula se torna muito mais prazerosa quando lecionada com qualidade, o desprazer pode estar relacionado com algum trauma tido no passado com a matéria e haver certos bloqueios, como também pode ser pouco entusiasmo do professor, que não conseguir relacionar a matéria com situações cotidianas da vida ocasionando insatisfação da turma com a área.'),(7,'A escola oferece ambiente confortável?','Um espaço físico adequado cria um ambiente envolvente e acolhedor, o que facilita e estimula, comprovadamente, o desenvolvimento e engajamento do aluno em sala de aula. Dando suporte favorável às práticas escolares auxiliando para que os alunos mantenham foco e atenção às aulas.'),(8,'Defasagem escolar','Dentre várias causas da defasagem abordaremos apenas temas já somos familiarizados, como a dificuldade em que alguns alunos tem em acompanhar a matéria, as vezes devido a faltas recorrentes ou por motivos específicos não detectados e a escola não obteve conhecimento, é preciso analisar caso a caso afim de conseguir minimizar barreira que impeçam o aluno de acompanhar a aula.');
/*!40000 ALTER TABLE `questionario_grupo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-03 23:17:00
