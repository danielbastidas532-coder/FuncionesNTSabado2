#Crear una funcion que de forma aleatoria crea una lista de N
#notas (enteras) y devuelve la lista

import random



def crearLista(cantidad):
         notas=[]
         for i in range(cantidad):
             nota=random.randint(1,5)
             notas.append(nota)
         return notas
cantidad=int(input("Ingrese la cantidad de notas: "))
lista=crearLista(cantidad)
print(lista)
