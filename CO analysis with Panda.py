# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:36:01 2018
Rapa Nui's Soundings Analysis, Carbon Monoxide
@author: David Trejo Cancino
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = open(r'C:\Users\David\Desktop\Geofísica\Práctica\COeicMonth1.txt', 'r')
datos = data.readlines()
dat = pd.read_excel(r'C:\Users\David\Desktop\Geofísica\Práctica\COeicEvent.xlsx', header=0)

"""def data_transfer_E(datos1):
    "Transfer data from the file to the program, Events analysis"
    lista = []
    for value in datos1:
        lis = np.array(value.split())
        lista.append(lis)
    lista = np.asmatrix(lista)
    year = np.str(lista[:, 0])
    y = lista [:, 0]
    month = np.str(lista[:, 1])
    day = np.str(lista[:, 2])
    co = np.str(lista[:, 6])
    return year, month, day, co, y
    """
   

def data_transfer_E(dat):
    year = dat['sample_year']
    month = dat['sample_month']
    day = dat['sample_day']
    co = dat['analysis_value']
    co = co / 1000
    date = []
    for i in range(len(year)):
        y = year[i]
        m = month[i]
        d = day[i]
        fecha = repr(y) + '-' + repr(m) + '-' + repr(d)
        date.append(fecha)
    return date, co

def data_transfer_M(datos):
    "Transfer data from the file to the program, Month analysis"
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


def Statistics_M(JA, FE, MR, AP, MY, JN, JL, AG, SP, OC, NV, DC):
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
    Es = np.std(np.array(JA))
    Fs = np.std(np.array(FE))
    Ms = np.std(np.array(MR))
    As = np.std(np.array(AP))
    MOs = np.std(np.array(MY))
    JIs = np.std(np.array(JN))
    JYs = np.std(np.array(JL))
    AOs = np.std(np.array(AG))
    Ss = np.std(np.array(SP))
    Os = np.std(np.array(OC))
    Ns = np.std(np.array(NV))
    Ds = np.std(np.array(DC))  
    Prom = [E, F, M, A, MO, JI, JY, AO, S, O, N, D]
    STD = [Es, Fs, Ms, As, MOs, JIs, JYs, AOs, Ss, Os, Ns, Ds]
    return Prom, STD


def arreglo_M(Prom):
    "Least squares fit of the data"
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    P = np.array(Prom)
    x = np.array(x1)
    z = np.polyfit(x, P, 4)  # Least Squares 4th degree polynomial fit
    return z


def plots_M(Prom, STD, z):
    "Plots CO concentrations vs time"
    x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
         'Sep', 'Oct', 'Nov', 'Dec']
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    plt.figure(num=1, figsize=(8,6))
    plt.xticks(x1, x)
    plt.plot(x1, Prom, '*-b', label='Average Seasonal Cycle')
    plt.title('Easter Island, Chile; Carbon Cycle Surface\n\
    (Sample Intake Height: 69 masl)', multialignment='center')
    plt.ylabel('CO [nmol / mol]')
    plt.xlabel('Months')
    y1 = np.poly1d(z)
    plt.plot(x1, y1(x1), 'r-', label='Least Squares Fit')
    plt.legend()
    plt.show()
    plt.figure(num=2, figsize=(8,6))
    plt.title('Easter Island, Chile; Carbon Cycle Surface\n\
    (Sample Intake Height: 69 masl)', multialignment='center')
    plt.ylabel('CO [nmol / mol]')
    plt.xlabel('Months')
    plt.xticks(x1, x)
    plt.errorbar(x1, Prom, STD, label='Average Seasonal Cycle and\n\
    its standard desviation') 
    plt.legend()
    plt.show()


"""def plots_E(date, co):
    df = pd.DataFrame(date)
    for i in range(len(co)):
        if co[i] < 0:
            df.
        if co[i] > 200:
            
            
    plt.plot(df, co, '*-')
    plt.ylabel('(CO) Carbon monoxide (nmol/mol)')
    plt.xlabel('Years')
    plt.show()"""
"""def plots_E(year, month, day, co, y1):
    x = ''
    for value in y1:
        x.join(str(value))
        print (str(value))
    print (x)
    y = [datetime.datetime.strptime(elem, '%Y') for elem in year]
    m = [datetime.datetime.strptime(elem, '%m') for elem in month]
    d = [datetime.datetime.strptime(elem, '%d') for elem in day]
    plt.figure(num=3, figsize=(8,6))
    plt.title('CO time series')
    plt.plot(y, co, '-*')"""
"Uso de las funciones"
y, m, co, JA, FE, MR, AP, MY, JN, JL, AG, SP, OC, NV, DC = data_transfer_M(datos)
Prom, std = Statistics_M(JA, FE, MR, AP, MY, JN, JL, AG, SP, OC, NV, DC)
z = arreglo_M(Prom)
plots_M(Prom, std, z)
date, co_e = data_transfer_E(dat)
#plots_E (date, co_e)
