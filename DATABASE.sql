DROP DATABASE IF EXISTS project;
CREATE DATABASE project;

USE project;
CREATE TABLE user (
    user_id INT AUTO_INCREMENT primary key NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(80),
    role ENUM("client", "employee", "admin") DEFAULT "client",
    compte_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE task (
    task_id INT AUTO_INCREMENT primary key NOT NULL,
    title VARCHAR(50) NOT NULL,
    start_time TIMESTAMP DEFAULT UTC_TIMESTAMP,
    end TIMESTAMP,
    status ENUM("not started", "in progress", "done") DEFAULT "not started"
);


CREATE TABLE user_has_task (
    fk_user_id INT NOT NULL,
    fk_task_id INT NOT NULL,
    CONSTRAINT fk_user FOREIGN KEY (fk_user_id) REFERENCES user(user_id),
    CONSTRAINT fk_task FOREIGN KEY (fk_task_id) REFERENCES task(task_id)
);

CREATE TABLE services (
  services_id INT AUTO_INCREMENT primary key NOT NULL,
  nom VARCHAR(100) NOT NULL,
  IMG VARCHAR(255),
  prix FLOAT
);

CREATE TABLE commandes (
  commande_id INT AUTO_INCREMENT primary key NOT NULL,
  user_id INT,
  devis VARCHAR(255),
  service_id INT,
  date_limite DATE,
  prix_tot FLOAT,
  CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES user(user_id),
  CONSTRAINT fk_services_id FOREIGN KEY (services_id) REFERENCES services(services_id)
);

--Garder seulement USE project;



