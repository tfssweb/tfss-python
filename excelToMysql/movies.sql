/*
Navicat MySQL Data Transfer

Source Server         : 172.18.18.203
Source Server Version : 50723
Source Host           : 172.18.18.203:23306
Source Database       : movies

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2018-12-08 20:56:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for movies
-- ----------------------------
DROP TABLE IF EXISTS `movies`;
CREATE TABLE `movies` (
  `name` varchar(255) DEFAULT NULL,
  `count` varchar(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of movies
-- ----------------------------
