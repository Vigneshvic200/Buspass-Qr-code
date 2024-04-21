-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: buspass
-- ------------------------------------------------------
-- Server version	8.2.0

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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-01-24 06:11:31.839903'),(2,'auth','0001_initial','2024-01-24 06:11:32.679171'),(3,'admin','0001_initial','2024-01-24 06:11:32.831194'),(4,'admin','0002_logentry_remove_auto_add','2024-01-24 06:11:32.846817'),(5,'admin','0003_logentry_add_action_flag_choices','2024-01-24 06:11:32.870072'),(6,'contenttypes','0002_remove_content_type_name','2024-01-24 06:11:32.959993'),(7,'auth','0002_alter_permission_name_max_length','2024-01-24 06:11:33.052681'),(8,'auth','0003_alter_user_email_max_length','2024-01-24 06:11:33.074593'),(9,'auth','0004_alter_user_username_opts','2024-01-24 06:11:33.090202'),(10,'auth','0005_alter_user_last_login_null','2024-01-24 06:11:33.160040'),(11,'auth','0006_require_contenttypes_0002','2024-01-24 06:11:33.163032'),(12,'auth','0007_alter_validators_add_error_messages','2024-01-24 06:11:33.175000'),(13,'auth','0008_alter_user_username_max_length','2024-01-24 06:11:33.250700'),(14,'auth','0009_alter_user_last_name_max_length','2024-01-24 06:11:33.342808'),(15,'auth','0010_alter_group_name_max_length','2024-01-24 06:11:33.370353'),(16,'auth','0011_update_proxy_permissions','2024-01-24 06:11:33.370353'),(17,'auth','0012_alter_user_first_name_max_length','2024-01-24 06:11:33.456950'),(18,'passenger','0001_initial','2024-01-24 06:11:33.492726'),(19,'passenger','0002_remove_passenger_email_passenger_city','2024-01-24 06:11:33.540695'),(20,'passes','0001_initial','2024-01-24 06:11:33.577256'),(21,'passes','0002_remove_passes_amount_remove_passes_contact_and_more','2024-01-24 06:11:33.647896'),(22,'passes','0003_alter_passes_table','2024-01-24 06:11:33.667844'),(23,'passes','0004_alter_passes_table','2024-01-24 06:11:33.687088'),(24,'passes','0005_alter_passes_table','2024-01-24 06:11:33.704027'),(25,'sessions','0001_initial','2024-01-24 06:11:33.740872'),(26,'transaction','0001_initial','2024-01-24 06:11:33.788610'),(27,'transaction','0002_alter_transaction_table','2024-01-24 06:11:33.808106');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-13 17:39:42
