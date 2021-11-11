CREATE DATABASE `educacaodb` /*!40100 DEFAULT CHARACTER SET latin1 */;

CREATE TABLE `consulta_caed` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recuperacao_continuada` varchar(45) DEFAULT NULL,
  `ano` int(11) DEFAULT NULL,
  `materia` varchar(45) DEFAULT NULL,
  `turma` varchar(45) DEFAULT NULL,
  `serie` int(11) DEFAULT NULL,
  `bimestre` int(11) DEFAULT NULL,  
  `estudante` varchar(250) DEFAULT NULL,  
  `participacao` varchar(45) DEFAULT NULL,
  `numero_itens_respondidos` varchar(45) DEFAULT NULL,
  `porcento_acertos` varchar(45) DEFAULT NULL,
  `categoria_desempenho` varchar(45) DEFAULT NULL,
  `tipo_intervencao` varchar(45) DEFAULT NULL,
  `itens_acertados` varchar(45) DEFAULT NULL,
  `h_01` varchar(45) DEFAULT NULL,
  `h_02` varchar(45) DEFAULT NULL,
  `h_03` varchar(45) DEFAULT NULL,
  `h_04` varchar(45) DEFAULT NULL,
  `h_05` varchar(45) DEFAULT NULL,
  `h_06` varchar(45) DEFAULT NULL,
  `h_07` varchar(45) DEFAULT NULL,
  `h_08` varchar(45) DEFAULT NULL,
  `h_09` varchar(45) DEFAULT NULL,
  `h_10` varchar(45) DEFAULT NULL,
  `h_11` varchar(45) DEFAULT NULL,
  `h_12` varchar(45) DEFAULT NULL,
  `h_13` varchar(45) DEFAULT NULL,
  `h_14` varchar(45) DEFAULT NULL,
  `h_15` varchar(45) DEFAULT NULL,
  `h_16` varchar(45) DEFAULT NULL,
  `h_17` varchar(45) DEFAULT NULL,
  `h_18` varchar(45) DEFAULT NULL,
  `h_19` varchar(45) DEFAULT NULL,
  `h_20` varchar(45) DEFAULT NULL,
  `h_21` varchar(45) DEFAULT NULL,
  `h_22` varchar(45) DEFAULT NULL,
  `h_23` varchar(45) DEFAULT NULL,
  `h_24` varchar(45) DEFAULT NULL,
  `h_25` varchar(45) DEFAULT NULL,
  `h_26` varchar(45) DEFAULT NULL,
  `h_27` varchar(45) DEFAULT NULL,
  `h_28` varchar(45) DEFAULT NULL,
  `h_29` varchar(45) DEFAULT NULL,
  `h_30` varchar(45) DEFAULT NULL,   
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `habilidade_caed` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ano` int(11) DEFAULT NULL,
  `materia` varchar(45) DEFAULT NULL,
  `turma` varchar(45) DEFAULT NULL,
  `serie` int(11) DEFAULT NULL,
  `bimestre` int(11) DEFAULT NULL,  
  `questao` varchar(45) DEFAULT NULL,  
  `cod_da_habilidade` varchar(45) DEFAULT NULL,   
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

