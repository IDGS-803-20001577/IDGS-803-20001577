
num1 = int(input("Dame un Numero"))

def tablaMultiplicar():
    contador = 1

    while contador < 11:
        print ("{} * {} = {}".format(num1,contador,(num1*contador)))
        contador = contador +1
        

tablaMultiplicar()
