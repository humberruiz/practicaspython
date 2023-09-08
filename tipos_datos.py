#esto es una lista

dias_semana = ['lunes','Martes', 'Miercoles', 'Jueves', 'Viernes','Sabado', 'Domingo']

#imprimir los datos de una lista for
print("Dias de la semana")

for dia in dias_semana:
    print(dia)

#esto es un diccionario de alumnos con sus calificaciones
calificaciones = {"Pepe" : [2,3,4],"Juan": [3,4,4], "Moises": [4,3,5]}
print("Lista de alumnos")
for c in calificaciones:
        print(c)

print("Lista de alumnos con sus calificaciones")
for c in calificaciones:
      print(c,':', calificaciones[c])

print("Lista de alumnos con sus calificaciones")
for c in calificaciones:
    print(c)
    suma = 0  
    for i in calificaciones[c]:
          suma +=i
    print('prom: {0}'.format((suma/len(calificaciones[c]))))

#tuplas semejante a las listas pero inmutables
print('Meses del año')
meses = ('Enero', 'Febrero','Marzo','Abril', 'Mayo')
for mes in meses:
      print(mes)

#otra lista, y los metodos de las lista
precios = [4500,1200,3600,8000]
print(precios)
#agregar elementos a la lista
precios.append(900)
print(precios)

#quitar elementos segun posicion
precios.remove(1200)
print(precios)
#quitar el ultimo elemento
print(precios.pop())
print(precios)

