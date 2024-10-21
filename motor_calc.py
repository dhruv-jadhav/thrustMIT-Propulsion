import math
import numpy as np
import matplotlib as mpl

# Casing Thickness Formula
def casing_thickness(t, R, S, E):
    """
    Calculates the minimum required thickness of the casing shell.

    P = Internal design pressure
    R = Inside radius of the shell under consideration
    S = Maximum allowable stress
    E = Joint efficiency
    t = Casing thickness
    """
    P1 = (S * E * t) / (R + 0.6 * t)

    P2 = (2 * S * E * t) / (R - 0.4 * t)

    pressure = min(P1, P2)

    print(P1, P2, pressure)

    if pressure < 0.385 * S * E:
        return pressure
    else:
        return "Equations Invalid"


# Forward Closure Thickness
def forward_closure_thickness(P, d, S, E, C):
    """
    Calculates the minimum required thickness of the flat head or cover.

    P = Internal design pressure
    d = Diameter or short span of flat head
    S = Maximum allowable stress value in tension
    E = Joint efficiency
    C = Factor depending on method of attachment
    """
    t = (P * d) / (2 * S * E * C)
    return t


# Bolt Shear Stress
def bolt_shear_stress(UTS, N, d_bolt_minor, safety_factor=1.5):
    """
    Calculates the shear stress on a bolt.

    UTS = Ultimate tensile strength
    N = Number of bolts
    d_bolt_minor = Minor diameter of the bolt
    safety_factor = Factor of safety (default = 1.5)
    """
    shear_strength = 0.75 * UTS
    sigma_shear = (N * d_bolt_minor ** 2 * math.pi) / (4 * safety_factor)
    return sigma_shear

#to find d4
def dia_4(d4_base):
    Tg_d4=39*10**(-6)
    d4_lower=d4_base
    d4_upper=d4_base + Tg_d4
    return d4_lower,d4_upper

#to find d9
def dia_9(d9_base):
    Tg_d9=25*10**(-6)
    dev_d9=-25*10**(-6)
    d9_lower=d9_base-Tg_d9+dev_d9
    d9_upper=d9_base+dev_d9
    return d9_lower,d9_upper

#to find d3
def dia_3(d3_base):
    Tg_d3=62*10**(-6)
    d3_lower=d3_base
    d3_upper=d4_base + Tg_d3
    return d3_lower,d3_upper

# O-ring Stretch
def oring_stretch(d1, d3):
    d3_lower,d3_upper=dia_3(d3_base)
    stretch_min = ((d3_lower - d1) / d1) * 100
    stretch_max = ((d3_upper - d1) / d1) * 100
    return stretch_min,stretch_max
#to find gland depth
def gland_depth():
    d4_lower,d4_upper=dia_4(d4_base)
    d3_lower,d3_upper=dia_3(d3_base)
    t_min= ((d4_lower-d3_upper)/2)
    t_max= ((d4_upper-d3_lower)/2)
    return t_min,t_max
# Gland Compression
def gland_compression(d2_base):
    t_min,t_max=gland_depth()
    compression_min = ((d2_base - t_max) / d2_base )* 100
    compression_max = ((d2_base - t_min) / d2_base )* 100
    return compression_min,compression_max

# Gland Fill
def gland_fill(d2,b):
    t_min,t_max=gland_depth()
    oring_csa = math.pi * (d2 / 2) ** 2
    gland_csa_min = t_min * b
    gland_csa_max = t_max * b
    fill_percentage_min = (oring_csa / gland_csa_max) * 100
    fill_percentage_max = (oring_csa / gland_csa_min) * 100
    return fill_percentage_min,fill_percentage_max

#d3_base=36.4mm
#d1_base=36.09mm
#d2_base=3.53mm
d4_base=float(input("input value of d4 base"))
d9_base=float(input("input value of d9 base"))
d3_base=float(input("iput value for d3 base"))
d1_base=float(input("input d1 value"))
d2_base=float(input("input d2 value"))
b=0.0048
