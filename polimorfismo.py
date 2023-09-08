class Persona:
    nombre = None 
    def __init__(self,nombre):
        self.nombre = nombre
    def avanza(self):
        return "Estoy caminando"

class Ciclista(Persona):
    def __init__(self,nombre):
        super().__init__(nombre)
    
    def avanza(self):
        return "Estoy andando en vini"

cicli = Ciclista("moises")

print(cicli.avanza())
print(per.avanza())