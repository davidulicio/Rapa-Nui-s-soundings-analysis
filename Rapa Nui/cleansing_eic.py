# -*- coding: utf-8 -*-
"""
Data cleansing for Rapa Nui
@author: David
"""

def data_cleansing(dco, co, dco2, co2, dp, p, dnP, nP, dnb, nb, de, 
                    e, dmp, mp, dmb, mb):
    """
    It applies a value filter for each vocs in Rapa Nui's data
    """
    # co filter
    DCO = []
    CO = []
    for i in range(len(co)):
        value = co[i]
        date = dco[i]
        if 40 <= value <= 100:
            CO.append(value)
            DCO.append(date)
    # co2 filter
    DCO2 = []
    CO2 = []
    for i in range(len(co2)):
        value = co2[i]
        date = dco2[i]
        if 350 <= value <= 405:
            CO2.append(value)
            DCO2.append(date)
    # ethane filter
    DE = []
    E = []
    for i in range(len(e)):
        value = e[i]
        date = de[i]
        if 50 <= value <= 500:
            E.append(value)
            DE.append(date)
    # propane filter
    DP = []
    P = []
    for i in range(len(p)):
        value = p[i]
        date = dp[i]
        if 0 <= value <= 1000:
            P.append(value)
            DP.append(date)
    # methylbutane filter
    DMB = []
    MB = []
    for i in range(len(mb)):
        value = mb[i]
        date = dmb[i]
        if 0 <= value <= 600:
            MB.append(value)
            DMB.append(date)
    # methylpropane filter
    DMP = []
    MP = []
    for i in range(len(mp)):
        value = mp[i]
        date = dmp[i]
        if 0 <= value <= 160:
            MP.append(value)
            DMP.append(date)
    # n-pentane filter
    DNP = []
    NP = []
    for i in range(len(nP)):
        value = nP[i]
        date = dnP[i]
        if 0 <= value <= 300:
            NP.append(value)
            DNP.append(date)
    # n-butane filter
    DNB = []
    NB = []
    for i in range(len(nb)):
        value = nb[i]
        date = dnb[i]
        if 0 <= value <= 350:
            NB.append(value)
            DNB.append(date)
    return DCO, CO, DCO2, CO2, DP, P, DNP, NP, DNB, NB, DE, E, DMP, MP, DMB, MB