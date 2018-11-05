from Bibliografia import *

class BibliografiaLibro(Bibliografia):
    def __init__(self,nombre,apellido,titulo,editorial,pais,paginas,isbn):
        Bibliografia.__init__(self,nombre,apellido,titulo,editorial,pais) 
        self.paginas = paginas
        self.isbn = isbn

    def __str__(self):
        tmp = ""
        tmp += "Nombre del autor:" + str( self.nombre)
        tmp += "\nApellidos del autor::" + str( self.apellidos)
        tmp += "\nTitulo del libro:" + str( self.titulo)
        tmp += "\nNombre de la Editorial:" + str(self.editorial)
        tmp+= "\nPais de publicacion:" + str(self.pais)
        tmp += "\nNumero de paginas:" + str(self.paginas)
        tmp += "\nISBN:" + str(self.isbn)
        return tmp    


#L2 = BibliografiaLibro("jose","machado rubio","cuentos fantasticos","trillas","polonia","323","3514364236") 
#L2.getTitulo()
#print(L2.getTitulo()) 
#print()
#print(L2)   
#print()
#L2.getDatP()
#print(L2.getDatP())   