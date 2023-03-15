'''Escribir un programa que pida al usuario dos numeros enteros y muestre por pantalla el cosiente de los dos numeros agregados y el resto que sobra '''

n1 = input("Introduca el dividiendo (entero): ")
n2 = input("Introduca el divisor (entero): ")
print(f"{n1} entre {n2} da un cociente {int(n1) // int(n2)} y un resto de {int(n1) % int(n2)}")
print(f"el resto que sobra es {int(n1) % int(n2)}")