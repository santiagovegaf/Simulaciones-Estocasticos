from time import time
from numpy import random
#import matplotlib.pyplot as plt


def exp(Lambda):
    return random.exponential(1/Lambda)

# Simulacion de una cola simple que llegan, esperan y salen. M/M/c/k

# Simulación para encontar número de clientes perdidos


def simulacion(OBJ, l1, l2, c, maximo_clientes):
    # l1: tasa llegada, l2: tasa salida de una caja, c: número de cajas.


    # Número de clientes atendodos
    NATE = 0

    # Número clientes perdidos
    NPER = 0

    # tot clientes que llegan
    NTOT = 0

    # en sistema
    NSIS = 0

    # reloj.
    T = 0

    # instante que ocurrira proximo evento 1 (llegada).
    TPE1 = exp(l1)

    # instante que ocurrira proximo evento 2 (salida).
    TPE2 = 1000000000

    # lista salidas
    TSALID = []

    while NTOT < OBJ:

        if TPE1 < TPE2:
            # llega alguien
            NTOT += 1
            
            T = TPE1
            TPE1 = T + exp(l1)
            if NSIS <= maximo_clientes:
                NSIS += 1
                if NSIS < c:
                    # Puede ingresar
                    TSALID.append(T + exp(l2*NSIS))
                    TPE2 = min(TSALID)
                else:
                    TSALID.append(T + exp(l2*c))
                    TPE2 = min(TSALID)
                
            else:
                # Se perde el cliente
                NPER += 1
            
        else:
            # sale alguien
            T = TPE2
            NSIS -= 1
            NATE += 1
            TSALID.remove(T)
            if len(TSALID)== 0:
                TPE2 = 100000000000
            else:
                TPE2 = min(TSALID)

    print(f"Promedio clientes perdidos: {NATE*100 /(NTOT)}%")


antes = time()
simulacion(1000, 600000, 0.5, 4, 10)
despues = time()
print("tiempo ejecución código:", despues - antes, "s")
