'''Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla calculado redondeado con dos decimales.'''

peso = input("Digite el peso en kg: ")
altura = input("Digite su altura en cm: ")
imc = float(peso)/float(altura)**2,2
print(f"su indice de imc es: {imc}")