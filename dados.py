import random
import os
import time

def lanzar_dados():
    num = random.randint(1,6)
    return num 

while true:
    dado = lanzar_dados()
    num_usuario = 0
     while(num_usuario < 1 or num_usuario > 6):
        num_usuario = int(input("Elige el numero del dado"))

    for x in range(0,4,1):
        print("Lanzando dado")
        print("*"*x)
        time.sleep(1)
        os.system("cls")

    if(num_usuario == dado):
        print("Has gando", dado)
    else: 
         print("Has perdido", dado)
    time.sleep(3)
    os.system("cls")
    resp = input("Desea seguir jugando: (si| no) ")
    if(resp == "no"):
        print("Vuelva pronto")
        break
