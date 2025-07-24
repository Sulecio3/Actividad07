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

def area(a,b):
    return print(f"El area de su rectangulo es: {a*b}")

def perimetro(a,b):
    return print(f"El perimetro de su rectangulo es: {(2*a)+(2*b)}")

def promedio(numeros):
    return suma(numeros)/len(numeros)

def numeroMayorMenor(listaNum):
    mayor = max(listaNum)
    menor = min(listaNum)
    return print(f"El numero mayor es: {mayor} y el numero menor es: {menor}")

def zonaRisego(lista):
    mayores85 = 0
    menores60 = 0
    for i in lista:
        if i >= 85:
            mayores85 += 1
        elif i < 60:
            menores60 +=1
    return print(f"Las calificaciones mayores o iguales a 85 son: {mayores85} y las que estan en zona de reisgo son: {menores60}")

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

def numPrimo(numero):
    if numero <= 1:
        print(f"{numero} no es un número primo")
    else:
        for i in range(2, numero):
            if numero % i == 0:
                print(f"{numero} no es un número primo")
                break
        else:
            print(f"{numero} es un número primo")

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
            base = int(input("Ingrese la base del rectangulo: "))
            altura = int(input("Ingrese la altura del rectangulo: "))
            area(base,altura)
            perimetro(base, altura)
            input("")
        case"3":
            numero = int(input("Ingrese el numero que quiere evaluar: "))
            numPrimo(numero)
            input("")
        case "4":
            calificaciones = []
            pedirDatos(calificaciones)
            print(f"El prommedio de sus caificaciones es {promedio(calificaciones)}")
            zonaRisego(calificaciones)
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