#coding: utf8
#Josué Laguna Alonso

salir = "N"
numero = 1
maximo = 5
suma = 0

if maximo <= 0:
    print "Error"
    
while (salir == "N"):
    #Hago cosas
    if (numero%2==0):
        print numero,
    if (numero == maximo -2):
        print "+",
        
    suma = (suma + numero)
    #Incremento
    numero = (numero + 1)
    
    #Activo indicador de salida si toca
    if (numero > maximo):
        salir = "S"
        
#Post bucle
print "=", numero
