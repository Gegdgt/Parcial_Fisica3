# Nombre de los programadores: Gabriel García 21352, Luis Pedro Montenegro 21
# Nombre del programa: Parcial1_Fisica3
# Fecha de ultima modificación: 24/08/2023

import math
#import numpy as np
#import matplotlib.pyplot as plt
import tkinter as ttk
from scipy.integrate import quad


# Función para calcular el anillo
def anillo(Q, R, x):
    def integrand():
        r = R
        return (1 / (4*math.pi*8.854187817e-12)) * (Q*x) / (x**2+r**2)**(3/2)
    # (Q / pow(r, 2)) / (pow(pow(r, 2) + pow(x, 2) - 2*r*x*math.cos(theta), 3/2)
    # quad es una función para realizar una integral numérica
    # _ Se utiliza para decir que no nos interesa el valor del error
    result, _ = quad(integrand, 0, 2*math.pi)
    return result

# Función para calcular el disco
def disco(Q, R, x):
    # Usar la formula del anillo para realizar la formula de la disco
    formula_anillo = anillo(Q, R, x)
    def integrand(r):
        return formula_anillo*2*math.pi*r / (pow(pow(r, 2) + pow(x, 2), 3/2))
    
    result, _ = quad(integrand, 0, R)
    return result

# Función para calcular la línea de carga
def linea(Q, L, x):
    # Usar la formula del disco para realizar la formula de la linea
    formula_disco = disco(Q, L, x)
    def integrand(r):
        return formula_disco*(Q / (2*math.pi*r)) / (pow(pow(r, 2) + pow(x, 2), 3/2))
    
    result, _ = quad(integrand, 0, L)
    return result

def graficas():
    root = Tk()
    frm = ttk.Frame(root, padding=12)
    frm.grid()
    ttk.Label(frm, text = "Campo eléctrico").grid(column = 6, row = 0)
    ttk.Button(frm, text = "Salir", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
    return None

sigue = True
while sigue:
    print("Seleccione una opción:")
    print("1. Realizar el anillo")
    print("2. Realizar el disco")
    print("3. Realizar la línea de carga")
    print("4. Cerrar el programa")
    menu = int(input())
    
    if menu == 1:
        Q = float(input("Ingrese la carga total (Q) en C: "))
        R = float(input("Ingrese el radio del anillo (R) en m "))
        x = float(input("Ingrese la distancia (x) en m: "))
        E = anillo(Q, R, x)
        print("Campo eléctrico del anillo: ", E, "N/C")
        
    elif menu == 2:
        Q = float(input("Ingrese la carga total (Q) en C: "))
        R = float(input("Ingrese el radio del disco (R) en m: "))
        x = float(input("Ingrese la distancia (x) en m: "))
        E = disco(Q, R, x)
        print("Campo eléctrico del disco:", E, "N/C")
        
    elif menu == 3:
        Q = float(input("Ingrese la carga total (Q) en C: "))
        L = float(input("Ingrese la longitud de la línea (L) en m: "))
        x = float(input("Ingrese la distancia (x) en m: "))
        E = linea(Q, L, x)
        print("Campo eléctrico de la línea de carga:", E, "N/C")
        
    elif menu == 4:
        print("Salir")
        sigue = False
        
    else:
        print("Ingrese correctamente alguna opcion")
