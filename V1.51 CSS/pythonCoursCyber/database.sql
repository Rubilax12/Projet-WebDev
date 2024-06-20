DROP DATABASE IF EXISTS project;
CREATE DATABASE project;

USE project;

CREATE TABLE user (
    user_id INT AUTO_INCREMENT primary key NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(80),
    role ENUM('client', 'employee', 'admin') DEFAULT 'client',
    compte_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE task (
    task_id INT AUTO_INCREMENT primary key NOT NULL,
    title VARCHAR(50) NOT NULL,
    start_time TIMESTAMP DEFAULT UTC_TIMESTAMP,
    end TIMESTAMP,
    status ENUM('not started', 'in progress', 'done') DEFAULT 'not started'
);

CREATE TABLE user_has_task (
    fk_user_id INT NOT NULL,
    fk_task_id INT NOT NULL,
    CONSTRAINT fk_user FOREIGN KEY (fk_user_id) REFERENCES user(user_id),
    CONSTRAINT fk_task FOREIGN KEY (fk_task_id) REFERENCES task(task_id)
);

CREATE TABLE services (
  services_id INT AUTO_INCREMENT primary key NOT NULL,
  nom VARCHAR(100) NOT NULL UNIQUE,
  images VARCHAR(255),
  prix FLOAT NOT NULL
);

-- Ajout d'index sur les colonnes de référence
ALTER TABLE user ADD INDEX (username);
ALTER TABLE services ADD INDEX (nom);

CREATE TABLE commandes (
  commande_id INT AUTO_INCREMENT primary key NOT NULL,
  username VARCHAR(50) NOT NULL,
  devis VARCHAR(255),
  services VARCHAR(100) NOT NULL,
  prix_tot FLOAT,
  CONSTRAINT fk_username FOREIGN KEY (username) REFERENCES user(username),
  CONSTRAINT fk_services FOREIGN KEY (services) REFERENCES services(nom)
);
SET GLOBAL FOREIGN_KEY_CHECKS=0;