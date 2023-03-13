'''
    id,nombre,precio,popularida,fechavencimiento
    Ingresar una empanada
    Mostrar todas ls empandas 
    buscar empanada por id
    editar una empanada por id (precio)
    eliminar 1 empanada por id
'''
option = 1

empanadas = []

while option != 0:
    print('*******Empanadas el canibal**********')
    print('Opcion 1 = Ingresar una empanada')
    print('Opcion 2= Mostrar todas las empanadas')
    print('Opcion 3= Buscar empanadas por un id')
    print('Opcion 4 = Editar empanada por id')
    print('Opcion 5 = Eliminar empanada')
    print('Presione 0 para salir')

    option = int(input("Escoja una opcion: "))

    if(option == 1):
        empanada = {}
        empanada = [id] = int(input('Digite el id de la empanada: ')),
        empanada = [nombre] = input('Digite el nombre de la empanada: '),
        empanada = [precio] = float(input('Digite el precio de la empanada: ')),
        empanada = [popularidad] = int(input('Digite la popularidad de la empanada: ')),
        empanada = [fechavencimiento] = input('Digite la fecha de vencimiento de la empanada: '),
        empanadas.append(empanada)
        print('Empanada registrada...')

    elif(option == 2):
        for empanada in empanadas:
            print(empanada)
    elif(option == 3):
        empanadaBuscar = int(input('Ingrese el id de la empanada a buscar: '))
        for empanada in empanadas:
            if(empanada['id'] == empanadaBuscar):
                print(f'existe {empanada}')
            else:
                print('empanada encontrada')
    elif(option == 4):
        empanadaBuscar = int(input('Ingrese el id de la empanada a buscar: '))
        for empanada in empanadas:
            if(empanada['id'] == empanadaBuscar):
                print(f'El precio actual es {precio}')    
            else:
                print('empanada encontrada')
    elif(option == 5):
        empanadaEliminar = int(input('Ingrese el id de la empanada a eliminar: '))
        for empanada in empanadas:
           if(empanada['id'] == empanadaEliminar):
                empanada.remove()         
    elif(option == 0):
        pass
    else:
        print("Opcion invalidad  ")

