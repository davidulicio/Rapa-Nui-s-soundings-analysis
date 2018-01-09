# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 12:22:44 2018
Rapa Nui's Soundings Analysis
@author: David Trejo Cancino
DGF Uchile

"""
import numpy as np
import matplotlib.pyplot as plt
print 'Trabajo de datos para Easter Island'
# print 'Ingrese ubicacion (ruta de acceso) al archivo'
# tabla = input()
tabla = 'C:\Users\David\Desktop\\rapanui_19941123_V01.dat'
data = open(tabla, 'r')  # Lectura de datos
datos = data.readlines()


def traspaso(datos):
    "Traspasa los datos para trabajarlos"
    lista = []
    lista2 = []
    for i in range(len(datos)):
        if i >= 21:
            lista.append(datos[i])
    for value in lista:
        lis = np.array(value.split())
        lista2.append(lis)
    lista = np.asarray(lista2)
    height = lista[:, 0]
    press = lista[:, 1]
    tem = lista[:, 2]
    RH = lista[:, 3]
    O3mPa = lista[:, 4]
    O3ppbv = lista[:, 5]
    O3DU = lista[:, 6]
    u = lista[:, 7]
    v = lista[:, 8]
    th = lista[:, 9]
    th_e = lista[:, 10]
    Q = lista[:, 11]
    return height, press, tem, RH, O3mPa, O3ppbv, O3DU, u, v, th, th_e, Q
   
    
def grafos(h, RH, tem, Oz):
    "Genera graficos"
    """ fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(range(10))
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.spines['bottom'].set_color('red')
    ax.spines['top'].set_color('red')
    ax.xaxis.label.set_color('red')
    ax.tick_params(axis='x', colors='red')"""

    fig1 = plt.figure(num=1)
    ax1 = fig1.add_subplot(111)
    ax1.set_xlabel('RH%       Ozone(nbar)')
    ax1.set_ylabel('Y-axis')
    ax1.spines['bottom'].set_color('red')
    plt.plot(RH, h, 'k', label='RH%')  # h vs RH
    plt.plot(tem, h, 'r', label='Temperature')  # h vs T
    plt.plot(Oz, h, 'b', label='Ozone(nbar)')  # h vs O3DU
    plt.legend()
    plt.show()
    
" USO DE LAS FUNCIONES "
h, press, tem, RH, O3mPa, O3ppbv, O3DU, u, v, th, th_e, Q = traspaso(datos)
grafos(h, RH, tem, O3DU)