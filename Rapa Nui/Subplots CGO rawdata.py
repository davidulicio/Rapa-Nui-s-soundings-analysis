# -*- coding: utf-8 -*-
"""
Cape Grim
@author: David Trejo Cancino
"""

import pandas as pd
from data_uso import data_transfer_E, prom
from rawCGO import subplots

dat = pd.read_excel(r'C:\Users\David\Box Sync\Cape Grim, Tazmania\Cape Grim.xlsx', header=0)


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
subplots(dco, co, dco2, co2, dp, p, dnP, nP, dnb, nb, de, e, dmp, mp, dmb, mb)
