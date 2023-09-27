#Desarrollar un programa que resuelva el cuadrado magico de nxn 
import itertools
import numpy as np

x = int(input("Ingrese de que dimensiones quiere el cuadro mágico: "))
cuadro= pow(x,2)

lst = list(itertools.repeat(0, cuadro))

class arbol:
    def __init__(self,nodo):
        self.raiz=nodo
        
class nodo:
    def __init__(self, cont):
        self.contenido=cont
        self.hijos=[]
    def generaHijos(self,n):
        for k in range(cuadro):
            i=k%x
            j=int(k/x)
            if(self.contenido[i][j]==0):
                contHijo = self.contenido.copy()
                contHijo[i]=n+1
                nod = nodo(contHijo)
                nod.generaHijos(n+1)
                self.hijos.append(nod)
                
Arbol=arbol(nodo(lst))
Arbol.raiz.generaHijos(0)

def verificar(matriz):
    a=verificarFilas(matriz)
    b=verificarColumnas(matriz)
    c=verificarDiagonales(matriz)
    return a and b and c

def verificarFilas(matriz):
    for f in matriz:
        if(not 0 in f):
            if(not sum(f)==15):
                return False
    return True

def verificarColumnas(matriz):
    return verificarFilas(np.transpose(matriz))

def verificarDiagonales(matriz):
    sumaA=0
    sumaB=0
    for i in range(len(matriz)):
        sumaA+=matriz[i][i]
        sumaB+=matriz[len(matriz)-1-i][i]
        
    if(sumaA==sumaB):
        return True