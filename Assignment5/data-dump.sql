-- MySQL dump 10.13  Distrib 26.10.0, for macos15 (arm64)
--
-- Host: localhost    Database: Rideshare
-- ------------------------------------------------------
-- Server version	26.10.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'd98d0886-ce75-11f1-9b8f-d42a552cdbc7:1-128';

--
-- Table structure for table `Driver`
--

DROP TABLE IF EXISTS `Driver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Driver` (
  `DriverID` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(255) NOT NULL,
  `mode` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`DriverID`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Driver`
--

LOCK TABLES `Driver` WRITE;
/*!40000 ALTER TABLE `Driver` DISABLE KEYS */;
INSERT INTO `Driver` VALUES (1,'kycabrera','kycabrera',0),(2,'happymax','max101',1),(3,'happydriver','1234',1),(5,'bossbaby','people',1),(6,'party2000','livinlife',0),(7,'hanginaround','dawg',1);
/*!40000 ALTER TABLE `Driver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ride`
--

DROP TABLE IF EXISTS `Ride`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ride` (
  `RideID` int NOT NULL AUTO_INCREMENT,
  `DriverID` int NOT NULL,
  `RiderID` int NOT NULL,
  `Rating` int DEFAULT NULL,
  `Origin` varchar(100) NOT NULL,
  `Destination` varchar(100) NOT NULL,
  `RideDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`RideID`),
  KEY `DriverID` (`DriverID`),
  KEY `RiderID` (`RiderID`),
  CONSTRAINT `ride_ibfk_1` FOREIGN KEY (`DriverID`) REFERENCES `Driver` (`DriverID`),
  CONSTRAINT `ride_ibfk_2` FOREIGN KEY (`RiderID`) REFERENCES `Rider` (`RiderID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ride`
--

LOCK TABLES `Ride` WRITE;
/*!40000 ALTER TABLE `Ride` DISABLE KEYS */;
INSERT INTO `Ride` VALUES (1,3,2,NULL,'Panther Village','Irvine Lecture Hall','2026-11-09 22:19:18'),(2,1,1,5,'San Clemente','Irvine','2026-11-10 12:38:05'),(3,2,2,5,'Orange','SC','2026-11-10 12:38:05'),(4,1,2,5,'Fallbrook','Temecula','2026-11-10 12:38:05'),(5,3,3,NULL,'California','Texas','2026-11-10 12:38:05'),(6,7,6,NULL,'California','Texas','2026-11-10 12:47:28');
/*!40000 ALTER TABLE `Ride` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rider`
--

DROP TABLE IF EXISTS `Rider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Rider` (
  `RiderID` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`RiderID`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rider`
--

LOCK TABLES `Rider` WRITE;
/*!40000 ALTER TABLE `Rider` DISABLE KEYS */;
INSERT INTO `Rider` VALUES (1,'dsivgna','sonvbods'),(2,'fleetwoodmac','silverspring'),(3,'rapunzel','frying_pan'),(4,'moana','boat_snack'),(5,'pocahontas','colors'),(6,'hellokitty','sanrio');
/*!40000 ALTER TABLE `Rider` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-10 15:33:27
