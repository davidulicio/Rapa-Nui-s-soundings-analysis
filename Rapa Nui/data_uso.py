# -*- coding: utf-8 -*-
"""
Rapa Nui's vocs analysis 
@author: David Trejo Cancino
"""
import pandas as pd


def data_transfer_E(dat):
    "Transfer data from the excel file to python"
    dCO = dat['CO date']
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
    datec = pd.Series(datec)
    return valuec, datec

def spring(date, value):
    valores = []
    fechas = []
    sept = []
    oct = []
    nov = []
    dic = []
    for i in range(len(date)):
        fecha = date[i]
        valor = value[i]
        m = fecha.month
        d = fecha.day
        if m == 10:
            sept
        if m == 10 or m==11:
            fechas.append(fecha) 
            valores.append(valor)
        if m == 9:
            if d >= 21:
                fechas.append(fecha)
                valores.append(valor)
        if m == 12:
            if d <= 21:
                fechas.append(fecha)
                valores.append(valor)
    return fechas, valores
