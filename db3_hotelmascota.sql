
CREATE DATABASE db3_hotelmascota;

USE db3_hotelmascota;

CREATE TABLE mascota_db3 (
   mascota_id INT NOT NULL AUTO_INCREMENT,
   mascota_nombre VARCHAR(100) NOT NULL,
   mascota_nombrePropietario VARCHAR(40) NOT NULL,
   mascota_rutPropietario VARCHAR(40) NOT NULL,
   mascota_fechaIngreso DATE,
   mascota_fechaRetiro DATE,
   mascota_edad INT NOT NULL,
   mascota_tipo VARCHAR(100) NOT NULL,
   PRIMARY KEY ( mascota_id )
);

INSERT INTO mascota_db3 (mascota_nombre, mascota_nombrePropietario, mascota_rutPropietario, mascota_fechaIngreso,  mascota_fechaRetiro, mascota_edad,  mascota_tipo)
VALUES ('ringo_db3','Carolina','17891999-k','2008-08-01','2009-08-10', 20, 'perro');