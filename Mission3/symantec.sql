CREATE TABLE `net_test`.`symantec` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `x_description` VARCHAR(45) NULL,
  `x_link` VARCHAR(100) NULL,
  `x_title` VARCHAR(45) NULL,
  `Updated` VARCHAR(45) NULL,
  `Risk_Impact` VARCHAR(10) NULL,
  `Infection_Length` VARCHAR(45) NULL,
  `x_pubDate` VARCHAR(15) NULL,
  `Type` VARCHAR(45) NULL,
  `System_Affected` VARCHAR(100) NULL,
  `Name` VARCHAR(75) NULL,
  `Writeup_By` VARCHAR(55) NULL,
  `Version` VARCHAR(30) NULL,
  `Publisher` VARCHAR(60) NULL,
  `File_Names` VARCHAR(110) NULL,
  `Discovered` VARCHAR(20) NULL,
  `Also_Known_As` VARCHAR(110) NULL,
  `Target_Platform` VARCHAR(35) NULL,
  `Characteristics` VARCHAR(65) NULL,
  `Region_Reported` VARCHAR(30) NULL,
  `Area_of_infection` VARCHAR(65) NULL,
  `Likelihood` VARCHAR(45) NULL,
  `Package_name` VARCHAR(25) NULL,
  `CVE_References` VARCHAR(15) CHARACTER SET 'utf8' NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));