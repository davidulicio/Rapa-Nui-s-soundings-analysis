# -*- coding: utf-8 -*-
"""
Correlation between ozone and VOCs
@author: DavidUlises
"""
import numpy as np
from Subplots_EIC import yearCO, yearCO2, yearP, yearNP, yearNB, yearE, yearMP, yearMB
from ozone import year

# Correlation coeficients
co = np.corrcoef(yearCO, year)
co2 = np.corrcoef(yearCO2, year)
p = np.corrcoef(yearP, year)
np = np.corrcoef(yearNP, year)
nb = np.corrcoef(yearNB, year)
e = np.corrcoef(yearE, year)
mp = np.corrcoef(yearMP, year)
mb = np.corrcoef(yearMB, year)
