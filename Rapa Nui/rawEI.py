# -*- coding: utf-8 -*-
"""
Rapa Nui's plots with raw data
@author: David
"""
import matplotlib.pyplot as plt

def subplots(dCO, CO, dCO2, CO2, dP, P, dnp, nP, dnb, nb, de, e,
                        dmp, mp, dmb, mb):
    """"
    Generates timeseries and histogram plots for every vocs in Easter Island
    with the raw data 
    """
    fig1, (axtco, axhco) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtco.plot(dCO, CO)
    axtco.set_title('CO timeseries, Easter Island')
    axtco.set_xlabel('Years')
    axtco.set_ylabel('nmol/mol (ppb)')
    axhco.hist(CO, bins=20)
    axhco.set_xlabel('nmol/mol (ppb)')
    axhco.set_title('CO histogram with raw data')
    fig2, (axtco2, axhco2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtco2.plot(dCO2, CO2)
    axtco2.set_title('CO2 timeseries, Easter Island')
    axtco2.set_xlabel('Years')
    axtco2.set_ylabel('ppm')
    axhco2.hist(CO2, bins=20)
    axhco2.set_xlabel('ppm')
    axhco2.set_title('CO2 histogram with raw data')
    fig3, (axtp, axhp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtp.plot(dP, P)
    axtp.set_title('Propane timeseries, Easter Island')
    axtp.set_xlabel('Years')
    axtp.set_ylabel('pmol/mol')
    axhp.hist(P, bins=20)
    axhp.set_xlabel('pmol/mol')
    axhp.set_title('Propane histogram with raw data')
    fig4, (axtnp, axhnp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtnp.plot(dnp, nP)
    axtnp.set_title('n-pentane timeseries, Easter Island')
    axtnp.set_xlabel('Years')
    axtnp.set_ylabel('pmol/mol')
    axhnp.hist(nP, bins=20)
    axhnp.set_xlabel('pmol/mol')
    axhnp.set_title('n-pentane histogram with raw data')
    fig5, (axtnb, axhnb) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtnb.plot(dnb, nb)
    axtnb.set_title('n-butane timeseries, Easter Island')
    axtnb.set_xlabel('Years')
    axtnb.set_ylabel('pmol/mol')
    axhnb.hist(nb, bins=20)
    axhnb.set_xlabel('pmol/mol')
    axhnb.set_title('n-butane histogram with raw data')
    fig6, (axte, axhe) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axte.plot(de, e)
    axte.set_title('Ethane timeseries, Easter Island')
    axte.set_xlabel('Years')
    axte.set_ylabel('pmol/mol')
    axhe.hist(e, bins=20)
    axhe.set_xlabel('pmol/mol')
    axhe.set_title('Ethane histogram with raw data')
    fig7, (axtmp, axhmp) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtmp.plot(dmp, mp)
    axtmp.set_title('Methylpropane timeseries, Easter Island')
    axtmp.set_xlabel('Years')
    axtmp.set_ylabel('pmol/mol')
    axhmp.hist(mp, bins=20)
    axhmp.set_xlabel('pmol/mol')
    axhmp.set_title('Metylpropane histogram with raw data')
    fig8, (axtmb, axhmb) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axtmb.plot(dmb, mb)
    axtmb.set_title('Methylbutane timeseries, Easter Island')
    axtmb.set_xlabel('Years')
    axtmb.set_ylabel('pmol/mol')
    axhmb.hist(mp, bins=20)
    axhmb.set_xlabel('pmol/mol')
    axhmb.set_title('Metylbutane histogram with raw data')