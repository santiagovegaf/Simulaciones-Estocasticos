from time import time
from numpy import random
#import matplotlib.pyplot as plt


def exp(Lambda):
    return random.exponential(1/Lambda)

# Simulacion de una cola simple que llegan, esperan y salen. M/M/c

# Simulación para encontar tiempo promedio de las primeros OBJ personas. 

def simulacion(OBJ, l1, l2):
# l1: tasa llegada, l2: tasa salida de una caja, c: número de cajas.

    # Número de personas en la cola.
    NCOL = 0

    # Caja ocupada o no (1/0).
    STATUS = 0

    # Número de personas que han completado espera en cola.
    NCLIENTES = 0

    # Tiempo de espera total en cola.
    ESTOT = 0

    # reloj.
    T = 0

    # instante que ocurrira proximo evento 1 (llegada).
    TPE1 = exp(l1)

    # instante que ocurrira proximo evento 2 (salida).
    TPE2 = 1000000000

    # Instante de llegada del trabajo en la posición i de la cola.
    TLLEG = []

    # Número personas que esperan más de 0.5 minutos.
    MAS = 0

    while NCLIENTES < OBJ:
       
        if TPE1 < TPE2:
            # llega alguien
            T = TPE1
            TPE1 = T + exp(l1)
        
            if STATUS == 0:
                # máquina desocupada
                NCLIENTES += 1
                STATUS = 1
                # Como hay una persona en el sistema, esta solo puede salir por una caja con tasa l2.
                TPE2 = T + exp(l2)
            else:
                # máquina ocupada
                NCOL += 1
                TLLEG.append(T)
        else:
            # sale alguien
            T = TPE2
            if NCOL > 0:
                # hay gente en la cola
                NCOL -= 1
                # D = variable auxiliar. Tiempo que paso esa persona en la cola.
                D = T - TLLEG.pop(0)
                ESTOT += D
                NCLIENTES += 1 
                TPE2 = T + exp(l2)
                if D > 0.5:
                    # Si persona pasa más de 0.5 min en cola se suma al contador
                    MAS += 1
            else:
                # Cola vacía.
                STATUS = 0
                TPE2 = 100000000

    print(f"Tiempo promedio en cola = {round(ESTOT/OBJ, 2)} min, más de 0.5 min en cola = {MAS*100/OBJ}%")


antes = time()
simulacion(10000, 5, 30)
despues = time()
print("tiempo ejecución código:", despues - antes, "s")
