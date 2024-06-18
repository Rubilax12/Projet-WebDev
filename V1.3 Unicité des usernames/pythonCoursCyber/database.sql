DROP DATABASE IF EXISTS project;
CREATE DATABASE project;

USE project;
CREATE TABLE user (
    user_id INT AUTO_INCREMENT primary key NOT NULL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(80) ,
    role ENUM("client", "employee") DEFAULT "client",
    compte_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
    fk_task_id VARCHAR(50) NOT NULL,
    CONSTRAINT fk_user FOREIGN KEY (fk_user_id) REFERENCES user(user_id),
    CONSTRAINT fk_task FOREIGN KEY (fk_task_id) REFERENCES task(task_id)
);


CREATE TABLE commandes (
  commande_id INT AUTO_INCREMENT primary key NOT NULL,
  employee_id INT,
  devis VARCHAR(255),
  client_id INT,
  service_id INT,
  date_limite DATE,
  prix_tot FLOAT,
  CONSTRAINT fk_employee_id FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
  CONSTRAINT fk_client_id FOREIGN KEY (client_id) REFERENCES client(client_id),
  CONSTRAINT fk_service_id FOREIGN KEY (service_id) REFERENCES service(service_id)

);

CREATE TABLE services {
  service_id INT AUTO_INCREMENT primary key NOT NULL,
  nom VARCHAR(100) NOT NULL,
  prix FLOAT
};



