/*
 Navicat MySQL Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : personnel_man

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 17/09/2018 12:05:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin_table
-- ----------------------------
DROP TABLE IF EXISTS `admin_table`;
CREATE TABLE `admin_table`  (
  `s_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pwd` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`s_no`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_table
-- ----------------------------
INSERT INTO `admin_table` VALUES ('000001', '123456');

-- ----------------------------
-- Table structure for checking
-- ----------------------------
DROP TABLE IF EXISTS `checking`;
CREATE TABLE `checking`  (
  `s_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `c_date` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `c_tdays` int(2) NULL DEFAULT NULL,
  `c_ldays` int(2) NULL DEFAULT NULL,
  `c_odays` int(2) NULL DEFAULT NULL,
  `c_adays` int(2) NULL DEFAULT NULL,
  PRIMARY KEY (`s_no`, `c_date`) USING BTREE,
  CONSTRAINT `checking_ibfk_1` FOREIGN KEY (`s_no`) REFERENCES `staff` (`s_no`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of checking
-- ----------------------------
INSERT INTO `checking` VALUES ('000001', '2018-08', 23, 2, 2, 0);
INSERT INTO `checking` VALUES ('000001', '2018-09', 20, 0, 2, 0);
INSERT INTO `checking` VALUES ('000002', '2018-09', 20, 0, 5, 0);
INSERT INTO `checking` VALUES ('000004', '2018-08', 23, 0, 0, 0);
INSERT INTO `checking` VALUES ('000005', '2018-07', 22, 0, 0, 0);
INSERT INTO `checking` VALUES ('000005', '2018-08', 23, 0, 0, 0);
INSERT INTO `checking` VALUES ('000006', '2018-07', 22, 0, 1, 0);
INSERT INTO `checking` VALUES ('000008', '2018-09', 22, 1, 5, 0);

-- ----------------------------
-- Table structure for current_salary
-- ----------------------------
DROP TABLE IF EXISTS `current_salary`;
CREATE TABLE `current_salary`  (
  `s_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `salary` float(11, 2) NOT NULL,
  `prize` float(11, 2) NULL DEFAULT NULL,
  `deduct` float(11, 2) NULL DEFAULT NULL,
  PRIMARY KEY (`s_no`) USING BTREE,
  CONSTRAINT `current_salary_ibfk_1` FOREIGN KEY (`s_no`) REFERENCES `staff` (`s_no`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of current_salary
-- ----------------------------
INSERT INTO `current_salary` VALUES ('000001', 5000.00, 200.00, 0.00);
INSERT INTO `current_salary` VALUES ('000002', 5000.00, 0.00, 0.00);
INSERT INTO `current_salary` VALUES ('000003', 5000.00, 500.00, 0.00);
INSERT INTO `current_salary` VALUES ('000004', 4000.00, 100.00, 0.00);
INSERT INTO `current_salary` VALUES ('000005', 3000.00, 0.00, 0.00);
INSERT INTO `current_salary` VALUES ('000006', 3000.00, 0.00, 0.00);
INSERT INTO `current_salary` VALUES ('000007', 3000.00, 100.00, 0.00);
INSERT INTO `current_salary` VALUES ('000008', 3000.00, 100.00, 120.00);

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department`  (
  `d_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `d_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `s_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`d_no`) USING BTREE,
  INDEX `s_no`(`s_no`) USING BTREE,
  CONSTRAINT `department_ibfk_1` FOREIGN KEY (`s_no`) REFERENCES `staff` (`s_no`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of department
-- ----------------------------
INSERT INTO `department` VALUES ('000001', '策划部', '000001');
INSERT INTO `department` VALUES ('000002', '人事部', '000002');
INSERT INTO `department` VALUES ('000003', '广告部', '000003');
INSERT INTO `department` VALUES ('000004', '广告1部', '000004');

-- ----------------------------
-- Table structure for education
-- ----------------------------
DROP TABLE IF EXISTS `education`;
CREATE TABLE `education`  (
  `s_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `xl` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `major` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `school` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `graduate_date` date NULL DEFAULT NULL,
  PRIMARY KEY (`s_no`) USING BTREE,
  CONSTRAINT `education_ibfk_1` FOREIGN KEY (`s_no`) REFERENCES `staff` (`s_no`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of education
-- ----------------------------
INSERT INTO `education` VALUES ('000001', '本科', '电子商务', '东南大学', '2016-06-12');
INSERT INTO `education` VALUES ('000002', '研究生', '会计', '南京大学', '2016-06-12');
INSERT INTO `education` VALUES ('000003', '研究生', '广告学', '南京林业大学', '2016-06-12');
INSERT INTO `education` VALUES ('000004', '本科', '家居设计', '南京林业大学', '2016-06-12');
INSERT INTO `education` VALUES ('000005', '本科', '软件工程', '南京农业大学', '2016-06-12');
INSERT INTO `education` VALUES ('000006', '本科', '经济学', '南京邮电大学', '2016-06-12');
INSERT INTO `education` VALUES ('000007', '本科', '电子商务', '南京工业大学', '2016-06-12');
INSERT INTO `education` VALUES ('000008', '小学', NULL, NULL, NULL);

-- ----------------------------
-- Table structure for personnel
-- ----------------------------
DROP TABLE IF EXISTS `personnel`;
CREATE TABLE `personnel`  (
  `p_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `predept` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `aftdept` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `prepost` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `aftpost` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `p_date` date NOT NULL,
  PRIMARY KEY (`p_no`) USING BTREE,
  INDEX `s_no`(`s_no`) USING BTREE,
  CONSTRAINT `personnel_ibfk_1` FOREIGN KEY (`s_no`) REFERENCES `staff` (`s_no`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of personnel
-- ----------------------------
INSERT INTO `personnel` VALUES ('1', '000001', '策划部', '策划部', '员工', '经理', '2017-07-01');
INSERT INTO `personnel` VALUES ('14', '000008', '无', '人事部', '无', '副经理', '2018-09-13');
INSERT INTO `personnel` VALUES ('15', '000008', '无', '人事部', '无', '实习生', '2018-09-13');
INSERT INTO `personnel` VALUES ('16', '000007', '策划部', '人事部', '实习生', '实习生', '2018-09-13');
INSERT INTO `personnel` VALUES ('17', '000008', '无', '人事部', '无', '副经理', '2018-09-13');
INSERT INTO `personnel` VALUES ('18', '000008', '无', '策划部', '无', '经理', '2018-09-13');
INSERT INTO `personnel` VALUES ('19', '000006', '策划部', '222', '实习生', '员工', '2018-09-13');
INSERT INTO `personnel` VALUES ('2', '000002', '人事部', '人事部', '实习生', '员工', '2017-08-15');
INSERT INTO `personnel` VALUES ('20', '000008', '策划部', '222', '经理', '员工', '2018-09-13');
INSERT INTO `personnel` VALUES ('21', '000003', '广告部', '222', '经理', '员工', '2018-09-13');
INSERT INTO `personnel` VALUES ('3', '000002', '人事部', '人事部', '员工', '经理', '2017-09-01');
INSERT INTO `personnel` VALUES ('4', '000003', '无', '人事部', '无', '经理', '2017-12-01');
INSERT INTO `personnel` VALUES ('5', '000004', '策划部', '策划部', '实习生', '员工', '2018-03-01');

-- ----------------------------
-- Table structure for professional
-- ----------------------------
DROP TABLE IF EXISTS `professional`;
CREATE TABLE `professional`  (
  `p_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `p_name` char(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`p_no`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of professional
-- ----------------------------
INSERT INTO `professional` VALUES ('000001', '经理');
INSERT INTO `professional` VALUES ('000002', '副经理');
INSERT INTO `professional` VALUES ('000003', '员工');
INSERT INTO `professional` VALUES ('000004', '实习生');

-- ----------------------------
-- Table structure for salary
-- ----------------------------
DROP TABLE IF EXISTS `salary`;
CREATE TABLE `salary`  (
  `sa_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `leastpays` float(11, 2) NOT NULL,
  `prize` float(11, 2) NULL DEFAULT NULL,
  `doublingpays` float(11, 2) NULL DEFAULT NULL,
  `dkannuity` float(11, 2) NULL DEFAULT NULL,
  `dkinsurrance` float(11, 2) NULL DEFAULT NULL,
  `s_date` date NULL DEFAULT NULL,
  `deduct` float(11, 2) NULL DEFAULT NULL,
  `real_salary` float(10, 2) NULL DEFAULT NULL,
  PRIMARY KEY (`sa_no`) USING BTREE,
  INDEX `s_no`(`s_no`) USING BTREE,
  CONSTRAINT `salary_ibfk_1` FOREIGN KEY (`s_no`) REFERENCES `staff` (`s_no`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of salary
-- ----------------------------
INSERT INTO `salary` VALUES ('1', '000001', 3000.00, 240.00, 0.00, 160.00, 60.00, '2018-07-01', 0.00, 3000.00);
INSERT INTO `salary` VALUES ('2', '000002', 3000.00, 240.00, 0.00, 160.00, 60.00, '2018-07-01', 0.00, 3000.00);
INSERT INTO `salary` VALUES ('4', '000006', 3000.00, 0.00, 0.00, 240.00, 60.00, '2018-07-01', 0.00, 2700.00);
INSERT INTO `salary` VALUES ('5', '000007', 3000.00, 0.00, 0.00, 240.00, 60.00, '2018-07-01', 0.00, 2700.00);
INSERT INTO `salary` VALUES ('6', '000006', 3000.00, 0.00, 0.00, 240.00, 60.00, '2018-08-12', 0.00, 2700.00);
INSERT INTO `salary` VALUES ('7', '000005', 3000.00, 0.00, 0.00, 240.00, 60.00, '2018-08-12', 0.00, 2700.00);
INSERT INTO `salary` VALUES ('8', '000004', 4000.00, 100.00, 0.00, 320.00, 80.00, '2018-08-12', 0.00, 3700.00);
INSERT INTO `salary` VALUES ('9', '000003', 5000.00, 500.00, 0.00, 400.00, 100.00, '2018-08-12', 0.00, 5000.00);

-- ----------------------------
-- Table structure for sp
-- ----------------------------
DROP TABLE IF EXISTS `sp`;
CREATE TABLE `sp`  (
  `s_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `p_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `d_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `entry_time` date NOT NULL,
  PRIMARY KEY (`s_no`) USING BTREE,
  INDEX `d_no`(`d_no`) USING BTREE,
  INDEX `p_no`(`p_no`) USING BTREE,
  CONSTRAINT `sp_ibfk_1` FOREIGN KEY (`s_no`) REFERENCES `staff` (`s_no`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `sp_ibfk_3` FOREIGN KEY (`d_no`) REFERENCES `department` (`d_no`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `sp_ibfk_4` FOREIGN KEY (`p_no`) REFERENCES `professional` (`p_no`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sp
-- ----------------------------
INSERT INTO `sp` VALUES ('000001', '000001', '000001', '2017-07-01');
INSERT INTO `sp` VALUES ('000002', '000001', '000002', '2017-09-01');
INSERT INTO `sp` VALUES ('000003', '000003', '000004', '2018-09-13');
INSERT INTO `sp` VALUES ('000004', '000003', '000004', '2018-09-13');
INSERT INTO `sp` VALUES ('000005', '000004', '000001', '2018-09-13');
INSERT INTO `sp` VALUES ('000006', '000003', '000004', '2018-09-13');
INSERT INTO `sp` VALUES ('000007', '000004', '000004', '2018-09-13');
INSERT INTO `sp` VALUES ('000008', '000003', '000004', '2018-09-13');

-- ----------------------------
-- Table structure for staff
-- ----------------------------
DROP TABLE IF EXISTS `staff`;
CREATE TABLE `staff`  (
  `s_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_name` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_sex` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_birth` date NOT NULL,
  `s_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_num` char(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_email` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_married` char(3) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_address` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`s_no`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of staff
-- ----------------------------
INSERT INTO `staff` VALUES ('000001', '王英才', '男', '1987-09-10', '3205221987', '123232', 'wang@163.com', '是', '南京玄武区');
INSERT INTO `staff` VALUES ('000002', '黎勇', '男', '1989-04-30', '3205221989', '12270113456', 'li@163.com', '是', '南京秦淮区');
INSERT INTO `staff` VALUES ('000003', '孙浩然', '男', '1987-02-10', '3223221989', '13470113456', 'sun@163.com', '是', '南京雨花台区');
INSERT INTO `staff` VALUES ('000004', '陈晓明', '女', '1987-05-10', '1223221122', '13776659521', 'xiaocheng@qq.com', '否', '南京栖霞区');
INSERT INTO `staff` VALUES ('000005', '秦佩佩', '女', '1981-06-10', '3221155432', '13655597553', 'Qing@qq.com', '否', '南京浦口');
INSERT INTO `staff` VALUES ('000006', '张伟', '男', '1990-07-20', '5542234763', '13422258832', 'Zzhang@qq.com', '否', '南京锁金村');
INSERT INTO `staff` VALUES ('000007', '包涵', '女', '1988-08-08', '1235745357', '18022235695', 'baobao@qq.com', '否', '南京龙蟠路');
INSERT INTO `staff` VALUES ('000008', '王子云', '男', '2018-01-01', '12347896545211', '13776625695', '1', '是', '1');

SET FOREIGN_KEY_CHECKS = 1;
