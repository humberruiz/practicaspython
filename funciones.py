lista = []

def cargar_lista(valor):
    if valor > 0:
        lista.append(valor)
    else:
        print("no puede ser cero")
    lista.append(valor)

def imprimir_lista():
    for x in lista:
        print("|", x )
        
if _name_=="_main_":        
cargar_lista(7)
cargar_lista(56)
cargar_lista(23)
imprimir_lista()

