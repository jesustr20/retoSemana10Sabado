-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: bodega
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `bill` (
  `bill_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `invIdenti` int(11) NOT NULL,
  `unitePrice` double(8,2) NOT NULL,
  `igv` double(8,2) NOT NULL,
  `totalPrice` double(8,2) NOT NULL,
  `created_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`bill_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `company` (
  `company_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `ruc` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `created_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'123456789','Carmen Happy','Villa maria','2019-10-21 09:24:39.829947','2019-10-21 14:39:31.505948'),(2,'01234567','SostSac S.A.C','Miraflores','2019-10-21 20:23:54.069243','2019-10-22 02:39:36.123033');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migrations`
--

DROP TABLE IF EXISTS `migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `migrations` (
  `migration` varchar(255) NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migrations`
--

LOCK TABLES `migrations` WRITE;
/*!40000 ALTER TABLE `migrations` DISABLE KEYS */;
INSERT INTO `migrations` VALUES ('2019_10_21_043624_create_company_table',1),('2019_10_21_043643_create_role_table',1),('2019_10_21_043657_create_users_table',1),('2019_10_21_043908_create_rocous_table',1),('2019_10_22_002946_create_product_table',2),('2019_10_22_003001_create_bill_table',2),('2019_10_22_003035_create_product_bill_table',2);
/*!40000 ALTER TABLE `migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `product` (
  `product_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `price` double(8,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  `created_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_bill`
--

DROP TABLE IF EXISTS `product_bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `product_bill` (
  `Product_bill_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `bill_id` int(11) NOT NULL,
  `created_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`Product_bill_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_bill`
--

LOCK TABLES `product_bill` WRITE;
/*!40000 ALTER TABLE `product_bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rocous`
--

DROP TABLE IF EXISTS `rocous`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `rocous` (
  `ro_co_us_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `company_id` int(11) NOT NULL,
  `users_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `created_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`ro_co_us_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rocous`
--

LOCK TABLES `rocous` WRITE;
/*!40000 ALTER TABLE `rocous` DISABLE KEYS */;
INSERT INTO `rocous` VALUES (1,1,1,1,'2019-10-21 10:20:21.892102','2019-10-22 03:01:33.503383'),(2,1,2,2,'2019-10-21 20:26:44.075966','2019-10-22 03:04:50.009623'),(3,1,3,2,'2019-10-21 22:07:59.312450','2019-10-21 22:07:59.312450'),(4,1,4,3,'2019-10-21 22:08:22.160757','2019-10-21 22:08:22.160757'),(5,1,5,3,'2019-10-21 22:08:32.822367','2019-10-21 22:08:32.822367'),(6,2,6,1,'2019-10-21 22:39:54.924017','2019-10-21 22:39:54.924017'),(7,2,7,2,'2019-10-21 22:40:08.235778','2019-10-21 22:40:08.235778'),(8,2,8,2,'2019-10-21 22:40:12.061997','2019-10-21 22:40:12.061997'),(9,2,9,3,'2019-10-21 22:40:18.156346','2019-10-21 22:40:18.156346'),(10,2,10,3,'2019-10-21 22:40:21.612543','2019-10-21 22:40:21.612543');
/*!40000 ALTER TABLE `rocous` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `role` (
  `role_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `created_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'Gerente','0','2019-10-21 09:52:00.409782','2019-10-21 14:58:19.464463'),(2,'Supervisor','1','2019-10-21 09:52:15.712658','2019-10-21 09:52:15.712658'),(3,'Usuario','2','2019-10-21 09:53:30.116913','2019-10-21 09:53:30.116913');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `users_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `created_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`users_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Carmen','Rodas','carmen@tiendas.pe','$2b$12$8nuHFuUxsD5UPDxG6eQWuudkPCqhna1BipeUs4KjXRgRTWX7vLmoK','activo','2019-10-21 10:08:05.795999','2019-10-22 02:42:26.801795'),(2,'Jesus','Tuesta','jesus@tiendas.pe','$2b$12$IVZcx.d3KSamniaRf4AtuOwWGmF3BZqntphfqMlYj1r/A4ZaJcmO2','activo','2019-10-21 20:12:35.022403','2019-10-22 02:42:46.492922'),(3,'Jesus','Roncal','jroncal@tiendas.pe','$2b$12$.sv78pEYYNBQj8qHvIE3T.8HEeqkVJszVTvGzydhWCWHZnN6Bl.Ga','activo','2019-10-21 21:43:22.710993','2019-10-21 21:43:22.710993'),(4,'Magaly','Churata','mchurata@tiendas.pe','$2b$12$4fqSLsDpbJCHi6aiNq0h.uWQMM5NjoE.wkP2YsvlfWEIZEKxgOE16','activo','2019-10-21 21:43:51.591645','2019-10-21 21:43:51.591645'),(5,'kiara','sanchez','ksanchez@tiendas.pe','$2b$12$o8tjvXf2CphfT8hYq8idpeEXYchvHoWVcgyGv9wVeyS47dXYEz2ku','activo','2019-10-21 21:44:43.939639','2019-10-21 21:44:43.939639'),(6,'miguel','cervantez','mcervantez@sost.pe','$2b$12$2i9jsFxogEYSWuU9kAC/B.J5rthA931sa86.q0DLcO3XBPmv46Tgu','activo','2019-10-21 22:33:13.943082','2019-10-21 22:33:13.943082'),(7,'marcos','gonzales','mgonzales@sost.pe','$2b$12$ljSEQt6rLRaEz3njM6RG.e5vhJkKUWbxJDQrl83XSqoztnFG9gS..','activo','2019-10-21 22:33:33.320190','2019-10-21 22:33:33.320190'),(8,'mario','vargas','mvargas@sost.pe','$2b$12$aJbuL5hAAiC6GJV0Wib1.e8S96h.6Dnnc0wDAzzHRvU8xo73ihZWu','activo','2019-10-21 22:37:05.056301','2019-10-21 22:37:05.056301'),(9,'erick','rojas','erojas@sost.pe','$2b$12$d.GvkhB.F57Tx8RYmA1/eeLNN9CzAofdzC7dmR.N6RmaKK2XHR75C','activo','2019-10-21 22:37:23.512357','2019-10-21 22:37:23.512357'),(10,'maria','fernandez','mfernandez@sost.pe','$2b$12$6NkELzGFTulhHQSMfcNwsuDl.43/IYcJLL8d7QFnMYeVGIGt7s3ni','activo','2019-10-21 22:37:48.506786','2019-10-21 22:37:48.506786');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-21 19:41:53
