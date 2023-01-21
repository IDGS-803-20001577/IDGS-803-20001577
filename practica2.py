
num1 = int(input("Elige una Funcion 1. Suma, 2. Resta, 3.Division, 4.Multiplicacion, 5.Salir"))

def main():
    
    if num1 == 1:
        suma()
    
    elif num1 == 2:
        resta()

    elif num1== 3:
        division()

    elif num1 == 4:
        multiplicacion()

    elif num1 == 5:
        print("Bye")
        exit()

def suma():
        x = int(input("Dame un Numero"))
        y = int(input("Dame un Numero"))
        print(x + y)

def resta():
        x = int(input("Dame un Numero"))
        y = int(input("Dame un Numero"))
        print(x - y)

def multiplicacion():
        x = int(input("Dame un Numero"))
        y = int(input("Dame un Numero"))
        print(x * y)

def division():
        x = int(input("Dame un Numero"))
        y = int(input("Dame un Numero"))
        print(x / y)


if __name__ == "__main__":
    main()






