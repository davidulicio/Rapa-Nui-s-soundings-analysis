# -*- coding: utf-8 -*-
"""
Rapa Nui's data subaxvlines with data cleansing 
@author: David
"""
import numpy as np
import matplotlib.pyplot as plt
import calendar


def example_clean(d1, c1, d2, c2):
    'Plots and example of the data cleansing'
    plt.figure(figsize=(10,8))
    plt.subplot(2,1,1)
    plt.plot(d1, c1)
    plt.title('CO2 raw data')
    plt.xlabel('Years')
    plt.ylabel('ppmv')
    plt.subplot(2,1,2)
    plt.plot(d2, c2)
    plt.title('CO2 cleansed data')
    plt.xlabel('Years')
    plt.ylabel('ppmv')
    plt.tight_layout()


def subplots(dCO, CO, dCO2, CO2, dP, P, dnp, nP, dnb, nb, de, e,\
             dmp, mp, dmb, mb):
    """
    Generates timeseries and histogram plot for every vocs in Easter Island
    with the cleaned data
    """
    fig1, (axtco, axhco) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtco.plot(dCO, CO, '-')
    axtco.set_title('CO timeseries, Easter Island')
    axtco.set_xlabel('Years')
    axtco.set_ylabel('nmol/mol (ppb)')
    axhco.hist(CO, bins=20)
    axhco.set_xlabel('nmol/mol (ppb)')
    axhco.set_title('CO histogram')
    fig2, (axtco2, axhco2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtco2.plot(dCO2, CO2)
    axtco2.set_title('CO2 timeseries, Easter Island')
    axtco2.set_xlabel('Years')
    axtco2.set_ylabel('ppm')
    axhco2.hist(CO2, bins=20)
    axhco2.set_xlabel('ppm')
    axhco2.set_title('CO2 histogram')
    fig3, (axtp, axhp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtp.plot(dP, P)
    axtp.set_title('Propane timeseries, Easter Island')
    axtp.set_xlabel('Years')
    axtp.set_ylabel('pmol/mol')
    axhp.hist(P, bins=20)
    axhp.set_xlabel('pmol/mol')
    axhp.set_title('Propane histogram')
    fig4, (axtnp, axhnp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtnp.plot(dnp, nP)
    axtnp.set_title('n-pentane timeseries, Easter Island')
    axtnp.set_xlabel('Years')
    axtnp.set_ylabel('pmol/mol')
    axhnp.hist(nP, bins=20)
    axhnp.set_xlabel('pmol/mol')
    axhnp.set_title('n-pentane histogram')
    fig5, (axtnb, axhnb) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtnb.plot(dnb, nb)
    axtnb.set_title('n-butane timeseries, Easter Island')
    axtnb.set_xlabel('Years')
    axtnb.set_ylabel('pmol/mol')
    axhnb.hist(nb, bins=20)
    axhnb.set_xlabel('pmol/mol')
    axhnb.set_title('n-butane histogram')
    fig6, (axte, axhe) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axte.plot(de, e)
    axte.set_title('Ethane timeseries, Easter Island')
    axte.set_xlabel('Years')
    axte.set_ylabel('pmol/mol')
    axhe.hist(e, bins=20)
    axhe.set_xlabel('pmol/mol')
    axhe.set_title('Ethane histogram')
    fig7, (axtmp, axhmp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtmp.plot(dmp, mp)
    axtmp.set_title('Methylpropane timeseries, Easter Island')
    axtmp.set_xlabel('Years')
    axtmp.set_ylabel('pmol/mol')
    axhmp.hist(mp, bins=20)
    axhmp.set_xlabel('pmol/mol')
    axhmp.set_title('Metylpropane histogram')
    fig8, (axtmb, axhmb) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtmb.plot(dmb, mb)
    axtmb.set_title('Methylbutane timeseries, Easter Island')
    axtmb.set_xlabel('Years')
    axtmb.set_ylabel('pmol/mol')
    axhmb.hist(mp, bins=20)
    axhmb.set_xlabel('pmol/mol')
    axhmb.set_title('Metylbutane histogram')


def mixing_ratios(co, value, nombre):
    "Plots mixing ratios of a voc vs co with their months averages"
    t = np.linspace(1,12,12)
    co = np.asarray(co)
    value = np.asarray(value)
    mx_rat = co/value
    plt.figure(figsize=(8,6))
    plt.plot(t, mx_rat, '*--')
    plt.title('Mixing ratio between CO and ' + nombre)
    plt.ylabel('Ratio')
    plt.xlabel('Months')
    plt.xticks(t, calendar.month_abbr[1:13], rotation=45)
    