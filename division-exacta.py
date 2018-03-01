#Josué Laguna Alonso
#coding: utf8

dividendo = input ("Escriba el dividendo: ")
divisor = input ("Escriba el divisor: ")

if (dividendo % divisor) == 0:
    print "Division exacta, cociente: ",dividendo/divisor,
elif divisor == 0:
    print "No se puede dividir este numero"
else:
    print "Division no exacta, cociente: ",dividendo/divisor, "Residu: ",dividendo%divisor

