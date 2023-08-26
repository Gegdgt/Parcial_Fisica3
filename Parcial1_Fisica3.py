# Nombre de los programadores: Gabriel García 21352, Luis Pedro Montenegro 21
# Nombre del programa: Parcial1_Fisica3
# Fecha de ultima modificación: 24/08/2023

import math
import numpy as np
import matplotlib.pyplot as plt
import tkinter as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.integrate import quad
from scipy.constants import epsilon_0 as e_0


# Función para calcular el anillo
def anillo(Q, R, z):
    def integrand(theta):
        r = R
        return (1 / (4*math.pi*e_0)) * (Q / pow(r, 2)) / (pow(pow(r, 2) + pow(z, 2) - 2*r*z*math.cos(theta), 3/2))
    # quad es una función para realizar una integral numérica
    # _ Se utiliza para decir que no nos interesa el valor del error
    result, _ = quad(integrand, 0, 2*math.pi)
    return result

# Función para calcular el disco
def disco(Q, R, z):
    # Usar la formula del anillo para realizar la formula de la disco
    formula_anillo = anillo(Q, R, z)
    def integrand(r):
        return formula_anillo*2*math.pi*r / (pow(pow(r, 2) + pow(z, 2), 3/2))
    
    result, _ = quad(integrand, 0, R)
    return result

# Función para calcular la línea de carga
def linea(Q, L, z):
    # Usar la formula del disco para realizar la formula de la linea
    formula_disco = disco(Q, L, z)
    def integrand(r):
        return formula_disco*(Q / (2*math.pi*r)) / (pow(pow(r, 2) + pow(z, 2), 3/2))
    
    result, _ = quad(integrand, 0, L)
    return result


class CampoElectricoGraficado:
    def __init__(self, root):
        #titulo
        self.root = root
        self.root.title("Vizualizador del campo eléctrico")

        #seleccion de figura
        self.geometry_label = ttk.Label(root, text="Seleccione figura:")
        self.geometry_label.pack()

        #opciones a elegir
        self.geometry_entry = ttk.Entry(root, values=["Anillo", "Disco", "Cilindro"])
        
        self.geometry_entry.pack()

        #comando para graficar
        self.plot_button = ttk.Button(root, text="Graficar", command=self.graficarCampoElectrico)
        self.plot_button.pack()
        
        #comando para salir
        self.exit_button = ttk.Button(root, text = "Salir", command=self.root.quit)
        self.exit_button.pack()

        #para el plano para graficar
        self.fig, self.axis = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack() 

    def graficarCampoElectrico(self):
        geometry = self.geometry_entry.get()
        if geometry == "Anillo":
            Q = float(input("Ingrese la carga total (Q) en C: "))
            R = float(input("Ingrese el radio del anillo (R) en m "))
            z = float(input("Ingrese la distancia (x) en m: "))
            E = anillo(Q, R, z)
            pass 
        elif geometry == "Disco":
            Q = float(input("Ingrese la carga total (Q) en C: "))
            R = float(input("Ingrese el radio del disco (R) en m: "))
            z = float(input("Ingrese la distancia (x) en m: "))
            E = disco(Q, R, z)
            pass
        elif geometry == "Cilindro":
            Q = float(input("Ingrese la carga total (Q) en C: "))
            L = float(input("Ingrese la longitud de la línea (L) en m: "))
            z = float(input("Ingrese la distancia (x) en m: "))
            E = linea(Q, L, z)
            pass

        #para graficar la figura
        fig = plt.figure()
        x = y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.axis.plot(x,y)
        self.axis.set_xlabel('eje x')
        self.axis.set_ylabel('eje y')

        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
root = ttk.Tk()
app = CampoElectricoGraficado(root)
root.mainloop()









#sigue = True
#while sigue:
#    print("Seleccione una opción:")
#    print("1. Realizar el anillo")
#    print("2. Realizar el disco")
#    print("3. Realizar la línea de carga")
#    print("4. Cerrar el programa")
#    menu = int(input())
#    
#    if menu == 1:
#        Q = float(input("Ingrese la carga total (Q) en C: "))
#        R = float(input("Ingrese el radio del anillo (R) en m "))
#        x = float(input("Ingrese la distancia (x) en m: "))
#        E = anillo(Q, R, x)
#        print("Campo eléctrico del anillo: ", E, "N/C")
#        
#    elif menu == 2:
#        Q = float(input("Ingrese la carga total (Q) en C: "))
#        R = float(input("Ingrese el radio del disco (R) en m: "))
#        x = float(input("Ingrese la distancia (x) en m: "))
#        E = disco(Q, R, x)
#        print("Campo eléctrico del disco:", E, "N/C")
#        
#    elif menu == 3:
#        Q = float(input("Ingrese la carga total (Q) en C: "))
#        L = float(input("Ingrese la longitud de la línea (L) en m: "))
#        x = float(input("Ingrese la distancia (x) en m: "))
#        E = linea(Q, L, x)
#        print("Campo eléctrico de la línea de carga:", E, "N/C")
#        
#    elif menu == 4:
#        print("Salir")
#        sigue = False
        
#    else:
#        print("Ingrese correctamente alguna opcion")
