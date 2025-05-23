create database veterinaria;
use veterinaria;

CREATE TABLE mascotas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_mascota VARCHAR(100) NOT NULL,
    especie VARCHAR(50) NOT NULL,
    raza VARCHAR(100),
    edad INT NOT NULL,
    nombre_duenio VARCHAR(100) NOT NULL
);