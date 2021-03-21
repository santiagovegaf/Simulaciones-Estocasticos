from time import time
from numpy import random
import matplotlib.pyplot as plt


def exp(Lambda):
    return random.exponential(1/Lambda)



#Ayudantia P2

def simulacion(c):

    # reloj
    T = 0

    # Horizonte de 5 años (en minutos)
    TMax = 10120

    # Nuúmero de sitios ocupados
    X = 0

    # Instante en el que llega una persona (ocurre evento)
    TPE1 = exp(20)

    # Instante en el que sale una persona (ocurre evento)
    TPE2 = 1000000000

    # arreglo que almacena los instanes de salida de los que entraron
    TSALID = []

    # Indicador. Número de total clientes ingresados
    NING = 0

    while T < TMax:
        if TPE1 < TPE2:
            #llega cliente
            T = TPE1
            if X < c:
                #puede entrar cliente
                X +=1
                NING +=1
                TPE1 = T + exp(20)
                TSALID.append(T+ exp(3))
                TPE2 = min(TSALID)
            else:
                #no puede entrar
                TPE1 = T + exp(20)
        else:
            #sale cliente
            T = TPE2
            X -= 1
            TSALID.remove(TPE2)
            if len(TSALID) == 0:
                TPE2 = 10**100
            else:
                TPE2 = min(TSALID)
    
    return NING * 4000 - 1200000*c


x = []
y = []
antes = time()
for c in range(100):
    x.append(c)
    y.append(simulacion(c))
despues = time()
print("tiempo", despues - antes, "s")
plt.scatter(x,y)
plt.show() 




