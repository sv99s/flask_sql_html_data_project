CREATE DATABASE videogames_review;
USE videogames_review;

CREATE TABLE videogames (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    anno INT,
    genere VARCHAR(100),
    voto INT,
    prezzo DECIMAL(6,2)
);