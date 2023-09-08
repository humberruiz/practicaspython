from tkinter import *
from tkinter import messagebox 
from biblioteca import Biblioteca
import os
biblioteca = None 
def crear_biblio():
    nombre = StringVar()
    def guardar_nombre():
        biblioteca = Biblioteca(nombre.get())
        messagebox.showinfo(message="Se a creado una biblioteca",title="Mensaje")
        v_biblio.destroy()


   v_biblio = Toplevel(ventana)
   v_biblio.title("Gestionar biblioteca")
   v_biblio.geometry("400x200+350+150")
   lbl_nombre = Label(v_biblio,text="Ingrese el nombre: ")
   lbl_nombre.place(x=5, y = 10)
   t_nombre = Entry(v_biblio,textvariable=nombre)
   t_nombre.place(x=200, y = 10)
   B_guardar=  Button(v_biblio,text="Guardar", command=guardar_nombre)
   B_guardar.place(x=300, y = 10)

def agregar_libro():
    pass

ventana = Tk()
ventana.geometry("640x480+300+200")
ventana.title("Sistema bibliotecario")
ventana.config(bg = "#94AFCC")

boton_crear_biblioteca = Button(ventana,text="Crear biblioteca", command=crear_biblio)
boton_crear_biblioteca.place(x=50, y = 50)
boton_agregar_libro = Button(ventana,text="Agregar libro", command=agregar_libro)
boton_agregar_libro.place(x=50, y = 100)
ventana.mainloop()