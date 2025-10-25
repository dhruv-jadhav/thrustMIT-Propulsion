import numpy as np
import matplotlib.pyplot as plt
import ignition_pressure
import mass_frac_consumed
import chamber_pressure 

def transient_loop():
    p = 1.749*10**3
    V = 1.167*10**(-3)
    m = 39.9*10**(-3)
    R = 8314
    T = 1600
    L = 0.02
    a = 5.132
    n = 0.220
    x = 5 #number of igniters
    radius_value = 0.005
    m_gass = 0
    At = 511*10**(-6)
    c_star = 908
    Charge_mass = L*p*np.pi*radius_value**(2)
    P = []
    G = []
    t = []
    charge_mass_it = []
    Po = []
    r = []
    radius = []
    G_value = 0
    i = 0
    l =[]
    for t_value in np.arange(0,2,0.00000001):
        P_value = ignition_pressure.ignition_pressure(G_value,p,Charge_mass,V,m,R,T,x,m_gass)
        P.append(P_value)
        G_value,l_value,charge_mass_it_value,r_value,radius_value = mass_frac_consumed.mass_frac_consumed(radius_value,t_value,P_value,a,n,L,p,Charge_mass,x)
        #Po_value = chamber_pressure.chamber_pressure(Ab,p,At,r_value,c_star)
        r.append(r_value)
        #Po.append(Po_value)
        G.append(G_value)
        t.append(t_value)
        l.append(l_value)
        radius.append(radius_value)
        charge_mass_it.append(charge_mass_it_value)
        if l_value <= 0:
            print("burned l")
            break
        elif radius_value <= 0:
            print("burned r")
            break
        i=i+1
        print(i)
    
    fig, plots = plt.subplots(1, 4, figsize=(17,10))
    plots[0].plot(t, P, label='pressure/time')
    plots[1].plot(t, l, label='length/time')
    plots[2].plot(t, r, label='burn /time')
    plots[3].plot(t, radius, label='radius/time')
    for ax in plots:
        ax.grid(True)
        ax.legend()
    fig.tight_layout()
    plt.show()
transient_loop()