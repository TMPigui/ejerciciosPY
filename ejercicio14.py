'''
Escribir in programa que almacene en una lista los sgte precios, 50,75,46,22,80,65,8, y muestre el menor y mayor
'''

listaNumeros = [50,75,46,22,80,65,8]
min = max = listaNumeros[0]

for numero in listaNumeros:  
    if numero < min:
        min = numero
    elif numero > max:
        max = numero
print(f"El maximo es {max} y el minimo es {min}")

