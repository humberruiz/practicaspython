from tkinter import *
import os 

def get_calc():
    os.system("calc")

ventana = Tk()
ventana.title("Primera ventana")
ventana.geometry("520x480")
ventana.config(bg="blue")
ventana.resizable(0,0)
boton = Button(text = "abrir calculadora",  command=get_calc)
boton.place(x=100, y=50)
ventana.mainloop() 
