# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 12:22:44 2018
Rapa Nui's Soundings Analysis
@author: David Trejo Cancino
DGF Uchile

"""
import numpy as np
print 'Trabajo de datos para Easter Island'
# print 'Ingrese ubicacion (ruta de acceso) al archivo'
# tabla = input()
tabla = 'C:\Users\David\Desktop\\rapanui_19941123_V01.dat'
data = open(tabla, 'r')  # Lectura de datos
datos = data.readlines()

def traspaso(data):
    "Traspasa los datos para trabajarlos"
    data = open(tabla, 'r')  # Lectura de datos
    datos = data.readlines()
    lista = []
    lista2 = []
    for i in range(len(datos)):
        if i >= 21:
            lista.append(datos[i])
    data.close()
    for value in lista:
        lis = np.array(value.split())
        lista2.append(lis)
    lista = np.asarray(lista2)
    height = lista[:, 0]
    pression = lista[:, 1]
    temperature = lista[:, 2]
    u = lista[:, 3]
    v = lista[:, 4]
    theta = lista[:, 5]
    theta_e = lista[:, 6]
    Q = lista[:, 7]
traspaso(datos)
