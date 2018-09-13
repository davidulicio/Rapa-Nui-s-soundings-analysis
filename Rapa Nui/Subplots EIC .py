# -*- coding: utf-8 -*-
"""
Easter Island Analysis
@author: David
"""

import pandas as pd
from data_uso import data_transfer_E, prom
from cleansing_eic import data_cleansing
from funct_subEIC import subplots

dat = pd.read_excel(r'C:\Users\David\Box Sync\Rapa Nui Complete dataset\RapaNui.xlsx', header=0)

"Use of the imported functions"
# The next line transfers the data to the idle
dCO, CO, dCO2, CO2, dP, P, dNP, NP, dNB, NB, dE, E, dMP, MP, dMB, MB = data_transfer_E(dat)
# The following ones calculates the mean average for every vocs
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