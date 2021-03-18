from time import time
from numpy import random
from random import choice
import matplotlib.pyplot as plt


def exp(Lambda):
    return random.exponential(1/Lambda)

def items():
    lista = [1,2,3,4,5]
    return choice(lista)

# dos cajas en paralelo
# llegan a tasa a (clientes por hora)
# cada cliente i compra  N(i) items
# tiempo demora cliente comprando: T = a*N*X/Max
# X: número de personas en supermercado
# Max: capacidad máxima supermercado
# a: constante proporcionalidad
# 2 cajas, se elige la más corta
# tiempo en caja: N * b (min)

# Medidas desempeño:
# % clientes que no entra
# Tiempo promedio esperando en cola caja

# Eventos:
# LLega cliente a supermercado (entra/ no entra)
# Cliente compra productos (elige caja 1/ caja 2)
# Cliente es atendido en caja 1 y sale
# Cliente es atendido en caja 2 y sale

def simulacion():

    #reloj
    T = 0

    # Número personas en supermercado
    X = 0

    # Estado caja 
    STATUS1 = 0
    STATUS2 = 0

    # Número personas en cola
    NCOL1 = 0
    NCOL2 = 0

    # Instante siguente llegada al supermercado
    TPE1 = exp(10)

    # Lista que almacena tiempos de salida del área de compras
    TELECCION = []

    # Instante siguente salida del área compras 
    TPE2 = 10000000

    # Instante salida caja 
    TPE31 = 1000000
    TPE32 = 1000000

    # Arreglo que almacena instantes llegada cola en orden
    TCOLA1 = []
    TCOLA2 = []


    # Números de ítems por comprar
    N = items()

    # Máximo personas en supermercado
    MAX = 50000

    # Tiempo de compra
    def TN (x):
        return  (items() * x  / MAX)

    # Tiempo atención caja
    TA = exp(3)

    # Número de personas que llegaron al supermercado
    NLLEG = 0

    # Número de personas que ingresaron al supermercado
    NING = 0

    # Número de personas que terminaron cola caja
    NTOT = 0

    # Suma tiempos de espera
    ESTOT = 0
    
    while NLLEG < 300:
        if TPE1 == min(TPE1, TPE2,TPE31, TPE32):
            #llega una persona al super
            T = TPE1
            TPE1 += exp(10)
            NLLEG += 1

            if X < MAX:
                # persona ingresa
                X += 1
                NING += 1
                TELECCION.append(T + TN(X))
                TPE2 = min(TELECCION)
            else:
                # super lleno
                pass

        elif TPE2 == min(TPE1, TPE2,TPE31, TPE32):
            # sale alguin del área compras
            T = TPE2
            TELECCION.remove(TPE2)
            if len(TELECCION) == 0:
                TPE2 = 10000000
            else:
                TPE2 = min(TELECCION)

            if NCOL1 <= NCOL2:
                if STATUS1 == 0:
                    STATUS1 = 1
                    TPE31 = T + exp(1)
                else:
                    NCOL1 += 1
                    TCOLA1.append(T)
            else:
                if STATUS2 == 0:
                    STATUS2 = 1
                    TPE32 = T + exp(1)
                else:
                    NCOL2 += 1
                    TCOLA2.append(T)
        elif TPE31 == min(TPE1, TPE2,TPE31, TPE32):
            # alguine sale cola 1
            if NCOL1 > 0:
                NCOL1 -= 1
                NTOT += 1
                ESTOT += T - TCOLA1.pop(0)
                TPE31 = T + exp(1)
            else:
                STATUS1 = 0
                TPE31 = 100000000

        elif TPE32 == min(TPE1, TPE2,TPE31, TPE32):
            # alguine sale cola 2
            if NCOL2 > 0:
                NCOL2 -= 1
                NTOT += 1
                ESTOT += T - TCOLA2.pop(0)
                TPE32 = T + exp(1)
            else:
                STATUS2 = 0
                TPE32 = 100000000
    else:
        no_entro = (NLLEG- NING)/ NLLEG
        espera_promedio = ESTOT/ NTOT
        print(f"% que no entro {no_entro}, espera prom {espera_promedio} min")

simulacion()