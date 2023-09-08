class Calculadora:
    historial = None 
    numero_1 = None
    numero_2 = None

    def __init__(self,n1,n2):
        self.historial = []
        self.numero_1 = n1
        self.numero_2 = n2

    def suma(self):
        return self.numero_1 + self.numero_2

    def resta(self):
        return self.numero_1 - self.numero_2

        

if __name__ == "__main__":
    calc = Calculadora(10,20)
    x = calc.suma()
    print("La suna es: ", x)