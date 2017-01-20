# Import flask and template operators
from flask import Flask, render_template, request, session, redirect, url_for, escape, request

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

#from app import app, bcrypt
from app import app
from app import db

#from models import Mascota
from models import MascotaDB1
from models import MascotaDB2
from models import MascotaDB3

from werkzeug.security import generate_password_hash, \
     check_password_hash

import hashlib

#from alembic import op
from sqlalchemy.sql import text
from sqlalchemy import union_all
from datetime import datetime

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

@app.route("/")
def index():
    return render_template('pages/index.html')

@app.route("/agregar")
def agregar():
    return render_template('pages/agregar.html')

@app.route('/agregarmascota', methods=['POST'])
def agregarmascota():

	nombreMascota     = request.form['nombreMascota']
	nombrePropietario = request.form['nombrePropietario']
	rutPropietario    = request.form['rutPropietario']
	fechaIngreso      = datetime.now()
	fechaRetiro       = 'null'
	edadMascota       = request.form['edadMascota']
	tipoMascota       = request.form['tipoMascota']

	# Broker
	totalBD  = 3
	stringID = rutPropietario

	hash_object = hashlib.sha1(stringID.encode())
	hex_dig     = hash_object.hexdigest()
	i           = int(hex_dig,16)
	idBaseDatos = i % totalBD

	# print(hex_dig)
	# print totalBD
	# print i
	# print idBaseDatos

	if (idBaseDatos==0):
		print "[DB1] Se insertara una mascota en la base de datos 1"
		mascota = MascotaDB1(nombreMascota,nombrePropietario,rutPropietario,fechaIngreso,fechaRetiro, edadMascota, tipoMascota)
		db.session.add(mascota)
		db.session.commit()
		print "[EXITO] Se inserta en la base de datos 1"
	elif (idBaseDatos==1):
		print "[DB2] Se insertara una mascota en la base de datos 2"
		mascota = MascotaDB2(nombreMascota,nombrePropietario,rutPropietario,fechaIngreso,fechaRetiro, edadMascota, tipoMascota)
		db.session.add(mascota)
		db.session.commit()
		print "[EXITO] Se inserta en la base de datos 2"
	elif (idBaseDatos ==2):
		print "[DB3] Se insertara una mascota en la base de datos 3"
		mascota = MascotaDB3(nombreMascota,nombrePropietario,rutPropietario,fechaIngreso,fechaRetiro, edadMascota, tipoMascota)
		db.session.add(mascota)
		db.session.commit()
		print "[EXITO] Se inserta en la base de datos 3"
	else:
		print "[ERROR] Ha ocurrido un error, no se ha podido agregar una mascota a alguna base de datos"
	return render_template('pages/agregar.html')

@app.route("/modificar")
def modificar():
    return render_template('pages/modificar.html')

@app.route("/eliminar")
def eliminar():
    return render_template('pages/eliminar.html')

@app.route('/listarmascotas')
def listar_mascotas():
	mascotas = MascotaDB1.query.all() + MascotaDB2.query.all() + MascotaDB3.query.all()
	return render_template('pages/listarmascotastodos.html',mascotas=mascotas)

@app.route('/listarmascotasDB1')
def listar_mascotasDB1():
	q        = MascotaDB1.query.all()
	mascotas = q
	return render_template('pages/listarmascotastodos.html', mascotas=mascotas)

@app.route('/listarmascotasDB2')
def listar_mascotasDB2():
	q        = MascotaDB2.query.all()
	mascotas = q
	return render_template('pages/listarmascotastodos.html', mascotas=mascotas)

@app.route('/listarmascotasDB3')
def listar_mascotasDB3():
	q        = MascotaDB3.query.all()
	mascotas = q
	return render_template('pages/listarmascotastodos.html', mascotas=mascotas)

@app.route('/mascotas/<nombremascota>')
def show_user(nombremascota):
	q       = Mascota.query.filter_by(nombremascota=nombremascota).first_or_404()
	mascota = q
	return render_template('pages/mostrarMascota.html', mascotas=mascotas)

@app.route('/consultar')
def indexConsultar():
	return render_template('pages/index_consultar.html')

@app.route('/consultarTipoForm')
def formConsultarTipo():
	return render_template('pages/consulta_tipo_form.html')

@app.route('/consultarNombreDuenoForm')
def formConsultarNombreDueno():
	return render_template('pages/form_consulta_nombredueino.html')

@app.route('/consultarRutDuenoForm')
def formConsultarRutDueno():
	return render_template('pages/form_consulta_rutdueno.html')

@app.route('/consultarNombreMascotaForm')
def formConsultarNombre():
	return render_template('pages/form_consulta_nombremascota.html')		

@app.route('/consultarTipo', methods=['POST'])
def consultarTipo():
	consulta = request.form['consultaTipoMascota']
	print "[EXITO] Consulta recibida con exito" 
	#print consulta
	#q1 = MascotaDB1.query.filter_by(mascota_tipo = consulta).all()
	#q2 = MascotaDB2.query.filter_by(mascota_tipo = consulta).all()
	#q3 = MascotaDB3.query.filter_by(mascota_tipo = consulta).all()
	mascotas =  MascotaDB1.query.filter_by(mascota_tipo = consulta).all() + MascotaDB2.query.filter_by(mascota_tipo = consulta).all() + MascotaDB3.query.filter_by(mascota_tipo = consulta).all()
	print "[EXITO] Consulta realizada con exito"
	#print mascotas
	return render_template('pages/listarmascotas.html', mascotas=mascotas)

@app.route('/consultarTipoPerro')
def consultarTipoPerro():
	consulta = 'perro'
	#q1 = MascotaDB1.query.filter_by(mascota_tipo = consulta).all()
	#q2 = MascotaDB2.query.filter_by(mascota_tipo = consulta).all()
	#q3 = MascotaDB3.query.filter_by(mascota_tipo = consulta).all()
	mascotas =  MascotaDB1.query.filter_by(mascota_tipo = consulta).all() + MascotaDB2.query.filter_by(mascota_tipo = consulta).all() + MascotaDB3.query.filter_by(mascota_tipo = consulta).all()
	return render_template('pages/listarmascotas.html', mascotas=mascotas)

@app.route('/consultarTipoGato')
def consultarTipoGato():
	consulta = 'gato'
	#q1 = MascotaDB1.query.filter_by(mascota_tipo = consulta).all()
	#q2 = MascotaDB2.query.filter_by(mascota_tipo = consulta).all()
	#q3 = MascotaDB3.query.filter_by(mascota_tipo = consulta).all()
	mascotas =  MascotaDB1.query.filter_by(mascota_tipo = consulta).all() + MascotaDB2.query.filter_by(mascota_tipo = consulta).all() + MascotaDB3.query.filter_by(mascota_tipo = consulta).all()
	return render_template('pages/listarmascotas.html', mascotas=mascotas)

@app.route('/consultarNombreDueno', methods=['POST'])
def consultarNombreDueno():
	consulta = request.form['consultaNombreDuenoMascota']
	print "[EXITO] Consulta recibida con exito" 
	mascotas =  MascotaDB1.query.filter_by(mascota_nombrePropietario = consulta).all() + MascotaDB2.query.filter_by(mascota_nombrePropietario = consulta).all() + MascotaDB3.query.filter_by(mascota_nombrePropietario = consulta).all()
	print "[EXITO] Consulta realizada con exito"
	return render_template('pages/listarmascotas.html', mascotas=mascotas)

@app.route('/consultarNombreMascota', methods=['POST'])
def consultarNombreMascota():
	consulta = request.form['consultaNombreMascota']
	print "[EXITO] Consulta recibida con exito" 
	mascotas =  MascotaDB1.query.filter_by(mascota_nombre = consulta).all() + MascotaDB2.query.filter_by(mascota_nombre = consulta).all() + MascotaDB3.query.filter_by(mascota_nombre = consulta).all()
	print "[EXITO] Consulta realizada con exito"
	return render_template('pages/listarmascotas.html', mascotas=mascotas)

@app.route('/consultarRutDueno', methods=['POST'])
def consultarRutDueno():
	consulta = request.form['consultaRutDuenoMascota']
	print "[EXITO] Consulta recibida con exito" 
	mascotas =  MascotaDB1.query.filter_by(mascota_rutPropietario = consulta).all() + MascotaDB2.query.filter_by(mascota_rutPropietario = consulta).all() + MascotaDB3.query.filter_by(mascota_rutPropietario = consulta).all()
	print "[EXITO] Consulta realizada con exito"
	return render_template('pages/listarmascotas.html', mascotas=mascotas)

@app.route('/actualizarDatosMascota')
def actualizarDatosMascota():
	dato_consulta_rut     = request.form['rutPropietario']
	newMascotaFechaRetiro = request.form['newMascotaFechaRetiro']
	newMascotaEdad        = request.form['newMascotaEdad']
	mascota = MascotaDB1.query.filter_by(mascota_rutPropietario=dato_consulta_rut).first() + MascotaDB2.query.filter_by(mascota_rutPropietario=dato_consulta_rut).first() + MascotaDB3.query.filter_by(mascota_rutPropietario=dato_consulta_rut).first()
	mascota.mascota_fechaRetiro = newMascotaFechaRetiro
	mascota.mascota_edad        = newMascotaEdad
	db.session.commit()
	return render_template('pages/actualizarDatosMascota.html')

@app.route('/BorrarMascota')
def BorrarMascota():
	dato_consulta_rut   = request.form['rutPropietario']
	dato_nombre_mascota = request.form['nombreMascota']
	mascota = MascotaDB1.query.filter_by(mascota_rutPropietario=dato_consulta_rut, mascota_nombre=dato_nombre_mascota).first() + MascotaDB2.query.filter_by(mascota_rutPropietario=dato_consulta_rut, mascota_nombre=dato_nombre_mascota).first() + MascotaDB3.query.filter_by(mascota_rutPropietario=dato_consulta_rut, mascota_nombre=dato_nombre_mascota).first()
	db.session.delete(mascota)
	db.session.commit()
	return render_template('pages/actualizarDatosMascota.html')