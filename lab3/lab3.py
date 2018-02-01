# lab3.py
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#
# Suite of Python functions for Lab3
#

import numpy as np
import matplotlib.pyplot as plt

def compute_cutoff_RC(R,C):
    """ Returns cutoff frequency for an RC filter """
    return 1./(2*np.pi*R*C)

def plot_bode_RC(R,C,omega_min,omega_max,flag):
    """ Plots the bode function between the given limits. The flag
    decides whether the transfer function used is for the high-pass 
    or low-pass filter"""
    Nomega = 1000
    H = np.zeros(Nomega)
    omega = np.linspace(np.log(omega_min),np.log(omega_max),Nomega)
    if(flag == 0):
        # Low pass
        H = 1./np.sqrt(1+(R*C*np.exp(omega))**2)
    elif(flag == 1):
        # High pass
        H = (R*C*np.exp(omega))/np.sqrt(1+(R*C*np.exp(omega))**2)
    plt.figure(1)
    plt.plot(omega,H,'r-.',label='$R = %.2f\, K\Omega, C = %.2f\, pF$' % (R/1e3,C/1e-9))
    plt.xlabel(r"$\ln\omega$")
    plt.ylabel(r"$H(\omega)$")
    plt.legend()
    plt.grid()
    plt.draw()
    return H

def generate_mock_RC(R,C,omega_min,omega_max,flag):
    """ Generates lots of mock data that follows bode curve """
    Npoints = 50
    Nomega = 1000
    omega = np.linspace(np.log(omega_min),np.log(omega_max),Nomega)
    P_omega = (1.0*np.ones(Nomega))/Nomega
    plt.figure(1)
    for i in range(Npoints): 
        omega_choice = np.random.choice(omega,p=P_omega)
        if(flag == 0):
            # Low pass
            H = 1./np.sqrt(1+(R*C*np.exp(omega_choice))**2)
        elif(flag == 1):
            # High pass
            H = (R*C*np.exp(omega_choice))/np.sqrt(1+(R*C*np.exp(omega_choice))**2)
        plt.plot(omega_choice,H,'bo')
        plt.draw()

def compute_parameters_BP(R,L,C):
    """ Returns the required parameters for a band-pass filter """
    f0 = 1/(2*np.pi*np.sqrt(L)*np.sqrt(C))
    Q = 2*np.pi*f0*R*C
    Z0 = 2*np.pi*f0*L
    return np.array([f0,Q,Z0])

def plot_bode_BP(R,L,C,omega_min,omega_max):
    """ Plots the bode function between the given limits. The flag
    decides whether the transfer function used is for the high-pass 
    or low-pass filter"""
    Nomega = 1000
    H = np.zeros(Nomega)
    omega = np.linspace(np.log(omega_min),np.log(omega_max),Nomega)
    H = R/np.sqrt(R**2+(np.exp(omega)*L-1/(np.exp(omega)*C))**2)
    
    plt.figure(1)
    plt.plot(omega,H,'r-.',label='$R = %.2f\, K\Omega, C = %.2f\, pF$' % (R/1e3,C/1e-9))
    plt.xlabel(r"$\ln\omega$")
    plt.ylabel(r"$H(\omega)$")
    plt.legend()
    plt.grid()
    plt.draw()
    return H

def generate_mock_BP(R,L,C,omega_min,omega_max):
    """ Generates lots of mock data that follows bode curve """
    Npoints = 50
    Nomega = 1000
    omega = np.linspace(np.log(omega_min),np.log(omega_max),Nomega)
    P_omega = (1.0*np.ones(Nomega))/Nomega
    plt.figure(1)
    for i in range(Npoints): 
        omega_choice = np.random.choice(omega,p=P_omega)
        H = R/np.sqrt(R**2+(np.exp(omega_choice)*L-1/(np.exp(omega_choice)*C))**2)
        plt.plot(omega_choice,H,'bo')
        plt.draw()


