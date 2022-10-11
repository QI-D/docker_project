CREATE DATABASE orders;

USE orders;

CREATE USER 'mysql_user'@'%' IDENTIFIED BY 'SecuRe_pwd1';
GRANT ALL PRIVILEGES ON orders.* TO 'mysql_user'@'%';

CREATE TABLE IF NOT EXISTS user
          (id INT NOT NULL AUTO_INCREMENT, 
          username VARCHAR(250) NOT NULL,
          password VARCHAR(250) NOT NULL,
          PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS expense
          (id INT NOT NULL AUTO_INCREMENT,
           order_id VARCHAR(36) NOT NULL,
           item_id VARCHAR(36) NOT NULL,
           item_name VARCHAR(250) NOT NULL,
           quantity INTEGER NOT NULL,
           price DECIMAL NOT NULL,
           timestamp VARCHAR(100) NOT NULL,
           date_created VARCHAR(100) NOT NULL,
           trace_id VARCHAR(36) NOT NULL,
           PRIMARY KEY (id));