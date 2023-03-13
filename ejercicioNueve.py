'''
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un numro de kilos y muestre por pantalla el precio de ese numero de kilos de fruta. si la fruta no esta debe mostrar mensaje de ello 
'''

frutas = {'Platano': 1.35,'Manzana': 0.80,'pera': 0.85,'naranja': 0.70}
fruta = input("Digite una fruta (platano,manzana,pera,naranja): ").title()
kg = float(input("Digite el numero de kilos que llevara: "))
if fruta in frutas:
    print(kg, 'kilos de', fruta,'vaken',frutas[fruta]*kg, '$')
else:
    print(f"lo siento la fruta {fruta}, no esta disponible")