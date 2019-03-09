# -*- coding: utf-8 -*-
"""
Ozone functions
@author: DavidUlises
"""
import numpy as np
import pandas as pd
import datetime as dT 


def date(tabla):
    "Find the date of the file"
    i = 0
    year = []
    month = []
    day = []
    for value in tabla:
        try:
            val = int(value)
            i = i + 1
            if 0 < i <= 4:
                year.append(str(val))
            if 4 < i <= 6:
                month.append(str(val))
            if 6 < i <= 8:
                day.append(str(val))
        except ValueError:
            pass
    year = int("".join(year))
    month = int("".join(month))
    day = int("".join(day))
    name = str(year) + '-' + str(month) + '-' + str(day)
    return year, month, day, name


def data_transfer(datos):
    "Transfer data from the file to the program"
    lista = []
    lista2 = []
    for i in range(len(datos)):
        if i >= 21:
            lista.append(datos[i])
    for value in lista:
        lis = np.array(value.split())
        lista2.append(lis)
    lista = np.asarray(lista2)
    height = lista[:, 0]
    press = lista[:, 1]
    tem = lista[:, 2]
    RH = lista[:, 3]
    O3mPa = lista[:, 4]
    O3ppbv = lista[:, 5]
    O3DU = lista[:, 6]
    u = lista[:, 7]
    v = lista[:, 8]
    th = lista[:, 9]
    the = lista[:, 10]
    Q = lista[:, 11]
    return height, press, tem, RH, O3mPa, O3ppbv, O3DU, u, v, th, the, Q


def data_cleansing(h, p, tem, RH, O3mPa, O3ppbv, O3DU, u, v, th, the, Q):
    "Detects and removes inaccurate records from each list"
    RHf = []
    h_RH = []
    for i in range(len(RH)):
        if float(RH[i]) != 9000.000:
            RHf.append(RH[i])
            h_RH.append(h[i])
    Tf = []
    h_T = []
    for i in range(len(tem)):
        if float(tem[i]) != 9000.000:
            Tf.append(float(tem[i]) - 273.15)
            h_T.append(h[i])
    O3 = []
    h_O3 = []
    for i in range(len(O3mPa)):
        if float(O3mPa[i]) != 9000.000:
            O3.append(float(O3mPa[i]) * 10)
            h_O3.append(h[i])
    O3ppb = []
    hppb = []
    for i in range(len(O3ppbv)):
        if float(O3ppbv[i]) != 9000.000:
            O3ppb.append(float(O3ppbv[i]))
            hppb.append(float(h[i]))
    U = []
    h_u = []
    for i in range(len(u)):
        if float(u[i]) != 9000.000:
            U.append(float(u[i]))
            h_u.append(h[i])
    V = []
    h_v = []
    for i in range(len(v)):
        if float(v[i]) != 9000.000:
            V.append(float(v[i]))
            h_v.append(h[i])

    return RHf, h_RH, Tf, h_T, O3, h_O3, U, h_u, V, h_v, O3ppb, hppb


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
        m = int(fecha.apply(lambda x: x.month))  # It gets the month
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


"""
def graphs(h1, h2, h3, h4, h5, RH, tem, Oz, u, v, y, m, d, tabla, i):
    "Genera graficos"
    plt.figure(num=i)
    plt.plot(RH, h1, 'k', label='RH%')  # h vs RH
    plt.plot(tem, h2, 'r', label='Temperature in Celcius')  # h vs T
    plt.plot(Oz, h3, 'b', label='Ozone(nbar)')  # h vs O3DU
    plt.legend()
   fig, axes = plt.subplots(ncols=2, figsize=(8, 4))
    fig.suptitle('Rapa Nui (27° S, 109° W); Date: ' + repr(y) + '/' + repr(m) + '/' + repr(d) + ';' + '\n\
              CR2 / DMC archive', multialignment='center')
    ax1 = axes[0]
    ax1.plot(RH, h1, 'k', label='RH%')  # h vs RH
    ax1.plot(tem, h2, 'r', label='Temperature in Celcius')  # h vs T
    ax1.plot(Oz, h3, 'b', label='Ozone(nbar)')  # h vs O3DU
    ax1.legend()
    ax2 = axes[1]
    ax2.plot
    ax2.plot(u, h4, 'b', label='Zonal Wind(u)')
    ax2.plot(v, h5, 'r', label='Meridional Wind(v)')
    ax2.set_xlim(-40, 80)
    ax2.legend()
    fig.show()
    
    plt.figure(num=int(repr(i)))
    plt.title('Rapa Nui (27° S, 109° W); Date: ' + repr(y) + '/' + repr(m) + '/' + repr(d) + ';' + '\n\
              CR2 / DMC archive', multialignment='center')
    f[i], (ax1, ax2) = plt.subplots(1, 2, sharey=False)
    ax1.set_xlabel('Temperature(Celcius)    Ozone(nbar)   RH%')
    ax1.set_ylabel('Altitude [km]')
    ax1.set_xticklabels()
    ax2.set_xlabel('m/s')
    ax1.plot(RH, h1, 'k', label='RH%')  # h vs RH
    ax1.plot(tem, h2, 'r', label='Temperature in Celcius')  # h vs T
    ax1.plot(Oz, h3, 'b', label='Ozone(nbar)')  # h vs O3DU
    ax2.plot(u, h4, 'b', label='Zonal Wind(u)')
    ax2.plot(v, h5, 'r', label='Meridional Wind(v)')
    ax2.set_xlim(-40, 80)
    ax1.legend()
    ax2.legend()
    plt.ioff()
    f.savefig(repr(tabla) + '.png')
    plt.close()"""
"""
i = 0
for value in filenames:
    i = i + 1
    tabla = value
    data = open(tabla, 'r')  # Data reading
    datos = data.readlines()
    h, press, tem, RH, O3mPa, O3ppbv, O3DU, u, v, th, the, Q = data_transfer(datos)
    RHf, h_RH, Tf, h_T, O3, h_O3, u, h_u, v, h_v = data_cleansing(h, press, 
                              tem, RH, O3mPa, O3mPa, O3DU, u, v, th, the, Q)
    y, m, d, name = date(tabla)
    graphs(h_RH, h_T, h_O3, h_u, h_v, RHf, Tf, O3, u, v, y, m, d, tabla, i)
"""