#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:11:20 2018

@author: David Trejo
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dat = pd.read_excel(r'/home/cr2practica/Escritorio/co - copia.xlsx')
data = pd.read_excel(r'/home/cr2practica/Escritorio/propane data.xlsx')
data1 = open(r'/home/cr2practica/Escritorio/Práctica/COeicMonth1.txt', 'r')
datos = data1.readlines()

def data_transfer_p(data):
    "takes propane data from the excel file to the python script, events"
    prop = data['propane']  # [pmol/mol]
    fecha = data['DATE']
    return fecha, prop


def data_transfer_co(dat):
    "takes co data from the excel file to the python script, events"
    #x = pd.DataFrame(dat, columns =[])
    DAT = dat['DATE']
    co = dat['CO'] * 1000  # ppb - > [pmol/mol]
    return DAT, co


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


def average_season(fecha, DAT, prop, co):
    """
    Classifies propane and co concentrations events into each month
    Input:
        fecha = date array for propane concentrations events
        DAT = date array for co concentrations events
        prop = array of propane concentrations values
        co = array of co concentrations values
    Output:
        prop_fecha: list of propane concentrations for each month
        co_fecha: list of co concentrations for each month
    """ 
    JA1 = []
    FE1 = []
    MR1 = []
    AP1 = []
    MY1 = []
    JN1 = []
    JL1 = []
    AG1 = []
    SP1 = []
    OC1 = []
    NV1 = []
    DC1 = []
    JA2 = []
    FE2 = []
    MR2 = []
    AP2 = []
    MY2 = []
    JN2 = []
    JL2 = []
    AG2 = []
    SP2 = []
    OC2 = []
    NV2 = []
    DC2 = []
    for i in range(len(fecha)):
        f = fecha[i]
        a, m, d = f.split('-')
        P = float(prop[i])
        m = int(m)
        if m == 1:
            JA1.append(P)
        if m == 2:
            FE1.append(P)
        if m == 3:
            MR1.append(P)
        if m == 4:
            AP1.append(P)
        if m == 5:
            MY1.append(P)
        if m == 6:
            JN1.append(P)
        if m == 7:
            JL1.append(P)
        if m == 8:
            AG1.append(P)
        if m == 9:
            SP1.append(P)
        if m == 10:
            OC1.append(P)
        if m == 11:
            NV1.append(P)
        if m == 12:
            DC1.append(P)
    prop_fecha = [JA1, FE1, MR1, AP1, MY1, JN1, JL1, AG1, SP1, OC1, NV1, DC1]
    for i in range(len(DAT)):
        g = DAT[i]
        A, M, D = g.split('-')
        CO = float(co[i])
        M = int(M)
        if M == 1:
            JA2.append(CO)
        if M == 2:
            FE2.append(CO)
        if M == 3:
            MR2.append(CO)
        if M == 4:
            AP2.append(CO)
        if M == 5:
            MY2.append(CO)
        if M == 6:
            JN2.append(CO)
        if M == 7:
            JL2.append(CO)
        if M == 8:
            AG2.append(CO)
        if M == 9:
            SP2.append(CO)
        if M == 10:
            OC2.append(CO)
        if M == 11:
            NV2.append(CO)
        if M == 12:
            DC2.append(CO)
    co_fecha = [JA2, FE2, MR2, AP2, MY2, JN2, JL2, AG2, SP2, OC2, NV2, DC2]
    return prop_fecha, co_fecha


def Statistics_M(JA, FE, MR, AP, MY, JN, JL, AG, SP, OC, NV, DC):
    """
    Calculation of the average per month and each standard desviation taking 
    monthly values given by NOAA
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


def means(pf, cf):
    "Calculates the mean for each month taking the complete data events"
    JA1 = np.mean(pf[0])
    FE1 = np.mean(pf[1])
    MR1 = np.mean(pf[2])
    AP1 = np.mean(pf[3])
    MY1 = np.mean(pf[4])
    JN1 = np.mean(pf[5])
    JL1 = np.mean(pf[6])
    AG1 = np.mean(pf[7])
    SP1 = np.mean(pf[8])
    OC1 = np.mean(pf[9])
    NV1 = np.mean(pf[10])
    DC1 = np.mean(pf[11])
    JA2 = np.mean(cf[0])
    FE2 = np.mean(cf[1])
    MR2 = np.mean(cf[2])
    AP2 = np.mean(cf[3])
    MY2 = np.mean(cf[4])
    JN2 = np.mean(cf[5])
    JL2 = np.mean(cf[6])
    AG2 = np.mean(cf[7])
    SP2 = np.mean(cf[8])
    OC2 = np.mean(cf[9])
    NV2 = np.mean(cf[10])
    DC2 = np.mean(cf[11])
    prop_fecha = [JA1, FE1, MR1, AP1, MY1, JN1, JL1, AG1, SP1, OC1, NV1, DC1]
    co_fecha = [JA2, FE2, MR2, AP2, MY2, JN2, JL2, AG2, SP2, OC2, NV2, DC2]
    return prop_fecha, co_fecha


def plots(prop, co, Prom, STD):
    x = np.linspace(1, 12, 12)
    Prom = np.multiply(Prom, 1000)  # nmol/mol  ->  pmol/mol
    x1 = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP',
          'OCT', 'NOV', 'DEC']
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(8, 6))
    ax1.plot(x, prop, 'b-', label='Propane concentration')
    ax1.set_title('CO and propane monthly average, Rapa Nui')
    ax1.set_ylabel('pmol/mol')
    ax1.legend()
    ax2.plot(x, co, 'y-', label='CO concentration calculated from every single event')
    ax2.set_ylabel('pmol/mol')
    ax2.legend()
    ax3.plot(x, Prom, 'r-', label='CO concentration calculated from montly average\n\
    given by NOAA ESRL Global Monitoring Division')
    ax3.set_ylabel('pmol/mol')
    ax3.legend()
    plt.setp((ax1, ax2, ax3), xticks=x, xticklabels=x1)
    


fecha, prop = data_transfer_p(data)
DAT, co = data_transfer_co(dat)
y, m, CO, JA, FE, MR, AP, MY, JN, JL, AG, SP, OC, NV, DC = data_transfer_M(datos)
pf, cf = average_season(fecha, DAT, prop, co)
prop_fecha, co_fecha = means(pf, cf)
Prom, std = Statistics_M(JA, FE, MR, AP, MY, JN, JL, AG, SP, OC, NV, DC)
plots(prop_fecha, co_fecha, Prom, std)
print('co monthly values: ' + repr(co_fecha))
print('propane monthly values: ' + repr(prop_fecha))
print('co given monthly values: ' + repr(Prom))
