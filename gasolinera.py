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
	print "Ha elegido la super normal, y ha elegido", litros "litros"

