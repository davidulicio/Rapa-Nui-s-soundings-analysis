# -*- coding: utf-8 -*-
"""
Data cleansing for Rapa Nui
@author: David
"""
import numpy as np
import pandas as pd


def sortSecond(val): 
    return val[1] 


def hist_clean(val_fecha, val_val):
    "Removes 10% of the higher and lowest values of each bin in the histogram"
    histval_val, binsval_val = np.histogram(val_val, bins=20)
    q=w=e=r=t=y=u=i=o=p=a=s=d=f=g=h=j=k=l=ñ=[]
    dq=dw=de=dr=dt=dy=du=di=do=dp=da=ds=dd=df=dg=dh=dj=dk=dl=dñ=[]
    listasd=[dq,dw,de,dr,dt,dy,du,di,do,dp,da,ds,dd,df,dg,dh,dj,dk,dl,dñ]
    listas=[q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,ñ]
    valores = []
    fechas = []
    tupla = []
    i = 0
    for value in listas:
        for j in range(len(val_val)):
            if binsval_val[i] <= val_val[j] < binsval_val[i+1]:
                value.append(val_val[j])
                listasd[i].append(val_fecha[j])
        i = i+1
    i = 0
    for valor in listas:
        n = int(len(listas) * 0.1)
        while n>0:
            ind = int(valor.index(max(valor)))
            valor.remove(max(valor))
            listasd[i].pop(ind)
            indmin = int(valor.index(min(valor)))
            valor.remove(min(valor))
            listasd[i].pop(indmin)
            n = n - 1
        i = i+1
    for k in range(len(listas)):
        v = listas[k]
        d = listasd[k]
        for h in range(len(v)):
            tupla.append([v[h],d[h]])
    tupla.sort(key = sortSecond)
    for vl in tupla:
        valores.append(vl[0])
        fechas.append(vl[1])
    return fechas, valores
    
    
def data_cleansing(dco, co, dco2, co2, dp, p, dnP, nP, dnb, nb, de, 
                    e, dmp, mp, dmb, mb):
    """
    Applies a value filter for each vocs in Rapa Nui's data
    """
    # co filter
    DCO = []
    CO = []
    MIN = np.nanmean(co)-3*np.nanstd(co)
    MAX = np.nanmean(co)+3*np.nanstd(co)
    for i in range(len(co)):
        value = co[i]
        date = dco[i]
        if MIN <= value <= MAX:
            CO.append(value)
            DCO.append(date)
    # co2 filter
    DCO2 = []
    CO2 = []
    MIN = np.nanmean(co2)-3*np.nanstd(co2)
    MAX = np.nanmean(co2)+3*np.nanstd(co2)
    for i in range(len(co2)):
        value = co2[i]
        date = dco2[i]
        if MIN <= value <= MAX:
            CO2.append(value)
            DCO2.append(date)
    # ethane filter
    DE = []
    E = []
    MIN = np.nanmean(e)-3*np.nanstd(e)
    MAX = np.nanmean(e)+3*np.nanstd(e)
    for i in range(len(e)):
        value = e[i]
        date = de[i]
        if MIN <= value <= MAX:
            E.append(value)
            DE.append(date)
    # propane filter
    DP = []
    P = []
    MIN = np.nanmean(p)-3*np.nanstd(p)
    MAX = np.nanmean(p)+3*np.nanstd(p)
    for i in range(len(p)):
        value = p[i]
        date = dp[i]
        if MIN <= value <= MAX:
            P.append(value)
            DP.append(date)
    # methylbutane filter
    DMB = []
    MB = []
    MIN = np.nanmean(mb)-3*np.nanstd(mb)
    MAX = np.nanmean(mb)+3*np.nanstd(mb)
    for i in range(len(mb)):
        value = mb[i]
        date = dmb[i]
        if MIN <= value <= MAX:
            MB.append(value)
            DMB.append(date)
    # methylpropane filter
    DMP = []
    MP = []
    MIN = np.nanmean(mp)-3*np.nanstd(mp)
    MAX = np.nanmean(mp)+3*np.nanstd(mp)
    for i in range(len(mp)):
        value = mp[i]
        date = dmp[i]
        if MIN <= value <= MAX:
            MP.append(value)
            DMP.append(date)
    # n-pentane filter
    DNP = []
    NP = []
    MIN = np.nanmean(nP)-3*np.nanstd(nP)
    MAX = np.nanmean(nP)+3*np.nanstd(nP)
    for i in range(len(nP)):
        value = nP[i]
        date = dnP[i]
        if MIN <= value <= MAX:
            NP.append(value)
            DNP.append(date)
    # n-butane filter
    DNB = []
    NB = []
    MIN = np.nanmean(nb)-3*np.nanstd(nb)
    MAX = np.nanmean(nb)+3*np.nanstd(nb)
    for i in range(len(nb)):
        value = nb[i]
        date = dnb[i]
        if MIN <= value <= MAX:
            NB.append(value)
            DNB.append(date)
    return DCO, CO, DCO2, CO2, DP, P, DNP, NP, DNB, NB, DE, E, DMP, MP, DMB, MB