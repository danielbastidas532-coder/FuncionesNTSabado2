#Crear una funcion que reciba una lista de numeros enteros y calcule su promedio para retornarlo

import random

def calcularPromedio(notas):
    #Como recorrer una lista en python
   """  suma=0
    for nota in notas:
        print(nota)
        suma+=nota
    promedio=suma/len(notas)
    return promedio
 """
   promedio=sum(notas)/len(notas)
   return promedio


notas=[1,1,2]
calcularPromedio(notas) 

