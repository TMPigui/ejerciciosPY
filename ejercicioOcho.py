'''Escribir un programa que guarde en una vaiable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una diva y muestre un simbolo o uun mensaje de aviso si la divisa no esta en el diciionario'''

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
#eltitle() convierte primera letra de cada palabra de cadena a mayúsculas.
if moneda.title() in monedas:
    print(f"la divisa de la moneda {moneda} es {monedas[moneda.title]}")
else:
    print("La divisa no se encuentrad")

'''
Forma con el metodo get
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))
'''