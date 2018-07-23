# -*- coding: utf-8 -*-
"""
Easter Island Analysis
@author: David
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dat = pd.read_excel(r'C:\Users\David\Desktop\Rapa Nui Complete dataset\RapaNui.xlsx', header=0)

"Functions"


def data_transfer_E(dat):
    "Transfer data from the excel file to python"
    dCO = dat['CO date']
    CO = dat['CO'] / 1000
    dCO2 = pd.Series(dat['CO2 date'])
    CO2 = dat['CO2'] / 1000
    dP = pd.Series(dat['Propane date'])
    P = dat['Propane'] / 1000
    dnp = pd.Series(dat['n-pentane date'])
    nP = dat['n-pentane'] / 1000
    dnb = pd.Series(dat['n-butane date'])
    nb = dat['n-butane'] / 1000
    de = pd.Series(dat['ethane date'])
    e = dat['ethane'] / 1000
    dmp = pd.Series(dat['methylpropane date'])
    mp = dat['methylpropane'] / 1000
    dmb = pd.Series(dat['methylbutane date'])
    mb = dat['methylbutane'] / 1000
    return dCO, CO, dCO2, CO2, dP, P, dnp, nP, dnb, nb, de, e, dmp, mp, dmb, mb


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
                valuec.append(float("{0:.2f}".format(valor, 2)))
                datec.append(value1)
            if value1 != value2:
                valuec.append(float("{0:.2f}".format(value[i], 2)))
                datec.append(value1)
    datec = pd.Series(datec)
    return valuec, datec

def data_cleansing(values, date):
    

"Use of the functions"
# Transfer the data to the idle
dCO, CO, dCO2, CO2, dP, P, dNP, NP, dNB, NB, dE, E, dMP, MP, dMB, MB = data_transfer_E(dat)
# Calculate the mean average for every vocs
co, dco = prom(dCO, CO)
co2, dco2 = prom(dCO2, CO2)
#co2 = np.asarray(co2)
p, dp = prom(dP, P)
nP, dnP = prom(dNP, NP)
nb, dnb = prom(dNB, NB)
e, de = prom(dE, E)
mp, dmp = prom(dMP, MP)
mb, dmb = prom(dMB, MB)