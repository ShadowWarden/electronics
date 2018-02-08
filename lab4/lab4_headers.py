# lab4/lab4_headers.py
#
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#
# Lab 4 headers
#

import numpy as np
import matplotlib.pyplot as plt

def compute_G(Rf,R):
    # Non inverting
    return 1.+Rf/R

def plot_bode(A0,f0,omega_min,omega_max,labelstring):
    """ Plots the bode function between the given limits. """
    Nomega = 1000
    H = np.zeros(Nomega)
    omega = np.linspace(np.log(omega_min),np.log(omega_max),Nomega)
    # Low pass
    H = A0/np.sqrt(1+(np.exp(omega)/f0)**2)
    
    plt.figure(1)
    plt.plot(omega,np.log(H),'-.',label=labelstring)
    plt.legend()
    plt.xlabel(r"$\ln f$")
    plt.ylabel(r"$\ln H(f)$")
    plt.grid()
    plt.draw()
    return np.array([H,omega])

def input_Z(Ri,A0,f,f0,R,Rf):
    N = np.sqrt((Ri*A0*R+Ri*(R+Rf))**2+(f/f0*Ri*(R+Rf))**2)
    D = np.sqrt((R+Rf)**2+((R+Rf)*f/f0)**2)**0.5
    return N/D

def output_Z(Ro,A0,f,f0,R,Rf):
    N = np.sqrt((Ro*(R+Rf))**2+(Ro*(R+Rf)*f/f0)**2)
    D = np.sqrt((A0*R+R+Rf)**2+((R+Rf)*f/f0)**2)
    return N/D
