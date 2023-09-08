class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self._libros = []

    def consultar_nombre_biblioteca(self):
        return self.nombre
    
    def agregar_libros(self, Libro):
        self._libros.append(
            {
                Libro.titulo,
                Libro.autor,
                Libro.cantidad_de_paginas,
                Libro.genero,
                Libro.sinopsis,
            }
        )
    def consultar_libros(self):
        return self._libros

    def consultar_libro(self,id):
        return self._libros[id]

    def quitar_libros(self,id):
        self._libros.pop(id)