# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 08:36:51 2021

@author: Martin
"""

from sense_hat import SenseHat
from time import sleep

senseHat = SenseHat()

# Konstanter
a = -0.0065
R = 287.06
g_0 = 9.81
N = 200

#Variabler
T1 = 16 + 273.15
p_1 = 100000 #Trykket målt ved høyden h_1
h_1 = 0 #Vi gjør målingene relative dersom vi ønsker ved a sette h_1 = 0

def calc_pressure_Pa():
    p = a
    for _ in range (N):
        p += senseHat.pressure
        sleep(0.001)
    return p*100/N #Vi vil ha p_1 i Pa, og multipliserer derfor med 100 etter vi deler på N


def stick down():
for e in senseHat.stick.get_events() :

    if e.direction=="down":
        return 1

while True:
    senseHat.show _message ("Venstre: maal - Hoyre: kalibrer - Ned: avbryt",0.05)

    event = senseHat.stick.wait for event)

    if event.direction == "left":
        while stick_down() != 1:
            p = calc_pressure_Pa()
            h = (T 1/a) * ( (p/p_1)**(-a*R/g_0) - 1) + h_1
            senseHat.show_message(str(round(h,2) )+ "m" ,0.07)
    if event.direction == "right":
        while stick down()) !=1:
            T_1 = senseHat.temp + 273.15
            p_1 = calc_pressure_Pa()
            senseHat.show_message(str(int (p_1))+" Pa "+str(T_1)+" K", 0.07)


# Ny kodefil

def write_to_log(write_data):
    with open(path, 'a') as f:
        f.write(str(write_data) + '\n')


# Ny kodefil

from sense_hat import SenseHat

senseHat =()
def draw():
    #Tegn hvilken etasje du er på

def calcEtasjer():
    # Konstanter
    a = -0.0065
    R = 287.06
    g_0 = 9.81
    
    # Variabler
    T_1 = 16 + 237.15
    p_1 = #Trykket målt i første etasje
    h_1 = 0 # Starthøyden (første etasje) er definert som 0
    h_e = # Høyden mellom etasjene
    
    p = senseHat.pressure * 100
    
    h = Hypsometrisk ligning
    
    etasje = h/h_e
    toppetasje = 14
    
    if etasje < 0:
        etasje = 0
    elif etasje > toppetasje:
        etasje = toppetasje
    return int(etasje)

while True:
    draw(calcEtasjer())
    
    
    
    