# -*- coding: utf-8 -*-
"""
Rapa Nui Analysis
@author: David Trejo C.
"""

import calendar
import pandas as pd
import scipy as sp
import scipy.signal as ss
import matplotlib.pyplot as plt
import numpy as np
from data_uso import data_transfer_E, prom, meses
from cleansing_eic import data_cleansing, hist_clean
from ozone import yearOZ, O3n, FECHA
#%% Data reading and simple statistics
directoriow = pd.read_excel(r'RapaNui.xlsx', header=0)
"Use of the imported functions"
# The next line transfers the data to the variables
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
#%% Raw histograms
plt.figure(num=1, figsize=(12,12))
O3n = np.asarray(O3n)
plt.subplot(3,3,1)
plt.hist(co, 20)
plt.title('CO histogram')
plt.ylabel('ppbv')
plt.subplot(3,3,2)
plt.hist(co2, 20)
plt.title('CO2 histogram')
plt.ylabel('ppmv')
plt.subplot(3,3,3)
plt.hist(e, 20)
plt.title('Ethane histogram')
plt.ylabel('pptv')
plt.subplot(3,3,4)
plt.hist(p, 20)
plt.title('Propane histogram')
plt.ylabel('pptv')
plt.subplot(3,3,5)
plt.hist(nP, 20)
plt.title('n-pentane histogram')
plt.ylabel('pptv')
plt.subplot(3,3,6)
plt.hist(nb, 20)
plt.title('n-butane histogram')
plt.ylabel('pptv')
plt.subplot(3,3,7)
plt.hist(mp, 20)
plt.title('Methylpropane histogram')
plt.ylabel('pptv')
plt.subplot(3,3,8)
plt.hist(mb, 20)
plt.title('Methylbutane histogram')
plt.ylabel('pptv')
plt.subplot(3,3,9)
plt.hist(O3n, 20)
plt.title('Ozone histogram')
plt.ylabel('ppbv')
plt.tight_layout()
#%% Cleansed histograms
plt.figure(num=2, figsize=(12,12))
plt.subplot(3,3,1)
plt.hist(CO, 20)
plt.title('CO histogram')
plt.ylabel('ppbv')
plt.subplot(3,3,2)
plt.hist(CO2, 20)
plt.title('CO2 histogram')
plt.ylabel('ppmv')
plt.subplot(3,3,3)
plt.hist(E, 20)
plt.title('Ethane histogram')
plt.ylabel('pptv')
plt.subplot(3,3,4)
plt.hist(P, 20)
plt.title('Propane histogram')
plt.ylabel('pptv')
plt.subplot(3,3,5)
plt.hist(NP, 20)
plt.title('n-pentane histogram')
plt.ylabel('pptv')
plt.subplot(3,3,6)
plt.hist(NB, 20)
plt.title('n-butane histogram')
plt.ylabel('pptv')
plt.subplot(3,3,7)
plt.hist(MP, 20)
plt.title('Methylpropane histogram')
plt.ylabel('pptv')
plt.subplot(3,3,8)
plt.hist(MB, 20)
plt.title('Methylbutane histogram')
plt.ylabel('pptv')
plt.subplot(3,3,9)
plt.hist(O3n, 20)
plt.title('Ozone histogram')
plt.ylabel('ppbv')
plt.tight_layout()
#%% Typical values - raw data
'CO'
print('Mean CO: '+ repr(np.mean(co)))
print('Median CO: '+ repr(np.median(co)))
print('Min CO: '+ repr(np.min(co)))
print('Max CO : '+ repr(np.max(co)))
print('Std CO: '+ repr(np.std(co)))
'CO2'
print('Mean CO2: '+ repr(np.mean(co2)))
print('Median CO2: '+ repr(np.median(co2)))
print('Min CO2: '+ repr(np.min(co2)))
print('Max CO2 : '+ repr(np.max(co2)))
print('Std CO2: '+ repr(np.std(co2)))
'ETHANE'
print('Mean E: '+ repr(np.mean(e)))
print('Median E: '+ repr(np.median(e)))
print('Min E: '+ repr(np.min(e)))
print('Max E : '+ repr(np.max(e)))
print('Std E: '+ repr(np.std(e)))
'PROPANE'
print('Mean P: '+ repr(np.mean(p)))
print('Median P: '+ repr(np.median(p)))
print('Min P: '+ repr(np.min(p)))
print('Max P : '+ repr(np.max(p)))
print('Std P: '+ repr(np.std(p)))
'n-pentane'
print('Mean np: '+ repr(np.mean(nP)))
print('Median np: '+ repr(np.median(nP)))
print('Min np: '+ repr(np.min(nP)))
print('Max np : '+ repr(np.max(nP)))
print('Std np: '+ repr(np.std(nP)))
'n-butane'
print('Mean nb: '+ repr(np.mean(nb)))
print('Median nb: '+ repr(np.median(nb)))
print('Min nb: '+ repr(np.min(nb)))
print('Max nb : '+ repr(np.max(nb)))
print('Std nb: '+ repr(np.std(nb)))
'methylpropane'
print('Mean mp: '+ repr(np.mean(mp)))
print('Median mp: '+ repr(np.median(mp)))
print('Min mp: '+ repr(np.min(mp)))
print('Max mp : '+ repr(np.max(mp)))
print('Std mp: '+ repr(np.std(mp)))
'methylbutane'
print('Mean mb: '+ repr(np.mean(mb)))
print('Median mb: '+ repr(np.median(mb)))
print('Min mb: '+ repr(np.min(mb)))
print('Max mb : '+ repr(np.max(mb)))
print('Std mb: '+ repr(np.std(mb)))
'Ozone'
print('Mean O3: '+ repr(np.mean(O3n)))
print('Median O3: '+ repr(np.median(O3n)))
print('Min O3: '+ repr(np.min(O3n)))
print('Max O3 : '+ repr(np.max(O3n)))
print('Std O3: '+ repr(np.std(O3n)))
#%% Typical values - cleansed data
'CO'
print('Mean CO: '+ repr(np.mean(CO)))
print('Median CO: '+ repr(np.median(CO)))
print('Min CO: '+ repr(np.min(CO)))
print('Max CO : '+ repr(np.max(CO)))
print('Std CO: '+ repr(np.std(CO)))
'CO2'
print('Mean CO2: '+ repr(np.mean(CO2)))
print('Median CO2: '+ repr(np.median(CO2)))
print('Min CO2: '+ repr(np.min(CO2)))
print('Max CO2 : '+ repr(np.max(CO2)))
print('Std CO2: '+ repr(np.std(CO2)))
'ETHANE'
print('Mean E: '+ repr(np.mean(E)))
print('Median E: '+ repr(np.median(E)))
print('Min E: '+ repr(np.min(E)))
print('Max E : '+ repr(np.max(E)))
print('Std E: '+ repr(np.std(E)))
'PROPANE'
print('Mean P: '+ repr(np.mean(P)))
print('Median P: '+ repr(np.median(P)))
print('Min P: '+ repr(np.min(P)))
print('Max P : '+ repr(np.max(P)))
print('Std P: '+ repr(np.std(P)))
'n-pentane'
print('Mean np: '+ repr(np.mean(NP)))
print('Median np: '+ repr(np.median(NP)))
print('Min np: '+ repr(np.min(NP)))
print('Max np : '+ repr(np.max(NP)))
print('Std np: '+ repr(np.std(NP)))
'n-butane'
print('Mean nb: '+ repr(np.mean(NB)))
print('Median nb: '+ repr(np.median(NB)))
print('Min nb: '+ repr(np.min(NB)))
print('Max nb : '+ repr(np.max(NB)))
print('Std nb: '+ repr(np.std(NB)))
'methylpropane'
print('Mean mp: '+ repr(np.mean(MP)))
print('Median mp: '+ repr(np.median(MP)))
print('Min mp: '+ repr(np.min(MP)))
print('Max mp : '+ repr(np.max(MP)))
print('Std mp: '+ repr(np.std(MP)))
'methylbutane'
print('Mean mb: '+ repr(np.mean(MB)))
print('Median mb: '+ repr(np.median(MB)))
print('Min mb: '+ repr(np.min(MB)))
print('Max mb : '+ repr(np.max(MB)))
print('Std mb: '+ repr(np.std(MB)))
#%% Scatter plots
O3=[]; FECHAS=[]
for value in O3n:
    O3.append(float(value))
for valor in FECHA:
    FECHAS.append(valor)

def fechas_int(d1, d2, x1, x2):
    """Returns the data where date from both samples intersect
    Inputs:
        d1= dates of the first data samples;
        d2= dates of the second data samples;
        x1= first data samples;
        x2= second data samples
    """
    n1 = np.in1d(d1, d2)
    n2 = np.in1d(d2, d1)
    x1 = np.asarray(x1); x2 = np.asarray(x2)
    X1 = x1[n1]
    X2 = x2[n2]
    return X1, X2
# Creating scattered data
co_int1, e_int = fechas_int(dCO, dE, CO, E)
co_int2, co2_int = fechas_int(dCO, dCO2, CO, CO2)
co_int3, p_int = fechas_int(dCO, dP, CO, P)
co_int4, np_int = fechas_int(dCO, dNP, CO, NP)
co_int5, nb_int = fechas_int(dCO, dNB, CO, NB)
co_int6, mp_int = fechas_int(dCO, dMP, CO, MP)
co_int7, mb_int = fechas_int(dCO, dMB, CO, MB)
co_int8, o3_int = fechas_int(dCO, FECHAS, CO, O3)
co_int8 = np.unique(co_int8)
plt.figure(num=3, figsize=(12,12))
plt.subplot(3,3,1)
plt.scatter(co_int2, co2_int)
plt.xlabel('CO [ppbv]')
plt.ylabel('CO2 [ppmv]')

plt.subplot(3,3,2)
plt.scatter(co_int1, e_int)
plt.xlabel('CO [ppbv]')
plt.ylabel('Ethane [pptv]')

plt.subplot(3,3,3)
plt.scatter(co_int3, p_int)
plt.xlabel('CO [ppbv]')
plt.ylabel('Propane [pptv]')

plt.subplot(3,3,4)
plt.scatter(co_int4, np_int)
plt.xlabel('CO [ppbv]')
plt.ylabel('n-pentane [pptv]')

plt.subplot(3,3,5)
plt.scatter(co_int5, nb_int)
plt.xlabel('CO [ppbv]')
plt.ylabel('n-butane [pptv]')

plt.subplot(3,3,6)
plt.scatter(co_int6, mp_int)
plt.ylabel('Methylpropane [ppbv]')
plt.xlabel('CO [ppbv]')

plt.subplot(3,3,7)
plt.scatter(co_int7, mb_int)
plt.ylabel('Methylbutane [ppbv]')
plt.xlabel('CO [ppbv]')

plt.subplot(3,3,8)
plt.scatter(co_int8, o3_int)
plt.xlabel('CO [ppbv]')
plt.ylabel('Ozone [ppbv]')
plt.tight_layout()
#%% Correlation coeficients
co_e = np.corrcoef(co_int1, e_int)
co_co2 = np.corrcoef(co_int2, co2_int)
co_p = np.corrcoef(co_int3, p_int)
co_np = np.corrcoef(co_int4, np_int)
co_nb = np.corrcoef(co_int5, nb_int)
co_mp = np.corrcoef(co_int6, mp_int)
co_mb = np.corrcoef(co_int7, mb_int)
co_oz = np.corrcoef(co_int8, o3_int)
print('COEF CO-E: ' + repr(co_e[1,0]))
print('COEF CO-CO2: ' + repr(co_co2[1,0]))
print('COEF CO-P: ' + repr(co_p[1,0]))
print('COEF CO-NP: ' + repr(co_np[1,0]))
print('COEF CO-NB: ' + repr(co_nb[1,0]))
print('COEF CO-MP: ' + repr(co_mp[1,0]))
print('COEF CO-MB: ' + repr(co_mb[1,0]))
print('COEF CO-OZ: ' + repr(co_oz[1,0]))
#%% Linear Trends
def pol(y):
    """
    Simple linear regression with polinomios
    
    Input: data
    
    Outputs: x-dates, predictions
    """
    n = len(y)
    x = np.linspace(1, 528, n)
    p = np.polyfit(x, y, 1)
    f = np.poly1d(p)
    return x, f(x)
pco = pol(CO)
pco2 = pol(CO2)
pe = pol(E)
pp = pol(P)
pnp = pol(NP)
pnb = pol(NB)
pmp = pol(MP)
pmb = pol(MB)
po3 = pol(O3)
plt.figure(num=4, figsize=(12,12))
plt.subplot(3,3,1)
plt.plot(pco[0], pco[1], 'b', label='CO trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('ppbv')
plt.xlabel('years')
plt.subplot(3,3,2)
plt.plot(pco2[0], pco2[1], 'r', label='CO2 trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('ppmv')
plt.xlabel('years')
plt.subplot(3,3,3)
plt.plot(pe[0], pe[1],'g', label='Ethane trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('pptv')
plt.xlabel('years')
plt.subplot(3,3,4)
plt.plot(pp[0], pp[1],'k', label='Propane trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('pptv')
plt.xlabel('years')
plt.subplot(3,3,5)
plt.plot(pnp[0], pnp[1],'m', label='n-pentane trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('pptv')
plt.xlabel('years')
plt.subplot(3,3,6)
plt.plot(pnb[0], pnb[1],'--b', label='n-butane trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('pptv')
plt.xlabel('years')
plt.subplot(3,3,7)
plt.plot(pmp[0], pmp[1],'--r', label='Methylpropane trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('pptv')
plt.xlabel('years')
plt.subplot(3,3,8)
plt.plot(pmb[0], pmb[1],'--k', label='Methylbutane trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('pptv')
plt.xlabel('years')
plt.subplot(3,3,9)
plt.plot(po3[0], po3[1],'--k', label='Ozone trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('ppbv')
plt.xlabel('years')
plt.tight_layout()
plt.show()
#%% Seasonal behaviors
"Monthly Concentrations"
t = np.linspace(1, 12, 12)
Eco, Fco, Mrco, Aco, Myco, Jco, Jlco, Agco, Sco, Oco, Nco, Dco = meses(dCO, CO)
yearCO = [Eco, Fco, Mrco, Aco, Myco, Jco, Jlco, Agco, Sco, Oco, Nco, Dco]
Eco2, Fco2, Mrco2, Aco2, Myco2, Jco2,\
 Jlco2, Agco2, Sco2, Oco2, Nco2, Dco2 = meses(dCO2, CO2)
yearCO2 = [Eco2, Fco2, Mrco2, Aco2, Myco2, Jco2, Jlco2, Agco2, Sco2, Oco2, 
           Nco2, Dco2]
Ee, Fe, Mre, Ae, Mye, Je, Jle, Age, Se, Oe, Ne, De = meses(dE, E)
yearE = [Ee, Fe, Mre, Ae, Mye, Je, Jle, Age, Se, Oe, Ne, De]
Ep, Fp, Mrp, Ap, Myp, Jp, Jlp, Agp, Sp, Op, Np, Dp = meses(dP, P)
yearP = [Ep, Fp, Mrp, Ap, Myp, Jp, Jlp, Agp, Sp, Op, Np, Dp]
EnP, FnP, MrnP, AnP, MynP, JnP, JlnP, AgnP, SnP, OnP, NnP, DnP = meses(dNP, NP)
yearNP = [EnP, FnP, MrnP, AnP, MynP, JnP, JlnP, AgnP, SnP, OnP, NnP, DnP]
Enb, Fnb, Mrnb, Anb, Mynb, Jnb, Jlnb, Agnb, Snb, Onb, Nnb, Dnb = meses(dNB, NB)
yearNB = [Enb, Fnb, Mrnb, Anb, Mynb, Jnb, Jlnb, Agnb, Snb, Onb, Nnb, Dnb]
Emp, Fmp, Mrmp, Amp, Mymp, Jmp, Jlmp, Agmp, Smp, Omp, Nmp, Dmp = meses(dMP, MP)
yearMP = [Emp, Fmp, Mrmp, Amp, Mymp, Jmp, Jlmp, Agmp, Smp, Omp, Nmp, Dmp]
Emb, Fmb, Mrmb, Amb, Mymb, Jmb, Jlmb, Agmb, Smb, Omb, Nmb, Dmb = meses(dMB, MB)
yearMB = [Emb, Fmb, Mrmb, Amb, Mymb, Jmb, Jlmb, Agmb, Smb, Omb, Nmb, Dmb]
"Plots"
plt.figure(num=5, figsize=(12,12))
plt.subplot(3,3,1)
plt.boxplot(yearCO)
plt.xlabel('Months')
plt.ylabel('ppbv')
plt.title('CO')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.subplot(3,3,2)
plt.boxplot(yearCO2)
plt.xlabel('Months')
plt.ylabel('ppmv')
plt.title('CO2')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.subplot(3,3,3)
plt.boxplot(yearE)
plt.xlabel('Months')
plt.ylabel('pptv')
plt.title('Ethane')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.subplot(3,3,4)
plt.boxplot(yearP)
plt.xlabel('Months')
plt.ylabel('pptv')
plt.title('Propane')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.subplot(3,3,5)
plt.boxplot(yearNP)
plt.xlabel('Months')
plt.ylabel('pptv')
plt.title('n-pentane')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.subplot(3,3,6)
plt.boxplot(yearNB)
plt.xlabel('Months')
plt.ylabel('pptv')
plt.title('n-butane')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.subplot(3,3,7)
plt.boxplot(yearMP)
plt.xlabel('Months')
plt.ylabel('pptv')
plt.title('Methylpropane')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.subplot(3,3,8)
plt.boxplot(yearP)
plt.xlabel('Months')
plt.ylabel('pptv')
plt.title('Methylbutane')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.subplot(3,3,9)
plt.boxplot(yearOZ)
plt.xlabel('Months')
plt.ylabel('ppbv')
plt.title('Ozone')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.tight_layout()
#%% Monthly correlation
def proms_mes(y):
    p=[]
    for i in range(len(y)):
        n = np.mean(y[i])
        p.append(n)
    return p
coy = proms_mes(yearCO)
co2y = proms_mes(yearCO2)
ey = proms_mes(yearE)
py = proms_mes(yearP)
npy = proms_mes(yearNP)
nby = proms_mes(yearNB)
mpy = proms_mes(yearMP)
mby = proms_mes(yearMB)
ozy = proms_mes(yearOZ)
plt.figure(num=5, figsize=(12,12))
plt.subplot(3,3,1)
plt.scatter(coy, co2y)
plt.xlabel('CO [ppbv]')
plt.ylabel('CO2 [ppmv]')

plt.subplot(3,3,2)
plt.scatter(coy, ey)
plt.xlabel('CO [ppbv]')
plt.ylabel('Ethane [pptv]')

plt.subplot(3,3,3)
plt.scatter(coy, py)
plt.xlabel('CO [ppbv]')
plt.ylabel('Propane [pptv]')

plt.subplot(3,3,4)
plt.scatter(coy, npy)
plt.xlabel('CO [ppbv]')
plt.ylabel('n-pentane [pptv]')

plt.subplot(3,3,5)
plt.scatter(coy, nby)
plt.xlabel('CO [ppbv]')
plt.ylabel('n-butane [pptv]')

plt.subplot(3,3,6)
plt.scatter(coy, mpy)
plt.xlabel('CO [ppbv]')
plt.ylabel('Methylpropane [pptv]')

plt.subplot(3,3,7)
plt.scatter(coy, mby)
plt.xlabel('CO [ppbv]')
plt.ylabel('Methylbutane [pptv]')

plt.subplot(3,3,8)
plt.scatter(coy, ozy)
plt.xlabel('CO [ppbv]')
plt.ylabel('Ozone [ppbv]')
plt.tight_layout()

co_e = np.corrcoef(coy, ey)
co_co2 = np.corrcoef(coy, co2y)
co_p = np.corrcoef(coy, py)
co_np = np.corrcoef(coy, npy)
co_nb = np.corrcoef(coy, nby)
co_mp = np.corrcoef(coy, mpy)
co_mb = np.corrcoef(coy, mby)
co_oz = np.corrcoef(coy, ozy)
print('COEF CO-E: ' + repr(co_e[1,0]))
print('COEF CO-CO2: ' + repr(co_co2[1,0]))
print('COEF CO-P: ' + repr(co_p[1,0]))
print('COEF CO-NP: ' + repr(co_np[1,0]))
print('COEF CO-NB: ' + repr(co_nb[1,0]))
print('COEF CO-MP: ' + repr(co_mp[1,0]))
print('COEF CO-MB: ' + repr(co_mb[1,0]))
print('COEF CO-OZ: ' + repr(co_oz[1,0]))
#%% Mixing ratios
coy = np.asarray(coy)*10**(3)  # ppbv to pptv
co2y = np.asarray(co2y)*10**(6) # ppmv to pptv
ey = np.asarray(ey)
py = np.asarray(py)
npy = np.asarray(npy)
nby = np.asarray(nby)
mpy = np.asarray(mpy)
mby = np.asarray(mby)
ozy = np.asarray(ozy)*10**(3)  # ppbv to pptv
plt.figure(num=5, figsize=(12,12))
plt.subplot(3,3,1)
plt.plot(coy/co2y, '-o')
plt.xlabel('Months')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.ylabel('Mixing ratio value')
plt.title('CO vs CO2')
plt.subplot(3,3,2)
plt.plot(coy/ey, '-o')
plt.xlabel('Months')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.ylabel('Mixing ratio value')
plt.title('CO vs Ethane')
plt.subplot(3,3,3)
plt.plot(coy/py, '-o')
plt.xlabel('Months')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.ylabel('Mixing ratio value')
plt.title('CO vs Propane')
plt.subplot(3,3,4)
plt.plot(coy/npy, '-o')
plt.xlabel('Months')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.ylabel('Mixing ratio value')
plt.title('CO vs n-pentane')
plt.subplot(3,3,5)
plt.plot(coy/nby, '-o')
plt.xlabel('Months')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.ylabel('Mixing ratio value')
plt.title('CO vs n-butane')
plt.subplot(3,3,6)
plt.plot(coy/mpy, '-o')
plt.xlabel('Months')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.ylabel('Mixing ratio value')
plt.title('CO vs Methylpropane')
plt.subplot(3,3,7)
plt.plot(coy/mby, '-o')
plt.xlabel('Months')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.ylabel('Mixing ratio value')
plt.title('CO vs Methylbutane')
plt.subplot(3,3,8)
plt.plot(coy/ozy, '-o')
plt.xlabel('Months')
plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
plt.ylabel('Mixing ratio value')
plt.title('CO vs Ozone')
plt.tight_layout()
#%% Examples
plt.figure(num=6, figsize=(8,6))
plt.subplot(2,1,1)
plt.plot(dco2,co2)
plt.ylabel('ppmv')
plt.title('CO2, raw data time series')
plt.subplot(2,1,2)
plt.plot(dCO2, CO2)
plt.title('CO2, cleansed data time series')
plt.ylabel('ppmv')
plt.tight_layout()

plt.figure(num=7, figsize=(15,15))
plt.subplot(3,3,1)
plt.plot(dco, co)
plt.title('Carbon monoxide')
plt.xlabel('years')
plt.ylabel('ppbv')

plt.subplot(3,3,2)
plt.plot(dco2, co2)
plt.title('Carbon dioxide')
plt.xlabel('years')
plt.ylabel('ppmv')

plt.subplot(3,3,3)
plt.plot(de, e)
plt.title('Ethane')

plt.subplot(3,3,4)
plt.plot(dp, p)
plt.title('Propane')
plt.xlabel('years')
plt.ylabel('pptv')

plt.subplot(3,3,5)
plt.plot(dnP, nP)
plt.title('n-pentane')
plt.xlabel('years')
plt.ylabel('pptv')

plt.subplot(3,3,6)
plt.plot(dnb, nb)
plt.title('n-butane')
plt.xlabel('years')
plt.ylabel('pptv')

plt.subplot(3,3,7)
plt.plot(dmp, mp)
plt.title('Methylpropane')
plt.xlabel('years')
plt.ylabel('pptv')

plt.subplot(3,3,8)
plt.plot(dmb, mb)
plt.title('Methylbutane')
plt.ylabel('pptv')
plt.xlabel('years')


plt.subplot(3,3,9)
plt.plot(FECHA, O3n, '-o')
plt.title('Tropospheric ozone')
plt.ylabel('pptv')
plt.xlabel('years')
plt.tight_layout()

#%% Periodograms

##Analisis con armonico
#n=length(CO);
#n2=n/2;
#for k in range(1, n2):
#    A1 = 0; B1 = 0;
#    for t in range(1, n):
#        A1 = A1+T(t)*cos(2*pi*k*t/n)
#        B1 = B1+T(t)*sin(2*pi*k*t/n)
#    A1 = 2*A1/n; B1=2*B1/n; C(k)=np.sqrt(A1**2 + B1**2)
#    if A1>0:
#        fi(k)=atan(B1/A1)
#    if A1<0:
#        i(k)=atan(B1/A1)+pi
#    if A1==0:
#        fi(k)=pi/2
#
#plt.figure(num=7, figsize=(8,6))
#f, s = ss.periodogram(CO)
#plt.semilogy(f, s)
#plt.xlabel('frecuency')