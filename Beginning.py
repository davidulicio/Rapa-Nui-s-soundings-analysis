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


def traspaso(data):
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
    pression = lista[:, 1]
    temperature = lista[:, 2]
    RH = lista[:, 3]
    O3mPa = lista[:, 4]
    O3ppbv = lista[:, 5]
    O3DU = lista[:, 6]
    u = lista[:, 7]
    v = lista[:, 8]
    theta = lista[:, 9]
    theta_e = lista[:, 10]
    Q = lista[:, 11]
    return lista
traspaso(datos)
print 