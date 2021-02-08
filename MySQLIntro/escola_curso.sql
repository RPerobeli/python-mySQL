-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: escola_curso
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `alunos`
--

DROP TABLE IF EXISTS `alunos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alunos` (
  `idAluno` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `dataNascimento` date NOT NULL,
  `endereco` varchar(255) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  PRIMARY KEY (`idAluno`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunos`
--

LOCK TABLES `alunos` WRITE;
/*!40000 ALTER TABLE `alunos` DISABLE KEYS */;
INSERT INTO `alunos` VALUES (1,'Rodrigo','1997-05-02','Av. Barao do Rio Branco, 907','12345678901'),(3,'Diego','1987-07-17','Av. Ibitiguaia','01234567891'),(4,'Fliper Ama','1984-05-02','Av. Carlos Comodoro','01234567891'),(5,'Joao Paulo','2000-07-03','Rua Bonfim','00011122234'),(6,'Vinicius Paulo','2001-07-03','Rua ComeçoRuim','00011122235');
/*!40000 ALTER TABLE `alunos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alunos_cursos`
--

DROP TABLE IF EXISTS `alunos_cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alunos_cursos` (
  `idAlunosCursos` int NOT NULL AUTO_INCREMENT,
  `idAluno` int NOT NULL,
  `idCurso` int NOT NULL,
  PRIMARY KEY (`idAlunosCursos`),
  KEY `fkIdAluno_idx` (`idAluno`),
  KEY `fkIdCurso_idx` (`idCurso`),
  CONSTRAINT `fkIdAluno` FOREIGN KEY (`idAluno`) REFERENCES `alunos` (`idAluno`),
  CONSTRAINT `fkIdCurso` FOREIGN KEY (`idCurso`) REFERENCES `cursos` (`idCurso`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunos_cursos`
--

LOCK TABLES `alunos_cursos` WRITE;
/*!40000 ALTER TABLE `alunos_cursos` DISABLE KEYS */;
INSERT INTO `alunos_cursos` VALUES (25,1,1),(26,1,2),(27,3,1),(28,3,3),(29,4,1),(30,4,2),(31,5,1),(32,6,1);
/*!40000 ALTER TABLE `alunos_cursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cursos`
--

DROP TABLE IF EXISTS `cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cursos` (
  `idCurso` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  PRIMARY KEY (`idCurso`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cursos`
--

LOCK TABLES `cursos` WRITE;
/*!40000 ALTER TABLE `cursos` DISABLE KEYS */;
INSERT INTO `cursos` VALUES (1,'Codeigniter'),(2,'MySQL'),(3,'Python');
/*!40000 ALTER TABLE `cursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notas`
--

DROP TABLE IF EXISTS `notas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notas` (
  `idNota` int NOT NULL AUTO_INCREMENT,
  `idAlunoCurso` int NOT NULL,
  `descricao` varchar(255) NOT NULL,
  `nota` decimal(5,2) NOT NULL,
  PRIMARY KEY (`idNota`),
  KEY `fkIdAlunCurso_idx` (`idAlunoCurso`),
  CONSTRAINT `fkIdAlunCurso` FOREIGN KEY (`idAlunoCurso`) REFERENCES `alunos_cursos` (`idAlunosCursos`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notas`
--

LOCK TABLES `notas` WRITE;
/*!40000 ALTER TABLE `notas` DISABLE KEYS */;
INSERT INTO `notas` VALUES (8,25,'prova 1',28.00),(9,27,'prova 1',25.00),(10,29,'prova 1',28.00),(11,26,'exercicio 1',10.00),(12,30,'exercicio 2',12.00),(13,25,'prova 2',22.00),(14,26,'prova 2',20.00);
/*!40000 ALTER TABLE `notas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-08 17:08:07
