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
from data_uso import data_transfer_E, prom, meses, media
from cleansing_eic import data_cleansing, hist_clean
from funct_subEIC import subplots, mixing_ratios

directoriow = pd.read_excel(r'RapaNui.xlsx', header=0)

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
dCO, CO = hist_clean(dco,co)
dCO2, CO2 = hist_clean(dco2,co2)
dP, P = hist_clean(dp,p)
dNP, NP = hist_clean(dnP,nP)
dNB, NB = hist_clean(dnb,nb)
dE, E = hist_clean(de,e)
dMP, MP = hist_clean(dmp,mp)
dMB, MB = hist_clean(dmb,mb)
meanco = sp.mean(CO)
meanco2 = sp.mean(CO2)
meanp = sp.mean(P)
meannp = sp.mean(NP)
meannb = sp.mean(NB)
meane = sp.mean(E)
meanmp = sp.mean(MP)
meanmb = sp.mean(MB)
# Detrending the data for each voc
CO = ss.detrend(CO) + meanco
CO2 = ss.detrend(CO2) + meanco2
P = ss.detrend(P) + meanp
NP = ss.detrend(NP) + meannp
NB = ss.detrend(NB) + meannb
E = ss.detrend(E) + meane
MP = ss.detrend(MP) + meanmp
MB = ss.detrend(MB) + meanmb
subplots(dCO, CO, dCO2, CO2, dP, P, dNP, NP, dNB, NB, dE, E, dMP, MP, dMB, MB)

"Monthly Concentrations"
t = numpy.linspace(1, 12, 12)
'CO Monthly concentrations'
eco, fco, mrco, aco, myco, jco, jlco, agco, sco, oco, nco, dco = meses(dco, co)
yearco = media(eco, fco, mrco, aco, myco, jco, jlco, agco, sco, oco, nco, dco)
Eco, Fco, Mrco, Aco, Myco, Jco, Jlco, Agco, Sco, Oco, Nco, Dco = meses(dCO, CO)
yearCO = media(Eco, Fco, Mrco, Aco, Myco, Jco, Jlco, Agco, Sco, Oco, Nco, Dco)
fig1, (axtco, axhco) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axtco, axhco
axtco.plot(t, yearco, '*--')
axtco.set_title('CO raw monthly concentrations, EIC')
axtco.set_xlabel('Months')
axtco.set_ylabel('nmol/mol (ppb)')
axhco.plot(t, yearCO, '*--')
axhco.set_xlabel('Months')
axhco.set_title('CO filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'CO2 Monthly concentrations'
eco2, fco2, mrco2, aco2, myco2, jco2,\
 jlco2, agco2, sco2, oco2, nco2, dco2 = meses(dco2, co2)
yearco2 = media(eco2, fco2, mrco2, aco2, myco2, jco2,\
                jlco2, agco2, sco2, oco2, nco2, dco2)
Eco2, Fco2, Mrco2, Aco2, Myco2, Jco2,\
 Jlco2, Agco2, Sco2, Oco2, Nco2, Dco2 = meses(dCO2, CO2)
yearCO2 = media(Eco2, Fco2, Mrco2, Aco2, Myco2, Jco2,\
                Jlco2, Agco2, Sco2, Oco2, Nco2, Dco2)
fig2, (axtco2, axhco2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axtco2, axhco2
axtco2.plot(t, yearco2, '*--')
axtco2.set_title('CO2 raw monthly concentrations, EIC')
axtco2.set_xlabel('Months')
axtco2.set_ylabel('ppm')
axhco2.plot(t, yearCO2, '*--')
axhco2.set_xlabel('Months')
axhco2.set_title('CO2 filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'Propane Monthly concentrations'
ep, fp, mrp, ap, myp, jp, jlp, agp, sp, op, np, dp = meses(dp, p)
yearp = media(ep, fp, mrp, ap, myp, jp, jlp, agp, sp, op, np, dp)
Ep, Fp, Mrp, Ap, Myp, Jp, Jlp, Agp, Sp, Op, Np, Dp = meses(dP, P)
yearP = media(Ep, Fp, Mrp, Ap, Myp, Jp, Jlp, Agp, Sp, Op, Np, Dp)
fig3, (axtp, axhp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axtp, axhp
axtp.plot(t, yearp, '*--')
axtp.set_title('Propane raw monthly concentrations, EIC')
axtp.set_xlabel('Months')
axtp.set_ylabel('pmol/mol')
axhp.plot(t, yearP, '*--')
axhp.set_xlabel('Months')
axhp.set_title('Propane filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'n-pentane Monthly concentrations'
enP, fnP, mrnP, anP, mynP, jnP, jlnP, agnP, snP, onP, nnP, dnP = meses(dnP, nP)
yearnP = media(enP, fnP, mrnP, anP, mynP, jnP, jlnP, agnP, snP, onP, nnP, dnP)
EnP, FnP, MrnP, AnP, MynP, JnP, JlnP, AgnP, SnP, OnP, NnP, DnP = meses(dNP, NP)
yearNP = media(EnP, FnP, MrnP, AnP, MynP, JnP, JlnP, AgnP, SnP, OnP, NnP, DnP)
fig4, (axtnp, axhnp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axtnp, axhnp
axtnp.plot(t, yearnP, '*--')
axtnp.set_title('n-pentane raw monthly concentrations, EIC')
axtnp.set_xlabel('Months')
axtnp.set_ylabel('pmol/mol')
axhnp.plot(t, yearNP, '*--')
axhnp.set_xlabel('Months')
axhnp.set_title('n-pentane filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'n-butane Monthly concentrations'
enb, fnb, mrnb, anb, mynb, jnb, jlnb, agnb, snb, onb, nnb, dnb = meses(dnb, nb)
yearnb = media(enb, fnb, mrnb, anb, mynb, jnb, jlnb, agnb, snb, onb, nnb, dnb)
Enb, Fnb, Mrnb, Anb, Mynb, Jnb, Jlnb, Agnb, Snb, Onb, Nnb, Dnb = meses(dNB, NB)
yearNB = media(Enb, Fnb, Mrnb, Anb, Mynb, Jnb, Jlnb, Agnb, Snb, Onb, Nnb, Dnb)
fig5, (axtnb, axhnb) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axtnb, axhnb
axtnb.plot(t, yearnb, '*--')
axtnb.set_title('n-butane raw monthly concentrations, EIC')
axtnb.set_xlabel('Months')
axtnb.set_ylabel('pmol/mol')
axhnb.plot(t, yearNB, '*--')
axhnb.set_xlabel('Months')
axhnb.set_title('n-butane filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'Ethane Monthly concentrations'
ee, fe, mre, ae, mye, je, jle, age, se, oe, ne, de = meses(de, e)
yeare = media(ee, fe, mre, ae, mye, je, jle, age, se, oe, ne, de)
Ee, Fe, Mre, Ae, Mye, Je, Jle, Age, Se, Oe, Ne, De = meses(dE, E)
yearE = media(Ee, Fe, Mre, Ae, Mye, Je, Jle, Age, Se, Oe, Ne, De)
fig6, (axte, axhe) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axte, axhe
axte.plot(t, yeare, '*--')
axte.set_title('Ethane raw monthly concentrations, EIC')
axte.set_xlabel('Months')
axte.set_ylabel('pmol/mol')
axhe.plot(t, yearE, '*--')
axhe.set_xlabel('Months')
axhe.set_title('Ethane filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'Methylpropane Monthly concentrations'
emp, fmp, mrmp, amp, mymp, jmp, jlmp, agmp, smp, omp, nmp, dmp = meses(dmp, mp)
yearmp = media(emp, fmp, mrmp, amp, mymp, jmp, jlmp, agmp, smp, omp, nmp, dmp)
Emp, Fmp, Mrmp, Amp, Mymp, Jmp, Jlmp, Agmp, Smp, Omp, Nmp, Dmp = meses(dMP, MP)
yearMP = media(Emp, Fmp, Mrmp, Amp, Mymp, Jmp, Jlmp, Agmp, Smp, Omp, Nmp, Dmp)
fig6, (axtmp, axhmp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axtmp, axhmp
axtmp.plot(t, yearmp, '*--')
axtmp.set_title('Methylpropane raw monthly concentrations, EIC')
axtmp.set_xlabel('Months')
axtmp.set_ylabel('pmol/mol')
axhmp.plot(t, yearMP, '*--')
axhmp.set_xlabel('Months')
axhmp.set_title('Methylpropane filtered monthly concentrations, EIC')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

'Methylbutane Monthly concentrations'
emb, fmb, mrmb, amb, mymb, jmb, jlmb, agmb, smb, omb, nmb, dmb = meses(dmb, mb)
yearmb = media(emb, fmb, mrmb, amb, mymb, jmb, jlmb, agmb, smb, omb, nmb, dmb)
Emb, Fmb, Mrmb, Amb, Mymb, Jmb, Jlmb, Agmb, Smb, Omb, Nmb, Dmb = meses(dMB, MB)
yearMB = media(Emb, Fmb, Mrmb, Amb, Mymb, Jmb, Jlmb, Agmb, Smb, Omb, Nmb, Dmb)
fig6, (axtmb, axhmb) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axtmb, axhmb
axtmb.plot(t, yearmb, '*--')
axtmb.set_title('Methylbutane raw monthly concentrations, EIC')
axtmb.set_xlabel('Months')
axtmb.set_ylabel('pmol/mol')
#axtmb.set_xticks(t, calendar.month_abbr[1:13])
axhmb.plot(t, yearMB, '*--')
axhmb.set_xlabel('Months')
axhmb.set_title('Methylbutane filtered monthly concentrations, EIC')
#axhmb.set_xticks(t, calendar.month_abbr[1:13])
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)

"Mixing Ratios"
yearCO = numpy.asarray(yearCO)
mixing_ratios(yearCO/1000, yearCO2, 'CO2')
mixing_ratios(yearCO*1000, yearP, 'Propane')
mixing_ratios(yearCO*1000, yearNP, 'n-pentane')
mixing_ratios(yearCO*1000, yearNB, 'n-butane')
mixing_ratios(yearCO*1000, yearE, 'Ethane')
mixing_ratios(yearCO*1000, yearMP, 'Methylpropane')
mixing_ratios(yearCO*1000, yearMB, 'Methylbutane')

