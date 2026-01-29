import random as rnd
import math

class neurona:
    def __init__(self,n,fA="sigmoidal"):
        self.nE = n
        self.pesos=[]
        for i in range(n):
            self.pesos.append(0)
        self.salida = 0
        self.sesgo = 0
        self.funcion=fA
        self.inicializarPesos()
   
    def inicializarPesos(self):
        for i in range(self.nE):
            self.pesos[i]=rnd.random()
   
    def escalon(self,x):
        if(x>0):
            return 1
        else:
            return 0
   
    def rampa(self,x):
        if(x<0):
            return 0
        elif(x<1):
            return x
        else:
            return 1
   
    def sigmoidal(self,x):
        return (1/(1+math.exp(-x)))
   
    def calculaSalida(self,Entradas):
        suma=0
        for i in range(len(Entradas)):
            suma+=self.pesos[i]*Entradas[i]
        suma+=self.sesgo
        if(self.funcion=="rampa"):
            self.salida= self.rampa(suma)
        if(self.funcion=="escalon"):
            self.salida=self.escalon(suma)
        if(self.funcion=="sigmoidal"):
            self.salida=self.sigmoidal(suma)
        return self.salida
    
class red:
    def __init__(self, nEntradas, nOcultas, nSalida):
        self.capaEntrada = []
        self.capaOculta = []
        self.capaSalida = []
        self.Salidas=[]
        for i in range(nEntradas):
            self.capaEntrada.append(neurona(1))
        for i in range(nOcultas):
            self.capaOculta.append(neurona(nEntradas))
        for i in range(nSalida):
            self.capaSalida.append(neurona(nOcultas))
            
    def calculaSalida(self, Entradas):
        sEntradas=[]
        sOcultas=[]
        self.Salidas=[]
        for i in range(len(self.capaEntrada)):
            sEntradas.append(self.capaEntrada[i].calculaSalida([Entradas[i]]))
        for i in range(len(self.capaOculta)):
            sOcultas.append(self.capaOculta[i].calculaSalida(sEntradas))
        for i in range(len(self.capaSalida)):
            self.Salidas.append(self.capaSalida[i].calculaSalida(sOcultas))

N1=neurona(4)
N1.inicializarPesos()
N1.calculaSalida([4,-4,2,7])