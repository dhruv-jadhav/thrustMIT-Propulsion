import numpy as np
def chamber_pressure(Ab,p,At,r,c_star):
    K = Ab/At
    Po = p*K*r*c_star
    return Po