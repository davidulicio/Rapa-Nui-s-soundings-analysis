# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 12:22:44 2018
Rapa Nui's Soundings Analysis
@author: David Trejo Cancino
DGF Uchile

"""
import numpy as np
import matplotlib.pyplot as plt
print ('Easter Island´s analysis')
print ('Ingrese ubicacion (ruta de acceso) al archivo entre comillas')
#tabla = input()
tabla = r'C:\Users\David\Desktop\Ozono CR2\uno\rapanui_19941123_V01.dat'
data = open(tabla, 'r')  # Data reading
datos = data.readlines()


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
            if i <= 4:
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
    return year, month, day


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
        if float(RH[i]) != 9000:
            RHf.append(RH[i])
            h_RH.append(h[i])
    Tf = []
    h_T = []
    for i in range(len(tem)):
        if float(tem[i]) != 9000:
            Tf.append(float(tem[i]) - 273.15)
            h_T.append(h[i])
    O3 = []
    h_O3 = []
    for i in range(len(O3mPa)):
        if float(O3mPa[i]) != 9000:
            O3.append(float(O3mPa[i]) * 10)
            h_O3.append(h[i])
    U = []
    h_u = []
    for i in range(len(u)):
        if float(u[i]) != 9000:
            U.append(float(u[i]))
            h_u.append(h[i])
    V = []
    h_v = []
    for i in range(len(v)):
        if float(v[i]) != 9000:
            V.append(float(v[i]))
            h_v.append(h[i])

    return RHf, h_RH, Tf, h_T, O3, h_O3, U, h_u, V, h_v


def graphs(h1, h2, h3, h4, h5, RH, tem, Oz, u, v, y, m, d):
    "Genera graficos"
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.set_title('Rapa Nui (27° S, 109° W); Date: ' + repr(y) + '/' + repr(m) +
              '/' + repr(d) + ';')
    ax2.set_title(' CR2 / DMC archive')
    ax1.set_xlabel('Temperature(Celcius)    Ozone(nbar)   RH%')
    ax1.set_ylabel('Altitude [km]')
    ax1.plot(RH, h1, 'k', label='RH%')  # h vs RH
    ax1.plot(tem, h2, 'r', label='Temperature in Celcius')  # h vs T
    ax1.plot(Oz, h3, 'b', label='Ozone(nbar)')  # h vs O3DU
    ax2.plot(u, h4, 'b', label='Zonal Wind(u)')
    ax2.plot(v, h5, 'r', label='Meridional Wind(v)')
    ax2.set_xlim(-40, 80)
    ax1.legend()
    ax2.legend()
    ax1.xticks([])
    ax1.show()
    ax2.show()
    

" USO DE LAS FUNCIONES "
h, press, tem, RH, O3mPa, O3ppbv, O3DU, u, v, th, the, Q = data_transfer(datos)
RHf, h_RH, Tf, h_T, O3, h_O3, u, h_u, v, h_v = data_cleansing(h, press,
                                                              tem, RH, O3mPa,
                                                              O3mPa, O3DU, u,
                                                              v, th, the, Q)
y, m, d = date(tabla)
graphs(h_RH, h_T, h_O3, h_u, h_v, RHf, Tf, O3, u, v, y, m, d)
