# README #

### Objetivo ###

* Diseñar e implementar un sistema de bases de datos distribuidas dada una función hash.

### Explicación ###

* Realizar un sistema que distribuya la inserción de datos de una BD, y que pueda también realizarse una búsqueda a donde sea necesario.

* Existirá un *broker* que estará encargado de aplicar una función *hash* a lo que se desee en la tupla o/y tabla que se vaya a insertar.

* Al momento que se desea insertar se aplicará esta función *hash*, para saber a cual de las BD disponibles debe insertar.

* Ejemplo: Puede aplicarse una función *hash* SHA-1 y luego aplicarle el módulo de la cantidad de servidores disponibles, de esta manera dará un número entre [0,n-1], donde *n* es la cantidad de servidores disponibles, como se muestra en el siguiente algoritmo.

* En el momento de la búsqueda, el *broker* deberá consultar la misma consulta a cada una de las BD.

* Luego, se realizará un *join* de todas las respuestas entregadas de las distintas BD, y será mostrar por la interfaz implementada.

### Puntajes ###

* Establecer conexión entre las BD y el broker. (2 ptos)
* Insertar una tupla según la función *hash*. (2 ptos)
* Realizar consultas simples a la BD. (2 ptos)

### Requerimientos ###

* Python 2.7.6
* MongoDB 3.0.2
* Mínimo 3 BD disponibles para la inserción de datos, todas debe ser con el mismo motor de BD.
* Conector de Python con MongoDB: SQLALCHEMY

### Instalación de paquetes necesarios ###

* Para instalar lo necesario:

* Flask
* pip install -r requirements.txt

### Ejecución ###

* Situarse en la carpeta principal del proyecto
* Escribir en la terminal: python run.py
* La aplicación esta corriendo en el puerto 5000: http://localhost:5000/
