lista_prod = ["Mouse","headphone", "keyboard"] #Una lista con productos 
lista_precio = [10,150,15] #Una lista con los precios de los productos anteriores
print("Detalle:{} = {}".format(lista_prod[1],lista_precio [1])) #Imprimimos Un producto con su precio

tupla_salario = (2500000,5600000) #Definimos una tupla "salario" con elementos 0 y  1
print("Salario1:", tupla_salario[0]) #Imprimimos el elemento 0 de la tupla  

dic_prod = {"Presilladora":45000,"Pincel":7500,"Hoja A4":500} #Definimos un diccionario con productos   

print("Detalle: Pincel = {}".format (dic_prod["Pincel"])) #Llamamos al elemento 1 con su clave "Pincel"


#lista_precio.insert(0,5) # se inserta en lista de precio el valor 5 en la posicion 0
lista_precio[0] = 5
lista_prod.append("Cable USB") #append es para insertar
lista_precio.append(2) 

print(lista_prod)
print(lista_precio)