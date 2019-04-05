# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 12:22:44 2018
Rapa Nui's Soundings Analysis (OZONE)
@author: David Trejo Cancino
DGF Uchile

"""
import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd
import calendar
from ozonefunctions import date, data_transfer, data_cleansing, meses, media
print ('Easter Islands Ozone Analysis')

" USO DE LAS FUNCIONES "
# Events analysis
filenames = sorted(glob.glob('rapanui*.dat'))
O3n = []
FECHA =[]
j = 0
for value in filenames:
    j = j + 1
    o3 = []
    data = open(value, 'r')  # Data reading
    datos = data.readlines()
    h, press, tem, RH, O3mPa, O3ppbv, O3DU, u,\
    v, th, the, Q = data_transfer(datos)
    RHf, h_RH, Tf, h_T, O3, h_O3, u, h_u,\
    v, h_v, o3ppb, hppb = data_cleansing(h, press, tem, RH, O3mPa,\
                                         O3ppbv, O3DU, u, v, th, the, Q)
    y, m, d, name = date(value)
    s = pd.Series(repr(d) + '/' + repr(m) + '/' + repr(y))
    fecha = pd.to_datetime(s, format='%d/%m/%Y')
    o3ppb = np.asarray(o3ppb)
    if j == 1:
        O3dia=o3ppb
        Heigth=hppb
        DiaMuestra=fecha
    i = 0
    try:
        while hppb[i] <= 1.5:
            o3rec = []
            i = i + 1
            o3rec.append(o3ppb[i])
        o3rec = np.asarray(o3rec)
        o3mean = np.mean(o3rec)
    except IndexError:
        pass
    try:
        O3n.append(o3mean)
        FECHA.append(fecha)
    except:
        pass

# Monthly analysis
en, feb, mar, abr, may, jun, jul, ag, sep, octu, nov, dic = meses(FECHA, O3n)
#year = media(en, feb, mar, abr, may, jun, jul, ag, sep, octu, nov, dic)
yearOZ = [en, feb, mar, abr, may, jun, jul, ag, sep, octu, nov, dic]
'Plots'
O3n = pd.DataFrame(O3n)
O3n.fillna(method='ffill', limit=1)
t = np.linspace(1, 12, 12)
plt.figure(num=1, figsize=[10,8])
plt.stem(FECHA, O3n)
plt.xlabel('Years')
plt.ylabel('Ozone Concentration [ppbv]')
plt.title('Mean Ozone Concentrations of Rapa Nui\'s Boundary \
Layer')
plt.figure(num=2, figsize=[10,8])
plt.boxplot(yearOZ)
#plt.plot(t, year, '*--')
plt.title('Monthly Ozone Concentrations of Rapa Nui\'s Boundary \
Layer')
plt.xlabel('Months')
plt.ylabel('Ozone Concentration [ppbv]')
plt.ylim([0, 50])
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
'Vertical Plot'
plt.figure(num=3, figsize=[12,10])
plt.subplot(2,1,1)
plt.plot(O3dia, Heigth, '-.')
plt.xlabel('Ozone Concentration [ppbv]')
plt.ylabel('Altitude [km]')
plt.title('Heigth ozone profile, 2006/02/25')
plt.hlines(1.5, 0, 10000)
plt.legend(['Ozone Concentration', 'Boundary Layer'])
plt.subplot(2,1,2)
plt.plot(O3dia, Heigth, '-.')
plt.xlabel('Ozone Concentration [ppbv]')
plt.ylabel('Altitude [km]')
plt.title('Heigth ozone profile, 2006/02/25')
plt.hlines(1.5, 0, 10000)
plt.legend(['Ozone Concentration', 'Boundary Layer'])  
plt.xlim([0, 50])
plt.ylim([0, 3])