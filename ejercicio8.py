'''Escribir un programa que guarde en una vaiable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una diva y muestre un simbolo o uun mensaje de aviso si la divisa no esta en el diciionario'''

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
#metodo get se utiliza para tneer valores entre claves en diccionarios
print(monedas.get(moneda.title(), "La divisa no se ncuentra en nustros archivos intente con otra"))

'''
eltitle() convierte primera letra de cada palabra de cadena a mayúsculas.
if moneda.title() in monedas:
    print(f"la divisa de la moneda {moneda} es {monedas[moneda.title]}")
else:
    print("La divisa no se encuentrad")


monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))
'''