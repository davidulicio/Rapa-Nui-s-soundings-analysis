# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 12:22:44 2018
Rapa Nui's Soundings Analysis
@author: David Trejo Cancino
DGF Uchile

"""
import numpy as np
import matplotlib.pyplot as plt
print 'Easter Island´s analysis'
# print 'Ingrese ubicacion (ruta de acceso) al archivo'
# tabla = input()
tabla = 'C:\Users\David\Desktop\\rapanui_19941123_V01.dat'
data = open(tabla, 'r')  # Data reading
datos = data.readlines()


def data_transfer(datos):
    "Transfer data from the file to the program"
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
    the = lista[:, 10]
    Q = lista[:, 11]
    return height, press, tem, RH, O3mPa, O3ppbv, O3DU, u, v, th, the, Q


def data_cleansing(h, p, tem, RH, O3mPa, O3ppbv, O3DU, u, v, th, the, Q):
    "Detects and removes inaccurate records from each list"
    RHf = []
    h_RH = []
    for i in range(len(RH)):
        if float(RH[i]) != 9000:
           RHf.append(RH[i])
           h_RH.append(h[i])
    Tf = []
    h_T = []
    for i in range(len(tem)):
        if float(tem[i]) != 9000:
           Tf.append(RH[i])
           h_T.append(h[i])
    O3 = []
    h_O3 = []
    for i in range(len(O3DU)):
        if float(O3DU[i]) != 9000:
           O3.append(O3DU[i])
           h_O3.append(h[i])
    return RHf, h_RH, Tf, h_T, O3, h_O3
    
def graphs(h1, h2, h3, RH, tem, Oz):
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

    plt.figure(num=1)
    plt.xlabel('RH%       Temperature(Celcius)     Ozone(nbar)')
    plt.ylabel('Altitude [km]')
    plt.plot(RH, h1, 'k', label='RH%')  # h vs RH
    plt.plot(tem, h2, 'r', label='Temperature in Celcius')  # h vs T
    plt.plot(Oz, h3, 'b', label='Ozone(nbar)')  # h vs O3DU
    plt.legend()
    plt.show()
    
" USO DE LAS FUNCIONES "
h, press, tem, RH, O3mPa, O3ppbv, O3DU, u, v, th, the, Q = data_transfer(datos)
RHf, h_RH, Tf, h_T, O3, h_O3 = data_cleansing(h, press, tem, 
                                              RH, O3mPa, O3mPa, O3DU, u, v,
                                              th, the, Q)
graphs(h_RH, h_T, h_O3, RHf, Tf, O3)
