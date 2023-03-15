''' Imagina que acabas de abrir una cuenta de ahorros que te ofrece el 4% de interes al año. estos   ahorros debido a intereses, que no se cobran hasta finales del año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comienze leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducidd por el usuario. Despues el programa debe mostrar y calcular por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales'''

inversion = float(input("Introduca la inversion inicial: "))
interes = 0.04
balance1  = inversion * (1 + interes)
print(f"balance tras el primer año:  {balance1, 2}")
balance2 = balance1 * (1 + interes)
print(f"balance tras el primer año:  {balance2, 2}")
balance3 = balance2 * (1 + interes)
print(f"balance tras el primer año:  {balance3, 2}")
