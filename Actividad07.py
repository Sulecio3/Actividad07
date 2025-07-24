def pedirDatos (lista):
    pedirNum = int(input("Ingrese la cantidad de numeros que quiere ingresar: "))
    for i in range(pedirNum):
        numero = int(input("Ingrese sus numeros: "))
        lista.append(numero)

def suma(numeros):
    suma = 0
    for i in numeros:
        suma += i
    return suma

def promedio(numeros):
    return suma(numeros)/len(numeros)

def numeroMayorMenor(listaNum):
    mayor = max(listaNum)
    menor = min(listaNum)
    return print(f"El numero mayor es: {mayor} y el numero menor es: {menor}")

def positivoNegativoCero (numeros):
    positivos = 0
    negativos = 0
    ceros = 0
    for i in numeros:
        if i > 0:
            positivos +=1
        elif i <0:
            negativos += 1
        else:
            ceros +=1
    return print(f"La cantidad de numeros positivos es: {positivos} de negativos: {negativos} y de ceros {ceros}")

def multiplos3(numeros):
    multiplos = 0
    for i in numeros:
        if i % 3 == 0:
            multiplos +=1
    return print(f"Hay {multiplos} multiplos de 3 en tu lista")

while True:
    print("--Bienvenido al Menu--")
    print("1. Suma, promedio, cantidad  de numeros positivos y negativos y  ceros y cuantos son multiplos de 3")
    print("2. Area y perimetro de un rectangulo")
    print("3. Verificar si el numero es primo o no")
    print("4. calcular el promedio")
    print("5. Mostrar cual es el mayor, menor y cuantos se repiten")
    print("6. caluculador")
    print("7. Salir")
    option = input("ingrese la opcion en la que quiera entrar: ")
    match option:
        case "1":
            listaNumeros = []
            pedirDatos(listaNumeros)
            print(f"La suma de todos sus numeros es: {suma(listaNumeros)}")
            print(f"El promedio de todos sus numeros es: {promedio(listaNumeros)}")
            positivoNegativoCero(listaNumeros)
            multiplos3(listaNumeros)
            input("")
        case "2":
            print("hola")
        case"3":
            print("hola")
        case "4":
            print("hola")
        case "5":
            print("hola")
        case "6":
            print("hola")
        case "7":
            print("Saliendo del programa")
            break
        case _:
            print("opcion no valida, intente de nuevo")
            input("")