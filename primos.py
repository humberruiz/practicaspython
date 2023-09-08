num = 5
bandera = 0
while(true): #mientras verdadero
    
    for x  in range(2,num,1):
        if (num % x == 0):
            bandera = 1
            break
    if (bandera == 0):
        print(num)

    #inicializar variables
    num +=1
    bandera = 0