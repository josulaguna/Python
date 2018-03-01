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
        print "Un triangulo de base",base, "y de altura",altura, "tiene un área de"



if (figura == "C"):
    radio = input ("Escriba el radio: ")
    if (radio >=0):

