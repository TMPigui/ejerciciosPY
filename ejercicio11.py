'''
Escribir un programa que pida unos numeors, los almacene en una lista y los imprima de menor a mayor y de mayor a menor
'''
numeroGan = []
for i in range(6):
    numeroGan.append(int(input("Introduce un numero ganador: ")))
numeroGan.sort()
print(f"Los numeros ganadores de menor a mayor son son: {str(numeroGan)}")
numeroGan.reverse()
print(f"Los numeros ganadores de mayor a menor son son: {str(numeroGan)}")



