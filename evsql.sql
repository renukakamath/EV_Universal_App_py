/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - ev_universal_app
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ev_universal_app` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `ev_universal_app`;

/*Table structure for table `bunk` */

DROP TABLE IF EXISTS `bunk`;

CREATE TABLE `bunk` (
  `bunk_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`bunk_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `bunk` */

insert  into `bunk`(`bunk_id`,`login_id`,`name`,`place`,`latitude`,`longitude`) values 
(1,13,'yyyff','ghff','9.9763343','76.2861962');

/*Table structure for table `company` */

DROP TABLE IF EXISTS `company`;

CREATE TABLE `company` (
  `company_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `company` */

insert  into `company`(`company_id`,`login_id`,`name`,`place`,`phone`,`email`) values 
(1,16,'reshma','kerala','0987654321','student@gmail.com');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`user_id`,`complaint`,`reply`,`date`) values 
(1,3,'user','ok','2023-01-15'),
(2,6,'boy','pending','2023-01-15'),
(3,13,'bu','pending','2023-01-15'),
(4,14,'me','pending','2023-01-15');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'shhwh','hsywuw','User'),
(2,'hsjw','jeiw','User'),
(14,'me','me','Mechanic'),
(4,'duh','duk','User'),
(5,'user','user','User'),
(6,'boy','boy','Deliveryboy'),
(17,'username','me','mechanic'),
(16,'re','re','company'),
(15,'admin','admin','admin'),
(13,'bu','bu','Bunk'),
(18,'user','usre','mechanic'),
(19,'user','usre','mechanic');

/*Table structure for table `mechanic` */

DROP TABLE IF EXISTS `mechanic`;

CREATE TABLE `mechanic` (
  `mechanic_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`mechanic_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `mechanic` */

insert  into `mechanic`(`mechanic_id`,`login_id`,`firstname`,`lastname`,`place`,`phone`,`email`,`latitude`,`longitude`) values 
(3,18,'hai','ha','dfsgs','23456789','student@gmail.com','9.980736837129689','76.27720255550476'),
(2,17,'me','me','palakkad','02345678901','me@gmail.com1','9.974678671483936','76.27582926448913'),
(4,19,'hai','ha','dfsgs','23456789','student@gmail.com','9.980736837129689','76.27720255550476');

/*Table structure for table `mechanicrequest` */

DROP TABLE IF EXISTS `mechanicrequest`;

CREATE TABLE `mechanicrequest` (
  `mrequest_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `mechanic_id` int(11) DEFAULT NULL,
  `servicceamount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`mrequest_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `mechanicrequest` */

insert  into `mechanicrequest`(`mrequest_id`,`user_id`,`mechanic_id`,`servicceamount`,`date`,`status`) values 
(1,3,1,'0','2023-01-15','canceled'),
(2,3,1,'100','2023-01-15','Accept');

/*Table structure for table `oderdetails` */

DROP TABLE IF EXISTS `oderdetails`;

CREATE TABLE `oderdetails` (
  `detail_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`detail_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `oderdetails` */

insert  into `oderdetails`(`detail_id`,`order_id`,`product_id`,`quantity`,`amount`,`date`) values 
(1,1,1,'3','15000','2023-01-15');

/*Table structure for table `order` */

DROP TABLE IF EXISTS `order`;

CREATE TABLE `order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `sparepart_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `order` */

insert  into `order`(`order_id`,`sparepart_id`,`user_id`,`total`,`status`) values 
(1,1,3,'15000','Delivery');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `requested_id` int(11) DEFAULT NULL,
  `requestedfor` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`requested_id`,`requestedfor`,`amount`,`date`) values 
(1,1,'request','5000','2023-01-14'),
(2,1,'request','5000','2023-01-14'),
(3,1,'request','5000','2023-01-14'),
(4,2,'request','5000','2023-01-14'),
(5,2,'request','5000','2023-01-14'),
(6,2,'request','5000','2023-01-14'),
(7,3,'request','5000','2023-01-14'),
(8,3,'request','5000','2023-01-14'),
(9,3,'request','5000','2023-01-14'),
(10,3,'request','5000','2023-01-14'),
(11,3,'request','5000','2023-01-14'),
(12,3,'request','5000','2023-01-14'),
(13,3,'request','5000','2023-01-14'),
(14,3,'request','5000','2023-01-14'),
(15,3,'request','5000','2023-01-14'),
(16,3,'request','5000','2023-01-14'),
(17,3,'request','5000','2023-01-14'),
(18,3,'request','5000','2023-01-14'),
(19,3,'request','5000','2023-01-14'),
(20,10,'request','5000','2023-01-15'),
(21,1,'Productbooking','15000','2023-01-15'),
(22,1,'Productbooking','15000','2023-01-15'),
(23,1,'Productbooking','15000','2023-01-15');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `sparepart_id` int(11) DEFAULT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  `stock` varchar(100) DEFAULT NULL,
  `rate` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`sparepart_id`,`product_name`,`image`,`stock`,`rate`) values 
(1,1,'product','uploads/images_63688fffe4e3c.jfif','500','5000'),
(2,6,'shoe','static/uploads/3a23c326-3d39-4ba1-bed1-2e41b5ecc4ccabc.jpg','500','2000');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `requested_id` int(11) DEFAULT NULL,
  `rating` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`user_id`,`requested_id`,`rating`,`date`) values 
(1,3,3,'2.0','2023-01-14'),
(2,3,3,'2.0','2023-01-14'),
(3,3,3,'2.0','2023-01-14'),
(4,3,3,'2.0','2023-01-14'),
(5,3,3,'2.0','2023-01-14'),
(6,3,3,'2.0','2023-01-14'),
(7,3,3,'2.0','2023-01-14'),
(8,3,1,'2.0','2023-01-15'),
(9,3,1,'4.0','2023-01-15'),
(10,3,1,'5.0','2023-01-15');

/*Table structure for table `rechargerequest` */

DROP TABLE IF EXISTS `rechargerequest`;

CREATE TABLE `rechargerequest` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `bunk_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `rechargerequest` */

insert  into `rechargerequest`(`request_id`,`user_id`,`bunk_id`,`amount`,`date`,`status`) values 
(1,3,1,'100','2023-01-15','Requested');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`request_id`,`vehicle_id`,`user_id`,`amount`,`date`,`status`) values 
(1,1,3,'5000','2023-01-14','deliver'),
(2,1,3,'5000','2023-01-14','Paid'),
(3,1,3,'5000','2023-01-14','Paid'),
(4,1,3,'5000','2023-01-14','Pending'),
(5,1,3,'5000','2023-01-14','Pending'),
(6,1,3,'5000','2023-01-14','Pending'),
(7,1,3,'5000','2023-01-14','Pending'),
(8,1,3,'5000','2023-01-14','Pending'),
(9,1,3,'5000','2023-01-14','Pending'),
(10,1,3,'5000','2023-01-15','Paid');

/*Table structure for table `sparepart` */

DROP TABLE IF EXISTS `sparepart`;

CREATE TABLE `sparepart` (
  `sparepart_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sparepart_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `sparepart` */

insert  into `sparepart`(`sparepart_id`,`login_id`,`firstname`,`lastname`,`place`,`phone`,`email`,`latitude`,`longitude`) values 
(1,6,'boy','boy','Ernakulam ','23685699','fchjj@ghhbjj','9.9762897','76.2862164');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`first_name`,`last_name`,`place`,`phone`,`email`,`latitude`,`longitude`) values 
(1,3,'dfhjkds','dfhds','dskjfhdks','sjhdbfs','djkhskjfs','9.9762809','76.2862103'),
(2,4,'xhu','dui','duj','syui','egu','9.9762841','76.2862198'),
(3,5,'vikkk','fuiii','etuii','dyu97649','ryindjs','9.9762841','76.2862014');

/*Table structure for table `vehicles` */

DROP TABLE IF EXISTS `vehicles`;

CREATE TABLE `vehicles` (
  `vehicle_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) DEFAULT NULL,
  `vehicle` varchar(100) DEFAULT NULL,
  `desc` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`vehicle_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `vehicles` */

insert  into `vehicles`(`vehicle_id`,`company_id`,`vehicle`,`desc`,`amount`) values 
(1,1,'vehi1','dsafaf1','fefw1');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
