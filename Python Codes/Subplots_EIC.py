# -*- coding: utf-8 -*-
"""
Easter Island Analysis
@author: David
"""
import calendar
import pandas as pd
import scipy as sp
import scipy.signal as ss
import matplotlib.pyplot as plt
import numpy
from sklearn.linear_model import LinearRegression
from data_uso import data_transfer_E, prom, meses, media
from cleansing_eic import data_cleansing, hist_clean
from funct_subEIC import subplots, mixing_ratios, example_clean
from ozone import yearOZ
#%% Data reading and simple statistics
directoriow = pd.read_excel(r'RapaNui.xlsx', header=0)
#directoriow = pd.read_excel(r'Easter_Island.xlsx', header=0)
"Use of the imported functions"
# The next line transfers the data to the idle
dCO, CO, dCO2, CO2, dP, P, dNP, NP, dNB, NB, dE, E, dMP, MP, dMB,\
 MB = data_transfer_E(directoriow)
# The following ones calculates the mean average for every vocs
co, dco = prom(dCO, CO)
co2, dco2 = prom(dCO2, CO2)
p, dp = prom(dP, P)
nP, dnP = prom(dNP, NP)
nb, dnb = prom(dNB, NB)
e, de = prom(dE, E)
mp, dmp = prom(dMP, MP)
mb, dmb = prom(dMB, MB)
# The following lines clean the data for a better analysis
dCO, CO, dCO2, CO2, dP, P, dNP, NP, dNB, NB, dE, E, dMP, MP, \
dMB, MB = data_cleansing(dco, co, dco2, co2, dp, p, dnP, nP, dnb,\
                         nb, de, e, dmp, mp, dmb, mb)
dCO, CO = hist_clean(dCO,CO)
dCO2, CO2 = hist_clean(dCO2,CO2)
dP, P = hist_clean(dP,P)
dNP, NP = hist_clean(dNP,NP)
dNB, NB = hist_clean(dNB,NB)
dE, E = hist_clean(dE,E)
dMP, MP = hist_clean(dMP,MP)
dMB, MB = hist_clean(dMB,MB)
meanco = sp.nanmean(CO)
meanco2 = sp.nanmean(CO2)
meanp = sp.nanmean(P)
meannp = sp.nanmean(NP)
meannb = sp.nanmean(NB)
meane = sp.nanmean(E)
meanmp = sp.nanmean(MP)
meanmb = sp.nanmean(MB)
#%% Detrends
# Detrending the data for each voc
CO = ss.detrend(CO) + meanco
CO2 = ss.detrend(CO2) + meanco2
P = ss.detrend(P) + meanp
NP = ss.detrend(NP) + meannp
NB = ss.detrend(NB) + meannb
E = ss.detrend(E) + meane
MP = ss.detrend(MP) + meanmp
MB = ss.detrend(MB) + meanmb
example_clean(dco2, co2, dCO2, CO2)
subplots(dCO, CO, dCO2, CO2, dP, P, dNP, NP, dNB, NB, dE, E, dMP, MP, dMB, MB)
#%% Monthly concentrations plots
"Monthly Concentrations"
t = numpy.linspace(1, 12, 12)
'CO Monthly concentrations'
eco, fco, mrco, aco, myco, jco, jlco, agco, sco, oco, nco, dco = meses(dco, co)
yearco = [eco, fco, mrco, aco, myco, jco, jlco, agco, sco, oco, nco, dco]
Eco, Fco, Mrco, Aco, Myco, Jco, Jlco, Agco, Sco, Oco, Nco, Dco = meses(dCO, CO)
yearCO = [Eco, Fco, Mrco, Aco, Myco, Jco, Jlco, Agco, Sco, Oco, Nco, Dco]
fig1, (axtco, axhco) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axtco, axhco
axtco.boxplot(yearco)
axtco.set_title('CO raw monthly concentrations, EIC')
axtco.set_xlabel('Months')
axtco.set_ylabel('nmol/mol (ppb)')
axhco.boxplot(yearCO)
axhco.set_xlabel('Months')
axhco.set_title('CO filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'CO2 Monthly concentrations'
eco2, fco2, mrco2, aco2, myco2, jco2,\
 jlco2, agco2, sco2, oco2, nco2, dco2 = meses(dco2, co2)
yearco2 = [eco2, fco2, mrco2, aco2, myco2, jco2, jlco2, agco2, 
           sco2, oco2, nco2, dco2]
Eco2, Fco2, Mrco2, Aco2, Myco2, Jco2,\
 Jlco2, Agco2, Sco2, Oco2, Nco2, Dco2 = meses(dCO2, CO2)
yearCO2 = [Eco2, Fco2, Mrco2, Aco2, Myco2, Jco2, Jlco2, Agco2, Sco2, Oco2, 
           Nco2, Dco2]
fig2, (axtco2, axhco2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axtco2, axhco2
axtco2.boxplot(yearco2)
axtco2.set_title('CO2 raw monthly concentrations, EIC')
axtco2.set_xlabel('Months')
axtco2.set_ylabel('ppm')
axhco2.boxplot(yearCO2)
axhco2.set_xlabel('Months')
axhco2.set_title('CO2 filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'Propane Monthly concentrations'
ep, fp, mrp, ap, myp, jp, jlp, agp, sp, op, np, dp = meses(dp, p)
yearp = [ep, fp, mrp, ap, myp, jp, jlp, agp, sp, op, np, dp]
Ep, Fp, Mrp, Ap, Myp, Jp, Jlp, Agp, Sp, Op, Np, Dp = meses(dP, P)
yearP = [Ep, Fp, Mrp, Ap, Myp, Jp, Jlp, Agp, Sp, Op, Np, Dp]
fig3, (axtp, axhp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axtp, axhp
axtp.boxplot(yearp)
axtp.set_title('Propane raw monthly concentrations, EIC')
axtp.set_xlabel('Months')
axtp.set_ylabel('pmol/mol')
axhp.boxplot(yearP)
axhp.set_xlabel('Months')
axhp.set_title('Propane filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'n-pentane Monthly concentrations'
enP, fnP, mrnP, anP, mynP, jnP, jlnP, agnP, snP, onP, nnP, dnP = meses(dnP, nP)
yearnP = [enP, fnP, mrnP, anP, mynP, jnP, jlnP, agnP, snP, onP, nnP, dnP]
EnP, FnP, MrnP, AnP, MynP, JnP, JlnP, AgnP, SnP, OnP, NnP, DnP = meses(dNP, NP)
yearNP = [EnP, FnP, MrnP, AnP, MynP, JnP, JlnP, AgnP, SnP, OnP, NnP, DnP]
fig4, (axtnp, axhnp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axtnp, axhnp
axtnp.boxplot(yearnP)
axtnp.set_title('n-pentane raw monthly concentrations, EIC')
axtnp.set_xlabel('Months')
axtnp.set_ylabel('pmol/mol')
axhnp.boxplot(yearNP)
axhnp.set_xlabel('Months')
axhnp.set_title('n-pentane filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'n-butane Monthly concentrations'
enb, fnb, mrnb, anb, mynb, jnb, jlnb, agnb, snb, onb, nnb, dnb = meses(dnb, nb)
yearnb = [enb, fnb, mrnb, anb, mynb, jnb, jlnb, agnb, snb, onb, nnb, dnb]
Enb, Fnb, Mrnb, Anb, Mynb, Jnb, Jlnb, Agnb, Snb, Onb, Nnb, Dnb = meses(dNB, NB)
yearNB = [Enb, Fnb, Mrnb, Anb, Mynb, Jnb, Jlnb, Agnb, Snb, Onb, Nnb, Dnb]
fig5, (axtnb, axhnb) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axtnb, axhnb
axtnb.boxplot(yearnb)
axtnb.set_title('n-butane raw monthly concentrations, EIC')
axtnb.set_xlabel('Months')
axtnb.set_ylabel('pmol/mol')
axhnb.boxplot(yearNB)
axhnb.set_xlabel('Months')
axhnb.set_title('n-butane filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'Ethane Monthly concentrations'
ee, fe, mre, ae, mye, je, jle, age, se, oe, ne, de = meses(de, e)
yeare = [ee, fe, mre, ae, mye, je, jle, age, se, oe, ne, de]
Ee, Fe, Mre, Ae, Mye, Je, Jle, Age, Se, Oe, Ne, De = meses(dE, E)
yearE = [Ee, Fe, Mre, Ae, Mye, Je, Jle, Age, Se, Oe, Ne, De]
fig6, (axte, axhe) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axte, axhe
axte.boxplot(yeare)
axte.set_title('Ethane raw monthly concentrations, EIC')
axte.set_xlabel('Months')
axte.set_ylabel('pmol/mol')
axhe.boxplot(yearE)
axhe.set_xlabel('Months')
axhe.set_title('Ethane filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'Methylpropane Monthly concentrations'
emp, fmp, mrmp, amp, mymp, jmp, jlmp, agmp, smp, omp, nmp, dmp = meses(dmp, mp)
yearmp = [emp, fmp, mrmp, amp, mymp, jmp, jlmp, agmp, smp, omp, nmp, dmp]
Emp, Fmp, Mrmp, Amp, Mymp, Jmp, Jlmp, Agmp, Smp, Omp, Nmp, Dmp = meses(dMP, MP)
yearMP = [Emp, Fmp, Mrmp, Amp, Mymp, Jmp, Jlmp, Agmp, Smp, Omp, Nmp, Dmp]
fig6, (axtmp, axhmp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axtmp, axhmp
axtmp.boxplot(yearmp)
axtmp.set_title('Methylpropane raw monthly concentrations, EIC')
axtmp.set_xlabel('Months')
axtmp.set_ylabel('pmol/mol')
axhmp.boxplot(yearMP)
axhmp.set_xlabel('Months')
axhmp.set_title('Methylpropane filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'Methylbutane Monthly concentrations'
emb, fmb, mrmb, amb, mymb, jmb, jlmb, agmb, smb, omb, nmb, dmb = meses(dmb, mb)
yearmb = [emb, fmb, mrmb, amb, mymb, jmb, jlmb, agmb, smb, omb, nmb, dmb]
Emb, Fmb, Mrmb, Amb, Mymb, Jmb, Jlmb, Agmb, Smb, Omb, Nmb, Dmb = meses(dMB, MB)
yearMB = [Emb, Fmb, Mrmb, Amb, Mymb, Jmb, Jlmb, Agmb, Smb, Omb, Nmb, Dmb]
fig6, (axtmb, axhmb) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axtmb, axhmb
axtmb.boxplot(yearmb)
axtmb.set_title('Methylbutane raw monthly concentrations, EIC')
axtmb.set_xlabel('Months')
axtmb.set_ylabel('pmol/mol')
axhmb.boxplot(yearMB)
axhmb.set_xlabel('Months')
axhmb.set_title('Methylbutane filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
#%% Some extra figures
'LAST FIGURE FOR ANALYSIS'
fig7, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
oz = axes[0]
eth = axes[1]
carbmonx = axes[2]
oz.boxplot(yearOZ)
oz.set_title('Ozone monthly concentrations, EIC')
oz.set_xlabel('Months')
oz.set_ylabel('ppbv')
eth.boxplot(yearE)
eth.set_title('Ethane monthly concentrations, EIC')
eth.set_xlabel('Months')
eth.set_ylabel('pmol/mol')
carbmonx.boxplot(yearCO)
carbmonx.set_title('CO monthly concentrations, EIC')
carbmonx.set_xlabel('Months')
carbmonx.set_ylabel('ppbv')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'Example of cleansing'

"Mixing Ratios"
#yearCO = numpy.asarray(yearCO)
#yearCO=numpy.division(yearCO / float(1000)
#mixing_ratios(yearCO, yearCO2, 'CO2')
#yearCO=yearCO * 1000
#mixing_ratios(yearCO, yearP, 'Propane')
#mixing_ratios(yearCO, yearNP, 'n-pentane')
#mixing_ratios(yearCO, yearNB, 'n-butane')
#mixing_ratios(yearCO, yearE, 'Ethane')
#mixing_ratios(yearCO, yearMP, 'Methylpropane')
#mixing_ratios(yearCO, yearMB, 'Methylbutane')
#%% Regression
#date=numpy.asarray(dCO).reshape((-1, 1))
#model = LinearRegression()
#model.fit(date, CO)
#r_sq = model.score(date, CO)
#print('intercept:', model.intercept_)
#print('slope:', model.coef_)
#slope, intercept, r_value, p_value, std_err = sp.stats.linregress(x,y)
CO = numpy.asarray(CO)
Trend = CO - numpy.mean(CO)
plt.figure()
plt.plot(Trend)