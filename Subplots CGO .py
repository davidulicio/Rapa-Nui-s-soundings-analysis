# -*- coding: utf-8 -*-
"""
Cape Grim Analysis
@author: David
"""
import pandas as pd
import matplotlib.pyplot as plt
dat = pd.read_excel(r'C:\Users\David\Desktop\Cape Grim, Tazmania\Cape Grim.xlsx', header=0)

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

def data_cleansing(dco, co, dco2, co2, dp, p, dnP, nP, dnb, nb, de, 
                    e, dmp, mp, dmb, mb):
    "A filter for the values of the concentrations is applied to the raw data"
    # co filter
    DCO = []
    CO = []
    for i in range(len(co)):
        value = co[i]
        date = dco[i]
        if 35 <= value <= 85:
            CO.append(value)
            DCO.append(date)
    # co2 filter
    DCO2 = []
    CO2 = []
    for i in range(len(co2)):
        value = co2[i]
        date = dco2[i]
        if 340 <= value <= 410:
            CO2.append(value)
            DCO2.append(date)
    # ethane filter
    DE = []
    E = []
    for i in range(len(e)):
        value = e[i]
        date = de[i]
        if 0 <= value <= 700:
            E.append(value)
            DE.append(date)
    # propane filter
    DP = []
    P = []
    for i in range(len(p)):
        value = p[i]
        date = dp[i]
        if 0 <= value <= 100:
            P.append(value)
            DP.append(date)
    # methylbutane filter
    DMB = []
    MB = []
    for i in range(len(mb)):
        value = mb[i]
        date = dmb[i]
        if 0 <= value <= 40:
            MB.append(value)
            DMB.append(date)
    # methylpropane filter
    DMP = []
    MP = []
    for i in range(len(mp)):
        value = mp[i]
        date = dmp[i]
        if 0 <= value <= 35:
            MP.append(value)
            DMP.append(date)
    # n-pentane filter
    DNP = []
    NP = []
    for i in range(len(nP)):
        value = nP[i]
        date = dnP[i]
        if 0 <= value <= 40:
            NP.append(value)
            DNP.append(date)
    # n-butane filter
    DNB = []
    NB = []
    for i in range(len(nb)):
        value = nb[i]
        date = dnb[i]
        if 0 <= value <= 60:
            NB.append(value)
            DNB.append(date)
    return DCO, CO, DCO2, CO2, DP, P, DNP, NP, DNB, NB, DE, E, DMP, MP, DMB, MB


def subplots(dCO, CO, dCO2, CO2, dP, P, dnp, nP, dnb, nb, de, e, dmp, mp, dmb, mb):
    "Generates timeseries and histogram plots for every vocs in Cape Grim"
    fig1, (axtco, axhco) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtco.plot(dCO, CO)
    axtco.set_title('CO timeseries, Cape Grim')
    axtco.set_xlabel('Years')
    axtco.set_ylabel('nmol/mol (ppb)')
    axhco.hist(CO, bins=70)
    axhco.set_xlabel('nmol/mol (ppb)')
    axhco.set_title('CO histogram')
    fig2, (axtco2, axhco2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtco2.plot(dCO2, CO2)
    axtco2.set_title('CO2 timeseries, Cape Grim')
    axtco2.set_xlabel('Years')
    axtco2.set_ylabel('ppm')
    axhco2.hist(CO2, bins=70)
    axhco2.set_xlabel('ppm')
    axhco2.set_title('CO2 histogram')
    fig3, (axtp, axhp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtp.plot(dP, P)
    axtp.set_title('Propane timeseries, Cape Grim')
    axtp.set_xlabel('Years')
    axtp.set_ylabel('pmol/mol')
    axhp.hist(P, bins=70)
    axhp.set_xlabel('pmol/mol')
    axhp.set_title('Propane histogram')
    fig4, (axtnp, axhnp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtnp.plot(dnp, nP)
    axtnp.set_title('n-pentane timeseries, Cape Grim')
    axtnp.set_xlabel('Years')
    axtnp.set_ylabel('pmol/mol')
    axhnp.hist(nP, bins=70)
    axhnp.set_xlabel('pmol/mol')
    axhnp.set_title('n-pentane histogram')
    fig5, (axtnb, axhnb) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtnb.plot(dnb, nb)
    axtnb.set_title('n-butane timeseries, Cape Grim')
    axtnb.set_xlabel('Years')
    axtnb.set_ylabel('pmol/mol')
    axhnb.hist(nb, bins='auto')
    axhnb.set_xlabel('pmol/mol')
    axhnb.set_title('n-butane histogram')
    fig6, (axte, axhe) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axte.plot(de, e)
    axte.set_title('Ethane timeseries, Cape Grim')
    axte.set_xlabel('Years')
    axte.set_ylabel('pmol/mol')
    axhe.hist(e, bins=70)
    axhe.set_xlabel('pmol/mol')
    axhe.set_title('Ethane histogram')
    fig7, (axtmp, axhmp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtmp.plot(dmp, mp)
    axtmp.set_title('Methylpropane timeseries, Cape Grim')
    axtmp.set_xlabel('Years')
    axtmp.set_ylabel('pmol/mol')
    axhmp.hist(mp, bins=70)
    axhmp.set_xlabel('pmol/mol')
    axhmp.set_title('Metylpropane histogram')
    fig8, (axtmb, axhmb) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtmb.plot(dmb, mb)
    axtmb.set_title('Methylbutane timeseries, Cape Grim')
    axtmb.set_xlabel('Years')
    axtmb.set_ylabel('pmol/mol')
    axhmb.hist(mp, bins=70)
    axhmb.set_xlabel('pmol/mol')
    axhmb.set_title('Metylbutane histogram')


"Use of the functions"
# Transfer the data to the idle
dCO, CO, dCO2, CO2, dP, P, dNP, NP, dNB, NB, dE, E, dMP, MP, dMB, MB = data_transfer_E(dat)
# Calculate the mean average for every vocs
co, dco = prom(dCO, CO)
co2, dco2 = prom(dCO2, CO2)
p, dp = prom(dP, P)
nP, dnP = prom(dNP, NP)
nb, dnb = prom(dNB, NB)
e, de = prom(dE, E)
mp, dmp = prom(dMP, MP)
mb, dmb = prom(dMB, MB)
dCO, CO, dCO2, CO2, dP, P, dNP, NP, dNB, NB, dE, E, dMP, MP, dMB, MB = data_cleansing(dco, co, dco2, co2, dp, p, dnP, nP, dnb, nb, de, 
                    e, dmp, mp, dmb, mb)
subplots(dCO, CO, dCO2, CO2, dP, P, dNP, NP, dNB, NB, dE, E, dMP, MP, dMB, MB)
