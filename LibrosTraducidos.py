from Bibliografia import *
from BibliografiaLibro import *

class LibrosTraducidos(BibliografiaLibro):
    def __init__(self,nombre,apellido,titulo,editorial,pais,paginas,isbn,idioma,traductores):
        Bibliografia.__init__(self,nombre,apellido,titulo,editorial,pais) 
        self.paginas = paginas
        self.isbn = isbn
        self.idioma = idioma
        self.traductores = traductores

    def __str__(self):
        tmp = ""
        tmp += "Nombre del autor:" + str( self.nombre)
        tmp += "\nApellidos del autor::" + str( self.apellidos)
        tmp += "\nTitulo del libro:" + str( self.titulo)
        tmp += "\nNombre de la Editorial:" + str(self.editorial)
        tmp+= "\nPais de publicacion:" + str(self.pais)
        tmp += "\nNumero de paginas:" + str(self.paginas)
        tmp += "\nISBN:" + str(self.isbn)
        tmp += "\nIdioma Original:" + str(self.idioma)
        tmp +="\nTraducctores:" + str(self.traductores)
        return tmp  

    def getTrad(self):
        return "Traducido por: " + self.traductores +" " + "del " + self.idioma  

L4 = LibrosTraducidos("jorge","Mendez Mora","carpe diem","trillas","italia","567","6546213","italiano","jesus gomez, natalaia juarez")
L4.getTrad()
print(L4.getTrad())
             


