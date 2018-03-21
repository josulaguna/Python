#coding: utf8
#Josué Laguna Alonso

salir = "N"
numero = 1
maximo = 5
suma = 0

while (salir == "N"):
    #Hago cosas
    print numero,
    
    if (numero <= maximo - 1):
        print "+",
    suma = suma + numero
    #Incremento
    numero = numero + 1
    
    #Activo indicador de salida si toca
    if (numero > maximo): #condicion de salida
        salir = "S"
  
#Post bucle
print "=", suma
