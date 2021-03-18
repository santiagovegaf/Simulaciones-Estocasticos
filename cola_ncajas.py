from time import time
from numpy import random
#import matplotlib.pyplot as plt


def exp(Lambda):
    return random.exponential(1/Lambda)

# Simulacion de una cola simple que llegan, esperan y salen. M/M/c sin cola

# Simulación para encontar número de clientes perdidos


def simulacion(OBJ, l1, l2, c):
    # l1: tasa llegada, l2: tasa salida de una caja, c: número de cajas.

    # Número cajas ocupadas
    NCAJAS = 0

    # Número de clientes atendodos
    NATE = 0

    # Número clientes perdidos
    NPER = 0

    # tot clientes que llegan
    NTOT = 0

    # reloj.
    T = 0

    # instante que ocurrira proximo evento 1 (llegada).
    TPE1 = exp(l1)

    # instante que ocurrira proximo evento 2 (salida).
    TPE2 = 1000000000

    # lista salidas
    TSALID = []

    while T < OBJ:

        if TPE1 < TPE2:
            # llega alguien
            NTOT += 1
            T = TPE1
            TPE1 = T + exp(l1)

            if NCAJAS < c:
                # Puede ingresar
                TSALID.append(T + exp(l2*c))
                NCAJAS += 1
                TPE2 = min(TSALID)
            else:
                # Se perde el cliente
                NPER += 1
            
        else:
            # sale alguien
            T = TPE2
            NCAJAS -= 1
            NATE += 1
            TSALID.remove(T)
            if len(TSALID)== 0:
                TPE2 = 100000000000
            else:
                TPE2 = min(TSALID)

    print(f"Promedio clientes perdidos: {NPER*100 /(NTOT)}%")


antes = time()
simulacion(10000, 6, 0.5, 4)
despues = time()
print("tiempo ejecución código:", despues - antes, "s")
