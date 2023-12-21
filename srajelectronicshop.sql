/*
SQLyog Community v12.09 (32 bit)
MySQL - 5.1.15-beta-community-nt : Database - srjelectronicshopy
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`srjelectronicshopy` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `srjelectronicshopy`;

/*Table structure for table `addemployee` */

DROP TABLE IF EXISTS `addemployee`;

CREATE TABLE `addemployee` (
  `eid` int(8) unsigned NOT NULL AUTO_INCREMENT,
  `ename` varchar(30) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `apost` varchar(20) DEFAULT NULL,
  `dtime` varchar(15) DEFAULT NULL,
  `contact` decimal(20,0) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `addemployee` */

insert  into `addemployee`(`eid`,`ename`,`address`,`apost`,`dtime`,`contact`,`dob`) values (1,'Suraj Dnyaneshwar Harale','sumangal nagar, vinchur','Manager','8 :00 to 9:00','8766405087','1998-04-16'),(2,'Sachin Sanjay Khaire','Wahegaon sal','Head Of Employee','8:00 to 9:00','9665272940','1998-04-20'),(3,'Umesh Kakade','Dharangaon','Employee','8:00 to 9:00','9763652058','1998-05-23'),(4,'Tushar Kakade','Dharangaon','Employee','8:00 to 9:00','9860372463','1997-02-19'),(5,'Rohit Khaire','Lasalgaon','Employee','8:00 to 9:00','7387883874','1996-06-25');

/*Table structure for table `costomer` */

DROP TABLE IF EXISTS `costomer`;

CREATE TABLE `costomer` (
  `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `date` varchar(20) DEFAULT NULL,
  `cname` varchar(40) DEFAULT NULL,
  `citem` varchar(30) DEFAULT NULL,
  `quantity` int(20) DEFAULT NULL,
  `brand` varchar(20) DEFAULT NULL,
  `price` int(30) DEFAULT NULL,
  `descript` varchar(50) DEFAULT NULL,
  `total` int(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `costomer` */

insert  into `costomer`(`id`,`date`,`cname`,`citem`,`quantity`,`brand`,`price`,`descript`,`total`) values (1,'10-3-2019',' Mr.Swapnil Kulkarni ','LCD',2,'Sony',11000,'32 inches',22000),(2,'10-3-2019',' Mr.Yogesh Pawar','Air Cooler',3,'Bajaj',4000,'3 side cooling pads',12000),(3,'10-3-2019','Mr.Dnyaneshwer Chavhan','Refrigerator',1,'Godrej',15000,'Double Door',15000),(4,'10-3-2019','Mr. Shekhar Dhomse','Microwave Oven',2,'LG',10000,'28 L',20000);

/*Table structure for table `dealer` */

DROP TABLE IF EXISTS `dealer`;

CREATE TABLE `dealer` (
  `id` int(8) unsigned NOT NULL AUTO_INCREMENT,
  `dealername` varchar(30) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `contact` decimal(20,0) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dealer` */

insert  into `dealer`(`id`,`dealername`,`address`,`contact`,`email`) values (1,'Suyog Kolhe','Lasalgaon','9860656278','suyog22544@gmail.com'),(2,'Sachin Harale','Vinchur','8600687129','sachinharale227@gmail.com'),(3,'Parikshit Wagh','Dongargaon','9168293203','pariwagh334412@gmail.com'),(4,'Atul Kahandal','Lasalgaon','9325820682','atulkahandal56@gmail.com');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`) values ('admin','admin'),('suraj','160498');

/*Table structure for table `viewelectronicdetail` */

DROP TABLE IF EXISTS `viewelectronicdetail`;

CREATE TABLE `viewelectronicdetail` (
  `Id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `item` varchar(30) DEFAULT NULL,
  `brand` varchar(20) DEFAULT NULL,
  `price` int(40) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `stock` int(30) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `viewelectronicdetail` */

insert  into `viewelectronicdetail`(`Id`,`item`,`brand`,`price`,`description`,`stock`) values (1,'Refrigerator','Godrej',15000,'Double Door Refrigerator',10),(2,'LCD tv','Sony',11000,'32 inches',20),(3,'Air Cooler','Bajaj',10000,'3side cooling ,dust filter net',8),(4,'Washing Mashine','LG',4000,'semi-automatic top-loading Washing',12),(5,'Microwave Oven','Samsung',10600,'28 L',10);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
