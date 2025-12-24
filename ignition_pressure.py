
def ignition_pressure(G,p,Charge_mass,V,m,R,T,x,m_gass):
    lf = x*Charge_mass/V
    lmd = 328798
    P = (G*lmd*lf*(p/(p-lf)))+101325
    return P