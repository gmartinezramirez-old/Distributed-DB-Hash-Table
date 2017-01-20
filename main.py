#!/usr/bin/env python
# -*- coding: utf-8 -*-
# main.py

#BD utilizada: MongoDB

from pymongo import MongoClient






# Bloque principal

ans=True
while ans:
	print('Menu')
	print('------------------')
	print ("""
	1. Insertar dato.
	2. Buscar dato.
	3. Salir.
	""")
	ans=raw_input("Que le gustaría hacer? ") 
	if ans=="1": 
		print("\n Insertar dato") 
	elif ans=="2":
		print("\n Buscar dato") 
	elif ans=="3":
		print("\n Adios") 
	elif ans !="":
		print("\n Opción no válida intente de nuvo") 