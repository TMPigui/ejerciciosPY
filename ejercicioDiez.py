'''
Escribir un programa que almacene las asignaturas de un curso en una lista(Matemáticas, Física, Química, Historia y Lengua), pregunte la nota que a sacado en cada asignatura, despues la muestre por pantalla con el mensaje  En <asignatura> has sacado <nota> donde <asignatura> 
'''


materias = ['Matematicas','Fisica','Quimica','Historia','Lengua']
notas = []

for materia in materias:
    nota = input(f"Digite la nota de {materia}:  ")
    notas.append(nota)

for i in  range(len(materias)):
    print("En " + materias[i] + " has sacado " + notas[i])

