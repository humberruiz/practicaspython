materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
#recorrer materias como materia
for materia in materias:
    calificacion = input("¿Que notas haz sacado en " + materia + "?")
    notas.append(calificacion)
for i in range(len(materias)):
    print("En " + materias [i] + " has sacado  " + notas[i])


persona = {}
continuar = True
while continuar:
    #puedes cargar cualquier dato sobre una persona en el formato clave:valor
    clave = input("¿Que valor quieres introducir? ")
    valor = input(clave + ':')
    persona[clave] = valor
    print(persona)
    #Tienes que escribir Si para continuar, en cualquier caso es False
    continuar = input('¿Quierse añadir mas informacion (Si/No)?') == "Si"

canasta = {}
continuar = True
while continuar:
    item = input('Introduce un articulo : ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    canasta[item] = precio
    #para continuar se debe escribir si
    continuar = input('¿Quieres añadir articulos a la lista (si/no)?') == "si"
coste = 0
print('Lista de compra')
for item, precio in canasta.items():
    print(item, '\t', precio)
    coste += precio
print('Coste total: ', coste)

