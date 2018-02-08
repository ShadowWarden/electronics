# lab4/lab4.py
# 
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#
# Lab 4 : Main python file
#

import numpy as np
import matplotlib.pyplot as plt
import lab4_headers as l4

# GBW in Hz
ft = 5e6

# Avol in V/mV
A0 = 200e3
f0 = ft/A0

l4.plot_bode(A0,f0,1.0,10e6,"Open Loop Gain")

# Magnitude of voltage swing in V
V0 = 13

# Maximum supply current
Imax = 7e-3

# Input resistance
Ri = 1e12

# Compute G for Rf=10e3 and R = 100
Rf = 10e3
R = 100
G0 = l4.compute_G(Rf,R)
print(G0)
fb = ft/G0
l4.plot_bode(G0,fb,1.0,10e6,"Closed Loop: Rf=10e3, R=100")
G02 = 1.0
fb2 = ft
l4.plot_bode(G02,fb2,1.0,10e6,"Closed Loop: Rf=0, R=infty")
plt.show()

Z = l4.input_Z(Ri,A0,1e3,f0,R,Rf)

Ro = 40
Zout = l4.output_Z(Ro,A0,1e3,f0,R,Rf)
