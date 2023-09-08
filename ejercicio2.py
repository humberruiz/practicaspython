###Variable

texto = "Curso de Pogramacion de Python"
print(texto)

numero_entero = 2023
print(numero_entero)

#la funcion type() retorna el tipo de dato de la variable
edad = 25
print("Edad es un tipo de dato", type (edad))

#variable booleadno True or false
acceso = False
print("Acceso es igual a ", acceso)

# se pueden definir variables en una sola linea
nombre, apellido, edad = "Moises", "Avalos", 34
print("Hola, soy:", nombre, apellido,".Tengo:", edad, "años")

#Inputs

nombre = input('¿Cuál es tu nombre?  ')
edad = input ('¿Cuántos años tienes?')

print("Hola{}, veo que tienes {} años".format(nombre,edad))
