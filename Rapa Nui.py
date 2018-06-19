# -*- coding: utf-8 -*-
"""
Rapa Nui
@author: David Trejo Cancino
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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


def nan_spot(value):
    "Spots NaN values in the raw data"
    nanlist=[]
    for ii in range(len(value)):
        if np.isnan(value[ii]):
            nanlist.append(ii)
        if value[ii] == "":
            nanlist.append(ii)
    return nanlist
        
def prom(date, value):
    "Calculate the mean average concentration of every day of the data"
    datec = []
    valuec = []
    for i in range(len(date)-1):
        value1 = date[i]
        value2 = date[i+1]
        if value1 not in datec and value1 > date[0]:  # Eliminate NaN and duplicate values
            if value1 == value2:
                valor = (value[i] + value[i+1]) / 2
                valuec.append(float("{0:.2f}".format(valor,2)))
                datec.append(value1)
            if value1 != value2:
                valuec.append(float("{0:.2f}".format(value[i],2)))
                datec.append(value1)
    datec = pd.Series(datec)
    
    return valuec, datec


def plots(dCO, CO, dCO2, CO2, dP, P, dnp, nP, dnb, nb, de, e, dmp, mp, dmb, mb):
    "Plot timeseries and histogram for the given data"
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
    plt.hist(CO, bins='auto', label='histogram with raw data')
    plt.title('CO histogram')
    plt.xlabel('nmol/mol')
    plt.figure(num=10)
    plt.hist(CO2, bins='auto', label='histogram with raw data')
    plt.title('CO2 histogram')
    plt.xlabel('ppm')
    plt.figure(num=11)
    plt.hist(P, bins='auto', label='histogram with raw data')
    plt.title('Propane histogram')
    plt.xlabel('pmol/mol')
    plt.figure(num=12)
    plt.hist(nP, bins='auto', label='histogram with raw data')
    plt.title('n-pentane histogram')
    plt.xlabel('pmol/mol')
    plt.figure(num=13)
    plt.hist(nb, bins='auto', label='histogram with raw data')
    plt.title('n-butane histogram')
    plt.xlabel('pmol/mol')
    plt.figure(num=14)
    plt.hist(nb, bins='auto', label='histogram with raw data')
    plt.title('Ethane histogram')
    plt.xlabel('pmol/mol')
    plt.figure(num=15)
    plt.hist(nb, bins='auto', label='histogram with raw data')
    plt.title('Methylpropane histogram')
    plt.xlabel('pmol/mol')
    plt.figure(num=16)
    plt.hist(nb, bins='auto', label='histogram with raw data')
    plt.title('Methylbutane histogram')
    plt.xlabel('pmol/mol')
    
    
    
"Use of the functions"
# Transfer the data to the idle
dCO, CO, dCO2, CO2, dP, P, dNP, NP, dNB, NB, dE, E, dMP, MP, dMB, MB = data_transfer_E(dat)
# Calculate the mean average for every vocs 
co, dco = prom(dCO, CO)
co2, dco2 = prom(dCO2, CO2)
nanlistco2 = nan_spot(co2)
p, dp = prom(dP, P)
nP, dnP = prom(dNP, NP)
nb, dnb = prom(dNB, NB)
e, de = prom(dE, E)
mp, dmp = prom(dMP, MP)
mb, dmb = prom(dMB, MB)
# Plot timeseries and histogram of every vocs
plots(dco, co, dco2, co2, dp, p, dnP, nP, dnb, nb, de, e, dmp, mp, dmb, mb)
