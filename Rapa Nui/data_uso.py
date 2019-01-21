# -*- coding: utf-8 -*-
"""
Rapa Nui's vocs analysis 
@author: David Trejo Cancino
"""
import pandas as pd
import numpy as np

def data_transfer_E(dat):
    "Transfer data from the excel file to python"
    dCO = pd.to_datetime(dat['CO date'])
    CO = dat['CO'] / 1000
    dCO2 = pd.Series(dat['CO2 date'])
    CO2 = dat['CO2'] / 1000
    dP = pd.Series(dat['Propane date'])
    P = dat['Propane'] / 1000
    dnp = pd.Series(dat['n-pentane date'])
    nP = dat['n-pentane'] / 1000
    dnb = pd.Series(dat['n-butane date'])
    nb = dat['n-butane'] / 1000
    de = pd.Series(dat['ethane date'])
    e = dat['ethane'] / 1000
    dmp = pd.Series(dat['methylpropane date'])
    mp = dat['methylpropane'] / 1000
    dmb = pd.Series(dat['methylbutane date'])
    mb = dat['methylbutane'] / 1000
    return dCO, CO, dCO2, CO2, dP, P, dnp, nP, dnb, nb, de, e, dmp, mp, dmb, mb


def prom(date, value):
    "Calculate the mean average concentration of every day of the data"
    datec = []
    valuec = []
    for i in range(len(date)-1):
        value1 = date[i]
        value2 = date[i+1]
        if value1 not in datec and value1 > date[0]:  # Eliminate NaN and duplicate values
            if value1 == value2:
                valor = (value[i] + value[i+1]) / 2
                valuec.append(float("{0:.2f}".format(valor, 2)))
                datec.append(value1)
            if value1 != value2:
                valuec.append(float("{0:.2f}".format(value[i], 2)))
                datec.append(value1)
    #valuec = pd.Series(valuec)
    datec = pd.to_datetime(datec)
    return valuec, datec

def meses(date, value):
    "Splits the concentration values in each month"
    en = []
    feb = []
    mar = []
    abr = []
    may = []
    jun = []
    jul = []
    ag = []
    sep = []
    octu = []
    nov = []
    dic = []
    for i in range(len(date)):
        fecha = date[i]
        valor = value[i]
        m = fecha.month
        #d = fecha.day  para obtener el dia en caso de necesitarlo
        if m == 1:
            en.append(valor)
        if m == 2:
            feb.append(valor)
        if m == 3:
            mar.append(valor)
        if m == 4:
            abr.append(valor)
        if m == 5:
            may.append(valor)
        if m == 6:
            jun.append(valor)
        if m == 7:
            jul.append(valor)
        if m == 8:
            ag.append(valor)
        if m == 9:
            sep.append(valor)
        if m == 10:
            octu.append(valor)
        if m == 11:
            nov.append(valor)
        if m == 12:
            dic.append(valor)
    return en, feb, mar, abr, may, jun, jul, ag, sep, octu, nov, dic


def media(e, f, m, ab, my, jn, jl, ag, s, o, n, d):
    E = np.mean(np.asarray(e))
    F = np.mean(np.asarray(f))
    M = np.mean(np.asarray(m))
    AB = np.mean(np.asarray(ab))
    MY = np.mean(np.asarray(my))
    JN = np.mean(np.asarray(jn))
    JL = np.mean(np.asarray(jl))
    AG = np.mean(np.asarray(ag))
    S = np.mean(np.asarray(s))
    O = np.mean(np.asarray(o))
    N = np.mean(np.asarray(n))
    D = np.mean(np.asarray(d))
    year = [E, F, M, AB, MY, JN, JL, AG, S, O, N, D]
    return year
