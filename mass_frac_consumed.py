import numpy as np
def mass_frac_consumed(radius,t,P,a,n,L,p,Charge_mass,x):
    r = a*(P*10**(-6))**n
    l = L-2*(r*t*10**(-3))
    A_it = np.pi*(radius-r*t)**2
    Charge_mass_it = A_it*l*p
    G =1- Charge_mass_it/Charge_mass
    radius_value = radius - r*t
    return G,l,Charge_mass_it,r,radius_value