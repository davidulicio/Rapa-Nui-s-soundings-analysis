# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 12:22:44 2018
Rapa Nui's Soundings Analysis
@author: David Trejo Cancino
DGF Uchile

"""
import numpy as np
tabla = 'C:\Users\David\Desktop\\rapanui_19941026_V01.dat'
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
traspaso(datos)
