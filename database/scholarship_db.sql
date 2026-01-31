/*
SQLyog Community v13.3.0 (64 bit)
MySQL - 9.1.0 : Database - scholarship
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`scholarship` /*!40100 DEFAULT CHARACTER SET latin1 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `scholarship`;

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category`) values 
(5,'courses');

/*Table structure for table `college` */

DROP TABLE IF EXISTS `college`;

CREATE TABLE `college` (
  `college_id` int NOT NULL AUTO_INCREMENT,
  `login_id` int DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`college_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `college` */

insert  into `college`(`college_id`,`login_id`,`fname`,`place`,`phone`,`email`) values 
(2,8,'uc','ernakaulams','02345678904','uc@gmail.com');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int NOT NULL AUTO_INCREMENT,
  `parent_id` int DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`parent_id`,`complaint`,`reply`,`date`) values 
(1,1,'sdfghjk','asdfgthy','2023-02-28'),
(2,11,'good','ok','2024-04-24 21:20:10'),
(3,11,'bbd','pending','2024-04-24 21:21:01'),
(4,11,'bbd','pending','2024-04-24 21:21:01');

/*Table structure for table `gallery` */

DROP TABLE IF EXISTS `gallery`;

CREATE TABLE `gallery` (
  `gallery_id` int NOT NULL AUTO_INCREMENT,
  `college_id` int DEFAULT NULL,
  `gallery` varchar(1000) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`gallery_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `gallery` */

insert  into `gallery`(`gallery_id`,`college_id`,`gallery`,`title`) values 
(1,1,'static/image11751f90-bf76-4f3e-8e52-4f08e665247ebike.jpg','title'),
(2,1,'static/image5083216b-a3b4-4831-bb43-b65c2fdd2147motorbike-front-side-bike-logo-fast-ride-symbol-2J54CKY.jpg','dfghjkl;');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'p','p','parent'),
(2,'c','c','college'),
(3,'admin','admin','admin'),
(4,'s','s','staff'),
(5,'renuka','xcvbn','staff'),
(6,'stjudes','stjudes','school_board'),
(7,'mg','mg','university'),
(8,'uc','uc','college'),
(9,'stu','stu','student'),
(10,'sch','sch','school'),
(11,'student','student','student'),
(12,'uc','st','school');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int NOT NULL AUTO_INCREMENT,
  `notification` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`notification`) values 
(1,'notifia'),
(3,'jjkj');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int NOT NULL AUTO_INCREMENT,
  `scholarship_id` int DEFAULT NULL,
  `student_id` int DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`request_id`,`scholarship_id`,`student_id`,`date`,`status`) values 
(1,3,1,'2023-03-11','accept'),
(2,3,3,'2024-04-24','pending');

/*Table structure for table `scholarship` */

DROP TABLE IF EXISTS `scholarship`;

CREATE TABLE `scholarship` (
  `scholarship_id` int NOT NULL AUTO_INCREMENT,
  `category_id` int DEFAULT NULL,
  `scholarship` varchar(100) DEFAULT NULL,
  `startdate` varchar(100) DEFAULT NULL,
  `enddate` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`scholarship_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `scholarship` */

insert  into `scholarship`(`scholarship_id`,`category_id`,`scholarship`,`startdate`,`enddate`,`date`,`status`) values 
(3,5,'ghg','2024-04-26','2024-05-10','2024-04-23','accept');

/*Table structure for table `school` */

DROP TABLE IF EXISTS `school`;

CREATE TABLE `school` (
  `school_id` int NOT NULL AUTO_INCREMENT,
  `login_id` int DEFAULT NULL,
  `school_board_id` int DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`school_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `school` */

insert  into `school`(`school_id`,`login_id`,`school_board_id`,`fname`,`place`,`phone`,`email`) values 
(1,10,1,'event',NULL,NULL,NULL),
(2,12,6,'uc','ernakaulam','02345678904','uc@gmail.com');

/*Table structure for table `school_board` */

DROP TABLE IF EXISTS `school_board`;

CREATE TABLE `school_board` (
  `school_board_id` int NOT NULL AUTO_INCREMENT,
  `login_id` int DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`school_board_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `school_board` */

insert  into `school_board`(`school_board_id`,`login_id`,`fname`,`place`,`phone`,`email`) values 
(2,6,'st judes','ernakaulams','02345678904','stjudesa@gmail.com');

/*Table structure for table `seatavailable` */

DROP TABLE IF EXISTS `seatavailable`;

CREATE TABLE `seatavailable` (
  `seatavailable_id` int NOT NULL AUTO_INCREMENT,
  `admission_id` int DEFAULT NULL,
  `seat_id` int DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`seatavailable_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `seatavailable` */

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `student_id` int NOT NULL AUTO_INCREMENT,
  `login_id` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `study_id` int DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`student_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`,`study_id`,`type`) values 
(1,'1','user','qwerty','ernakulam1','02345678907','student@gmail.com',NULL,NULL),
(2,'10','jùjús','sea','jhwkjs','02345678904','kjsjdksa@gmail.com',8,'college'),
(3,'11','jùjú','sea','jhwkjs','02345678904','kjsjdksa@gmail.com',10,'school');

/*Table structure for table `university` */

DROP TABLE IF EXISTS `university`;

CREATE TABLE `university` (
  `university_id` int NOT NULL AUTO_INCREMENT,
  `login_id` int DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`university_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `university` */

insert  into `university`(`university_id`,`login_id`,`fname`,`place`,`phone`,`email`) values 
(3,7,'mg','ernakulams','1234567890','mgs@gmail');

/*Table structure for table `uploaddetails` */

DROP TABLE IF EXISTS `uploaddetails`;

CREATE TABLE `uploaddetails` (
  `uploaddetails_id` int NOT NULL AUTO_INCREMENT,
  `admission_id` int DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `files` varchar(1000) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`uploaddetails_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `uploaddetails` */

insert  into `uploaddetails`(`uploaddetails_id`,`admission_id`,`title`,`files`,`date`) values 
(1,1,'asdfghyju','static/image77e364e7-773b-48c6-aff0-75b7b50ffabdmotorbike-front-side-bike-logo-fast-ride-symbol-2J54CKY.jpg','2023-03-10');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
