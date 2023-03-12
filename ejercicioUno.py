'''
Leer 20 números enteros y guardar en una lista, después permitir
que el usuario busque un número y si este se encuentra en la lista
indicar con un mensaje que el resultado es exitoso
'''

canNum = int(input(f"Digite la cantidad de numeros a ingresar: "))
num = []
for i in range(canNum):
    num.append((input("Digite un numero: ")))
numeroUsuario = int(input(f"Digite el numero a buscar: "))

print(num)


