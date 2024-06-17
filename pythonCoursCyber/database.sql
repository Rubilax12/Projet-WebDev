DROP DATABASE IF EXISTS project;
CREATE DATABASE project;

USE project;
CREATE TABLE user (
    user_id INT AUTO_INCREMENT primary key NOT NULL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);
CREATE TABLE task (
    task_id INT AUTO_INCREMENT primary key NOT NULL,
    title VARCHAR(50) NOT NULL,sys
    begin TIMESTAMP DEFAULT UTC_TIMESTAMP,
    end TIMESTAMP,
    status ENUM("not started", "in progress", "done") DEFAULT "not started"
);
CREATE TABLE user_has_task (
    fk_user_id VARCHAR(50) NOT NULL,
    fk_task_id VARCHAR(50) NOT NULL
);`user`