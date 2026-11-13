lista_numeros = []
Opcion = 0
while Opcion != 3:
    print("menu")
    print("1. Ordenar menor a mayor")
    print("2. Ordenar mayor a menor")
    print("3. Salir")
    Opcion = int(input("Ingrese una opción"))
    match Opcion:
        case 1:
            try:
                for i in range(10):
                    numeros =  int(input("Ingrese numero\n"))
                    lista_numeros.append(numeros)
                    lista_numeros.sort()
                print(f'aqui está la lista de numeros ordenados de menor a mayor {lista_numeros}')
            except:
                print("Valor invalido")
        case 2:
            print()
        case 3:
            break
        case _:
            print("Opcion error")