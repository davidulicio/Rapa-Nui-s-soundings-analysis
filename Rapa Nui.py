# -*- coding: utf-8 -*-
"""
Rapa Nui
@author: David Trejo Cancino
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dat = pd.read_excel(r'C:\Users\David\Desktop\Rapa Nui Complete dataset\EasterIsland.xlsx', header=0)

"Functions"


def data_transfer_E(dat):
    "Transfer data from the excel file to python"
    dCO = dat['CO date']
    CO = dat['CO']
    dCO2 = pd.Series(dat['CO2 date'])
    CO2 = dat['CO2']
    dP = pd.Series(dat['Propane date'])
    P = dat['Propane']
    dnp = pd.Series(dat['n-pentane date'])
    nP = dat['n-pentane']
    dnb = pd.Series(dat['n-butane date'])
    nb = dat['n-butane']
    de = pd.Series(dat['ethane date'])
    e = dat['ethane']
    dmp = pd.Series(dat['methylpropane date'])
    mp = dat['methylpropane']
    dmb = pd.Series(dat['methylbutane date'])
    mb = dat['methylbutane']
    return dCO, CO, dCO2, CO2, dP, P, dnp, nP, dnb, nb, de, e, dmp, mp, dmb, mb


def prom(date, value):
    "Calculate the mean average concentration of every day of the data"
    datec = []
    valuec = []
    for i in range(len(date)-1):
        value1 = date[i]
        value2 = date[i+1]
        if value1 not in datec:
            if value1 == value2:
                valor = (value[i] + value[i+1]) / 2
                valuec.append(valor)
                datec.append(value1)
            if value1 != value2:
                valuec.append(CO[i])
                datec.append(value1)
    datec = pd.Series(datec)
    
    return valuec, datec


def plots(dCO, CO, dCO2, CO2, dP, P, dnp, nP, dnb, nb, de, e, dmp, mp, dmb, mb):
    plt.figure(num=1)
    plt.plot(dCO, CO, label='CO events')
    plt.title('CO timeseries, Easter Island')
    plt.xlabel('Years')
    plt.ylabel('nmol/mol')
    plt.figure(num=2)
    plt.plot(dCO2, CO2, label='CO2 events')
    plt.title('CO2 timeseries, Easter Island')
    plt.xlabel('Years')
    plt.ylabel('ppm')
    plt.figure(num=3)
    plt.plot(dP, P, label='propane events')
    plt.title('Propane timeseries, Easter Island')
    plt.xlabel('Years')
    plt.ylabel('pmol/mol')
    plt.figure(num=4)
    plt.plot(dnp, nP, label='n-pentane events')
    plt.title('n-pentane timeseries, Easter Island')
    plt.xlabel('Years')
    plt.ylabel('pmol/mol')
    plt.figure(num=5)
    plt.plot(dnb, nb, label='n-butane events')
    plt.title('n-butane timeseries, Easter Island')
    plt.xlabel('Years')
    plt.ylabel('pmol/mol')
    plt.figure(num=6)
    plt.plot(de, e, label='ethane events')
    plt.title('Ethane timeseries, Easter Island')
    plt.xlabel('Years')
    plt.ylabel('pmol/mol')
    plt.figure(num=7)
    plt.plot(dmp, mp, label='methylpropane events')
    plt.title('Methylpropane timeseries, Easter Island')
    plt.xlabel('Years')
    plt.ylabel('pmol/mol')
    plt.figure(num=8)
    plt.plot(dmb, mb, label='methylbutane events')
    plt.title('Methylbutane timeseries, Easter Island')
    plt.xlabel('Years')
    plt.ylabel('pmol/mol')
    plt.figure(num=9)
    plt.hist(np.histogram(CO), bins='auto')
    
    
"Use of the functions"
dCO, CO, dCO2, CO2, dP, P, dNP, NP, dNB, NB, dE, E, dMP, MP, dMB, MB = data_transfer_E(dat)
co, dco = prom(dCO, CO)
co2, dco2 = prom(dCO2, CO2)
p, dp = prom(dP, P)
nP, dnP = prom(dNP, NP)
nb, dnb = prom(dNB, NB)
co2, dco2 = prom(dCO2, CO2)
plots(dco, co, dCO2, CO2, dP, P, dnp, nP, dnb, nb, de, e, dmp, mp, dmb, mb)
