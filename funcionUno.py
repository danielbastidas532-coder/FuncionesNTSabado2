#Declarar una funcion que permita crear una lista de N estudiantes
def crearListaEstudiantes(cantidadEstudiantes):
    estudiantes=[]
    for i in range(cantidadEstudiantes):
        estudiantes=[]
        for i in range(cantidadEstudiantes):
            estudiante={}
            estudiante["id"]=input("Ingrese el id del estudiante: ")
            estudiante["documento"]=input("Ingrese el documento del estudiante: ")
            estudiante["nombres"]=input("Ingrese los nombres del estudiante: ")
            estudiante["correoelectronico"]=input("Ingrese el correo electronico del estudiante: ")
            estudiante["telefono"]=input("Ingrese el telefono del estudiante: ")
            estudiante["promedio"]=float(input("Ingrese el promedio del estudiante: "))
            estudiante["semestre"]=input("Ingrese el semestre del estudiante: ")
            estudiante["esBecado"]=input("Ingrese si el estudiante es becado o no: ")

            estudiantes.append(estudiante)
    return estudiantes

#Invocando la funcion para crear una lista de estudiantes
cantidad=int(input("Ingrese la cantidad de estudiantes: "))
lista=crearListaEstudiantes(cantidad)
print(lista)
    