#Josué Laguna Alonso
#coding: utf8
import time
salir = "N"
numero = 1 
numeromax2 = input ("Hasta que numero quieres que cuente?")
while (salir=="N"):
	#Hago cosas
	print "informe año: ",numero
    
	#Incremento
	numero = numero +1
	time.sleep(0.1)
	# Activo indicador de salida si toca
	if (numero>numeromax2): # Condición de salida
    	    salir = "S"    	    
