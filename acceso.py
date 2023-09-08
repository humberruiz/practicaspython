#Sistema de acceso
contador = 0 
while (contador < 3): #mientras contador sea menor a 3

    user = input("Escribi tu ususario kp: ")
    password = input("Teclea tu contraseña a continuacion ")

    if(user == "admin" and password == "12345"): #indentacion debajo del if, para que se parte
        print("Bienvenido", user)
        break
    else:
        contador +=1
        print("Usuario o contraseña incorrecta. Intento {} de 3".format(contador))
        