# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

print "[CONECTANDO] Conectando a las 3 bases de datos"
databases = {
    'mysql_db1': 'mysql://root:root@localhost/db1_hotelmascota',
    'mysql_db2': 'mysql://root:root@localhost/db2_hotelmascota',
    'mysql_db3': 'mysql://root:root@localhost/db3_hotelmascota'
}

app.config['SQLALCHEMY_BINDS'] = databases
app.config.from_object('config')
app.config['MYSQL_DATABASE_USER']     = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = "root"

print "[EXITO] Se ha conectado a ", 'mysql_db1'
print "[EXITO] Se ha conectado a ", 'mysql_db2'
print "[EXITO] Se ha conectado a ", 'mysql_db3'

print '[EXITO] Se ha conectado a las 3 bases de datos'

db  = SQLAlchemy(app)

from app import models, views

#db.create_all()