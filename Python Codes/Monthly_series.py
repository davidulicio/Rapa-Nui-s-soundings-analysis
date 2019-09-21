# -*- coding: utf-8 -*-
"""
Monthly time series
Rapa Nui
@author: DavidTrejo
"""
import pandas as pd
import numpy as np
import numpy.matlib as nmat
import matplotlib.pyplot as plt
from data_uso import data_transfer_E, prom
from cleansing_eic import data_cleansing, hist_clean
from ozone import yearOZ, O3n, FECHA1
#%% Functions


def meses(date, value):
    "Splits the concentration values in each month"
    EN = []; FEB = []; MAR = []; ABR = []; MAY = []; JUN = []; JUL = []
    AG = []; SEP = []; OCTU = []; NOV = []; DIC = []
    for i in range(len(date)):
        fecha = date[i]
        valor = np.float(value[i])
        m = fecha.month
        y = fecha.year
        #d = fecha.day  para obtener el dia en caso de necesitarlo
        if m == 1:
            EN.append([valor, y])
        if m == 2:
            FEB.append([valor, y])
        if m == 3:
            MAR.append([valor, y])
        if m == 4:
            ABR.append([valor, y])
        if m == 5:
            MAY.append([valor, y])
        if m == 6:
            JUN.append([valor, y])
        if m == 7:
            JUL.append([valor, y])
        if m == 8:
            AG.append([valor, y])
        if m == 9:
            SEP.append([valor, y])
        if m == 10:
            OCTU.append([valor, y])
        if m == 11:
            NOV.append([valor, y])
        if m == 12:
            DIC.append([valor, y])
    EN = np.asarray(EN); FEB = np.asarray(FEB); MAR = np.asarray(MAR)
    ABR = np.asarray(ABR); MAY = np.asarray(MAY); JUN = np.asarray(JUN)
    JUL = np.asarray(JUL); AG = np.asarray(AG); SEP = np.asarray(SEP)
    OCTU = np.asarray(OCTU); NOV = np.asarray(NOV); DIC = np.asarray(DIC)
    YM = np.asarray([EN, FEB, MAR, ABR, MAY, JUN, JUL, AG, SEP, OCTU, NOV,
                     DIC])
    return YM


def new_serie(data):
    """ 
    Creates a monthly series of the data. Through a boolean mask verifies that 
    each month of the resulting monthly series is well represented, otherwise 
    it is not considered and that month is put as a nan value
    """
    mes_s = []
    fecha = []
    t = np.linspace(2006, 2016, 11)
    i = 0
    for nmes in range(len(data)):
        value = data[nmes]
        for yr in t:
            i = i + 1
            mask = yr==value[:, 1]
            val = value[mask, 0]
            if len(val)>=3:
                val = np.nanmean(val)
                mes_s.append(val)
                fecha.append(i)
            else:
                mes_s.append(np.nan)
                fecha.append(i)
    mes_s = np.asarray(mes_s)
    fecha = np.asarray(fecha)
    return mes_s, fecha


def new_serieOZ(data):
    "Creates the ozone monthly series"
    mes_s = []
    fecha = []
    t = np.linspace(2006, 2016, 11)
    i = 0
    for nmes in range(len(data)):
        value = data[nmes]
        for yr in t:
            i = i + 1
            mask = yr==value[:, 1]
            val = value[mask, 0]
            val = np.nanmean(val)
            mes_s.append(val)
            fecha.append(i)
    mes_s = np.asarray(mes_s)
    fecha = np.asarray(fecha)
    return mes_s, fecha


def armonicos(T):
    "Produces the harmonic series of the given data"
    T = np.asarray(T)
    n = len(T)
    n2 = int(n/2)
    A = np.zeros([n2, n]); fi = np.zeros(n2)
    C = np.zeros(n2)
    for k in range(1, n2):
        A1 = 0; B1 = 0
        for t in range(1, n):
            A1 = A1 + T[t] * np.cos(2*np.pi*k*t/n)
            B1 = B1 + T[t] * np.sin(2*np.pi*k*t/n)
            A1 = 2*A1/n; B1=2*B1/n; C[k]=np.sqrt(A1**2 + B1**2)
            if A1>0:
                fi[k] = np.arctan(B1/A1)
            if A1<0:
                fi[k] = np.arctan(B1/A1) + np.pi
            if A1==0:
                fi[k] = np.pi/2
    for k in range(1, n2):
        for t in range(1, n):
            A[k,t] = C[k] * np.cos(2*np.pi*k*t/n - fi[k]);
    A = A[1: len(A), 1:len(A[1,:])]
    return A
#%% Data reading and simple statistics
directoriow = pd.read_excel(r'RapaNui.xlsx', header=0)
"Use of the imported functions"
# The next line transfers the data to the variables
dCO, CO, dCO2, CO2, dP, P, dNP, NP, dNB, NB, dE, E, dMP, MP, dMB,\
 MB = data_transfer_E(directoriow); del directoriow
# The following ones calculates the mean average for every vocs
co, dco = prom(dCO, CO)
co2, dco2 = prom(dCO2, CO2)
p, dp = prom(dP, P)
nP, dnP = prom(dNP, NP)
nb, dnb = prom(dNB, NB)
e, de = prom(dE, E)
mp, dmp = prom(dMP, MP)
mb, dmb = prom(dMB, MB)
dCO, CO, dCO2, CO2, dP, P, dNP, NP, dNB, NB, dE, E, dMP, MP, \
dMB, MB = data_cleansing(dco, co, dco2, co2, dp, p, dnP, nP, dnb,\
                         nb, de, e, dmp, mp, dmb, mb)
dco, co = hist_clean(dCO,CO)
dCO2, co2 = hist_clean(dCO2,CO2)
dp, p = hist_clean(dP,P)
dnP, nP = hist_clean(dNP,NP)
dnb, nb = hist_clean(dNB,NB)
de, e = hist_clean(dE,E)
dmp, mp = hist_clean(dMP,MP)
dmb, mb = hist_clean(dMB,MB)
#%% Calculation of monthly series with raw-data
yco = meses(dco, co)
yc2 = meses(dco2, co2)
yp = meses(dp, p)
ynp = meses(dnP, nP)
ynb = meses(dnb, nb)
ye = meses(de, e)
ymp = meses(dmp, mp)
ymb = meses(dmb, mb)
O3n = O3n.values
yoz = meses(FECHA1, O3n)
#%% Months
mco, fco = new_serie(yco); dfco = pd.DataFrame(mco)
mc2, fc2 = new_serie(yc2); dfc2 = pd.DataFrame(mc2)
myp, fyp = new_serie(yp); dfyp = pd.DataFrame(myp)
mnp, fnp = new_serie(ynp); dfnp = pd.DataFrame(mnp)
mnb, fnb = new_serie(ynb); dfnb = pd.DataFrame(mnb)
mye, fye = new_serie(ye); dfye = pd.DataFrame(mye)
mmp, fmp = new_serie(ymp); dfmp = pd.DataFrame(mmp)
mmb, fmb = new_serie(ymb); dfmb = pd.DataFrame(mmb)
moz, f = new_serieOZ(yoz); dfoz = pd.DataFrame(moz)
X = np.zeros([9,132])
X[0] = mco; X[1] = mc2; X[2] = mye; X[3] = myp; X[4] = mnp; X[5] = mnb;
X[6] = mmp; X[7] = mmb; X[8] = moz;
np.savetxt('seriesmensuales.txt', X)
#%% MLR
dfco = dfco.fillna(method='ffill')
dfc2 = dfc2.fillna(method='ffill')
dfyp = dfyp.fillna(method='ffill')
dfnp = dfnp.fillna(method='ffill')
dfnb = dfnb.fillna(method='ffill')
dfye = dfye.fillna(method='ffill')
dfmp = dfmp.fillna(method='ffill')
dfmb = dfmb.fillna(method='ffill')
dfoz = dfoz.fillna(method='ffill')
Y = pd.concat([dfco, dfc2, dfye, dfyp, dfnp, dfnb, dfmp, dfmb, dfoz], axis=1) #np.zeros([8,132])
#Y[0] = np.asarray(dfco)
#Y[1] = dfc2; Y[2] = dfye; Y[3] = dfyp; Y[4] = dfnp; Y[5] = dfnb;
#Y[6] = dfmp; Y[7] = dfmb;
np.savetxt('seriesmensualesrellenadas.txt', Y)
#%% Plots
plt.figure(num=1, figsize=(10,10))
plt.subplot(3,3,1)
plt.plot(mco, '*', label='observed values')
plt.plot(dfco, '-', label='interpolation')
plt.ylabel('ppbv')
plt.xlabel('Months')
plt.title('CO')
plt.subplot(3,3,2)
plt.plot(mc2, '*', label='observed values')
plt.plot(dfc2, '-', label='interpolation')
plt.ylabel('ppmv')
plt.xlabel('Months')
plt.title(r'$CO_{2}$')
plt.subplot(3,3,3)
plt.plot(myp, '*', label='observed values')
plt.plot(dfyp, '-', label='interpolation')
plt.ylabel('pptv')
plt.xlabel('Months')
plt.title('Propane')
plt.subplot(3,3,4)
plt.plot(mye, '*', label='observed values')
plt.plot(dfye, '-', label='interpolation')
plt.ylabel('pptv')
plt.xlabel('Months')
plt.title('Ethane')
plt.subplot(3,3,5)
plt.plot(mnb, '*', label='observed values')
plt.plot(dfnb, '-', label='interpolation')
plt.ylabel('pptv')
plt.xlabel('Months')
plt.title('n-butane')
plt.subplot(3,3,6)
plt.plot(mnp, '*', label='observed values')
plt.plot(dfnp, '-', label='interpolation')
plt.ylabel('pptv')
plt.xlabel('Months')
plt.title('n-pentane')
plt.subplot(3,3,7)
plt.plot(mmp, '*', label='observed values')
plt.plot(dfmp, '-', label='interpolation')
plt.ylabel('pptv')
plt.xlabel('Months')
plt.title('Methylpropane')
plt.subplot(3,3,8)
plt.plot(mmb, '*', label='observed values')
plt.plot(dfmb, '-', label='interpolation')
plt.ylabel('pptv')
plt.xlabel('Months')
plt.title('Methylbutane')
plt.subplot(3,3,9)
plt.plot(moz, '*', label='observed values')
plt.plot(dfoz, '-', label='interpolation')
plt.ylabel('pptv')
plt.xlabel('Months')
plt.title('Ozone')
plt.legend()
plt.tight_layout()
#%% Harmonic analysis
aco = armonicos(dfco)
ac2 = armonicos(dfc2)
aye = armonicos(dfye)
dfyp = dfyp.drop(index=0); dfyp = dfyp.drop(index=1)
ayp = armonicos(dfyp)
amp = armonicos(dfmp)
amb = armonicos(dfmb)
anb = armonicos(dfnb)
anp = armonicos(dfnp)
aoz = armonicos(dfoz)
dfco = dfco.drop(index=0)
dfc2 = dfc2.drop(index=0)
dfnp = dfnp.drop(index=0)
dfnb = dfnb.drop(index=0)
dfye = dfye.drop(index=0)
dfmp = dfmp.drop(index=0)
dfmb = dfmb.drop(index=0)
dfoz = dfoz.drop(index=0)
#%% Removing seasonal cycle
rco = np.fft.fft(np.asarray(dfco)[:,0])
rco = np.fft.ifft(rco) - np.nanmean(dfco) - (aco[0] + aco[1] + aco[2])
rc2 = np.fft.fft(np.asarray(dfc2)[:,0])
rc2 = np.fft.ifft(rc2) - np.nanmean(dfc2) - (ac2[0] + ac2[1] + ac2[2])
ryp = np.fft.fft(np.asarray(dfyp)[:,0])
ryp = np.fft.ifft(ryp[1:131]) - np.nanmean(dfyp) - (ayp[0] + ayp[1] + ayp[2])
rye = np.fft.fft(np.asarray(dfye)[:,0])
rye = np.fft.ifft(rye) - np.nanmean(dfye) - (aye[0] + aye[1] + aye[2])
rnp = np.fft.fft(np.asarray(dfnp)[:,0])
rnp = np.fft.ifft(rnp) - np.nanmean(dfnp) - (anp[0] + anp[1] + anp[2])
rnb = np.fft.fft(np.asarray(dfnb)[:,0])
rnb = np.fft.ifft(rnb) - np.nanmean(dfnb) - (anb[0] + anb[1] + anb[2])
rmb = np.fft.fft(np.asarray(dfmb)[:,0])
rmb = np.fft.ifft(rmb) - np.nanmean(dfmb) - (amb[0] + amb[1] + amb[2])
rmp = np.fft.fft(np.asarray(dfmp)[:,0])
rmp = np.fft.ifft(rmp) - np.nanmean(dfmp) - (amp[0] + amp[1] + amp[2])
roz = np.fft.fft(np.asarray(dfoz)[:,0])
roz = np.fft.ifft(roz) - np.nanmean(dfoz) - (aoz[0] + aoz[1] + aoz[2])
#%% Correlation coeficients
oz_e = np.corrcoef(roz, rye)
oz_co2 = np.corrcoef(roz, rc2)
oz_p = np.corrcoef(roz[2:131], ryp)
oz_np = np.corrcoef(roz, rnp)
oz_nb = np.corrcoef(roz, rnb)
oz_mp = np.corrcoef(roz, rmp)
oz_mb = np.corrcoef(roz, rmb)
oz_co = np.corrcoef(roz, rco)
#co_oz = np.corrcoef(rco, oint)
print('COEF OZ-E: ' + repr(oz_e[1,0]))
print('COEF OZ-CO2: ' + repr(oz_co2[1,0]))
print('COEF OZ-P: ' + repr(oz_p[1,0]))
print('COEF OZ-NP: ' + repr(oz_np[1,0]))
print('COEF OZ-NB: ' + repr(oz_nb[1,0]))
print('COEF OZ-MP: ' + repr(oz_mp[1,0]))
print('COEF OZ-MB: ' + repr(oz_mb[1,0]))
print('COEF OZ-CO: ' + repr(oz_co[1,0]))

#%% Correlation coeficients with CO
co_e = np.corrcoef(rco, rye)
co_co2 = np.corrcoef(rco, rc2)
co_p = np.corrcoef(rco[2:131], ryp)
co_np = np.corrcoef(rco, rnp)
co_nb = np.corrcoef(rco, rnb)
co_mp = np.corrcoef(rco, rmp)
co_mb = np.corrcoef(rco, rmb)
co_oz = np.corrcoef(rco, roz)
#co_oz = np.corrcoef(rco, oint)
print('COEF CO-E: ' + repr(co_e[1,0]))
print('COEF CO-CO2: ' + repr(co_co2[1,0]))
print('COEF CO-P: ' + repr(co_p[1,0]))
print('COEF CO-NP: ' + repr(co_np[1,0]))
print('COEF CO-NB: ' + repr(co_nb[1,0]))
print('COEF CO-MP: ' + repr(co_mp[1,0]))
print('COEF CO-MB: ' + repr(co_mb[1,0]))
print('COEF CO-OZ: ' + repr(co_oz[1,0]))
#print('COEF CO-OZ: ' + repr(co_oz[1,0]))
#%% Trends of the unseasonalized data and statistics
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
pco = pol(rco)
pco2 = pol(rc2)
pe = pol(rye)
pp = pol(ryp)
pnp = pol(rnp)
pnb = pol(rnb)
pmp = pol(rmp)
pmb = pol(rmb)
#po3 = pol(O3)
'varianza de residuales'
co_re = np.asarray(dfco) - pco[0] #residuales
c2_re = np.asarray(dfc2) - pco2[0] #residuales
yp_re = np.asarray(dfyp) - pp[0] #residuales
ye_re = np.asarray(dfye) - pe[0] #residuales
np_re = np.asarray(dfnp) - pnp[0] #residuales
nb_re = np.asarray(dfnb) - pnb[0] #residuales
mp_re = np.asarray(dfmp) - pmp[0] #residuales
mb_re = np.asarray(dfmb) - pmb[0] #residuales
#oz_re=dfco - pco #residuales
'''SSE suma del cuadrado de los errores, es el cuadrado de los residuales. sum
squared error'''
co_SSE = sum(co_re**2)
c2_SSE = sum(c2_re**2)
yp_SSE = sum(yp_re**2)
ye_SSE = sum(ye_re**2)
np_SSE = sum(np_re**2)
nb_SSE = sum(nb_re**2)
mp_SSE = sum(mp_re**2)
mb_SSE = sum(mb_re**2)
'''SSR suma de la diferencia al cuadrado de los valores estimados menos la 
media de los valores de y. sum squared regression'''
co_SSR=sum((pco-np.nanmean(dfco))**2)
c2_SSR=sum((pco2-np.nanmean(dfco))**2)
yp_SSR=sum((pp-np.nanmean(dfco))**2)
ye_SSR=sum((pe-np.nanmean(dfco))**2)
np_SSR=sum((pnp-np.nanmean(dfco))**2)
nb_SSR=sum((pnb-np.nanmean(dfco))**2)
mp_SSR=sum((pmp-np.nanmean(dfco))**2)
mb_SSR=sum((pmb-np.nanmean(dfco))**2)
"""SST suma total de los cuadrados. sum squared total"""
co_SST=sum((dfco-np.nanmean(dfco))**2)
c2_SST=sum((dfc2-np.nanmean(dfc2))**2)
yp_SST=sum((dfyp-np.nanmean(dfyp))**2)
ye_SST=sum((dfye-np.nanmean(dfye))**2)
np_SST=sum((dfnp-np.nanmean(dfnp))**2)
nb_SST=sum((dfnb-np.nanmean(dfnb))**2)
mp_SST=sum((dfmp-np.nanmean(dfmp))**2)
mb_SST=sum((dfmb-np.nanmean(dfmb))**2)
"""MSE=SSE/DFE stats(1,4) en regress (error variance o error de la varianza).
mean squared error"""
co_MSE=co_SSE/(len(dfco)-2) #Se^2
c2_MSE=c2_SSE/(len(dfc2)-2)
yp_MSE=yp_SSE/(len(dfyp)-2)
ye_MSE=ye_SSE/(len(dfye)-2)
np_MSE=np_SSE/(len(dfnp)-2)
nb_MSE=nb_SSE/(len(dfnb)-2)
mp_MSE=mp_SSE/(len(dfmp)-2)
mb_MSE=mb_SSE/(len(dfmb)-2)
#SST
co_SST_SUM=co_SSR+co_SSE;
#MSR
co_MSR=co_SSR/1;
"""Rectas de error"""
l1_co = 1.96 * np.sqrt(co_MSE)
l1_c2 = 1.96 * np.sqrt(c2_MSE)
l1_yp = 1.96 * np.sqrt(yp_MSE)
l1_ye = 1.96 * np.sqrt(ye_MSE)
l1_np = 1.96 * np.sqrt(np_MSE)
l1_nb = 1.96 * np.sqrt(nb_MSE)
l1_mp = 1.96 * np.sqrt(mp_MSE)
l1_mb = 1.96 * np.sqrt(mb_MSE)
PR = np.linspace(1, 131, 131)
dfx = (PR-nmat.repmat(np.mean(pco[0]),len(PR),1))**2
sdfx = sum((pco[0] - nmat.repmat(np.mean(pco[0]),len(pco[0]),1))**2)
syco = co_MSE * ((1/len(pco[0])) + dfx/sdfx)
#a7=plot(years,mdl1.Fitted+1.96*sqrt(sy),'-g'); IC de regresion

#%% Plots of the unseasonalized data
plt.figure(num=4, figsize=(12,12))
plt.subplot(3,3,1)
plt.plot(pco[0], rco, 'o-')
plt.plot(pco[0], pco[1], 'k', label='CO trend')
#plt.plot(pco[0], pco[1]+l1_co,'r--','Residuals variance')
#plt.plot(pco[0], pco[1]-l1_co,'r--')
plt.plot(pco[0], pco[1]+1.96*np.sqrt(syco[1,:]),'-g')  # IC de regresion
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('ppbv')
plt.xlabel('years')
plt.subplot(3,3,2)
plt.plot(pco2[0], rc2, 'o-')
plt.plot(pco2[0], pco2[1], 'k', label='CO2 trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('ppmv')
plt.xlabel('years')
plt.subplot(3,3,3)
plt.plot(pe[0], rye, 'o-')
plt.plot(pe[0], pe[1],'k', label='Ethane trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('pptv')
plt.xlabel('years')
plt.subplot(3,3,4)
plt.plot(pp[0], ryp, 'o-')
plt.plot(pp[0], pp[1],'k', label='Propane trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('pptv')
plt.xlabel('years')
plt.subplot(3,3,5)
plt.plot(pnp[0], rnp, 'o-')
plt.plot(pnp[0], pnp[1],'k', label='n-pentane trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('pptv')
plt.xlabel('years')
plt.subplot(3,3,6)
plt.plot(pnb[0], rnb, 'o-')
plt.plot(pnb[0], pnb[1],'k', label='n-butane trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('pptv')
plt.xlabel('years')
plt.subplot(3,3,7)
plt.plot(pmp[0], rmp, 'o-')
plt.plot(pmp[0], pmp[1],'k', label='Methylpropane trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('pptv')
plt.xlabel('years')
plt.subplot(3,3,8)
plt.plot(pmb[0], rmb, 'o-')
plt.plot(pmb[0], pmb[1],'k', label='Methylbutane trend')
plt.legend()
plt.xticks([0, 480], ('2006', '2016'))
plt.ylabel('pptv')
plt.xlabel('years')
#plt.subplot(3,3,9)
#plt.plot(po3[0], po3[1],'--k', label='Ozone trend')
#plt.xticks([0, 480], ('2006', '2016'))
#plt.ylabel('ppbv')
#plt.xlabel('years')
plt.tight_layout()
plt.show()