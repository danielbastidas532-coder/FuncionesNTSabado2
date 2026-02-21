#Como puedo crear 200 notas de 1 a 5 en python 
#sin pedir los datos al usuario y sin quemar los datos manualmente 
import random
notas=[]
for i in range(5):
    nota=random.randint(1,5)
    notas.append(nota)

notas.insert(0,90)
notas.insert(1,90)
notas.remove(90)
notas.pop(0)
notas.sort()
notas.clear()
print(notas)