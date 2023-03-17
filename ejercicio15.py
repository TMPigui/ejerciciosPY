'''
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
'''


option = 1

facturas = []

while option != 1:
    print('**********Credito CasaCoronaMarinilla ***********')
    print('******opcion 1 = Ingrese una nueva factura ******')
    print('*****opcion 2 = Pagar o abonar a una factura ****')
    print('********opcion 3 = Pagar prestamo tota l*********')
    print('***********opcion 4 = SALIR *********************')

    option = int(input("Escoja una de las opciones: "))

if(option == 1):
        factura = {}
        factura['id'] = int(input('Agregue el identificador de la factura: '))
        factura['costo'] = float(input('Digite el costo de la factura: '))
        facturas.append(factura)
        print('FACTURA REGISTRADA CON EXITO')
        print(f'La deuda total es: {factura}')

elif(option == 2):
    pagarFac = int(input('Digite el identificador de la factura: '))
    for factura in facturas:
        if(factura[id] == pagarFac):
                factura.pop()
                print('factura eliminada con exito: ')
        else:
                print('factura no encontrada...')
                



