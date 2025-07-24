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

def numeroMayorMenor(listaNum):
    mayor = max(listaNum)
    menor = min(listaNum)
    repitentes = 0
    for i in listaNum:
        if i == listaNum[0]:
            repitentes +=1
    return print(f"El numero mayor es: {mayor} el numero menor es: {menor}, se repiten {repitentes} numeros")

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

def sum(a,b):
    return print(f"La suma de {a} + {b} da como resultado: {a+b}")

def resta(a,b):
    return print(f"La resta de {a} - {b} da como resultado: {a-b}")

def multi(a,b):
    return print(f"La multiplicacion de {a} x {b} da como resultado: {a*b}")

def divi(a,b):
    if b == 0:
        return print("No se puede dividir dentro de 0")
    else:
        return print(f"La division de {a} / {b} da como resultado: {a/b}")

while True:
    print("--Bienvenido al Menu--")
    print("1. Suma, promedio, cantidad  de numeros positivos y negativos y  ceros y cuantos son multiplos de 3")
    print("2. Area y perimetro de un rectangulo")
    print("3. Verificar si el numero es primo o no")
    print("4. calcular el promedio")
    print("5. Mostrar cual es el mayor, menor y cuantos se repiten")
    print("6. caluculadora")
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
            input("")
        case "5":
            listaNumeros = []
            pedirDatos(listaNumeros)
            numeroMayorMenor(listaNumeros)
            input("")
        case "6":
            print("Bienvenido a la calculadora basica")
            print("Como primer punto ingrese sus 2 numeros")
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            while True:
                print("1. Suma")
                print("2. Resta")
                print("3. Multiplicacion")
                print("4. division")
                print("5. Salir")
                option = input("Ingrese la opcion que quiere realizar con sus dos numeros: ")
                match option:
                    case "1":
                        sum(num1,num2)
                        input("")
                    case "2":
                        resta(num1,num2)
                        input("")
                    case "3":
                        multi(num1, num2)
                        input("")
                    case "4":
                        divi(num1, num2)
                        input("")
                    case "5":
                        print("Saliendo del programa")
                        break
                    case _:
                        print("Opcion no valida")
                        input("")

        case "7":
            print("Saliendo del programa")
            break
        case _:
            print("opcion no valida, intente de nuevo")
            input("")