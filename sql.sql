/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - used_study_material
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`used_study_material` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `used_study_material`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add category',7,'add_category'),
(26,'Can change category',7,'change_category'),
(27,'Can delete category',7,'delete_category'),
(28,'Can view category',7,'view_category'),
(29,'Can add institution type',8,'add_institutiontype'),
(30,'Can change institution type',8,'change_institutiontype'),
(31,'Can delete institution type',8,'delete_institutiontype'),
(32,'Can view institution type',8,'view_institutiontype'),
(33,'Can add login',9,'add_login'),
(34,'Can change login',9,'change_login'),
(35,'Can delete login',9,'delete_login'),
(36,'Can view login',9,'view_login'),
(37,'Can add material',10,'add_material'),
(38,'Can change material',10,'change_material'),
(39,'Can delete material',10,'delete_material'),
(40,'Can view material',10,'view_material'),
(41,'Can add user',11,'add_user'),
(42,'Can change user',11,'change_user'),
(43,'Can delete user',11,'delete_user'),
(44,'Can view user',11,'view_user'),
(45,'Can add request',12,'add_request'),
(46,'Can change request',12,'change_request'),
(47,'Can delete request',12,'delete_request'),
(48,'Can view request',12,'view_request'),
(49,'Can add feedback',13,'add_feedback'),
(50,'Can change feedback',13,'change_feedback'),
(51,'Can delete feedback',13,'delete_feedback'),
(52,'Can view feedback',13,'view_feedback'),
(53,'Can add complaints',14,'add_complaints'),
(54,'Can change complaints',14,'change_complaints'),
(55,'Can delete complaints',14,'delete_complaints'),
(56,'Can view complaints',14,'view_complaints'),
(57,'Can add chat',15,'add_chat'),
(58,'Can change chat',15,'change_chat'),
(59,'Can delete chat',15,'delete_chat'),
(60,'Can view chat',15,'view_chat');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'MATERIAL','category'),
(15,'MATERIAL','chat'),
(14,'MATERIAL','complaints'),
(13,'MATERIAL','feedback'),
(8,'MATERIAL','institutiontype'),
(9,'MATERIAL','login'),
(10,'MATERIAL','material'),
(12,'MATERIAL','request'),
(11,'MATERIAL','user'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'MATERIAL','0001_initial','2023-10-31 04:00:06.706183'),
(2,'MATERIAL','0002_remove_chat_time','2023-10-31 04:00:06.772209'),
(3,'contenttypes','0001_initial','2023-10-31 04:00:06.882152'),
(4,'auth','0001_initial','2023-10-31 04:00:07.825156'),
(5,'admin','0001_initial','2023-10-31 04:00:07.989039'),
(6,'admin','0002_logentry_remove_auto_add','2023-10-31 04:00:07.993635'),
(7,'admin','0003_logentry_add_action_flag_choices','2023-10-31 04:00:08.003647'),
(8,'contenttypes','0002_remove_content_type_name','2023-10-31 04:00:08.130652'),
(9,'auth','0002_alter_permission_name_max_length','2023-10-31 04:00:08.187840'),
(10,'auth','0003_alter_user_email_max_length','2023-10-31 04:00:08.243538'),
(11,'auth','0004_alter_user_username_opts','2023-10-31 04:00:08.243538'),
(12,'auth','0005_alter_user_last_login_null','2023-10-31 04:00:08.320760'),
(13,'auth','0006_require_contenttypes_0002','2023-10-31 04:00:08.324104'),
(14,'auth','0007_alter_validators_add_error_messages','2023-10-31 04:00:08.326924'),
(15,'auth','0008_alter_user_username_max_length','2023-10-31 04:00:08.385036'),
(16,'auth','0009_alter_user_last_name_max_length','2023-10-31 04:00:08.436944'),
(17,'auth','0010_alter_group_name_max_length','2023-10-31 04:00:08.495319'),
(18,'auth','0011_update_proxy_permissions','2023-10-31 04:00:08.495319'),
(19,'auth','0012_alter_user_first_name_max_length','2023-10-31 04:00:08.567769'),
(20,'sessions','0001_initial','2023-10-31 04:00:08.637048');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('8vcimbrm6trrsjp14ppxhsqal6269t5p','.eJyrVsrJTFGyMjTVUSrJBzOVzJRAbDDT0BjILgIzjZRqARMOC7c:1r4gRq:k_2xpyd4FFPHgQcYWvlJuc0LoZdyIwJP3t9s0g9wx-4','2023-12-03 11:58:46.329526'),
('hfcp9hvvnzvim5oidj89gda7sug5vm70','eyJsaWQiOjF9:1qxgT8:NVhF40OFWnDhV4Bx9EfBSOUtTrfG_4wIWIW3MVr5pIw','2023-11-14 04:35:10.209893'),
('owykafgzucxerl5q2m9byfqq8up99luu','eyJsaWQiOjF9:1qxfx0:OG2hclpdGS3RI7KHh9xzR3OgdQV-yIVfz5D9aTr_dEQ','2023-11-14 04:01:58.186540');

/*Table structure for table `material_category` */

DROP TABLE IF EXISTS `material_category`;

CREATE TABLE `material_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(20) NOT NULL,
  `INSTITUTIONTYPE_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MATERIAL_category_INSTITUTIONTYPE_id_601c7ee2_fk_MATERIAL_` (`INSTITUTIONTYPE_id`),
  CONSTRAINT `MATERIAL_category_INSTITUTIONTYPE_id_601c7ee2_fk_MATERIAL_` FOREIGN KEY (`INSTITUTIONTYPE_id`) REFERENCES `material_institutiontype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `material_category` */

insert  into `material_category`(`id`,`category_name`,`INSTITUTIONTYPE_id`) values 
(2,'BOOKS',2),
(3,'BOOKS',3),
(4,'BOOKS',4),
(5,'BOOKS',5),
(6,'BOOKS',6),
(7,'Mini drafter',4),
(8,'CALCULATOR',2),
(9,'CALCULATOR',3),
(10,'CALCULATOR',4),
(11,'CALCULATOR',5),
(12,'CALCULATOR',6),
(13,'cat',7);

/*Table structure for table `material_chat` */

DROP TABLE IF EXISTS `material_chat`;

CREATE TABLE `material_chat` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `message` varchar(500) NOT NULL,
  `FROM_ID_id` bigint(20) NOT NULL,
  `TO_ID_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MATERIAL_chat_FROM_ID_id_22ef0c58_fk_MATERIAL_login_id` (`FROM_ID_id`),
  KEY `MATERIAL_chat_TO_ID_id_0eefdfd7_fk_MATERIAL_login_id` (`TO_ID_id`),
  CONSTRAINT `MATERIAL_chat_FROM_ID_id_22ef0c58_fk_MATERIAL_login_id` FOREIGN KEY (`FROM_ID_id`) REFERENCES `material_login` (`id`),
  CONSTRAINT `MATERIAL_chat_TO_ID_id_0eefdfd7_fk_MATERIAL_login_id` FOREIGN KEY (`TO_ID_id`) REFERENCES `material_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;

/*Data for the table `material_chat` */

insert  into `material_chat`(`id`,`date`,`message`,`FROM_ID_id`,`TO_ID_id`) values 
(1,'2023-11-04','hi',6,7),
(2,'2023-11-04','hi',7,7),
(3,'2023-11-04','sreeragm',7,7),
(4,'2023-11-04','hi',6,7),
(5,'2023-11-04','sreeragm',6,7),
(6,'2023-11-04','hi',7,7),
(7,'2023-11-04','hi',7,7),
(8,'2023-11-04','jggjg',7,6),
(9,'2023-11-04','hffhfhfhfjfj',7,6),
(10,'2023-11-04','helllo',6,7),
(11,'2023-11-04','hello',6,7),
(12,'2023-11-04','nvnvvbvb',7,6),
(13,'2023-11-04','adsds',7,6),
(14,'2023-11-04','sreeragm',6,7),
(15,'2023-11-04','sreeragm',6,7),
(16,'2023-11-04','pranav',7,6),
(17,'2023-11-04','pranav',7,6),
(18,'2023-11-04','sakthi',3,2),
(19,'2023-11-04','hari',2,3),
(20,'2023-11-04','hari',2,3),
(21,'2023-11-04','sakthi',3,2),
(22,'2023-11-04','sakthi',3,2),
(23,'2023-11-04','sakthi',3,2),
(24,'2023-11-04','hari',2,3),
(25,'2023-11-04','hari',2,3),
(26,'2023-11-04','hari',2,3),
(27,'2023-11-04','hari',2,3),
(28,'2023-11-04','sakthi',3,2),
(29,'2023-11-04','hari',2,3),
(30,'2023-11-04','sakthi',3,2),
(31,'2023-11-11','hi',12,13),
(32,'2023-11-11','hi',12,13),
(33,'2023-11-11','hi',13,12),
(34,'2023-11-11','hi',12,13),
(35,'2023-11-19','hi name3',14,15),
(36,'2023-11-19','hi name4',15,14);

/*Table structure for table `material_complaints` */

DROP TABLE IF EXISTS `material_complaints`;

CREATE TABLE `material_complaints` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(500) NOT NULL,
  `status` varchar(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MATERIAL_complaints_USER_id_30181ba2_fk_MATERIAL_user_id` (`USER_id`),
  CONSTRAINT `MATERIAL_complaints_USER_id_30181ba2_fk_MATERIAL_user_id` FOREIGN KEY (`USER_id`) REFERENCES `material_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `material_complaints` */

insert  into `material_complaints`(`id`,`complaint`,`date`,`reply`,`status`,`USER_id`) values 
(1,'complaint','2023-10-31','ok','replyed',3),
(2,'qwert','2023-11-04','qwert','replyed',7),
(3,'Complaint','2023-11-11','Reply','replyed',3),
(4,'name3','2023-11-19','ok','replyed',13);

/*Table structure for table `material_feedback` */

DROP TABLE IF EXISTS `material_feedback`;

CREATE TABLE `material_feedback` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MATERIAL_feedback_USER_id_ee527ef2_fk_MATERIAL_user_id` (`USER_id`),
  CONSTRAINT `MATERIAL_feedback_USER_id_ee527ef2_fk_MATERIAL_user_id` FOREIGN KEY (`USER_id`) REFERENCES `material_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `material_feedback` */

insert  into `material_feedback`(`id`,`feedback`,`date`,`USER_id`) values 
(1,'good web','2023-10-31',3),
(2,'feedback','2023-11-07',3),
(3,'FeedBack','2023-11-11',3),
(4,'Feedback','2023-11-11',11),
(5,'name3','2023-11-19',13);

/*Table structure for table `material_institutiontype` */

DROP TABLE IF EXISTS `material_institutiontype`;

CREATE TABLE `material_institutiontype` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Type` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `material_institutiontype` */

insert  into `material_institutiontype`(`id`,`Type`) values 
(2,'MCA'),
(3,'DEGREE'),
(4,'POLYTECHNIC'),
(5,'B-TEC'),
(6,'M-TEC'),
(7,'Ins');

/*Table structure for table `material_login` */

DROP TABLE IF EXISTS `material_login`;

CREATE TABLE `material_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `material_login` */

insert  into `material_login`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'Hari@gmail.com','hari','user'),
(3,'Sakthi@gmail.com','sakthi','user'),
(4,'Ajin@gmail.com','ajin','user'),
(5,'sreerag@gmail.com','sreerag','user'),
(6,'sreeragm@gmail.com','sreeragm','user'),
(7,'pranav@gmail.com','pranav','user'),
(8,'anandhu@gmail.com','anandhu','user'),
(10,'bd1@gmail.com','vh43{ikP','user'),
(11,'ad1@gmail.com','ad1','user'),
(12,'name1@gmail.com','Name1','user'),
(13,'name2@gmail.com','name2','user'),
(14,'name3@gmail.com','name3','user'),
(15,'name4@gmail.com','name4','user');

/*Table structure for table `material_material` */

DROP TABLE IF EXISTS `material_material`;

CREATE TABLE `material_material` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `material_name` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `image` varchar(250) NOT NULL,
  `price` varchar(20) NOT NULL,
  `condition` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL,
  `CATEGORY_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MATERIAL_material_USER_id_f84117e3_fk_MATERIAL_user_id` (`USER_id`),
  KEY `MATERIAL_material_CATEGORY_id_4419ef33_fk_MATERIAL_category_id` (`CATEGORY_id`),
  CONSTRAINT `MATERIAL_material_CATEGORY_id_4419ef33_fk_MATERIAL_category_id` FOREIGN KEY (`CATEGORY_id`) REFERENCES `material_category` (`id`),
  CONSTRAINT `MATERIAL_material_USER_id_f84117e3_fk_MATERIAL_user_id` FOREIGN KEY (`USER_id`) REFERENCES `material_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;

/*Data for the table `material_material` */

insert  into `material_material`(`id`,`material_name`,`date`,`image`,`price`,`condition`,`status`,`CATEGORY_id`,`USER_id`) values 
(5,'Computer','2023-10-01','/20231104-153334.jpg','100','good condition','pending',2,4),
(6,'Maths','2023-10-01','/20231104-160210.jpg','150','good condition','pending',3,6),
(7,'statistics','2023-10-01','/20231104-170320.jpg','300','good condition','pending',3,2),
(8,'statistics','2023-10-01','/20231104-172619.jpg','300','good condition','pending',2,7),
(10,'Aj1','2023-10-01','/20231111-120006.jpg','200','good condition','pending',2,3),
(11,'Aj2','2023-10-01','/20231111-120026.jpg','300','good condition','pending',2,3),
(12,'Aj3','2023-10-01','/20231111-120048.jpg','300','good condition','pending',2,3),
(13,'An1','2023-10-01','/20231111-121124.jpg','300','good condition','pending',3,7),
(14,'An2','2023-10-01','/20231111-121159.jpg','100','good condition','pending',3,7),
(15,'SA1','2023-10-01','/20231111-123452.jpg','200','good condition','pending',3,2),
(16,'Aos','2023-10-01','/20231111-140627.jpg','300','good condition','pending',2,2),
(18,'Aos','2023-10-01','/20231111-141837.jpg','300','good condition','pending',3,2),
(19,'pr1','2023-10-01','/20231111-151004.jpg','200','good condition','Available',13,11),
(20,'pr2','2023-10-01','/20231111-151028.jpg','200','good condition','pending',13,11),
(21,'pr3','2023-10-01','/20231111-151652.jpg','400','good condition','pending',13,11),
(22,'pr4','2023-10-01','/20231111-151912.jpg','200','good condition','pending',13,11),
(23,'pr5','2023-10-01','/20231111-151940.jpg','300','good condition','pending',13,11),
(24,'pr6','2023-10-01','/20231111-155457.jpg','300','good condition','pending',13,11),
(25,'Book7','2023-10-01','/20231119-153137.jpg','100','good condition','pending',2,3),
(26,'Book 10','2023-10-01','/20231119-154636.jpg','200','good condition','pending',2,1),
(27,'Book11','2023-10-01','/20231119-154708.jpg','250','good condition','pending',2,1),
(28,'Book12','2023-10-01','/20231119-155135.jpg','200','good condition','pending',2,3),
(29,'Book13','2023-10-01','/20231119-155332.jpg','200','good condition','pending',2,3),
(30,'name3.1','2023-10-01','/20231119-160149.jpg','300','good condition','Available',2,13),
(31,'name3.2','2023-10-03','/20231119-160212.jpg','200','good condition','pending',2,13),
(32,'name4,1','2023-10-01','/20231119-170849.jpg','200','good condition','pending',2,14),
(33,'name4,2','2023-10-01','/20231119-170913.jpg','220','good condition','Available',2,14),
(34,'material1','2023-10-01','/20231119-171350.jpg','280','good condition','pending',3,3),
(35,'material2','2023-10-01','/20231119-171406.jpg','280','good condition','pending',3,3);

/*Table structure for table `material_request` */

DROP TABLE IF EXISTS `material_request`;

CREATE TABLE `material_request` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `MATERIAL_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MATERIAL_request_MATERIAL_id_2d891464_fk_MATERIAL_material_id` (`MATERIAL_id`),
  KEY `MATERIAL_request_USER_id_26a12926_fk_MATERIAL_user_id` (`USER_id`),
  CONSTRAINT `MATERIAL_request_MATERIAL_id_2d891464_fk_MATERIAL_material_id` FOREIGN KEY (`MATERIAL_id`) REFERENCES `material_material` (`id`),
  CONSTRAINT `MATERIAL_request_USER_id_26a12926_fk_MATERIAL_user_id` FOREIGN KEY (`USER_id`) REFERENCES `material_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

/*Data for the table `material_request` */

insert  into `material_request`(`id`,`date`,`status`,`MATERIAL_id`,`USER_id`) values 
(1,'2023-11-04','Approved',5,3),
(2,'2023-11-04','Approved',6,5),
(3,'2023-11-04','requested',6,5),
(4,'2023-11-04','Approved',7,1),
(5,'2023-11-07','requested',8,2),
(6,'2023-11-07','requested',5,2),
(7,'2023-11-07','requested',6,2),
(8,'2023-11-11','requested',5,2),
(10,'2023-11-11','requested',8,2),
(11,'2023-11-11','Approved',10,2),
(12,'2023-11-11','Approved',11,2),
(13,'2023-11-11','requested',12,2),
(14,'2023-11-11','requested',13,2),
(15,'2023-11-11','Approved',14,2),
(16,'2023-11-11','requested',5,2),
(17,'2023-11-11','requested',22,12),
(18,'2023-11-11','Approved',23,12),
(19,'2023-11-11','requested',22,12),
(20,'2023-11-11','Rejected',24,12),
(21,'2023-11-11','requested',21,12),
(22,'2023-11-11','requested',21,12),
(23,'2023-11-11','requested',21,12),
(24,'2023-11-11','requested',21,12),
(25,'2023-11-19','requested',5,2),
(26,'2023-11-19','requested',8,2),
(27,'2023-11-19','requested',10,2),
(28,'2023-11-19','requested',8,2),
(29,'2023-11-19','requested',8,2),
(30,'2023-11-19','requested',5,2),
(31,'2023-11-19','requested',16,2),
(32,'2023-11-19','requested',16,2),
(33,'2023-11-19','requested',5,2),
(34,'2023-11-19','requested',11,2),
(35,'2023-11-19','requested',11,2),
(36,'2023-11-19','requested',5,2),
(37,'2023-11-19','requested',25,2),
(38,'2023-11-19','requested',26,3),
(39,'2023-11-19','requested',27,3),
(40,'2023-11-19','Approved',31,14);

/*Table structure for table `material_user` */

DROP TABLE IF EXISTS `material_user`;

CREATE TABLE `material_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `place` varchar(50) NOT NULL,
  `District` varchar(50) NOT NULL,
  `pin` bigint(20) NOT NULL,
  `photo` varchar(250) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MATERIAL_user_LOGIN_id_1f29f01a_fk_MATERIAL_login_id` (`LOGIN_id`),
  CONSTRAINT `MATERIAL_user_LOGIN_id_1f29f01a_fk_MATERIAL_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `material_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `material_user` */

insert  into `material_user`(`id`,`name`,`phone`,`email`,`place`,`District`,`pin`,`photo`,`LOGIN_id`) values 
(1,'Hari',3245674523,'Hari@gmail.com','Mankavu','Kozhikode',673576,'/20231031-105432.jpg',2),
(2,'Sakthi',3623654545,'Sakthi@gmail.com','feroke','Kozhikode',673576,'/20231031-105555.jpg',3),
(3,'Ajin',2332414342,'Ajin@gmail.com','Kuttikattoor','Kozhikode',673576,'/20231031-105640.jpg',4),
(4,'Sreerag',5467575634,'sreeraj@gmail.com','kozhikode','kozhikode',673576,'/20231104-152654.jpg',5),
(5,'Sreerag m',5467575634,'sreeragm@gmail.com','kozhikode','kozhikode',673576,'/20231104-155916.jpg',6),
(6,'pranav',8635678978,'pranav@gmail.com','Kuttikattoor','kozhikode',673576,'/20231104-160109.jpg',7),
(7,'anandhu',4536373635,'ananthu@gmail.com','Kuttikattoor','kozhikode',673576,'/20231104-172425.jpg',8),
(11,'name1',2345678912,'name1@gmail.com','place1','kozhikode',673576,'/20231111-150757.jpg',12),
(12,'name2',1234567890,'name2@gmail.com','place1','kozhikode',673576,'/20231111-150847.jpg',13),
(13,'name3',1234567890,'name3@gmail.com','place1','kozhikode',673576,'/20231119-155834.jpg',14),
(14,'name4',1234567890,'name4@gmail.com','place1','kozhikode',673576,'/20231119-160056.jpg',15);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
