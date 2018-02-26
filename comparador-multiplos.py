#Josué Laguna Alonso
#26/02/18
#coding: utf8
import os
os.system ('clear')

print """
***********************
Comparador de Multiplos
***********************
"""

valor1 = input ("Escriba el primer numero entero positivo: ")
valor2 = input ("Escriba el segundo numero entero positivo: ")

if (valor1<=0 or valor2<=0):
  print "La operación no se puede realizar ya que son numeros negativos o no son multiples"
elif (valor1%valor2==0 and valor1>valor2):
  print valor1, "es mayor y es multiple de" ,valor2
elif (valor1%valor2==0 and valor1==valor2):
  print valor1, "los numeros son iguales y multiples de" ,valor2
elif (valor2%valor1==0 and valor2>valor1):
  print valor2 "es mayor y multiple de" ,valor1
elif (valor2%valor1==0 and valor2==valor1):
  print valor2, ",los numeros son iguales y multiples de" ,valor1
else:
  print valor1, "y" ,valor2, "no son multiples"
