# Operadores aritmeticos
#Imprimir la suma de 3+4

print("La suma de 3 + 4 es:", 3 + 4)

#Resolver todas las operaciones : 10-4 ,10*4, 10/4, 10%4, 10//4, 10**4
resta = 10-4
multi = 10*4
div = 10/4
resto = 10%4 
cociente = 10//4
potencia = 10**4

print(",La resta es: " ,resta, ",La multiplicacion es:",multi,",La division es:",div, 
",El resto es:",resto,",El cociente es",cociente,"y la potencia es :",potencia)


#Resolver la ecuacion cuadratica: 2x²-7+3 = 0 
a = 2
b = -7
c = 3

# Operaciones con cadenas de texto
print("SNPP" + "CTFPPJ"+" PROGRMACION PYTHON")

#print("AULA" + 2102) #aqui tendremos un error, 210 no es una cadena de texto usar str()

#operaciones mixttas
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

#operaciones con cadenas de texto
print("python" > "PYTHON")
print("aaaa">= "abaa")# Ordenacion alfabetica por ASCII
print(len("aaaa") >= len("abaa")) #Cuenta caracteres

print("python" != "PYTHON")

### Operadores Logicos

print(10> 4 and "Z" > "A")
print(10 > 4 or "Z" > "A")
print(not(10 > 4)and "Z" > "A")