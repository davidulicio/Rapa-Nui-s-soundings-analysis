# -*- coding: utf-8 -*-
"""
Pandas timeseries function
@author: David
"""
import matplotlib.pyplot as plt
import statsmodels.api as sm
def timeser_pd(data):
    decomposition = sm.tsa.seasonal_decompose(data, model='additive')
    decomposition.plot()
    plt.rcParams['figure.figsize']=[9.0, 5.0]
    #statsmodels.tsa.seasonal.seasonal_decompose(x, model='additive', filt=None, freq=None, two_sided=True, extrapolate_trend=0)