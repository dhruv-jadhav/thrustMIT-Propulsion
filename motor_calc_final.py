import math


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
#nigga got a large shlong
    P1 = (S * E * t) / (R + 0.6 * t)

    P2 = (2 * S * E * t) / (R - 0.4 * t)

    pressure = min(P1, P2)

    print(P1, P2, pressure)

    if pressure == P1:
        if pressure < 0.385 * S * E:
            return pressure
        else:
            return "Equations Invalid"
    elif pressure == P2:
        if pressure * S * E:
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
    t = d * math.sqrt(((C * P) / (S * E)))

    return t


# Liner Thickness
def liner_thickness(te, re, f):
    """
    Calculates the liner thickness.

    te = Exposure time
    re = Erosion rate
    f = Factor of safety
    """
    d = te * re * f

    return d


# Bolting Calculations
# Bolt Shear Stress
def bolt_shear(D_i_casing, d_bolt_minor, MEOP, N, UTS):
    """
    Calculates the bolt shear stress and factor of safety.

    D_i_casing: Inside diameter of the casing (mm)
    d_bolt_minor: Minor diameter of the bolt (mm)
    MEOP: Maximum Expected Operating Pressure (MPa)
    N: Number of bolts
    UTS: Ultimate Tensile Strength of the fastener/bolt (MPa)
    """
    # Numerator: (π/4) * D_i_casing^2 * MEOP
    numerator = (math.pi / 4) * (D_i_casing ** 2) * MEOP

    # Denominator: N * (π/4) * d_bolt_minor^2
    denominator = N * (math.pi / 4) * (d_bolt_minor ** 2)

    # Bolt shear stress
    bolt_shear_stress = numerator / denominator

    FS_bolt_shear = (0.75 * UTS) / bolt_shear_stress

    return bolt_shear_stress, FS_bolt_shear


def bolt_tear_out(D_i_casing, d_bolt_major, MEOP, N, E, t, shear_strength):
    """
        Calculates the bolt tear-out stress and factor of safety.

        D_i_casing: Inside diameter of the casing (mm)
        d_bolt_major: Major diameter of the bolt (mm)
        MEOP: Maximum Expected Operating Pressure (MPa)
        E: Minimum Edge Distance (mm)
        t: casing thickness (mm)
        shear_strength: Shear strength of casing material (MPa)
        N: Number of bolts
    """

    # Calculate bolt force
    F_bolt = (math.pi * D_i_casing ** 2 * MEOP) / (4 * N)

    # Calculate E_min
    E_min = E - d_bolt_major / 2

    # Ensure E is at least twice d_bolt_major
    if E < 2 * d_bolt_major:
        raise ValueError("E_min must be at least twice d_bolt_major")

    # Calculate tear-out shear stress
    tear_out_stress = F_bolt / (E_min * 2 * t)

    # Calculate factor of safety
    FS_tear_out = shear_strength / tear_out_stress

    return tear_out_stress, FS_tear_out


def casing_tensile_stress(D_o_casing, t, N, d_bolt_major, MEOP, YTS):
    """
    Calculates the tensile stress and factor of safety.

    D_o_casing: Casing outside diameter (mm)
    t: Thickness of the casing wall (mm)
    N: Number of bolts
    d_bolt_major: Major diameter of the bolt (mm)
    MEOP: Maximum expected operating pressure (MPa)
    YTS: Yield Tensile Strength of the casing material (MPa)
    """
    # Calculate tensile stress
    numerator = (math.pi / 4) * D_o_casing ** 2 * MEOP
    denominator = ((D_o_casing - t) * math.pi) - N * d_bolt_major
    tensile_stress = numerator / (denominator * t)

    FS_tensile = YTS / tensile_stress

    return tensile_stress, FS_tensile


def casing_bearing_stress(D_i_casing, MEOP, N, d_bolt_major, t, BYS):
    """
    Calculates the bearing stress and factor of safety.

    F_bolt: Force applied by the bolt (N)
    D_i_casing: Inside diameter of the casing (mm)
    d_bolt_major: Major diameter of the bolt (mm)
    t: Thickness of the casing wall (mm)
    MEOP: Maximum Expected Operating Pressure (MPa)
    BYS: Bearing Yield Strength of the casing material (MPa)
    """
    F_bolt = (math.pi * D_i_casing ** 2 * MEOP) / (4 * N)

    # Calculate bearing stress
    bearing_stress = F_bolt / (d_bolt_major * t)

    FS_bearing = BYS / bearing_stress

    return bearing_stress, FS_bearing


# to find d4
def dia_4(d4_base):
    Tg_d4 = 39 * 10 ** (-6)
    d4_lower = d4_base
    d4_upper = d4_base + Tg_d4
    return d4_lower, d4_upper


# to find d9
def dia_9(d9_base):
    Tg_d9 = 25 * 10 ** (-6)
    dev_d9 = -25 * 10 ** (-6)
    d9_lower = d9_base - Tg_d9 + dev_d9
    d9_upper = d9_base + dev_d9
    return d9_lower, d9_upper


# to find d3
def dia_3(d3_base):
    Tg_d3 = 62 * 10 ** (-6)
    d3_lower = d3_base
    d3_upper = d4_base + Tg_d3
    return d3_lower, d3_upper


# O-ring Stretch
def oring_stretch(d1, d3):
    d3_lower, d3_upper = dia_3(d3_base)
    stretch_min = ((d3_lower - d1) / d1) * 100
    stretch_max = ((d3_upper - d1) / d1) * 100
    return stretch_min, stretch_max


# to find gland depth
def gland_depth():
    d4_lower, d4_upper = dia_4(d4_base)
    d3_lower, d3_upper = dia_3(d3_base)
    t_min = ((d4_lower - d3_upper) / 2)
    t_max = ((d4_upper - d3_lower) / 2)
    return t_min, t_max


# Gland Compression
def gland_compression(d2_base):
    t_min, t_max = gland_depth()
    compression_min = ((d2_base - t_max) / d2_base) * 100
    compression_max = ((d2_base - t_min) / d2_base) * 100
    return compression_min, compression_max


# Gland Fill
def gland_fill(d2, b):
    t_min, t_max = gland_depth()
    oring_csa = math.pi * (d2 / 2) ** 2
    gland_csa_min = t_min * b
    gland_csa_max = t_max * b
    fill_percentage_min = (oring_csa / gland_csa_max) * 100
    fill_percentage_max = (oring_csa / gland_csa_min) * 100
    return fill_percentage_min, fill_percentage_max


# d3_base=36.4mm
# d1_base=36.09mm
# d2_base=3.53mm
d4_base = float(input("input value of d4 base"))
d9_base = float(input("input value of d9 base"))
d3_base = float(input("iput value for d3 base"))
d1_base = float(input("input d1 value"))
d2_base = float(input("input d2 value"))
b = 0.0048
