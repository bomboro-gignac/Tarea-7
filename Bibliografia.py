import random as r
class Bibliografia:
    def __init__(self,nombre,apellidos,titulo,editorial,pais):
        self.nombre = nombre
        self.apellidos = apellidos
        self.titulo = titulo 
        self.editorial = editorial
        self.pais = pais

    def __str__(self):
        tmp = ""
        tmp += "Nombre del autor:" + str( self.nombre)
        tmp += "\nApellidos del autor::" + str( self.apellidos)
        tmp += "\nTitulo del libro:" + str( self.titulo)
        tmp += "\nNombre de la Editorial:" + str(self.editorial)
        tmp+= "\nPais de publicacion:" + str(self.pais)
        return tmp

    def getTitulo(self):  
        return self.titulo  

    def getDatP(self):
        return self.apellidos + "  " + self.nombre   
    
    def lista_pseudo(n):
        lista = []
        lista_editoriales = ["trillas","reverte","fondo de cultura","alfaguara"]
        lista_paises = ["colombia","peru","brasil","mexico","argentina","uruguay"]
        abc = "abcdefghijklmnopqrstuvwxyz"
        ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
        for i in range(n):
            letras_nombre = r.randint(4,5)
            numeros_t = r.randint(10,20)
            nombre = ABC[r.randint(0,25)]
            for j in range(1,letras_nombre):
                nombre = nombre + abc[r.randint(0,25)]
            apellidos = ABC[r.randint(0,25)]
            for s in range(1,letras_nombre):
                apellidos = apellidos + abc[r.randint(0,25)]
            for t in range(1,numeros_t):
                isbn = [r.randint(100,1000)]
            for o in range(1,numeros_t): 
                paginas = [r.randint(1,1000)]     
            
            titulo = ABC[r.randint(0,25)]
            for u in range(1,letras_nombre):
                titulo = titulo + abc[r.randint(0,25)]
            editorial = lista_editoriales[r.randint(0,3)]
            pais = lista_paises[r.randint(0,5)]   
            lista.append(Bibliografia(nombre,apellidos,titulo,editorial,pais))
        return lista
        
    def getListaDatP(original):
        lista=[]
        for i in range ( len(original)):
            aux = original[i].getDatP()
            lista.append(aux)
        return lista

    def getTitulos(original):
        lista = []
        for i in range(len(original)):
            aux = original[i].getTitulo()
            lista.append(aux)
        return lista            

    def comparacion(original,nombre,apellidos):
        
        flag = False

        for i in range(len(original)):
            aux = apellidos + " " + nombre
            if original[i].getDatP() == aux:
                flag = true
        return flag        
    
    def getAutores(original1,original2):
        for i in range(len(original1)):
            aux = original1[i].nombre      
            aux2 = original1[i].apellidos
            if (Bibliografia.comparacion(original2,aux,aux2)):
                print(aux2+" "+aux)
        return

lista = Bibliografia.lista_pseudo(5000)
lista2 = Bibliografia.lista_pseudo(5000)
listaAutor= Bibliografia.getListaDatP(lista)
listaTitulo= Bibliografia.getTitulos(lista)
flag = Bibliografia.comparacion(lista,"Prrpwcoidpdklqp","Hjyxksqbhdky")
for m in range(3):
    print(lista[m])
    print()
print("\n\n*******************\n\n")
for m in range(3):
    print(listaAutor[m])
    print()
print("\n\n*******************\n\n")
print(flag)
print("\n\n*******************\n\n")
print("busqueda en dos listas")
Bibliografia.getAutores(lista,lista2)
print("\n\n*******************\n\n")
for m in range(3):
    print(listaTitulo[m])
    print()

