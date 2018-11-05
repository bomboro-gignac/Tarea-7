from Bibliografia import *

class BibliografiaArticuloDeInvestigacion(Bibliografia):
    def __init__(self,nombre,apellidos,titulo,editorial,pais,paginas,isbn,area,doi):
        Bibliografia.__init__(self,nombre,apellidos,titulo,editorial,pais) 
        self.paginas = paginas
        self.isbn = isbn
        self.area = area
        self.doi = doi 

    def __str__(self):
        tmp = ""
        tmp += "Nombre del autor:" + str( self.nombre)
        tmp += "\nApellidos del autor::" + str( self.apellidos)
        tmp += "\nTitulo del libro:" + str( self.titulo)
        tmp += "\nNombre de la Editorial:" + str(self.editorial)
        tmp+= "\nPais de publicacion:" + str(self.pais)
        tmp += "\nNumero de paginas:" + str(self.paginas)
        tmp += "\nISBN:" + str(self.isbn)
        tmp += "\nArea del articulo de investigacion:" + str(self.area)
        tmp += "\nDOI:" + str(self.doi)
        return tmp 
    
    def getDatP(self):
        return self.apellidos + "  " + self.nombre[0]

L3 = BibliografiaArticuloDeInvestigacion("jose","machado rubio","cuentos fantasticos","trillas","polonia","323","3514364236","fisica","89889")

L3.getTitulo()
print(L3.getTitulo()) 
print()
print(L3)   
print()
L3.getDatP()
print(L3.getDatP()) 