class operaciones():
    x = int(input("Dame un Numero"))
    y = int(input("Dame un Numero"))
    resultado = 0

    def suma(self):
        
        self.resultado=self.x+self.y

    def resta(self):
        self.resultado=self.x-self.y

    def multiplicacion(self):
        self.resultado = self.x*self.y

    def division(self):
        self.resultado = self.x/self.y

def main():
            
        num1 = int(input("Elige una Funcion 1. Suma, 2. Resta, 3.Division, 4.Multiplicacion, 5.Salir"))       
        if num1 == 1:  
            obj = operaciones()
            obj.suma()
            print(obj.resultado)
    
        elif num1 == 2:
            obj = operaciones()
            obj.resta()
            print(obj.resultado)

        elif num1 == 3:
            obj = operaciones()
            obj.multiplicacion()
            print(obj.resultado)

        elif num1 == 4:
            obj = operaciones()
            obj.division()
            print(obj.resultado)


if __name__ == "__main__":
        main()




