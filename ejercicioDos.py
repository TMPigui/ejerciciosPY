''' 
Escribir un programa que pregunte al usuario los numeros ganadores de la loteria,
que los alamacene en una lista y los muestre ordenados de menor a mayor
'''

canGanadores = int(input(f"Digite cuantos numeros de loyeria ganaron: "))

ganadores = []
for i in range(canGanadores):
    #append agrega el elemento al final
    ganadores.append(int(input(f"Digite un numero ganador: ")))
ganadores.sort()
print(f"Los numeros ganadores son: {ganadores}")