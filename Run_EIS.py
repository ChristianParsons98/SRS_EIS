#This Python file interfaces with a Stanford Research Systems SR830 Lock-in amplifier.
# The algorithm measures the in phase and out of phase impedance response at various frequencies.
#Author: Christian Parsons
#First Created: 17 October 2024
#Last Updated: 17 October 2024

import pyvisa
import time
import csv
import win32api
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#The instruments need to be turned on before they will show up here.
#Opening a Resource Manager - Uses Labview backend, NI, to interface with Instruments.
rm = pyvisa.ResourceManager()

#Define the instrument as an object in python.
#This is the Lockin
Lockin=rm.open_resource("GPIB0::8::INSTR")

#Uncomment to check the identification of the instrument if GPIB channels are redifined. 
#print(Lockin.query('*IDN?'))

#Reset the instrument settings to default - so we know what we are starting with
Lockin.write("*rst; status:preset; *cls")

#This function takes the in phase and out of phase impedance response measurement at a given frequency
def measureZ(freq):
Lockin.write("FREQ 10")
Lockin.write("SLVL 0.005")
Lockin.write("SENS 17")
Lockin.write("APHS")
result = Lockin.query("SNAP? 1,2")
print(result.split(',')[0])
Lockin.write("*rst; status:preset; *cls")
