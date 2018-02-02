# lab3.py
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#
# Suite of Python functions for Lab3
#
__author__="Omkar H. Ramachandran"
__date__="31/01/2018"

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
    plt.plot(omega,np.log(H),'-.',label='$R = %.2f\, K\Omega, C = %.2f\, nF$' % (R/1e3,C/1e-9))
    plt.xlabel(r"$\ln\omega$")
    plt.ylabel(r"$\ln H(\omega)$")
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
        plt.plot(omega_choice,np.log(H),'bo')
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
    omega = np.linspace(np.log(omega_min),np.log(omega_max),Nomega)
    H =abs(1/(1./(2*np.pi*np.exp(omega)*L)-(2*np.pi*np.exp(omega)*C)))/np.sqrt(R**2+1/(1./(2*np.pi*np.exp(omega)*L)-(2*np.pi*np.exp(omega)*C))**2)
    
    plt.figure(1)
    plt.plot(omega,np.log(H),'-.',label='$R = %.2f\, K\Omega, C = %.2f\, nF$' % (R/1e3,C/1e-9))
    plt.xlabel(r"$\ln f$")
    plt.ylabel(r"$\ln H(\omega)$")
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
        H =abs(1./(1./(2*np.pi*np.exp(omega_choice)*L)-2*np.pi*np.exp(omega_choice)*C))/np.sqrt(R**2+(1./(2*np.pi*np.exp(omega_choice)*L)-(2*np.pi*np.exp(omega_choice)*C))**2)
        plt.plot(omega_choice,np.log(H),'bo')
        plt.draw()

def plot_point(omega,H):
    plt.plot(np.log(omega),np.log(H),'go')
    plt.draw()

def plot_bode_Res(R1,R2,omega_min,omega_max):
    Nomega = 1000 
    omega = np.linspace(np.log(omega_min),np.log(omega_max),Nomega)
    H = R2/(R1+R2)*np.ones(Nomega)
    
    plt.figure(1)
    plt.plot(omega,np.log(H),'-.',label='$R1 = %.2f\, k\Omega, R2 = %.2f\, k\Omega$' % (R1/1e3,R2/1e3))
    plt.xlabel(r"$\ln f$")
    plt.ylabel(r"$\ln H(\omega)$")
    plt.legend()
    plt.grid()
    plt.draw()
    return H

def computeH(Rargs,omega,flag):
    H = 0.0
    if(flag == 0):
        # Resistive
        # Rargs[0] = R1, [1] = R2
        H = Rargs[1]/(Rargs[0]+Rargs[1])
    if(flag == 1):
        # Low pass
        H = 1./np.sqrt(1+(Rargs[0]*Rargs[1]*omega)**2)
    elif(flag == 2):
        # High pass
        H = (Rargs[0]*Rargs[1]*omega)/np.sqrt(1+(Rargs[0]*Rargs[1]*omega)**2)
    elif(flag == 3):
        H =abs(-1/(2*np.pi*omega*Rargs[2])+(2*np.pi*omega*Rargs[1]))/np.sqrt(Rargs[0]**2+(-1/(2*np.pi*omega*Rargs[2])+(2*np.pi*omega*Rargs[1]))**2)

    return H
