from app import db
#from app import db1
#from app import db2
#from app import db3
from datetime import datetime
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from flask.views import View

Base = declarative_base()

# Base de datos 1
class MascotaDB1(db.Model):
	__tablename__ = 'mascota_db1'
	__bind_key__  = 'mysql_db1'
	mascota_id                = db.Column(db.Integer, primary_key=True)
	mascota_nombre            = db.Column(db.String(80))
	mascota_nombrePropietario = db.Column(db.String(80))
	mascota_rutPropietario    = db.Column(db.String(80))
	mascota_fechaIngreso      = db.Column(db.DateTime)
	mascota_fechaRetiro       = db.Column(db.DateTime)
	mascota_edad              = db.Column(db.Integer)
	mascota_tipo              = db.Column(db.String(20))

	def __init__(self, mascota_nombre, mascota_nombrePropietario,
		         mascota_rutPropietario, mascota_fechaIngreso, mascota_fechaRetiro,
		         mascota_edad, mascota_tipo):
		self.mascota_nombre            = mascota_nombre
		self.mascota_nombrePropietario = mascota_nombrePropietario
		self.mascota_rutPropietario    = mascota_rutPropietario
		self.mascota_fechaIngreso      = mascota_fechaIngreso
		self.mascota_fechaRetiro       = mascota_fechaRetiro
		self.mascota_edad              = mascota_edad
		self.mascota_tipo              = mascota_tipo


	def __repr__(self):
		return '<Mascota %r>' % self.mascota_nombre

# Base de datos 2
class MascotaDB2(db.Model):
	__tablename__ = 'mascota_db2'
	__bind_key__  = 'mysql_db2'
	mascota_id                = db.Column(db.Integer, primary_key=True)
	mascota_nombre            = db.Column(db.String(80))
	mascota_nombrePropietario = db.Column(db.String(80))
	mascota_rutPropietario    = db.Column(db.String(80))
	mascota_fechaIngreso      = db.Column(db.DateTime)
	mascota_fechaRetiro       = db.Column(db.DateTime)
	mascota_edad              = db.Column(db.Integer)
	mascota_tipo              = db.Column(db.String(20))

	def __init__(self, mascota_nombre, mascota_nombrePropietario,
		         mascota_rutPropietario, mascota_fechaIngreso, mascota_fechaRetiro,
		         mascota_edad, mascota_tipo):
		self.mascota_nombre            = mascota_nombre
		self.mascota_nombrePropietario = mascota_nombrePropietario
		self.mascota_rutPropietario    = mascota_rutPropietario
		self.mascota_fechaIngreso      = mascota_fechaIngreso
		self.mascota_fechaRetiro       = mascota_fechaRetiro
		self.mascota_edad              = mascota_edad
		self.mascota_tipo              = mascota_tipo

	def __repr__(self):
		return '<Mascota %r>' % self.mascota_nombre

# Base de datos 3
class MascotaDB3(db.Model):
	__tablename__ = 'mascota_db3'
	__bind_key__  = 'mysql_db3'
	mascota_id                = db.Column(db.Integer, primary_key=True)
	mascota_nombre            = db.Column(db.String(80))
	mascota_nombrePropietario = db.Column(db.String(80))
	mascota_rutPropietario    = db.Column(db.String(80))
	mascota_fechaIngreso      = db.Column(db.DateTime)
	mascota_fechaRetiro       = db.Column(db.DateTime)
	mascota_edad              = db.Column(db.Integer)
	mascota_tipo              = db.Column(db.String(20))

	def __init__(self, mascota_nombre, mascota_nombrePropietario,
		         mascota_rutPropietario, mascota_fechaIngreso, mascota_fechaRetiro,
		         mascota_edad, mascota_tipo):
		self.mascota_nombre            = mascota_nombre
		self.mascota_nombrePropietario = mascota_nombrePropietario
		self.mascota_rutPropietario    = mascota_rutPropietario
		self.mascota_fechaIngreso      = mascota_fechaIngreso
		self.mascota_fechaRetiro       = mascota_fechaRetiro
		self.mascota_edad              = mascota_edad
		self.mascota_tipo              = mascota_tipo

	def __repr__(self):
		return '<Mascota %r>' % self.mascota_nombre