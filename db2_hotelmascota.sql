
CREATE DATABASE db2_hotelmascota;

USE db2_hotelmascota;

CREATE TABLE mascota_db2 (
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

INSERT INTO mascota_db2 (mascota_nombre, mascota_nombrePropietario, mascota_rutPropietario, mascota_fechaIngreso,  mascota_fechaRetiro, mascota_edad,  mascota_tipo)
VALUES ('blanca_db2','maria','18045598-1','2015-08-01','null', 15, 'tortuga');