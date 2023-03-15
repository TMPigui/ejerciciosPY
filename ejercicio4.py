'''
Una panaderia vende barras de pan a 10.5 cada una

. el pan que no es del mismo dia tiene un descuento del 60% escribir un programa que comienze leyendo un numero de barras de pan vendidas que no son del dia. Despues el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresco y el costo final
'''

numPan = float(input(f"Digite cuantos panes de la promo llevara: "))
costoPan = 10.6
rebaja = 0.6
totalPagar = numPan * costoPan -(1 - rebaja)
print(f"El costo del pan fresco es {costoPan} y la rebaja es de un {rebaja} para un total de {totalPagar}")