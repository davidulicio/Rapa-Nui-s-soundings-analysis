# -*- coding: utf-8 -*-
"""
Rapa Nui
@author: David Trejo Cancino
"""
import pandas as pd
import matplotlib.pyplot as plt
from data_uso import data_transfer_E, prom
from rawEI import subplots
#dat = pd.read_excel(r'C:\Users\David\Box Sync\Rapa Nui Complete dataset\RapaNui.xlsx', header=0)
dat= pd.read_excel(r'RapaNui.xlsx', header=0)
"Functions"

def spring_subplots(dCO, CO, dCO2, CO2, dP, P, dnp, nP, dnb, nb, de, e, dmp, mp, dmb, mb):
    "Generates timeseries and histogram plots for every vocs in Easter Island"
    fig1, (axtco, axhco) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtco.plot(dCO, CO)
    axtco.set_title('Spring CO timeseries, Easter Island')
    axtco.set_xlabel('Years')
    axtco.set_ylabel('nmol/mol (ppb)')
    axhco.hist(CO, bins=20)
    axhco.set_xlabel('nmol/mol (ppb)')
    axhco.set_title('Spring CO histogram with raw data')
    fig2, (axtco2, axhco2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtco2.plot(dCO2, CO2)
    axtco2.set_title('Spring CO2 timeseries, Easter Island')
    axtco2.set_xlabel('Years')
    axtco2.set_ylabel('ppm')
    axhco2.hist(CO2, bins=20)
    axhco2.set_xlabel('ppm')
    axhco2.set_title('Spring CO2 histogram with raw data')
    fig3, (axtp, axhp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtp.plot(dP, P)
    axtp.set_title('Spring Propane timeseries, Easter Island')
    axtp.set_xlabel('Years')
    axtp.set_ylabel('pmol/mol')
    axhp.hist(P, bins=20)
    axhp.set_xlabel('pmol/mol')
    axhp.set_title('Spring Propane histogram with raw data')
    fig4, (axtnp, axhnp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtnp.plot(dnp, nP)
    axtnp.set_title('Spring n-pentane timeseries, Easter Island')
    axtnp.set_xlabel('Years')
    axtnp.set_ylabel('pmol/mol')
    axhnp.hist(nP, bins=20)
    axhnp.set_xlabel('pmol/mol')
    axhnp.set_title('Spring n-pentane histogram with raw data')
    fig5, (axtnb, axhnb) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtnb.plot(dnb, nb)
    axtnb.set_title('Spring n-butane timeseries, Easter Island')
    axtnb.set_xlabel('Years')
    axtnb.set_ylabel('pmol/mol')
    axhnb.hist(nb, bins='auto')
    axhnb.set_xlabel('pmol/mol')
    axhnb.set_title('Spring n-butane histogram with raw data')
    fig6, (axte, axhe) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axte.plot(de, e)
    axte.set_title('Spring Ethane timeseries, Easter Island')
    axte.set_xlabel('Years')
    axte.set_ylabel('pmol/mol')
    axhe.hist(e, bins=20)
    axhe.set_xlabel('pmol/mol')
    axhe.set_title('Spring Ethane histogram with raw data')
    fig7, (axtmp, axhmp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtmp.plot(dmp, mp)
    axtmp.set_title('Spring Methylpropane timeseries, Easter Island')
    axtmp.set_xlabel('Years')
    axtmp.set_ylabel('pmol/mol')
    axhmp.hist(mp, bins=20)
    axhmp.set_xlabel('pmol/mol')
    axhmp.set_title('Spring Metylpropane histogram with raw data')
    fig8, (axtmb, axhmb) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtmb.plot(dmb, mb)
    axtmb.set_title('Spring Methylbutane timeseries, Easter Island')
    axtmb.set_xlabel('Years')
    axtmb.set_ylabel('pmol/mol')
    axhmb.hist(mp, bins=20)
    axhmb.set_xlabel('pmol/mol')
    axhmb.set_title('Spring Metylbutane histogram with raw data')

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
# Plot timeseries and histogram of every vocs
subplots(dco, co, dco2, co2, dp, p, dnP, nP, dnb, nb, de, 
                    e, dmp, mp, dmb, mb)
"""
dco, co = spring(dco, co)
dco2, co2 = spring(dco2, co2)
dp, p = spring(dp, p)
dnP, nP = spring(dnP, nP)
dnb, nb = spring(dnb, nb)
de, e = spring(de, e)
dmp, mp = spring(dmp, mp)
dmb, mb = spring(dmb, mb)
spring_subplots(dco, co, dco2, co2, dp, p, dnP, nP, dnb, nb, de, e, dmp, mp,
                dmb, mb)
"""