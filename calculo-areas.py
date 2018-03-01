#coding: utf8
import os
os.system ("clear")
from math import pi

print """
 ********************
 Calculadora de áreas
 ********************
 
 a) Triángulo
 b) Círculo
 
"""
 
figura = raw_input ("¿Qué figura quiere calcular (Escriba T o C)? ")

if (figura == "T"):
    base = input ("Escriba la base: ")
    altura = input ("Escriba la altura: ")
    if (base >=0 and altura >=0):
        print "Un triangulo de base",base, "y de altura",altura, "tiene un área de ",base*altura/2
    else:
        print "No se puede calcular, ya que hay números negativos"

if (figura == "C"):
    radio = input ("Escriba el radio: ")
    if (radio >=0):
        print "El radio es",radio, "y tiene un área de " ,2*pi*radio

