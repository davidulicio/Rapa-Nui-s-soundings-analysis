# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:36:01 2018
Rapa Nui's Soundings Analysis, Carbon Monoxide
@author: David Trejo Cancino
"""
import numpy as np
import matplotlib.pyplot as plt
data = open(r'C:\Users\David\Desktop\Geofísica\Práctica\COeicMonth1.txt', 'r')
datos = data.readlines()
def data_transfer(datos):
    "Transfer data from the file to the program"
    lista = []
    JA = []
    FE = []
    MR = []
    AP = []
    MY = []
    JN = []
    JL = []
    AG = []
    SP = []
    OC = []
    NV = []
    DC = []
    for value in datos:
        lis = np.array(value.split())
        lista.append(lis)
    lista = np.asarray(lista)
    year = lista[:, 1]
    month= lista[:, 2]
    co = lista[:, 3]
    for i in range(len(month)):
        value = float(co[i])
        m = int(month[i])
        if m == 1:
            JA.append(value)
        if m == 2:
            FE.append(value)
        if m == 3:
            MR.append(value)
        if m == 4:
            AP.append(value)
        if m == 5:
            MY.append(value)
        if m == 6:
            JN.append(value)
        if m == 7:
            JL.append(value)
        if m == 8:
            AG.append(value)
        if m == 9:
            SP.append(value)
        if m == 10:
            OC.append(value)
        if m == 11:
            NV.append(value)
        if m == 12:
            DC.append(value)
    return year, month, co, JA, FE, MR, AP, MY, JN, JL, AG, SP, OC, NV, DC


def means(JA, FE, MR, AP, MY, JN, JL, AG, SP, OC, NV, DC):
    """
    Calculation of the average per month and  each standard desviation
    Inputs: CO concentration values for each month since 1994
    Output: Averages and standard desviations
    """
    E = np.mean(np.array(JA))
    F = np.mean(np.array(FE))
    M = np.mean(np.array(MR))
    A = np.mean(np.array(AP))
    MO = np.mean(np.array(MY))
    JI = np.mean(np.array(JN))
    JY = np.mean(np.array(JL))
    AO = np.mean(np.array(AG))
    S = np.mean(np.array(SP))
    O = np.mean(np.array(OC))
    N = np.mean(np.array(NV))
    D = np.mean(np.array(DC))
    Prom = [E, F, M, A, MO, JI, JY, AO, S, O, N, D]
    return Prom

def plots(Prom):
    "Plots CO concentrations vs time"
    x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
         'Sep', 'Oct', 'Nov', 'Dec']
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    plt.figure(num=1)
    plt.xticks(x1, x)
    plt.plot(x1, Prom, '*-b', label='Average Seasonal Cycle')
    plt.title('Easter Island, Chile; Carbon Cycle Surface\n\
    (Sample Intake Height: 69 masl)', multialignment='center')
    plt.ylabel('CO [nmol / mol]')
    plt.xlabel('Months')
    plt.legend()
    plt.show()
"Uso de las funciones"
y, m, co, JA, FE, MR, AP, MY, JN, JL, AG, SP, OC, NV, DC = data_transfer(datos)
Prom = means(JA, FE, MR, AP, MY, JN, JL, AG, SP, OC, NV, DC)
plots(Prom)

