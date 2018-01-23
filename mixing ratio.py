#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:11:20 2018

@author: David Trejo
"""
import pandas as pd
dat = pd.read_excel(r'/home/cr2practica/Escritorio/co - copia.xlsx')
data = pd.read_excel(r'/home/cr2practica/Escritorio/propane data.xlsx')


def data_transfer_p(data):
    prop = data['propane']  # [pmol/mol]
    fecha = data['DATE']
    return fecha, prop


def data_transfer_co(dat):
    #x = pd.DataFrame(dat, columns =[])
    DAT = dat['DATE']
    co = dat['CO'] * 0.001  # ppb - > [pmol/mol]
    return DAT, co


d, c = data_transfer_p(data)
b, v = data_transfer_co(dat)
