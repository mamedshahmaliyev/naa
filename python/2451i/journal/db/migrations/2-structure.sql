
CREATE DATABASE IF NOT EXISTS `journal`;
USE `journal`;

CREATE TABLE IF NOT EXISTS `subjects` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `credits` int unsigned DEFAULT NULL,
  `hours` int unsigned NOT NULL,
  `code` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `student_groups` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `students` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `father_name` varchar(255),
  `gender` ENUM('male', 'female'),
  `entry_year` int unsigned,
  PRIMARY KEY (`id`),
  UNIQUE KEY (first_name, last_name, father_name)
);

CREATE TABLE IF NOT EXISTS `students_groups` (
  `student_id` bigint unsigned NOT NULL,
  `group_id` bigint unsigned NOT NULL,
  PRIMARY KEY (`student_id`, `group_id`),
  CONSTRAINT `students_groups_FK1` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`),
  CONSTRAINT `students_groups_FK2` FOREIGN KEY (`group_id`) REFERENCES `student_groups` (`id`)
);

CREATE TABLE IF NOT EXISTS `teachers` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `father_name` varchar(255),
  `gender` ENUM('male', 'female'),
  `experience` INT,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `journal` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `kafedra` varchar(100) NOT NULL,
  `faculty` varchar(100) NOT NULL,
  `group_id` bigint unsigned,
  `start_date` date,
  `end_date` date,
  PRIMARY KEY (`id`),
  CONSTRAINT `journal_student_groups_FK` FOREIGN KEY (`group_id`) REFERENCES `student_groups` (`id`)
);

CREATE TABLE IF NOT EXISTS `journal_records` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `teacher_id` bigint unsigned NOT NULL,
  `student_id` bigint unsigned NOT NULL,
  `record_type` enum('lecture', 'practice', 'lab', 'kollokvium'),
  `mark` tinyint unsigned,
  `presence` enum('present', 'absent', 'holiday', 'valid_reason'),
  `hour` tinyint unsigned,
  `record_date` date,
  PRIMARY KEY (`id`),
  CONSTRAINT `journal_records_teacher_FK` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`id`),
  CONSTRAINT `journal_records_student_FK` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`)
);