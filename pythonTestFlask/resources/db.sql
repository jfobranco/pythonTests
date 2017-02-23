CREATE DATABASE exercise CHARACTER SET 'utf8';
USE exercise;
CREATE TABLE contact (
	contact_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	firstname VARCHAR(50) NOT NULL,
	lastname VARCHAR(50) NOT NULL,
	email VARCHAR(255) NOT NULL,
	address VARCHAR(255),
	phone VARCHAR(30)
);

INSERT INTO contact (firstname, lastname, email, address, phone) VALUES ('Joao', 'Branco', 'jfobranco@gmail.com', 'Englisch-Gruss-Strasse, 32', '765893351');