
CREATE DATABASE db1_hotelmascota;

USE db1_hotelmascota;

CREATE TABLE mascota_db1 (
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

INSERT INTO mascota_db1 (mascota_nombre, mascota_nombrePropietario, mascota_rutPropietario, mascota_fechaIngreso,  mascota_fechaRetiro, mascota_edad,  mascota_tipo)
VALUES ('negro_db1','john','18045598-0','2015-08-01','2015-08-10', 15, 'gato');