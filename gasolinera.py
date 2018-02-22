#Josué Laguna Alonso
#22/02/18
#coding: utf8
import os
os.system ("clear")

print """
******************************************
| Tipos: Super normal = 1                |
|        Super turbo = 2                 |
|        Sin plomo normal = 3            |
|        Sin plomo con aditivos = 4      |
|        Diesel normal = 5               |
|        Diesel Fast&Furius = 6          |
******************************************
"""

tipo = input ("Que tipo de gasolina quiere? ")
litros = input ("Cuantos litros quiere? ")

if (tipo == 1):
    print "Ha elegido la super normal, cantidad de litros:", litros ,"litros. Importe: ", litros * 1.5, "euros"
if (tipo == 2):
    print "Ha elegido la super turbo, cantidad de litros:", litros ,"litros. Importe: ", litros * 1.55, "euros"
if (tipo == 3):
    print "Ha elegido la sin plomo normal, cantidad de litros:", litros ,"litros. Importe: ", litros * 1.6, "euros"
if (tipo == 4):
    print "Ha elegido la sin plomo con aditivos, cantidad de litros:", litros ,"litros. Importe: ", litros * 1.65, "euros"
if (tipo == 5):
    print "Ha elegido la diesel normal, cantidad de litros:", litros ,"litros. Importe: ", litros * 1.7, "euros"
if (tipo == 6):
    print "Ha elegido la diesel Fast&Furius, cantidad de litros:", litros ,"litros. Importe: ", litros * 1.75, "euros"
