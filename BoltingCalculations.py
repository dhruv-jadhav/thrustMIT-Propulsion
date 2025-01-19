# Bolting Calculations
# Bolt Shear Stress
import math


def bolt_shear(D_i_casing, d_bolt_minor, MEOP, N, bolt_shear_strength):
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

    FS_bolt_shear = bolt_shear_strength / bolt_shear_stress

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
    F_bolt = (math.pi * D_i_casing ** 2 * MEOP) / 4

    # Calculate E_min
    E_min = E - d_bolt_major / 2

    # Ensure E is at least twice d_bolt_major
    if E < 2 * d_bolt_major:
        raise ValueError("E_min must be at least twice d_bolt_major")

    # Calculate tear-out shear stress
    tear_out_stress = F_bolt / (E_min * 2 * t * N)

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
    F_bolt = (math.pi * D_i_casing ** 2 * MEOP) / 4

    # Calculate bearing stress
    bearing_stress = F_bolt / (N * d_bolt_major * t)

    FS_bearing = BYS / bearing_stress

    return bearing_stress, FS_bearing
def two_layer_bolt_shear(MEOP,d_i_case,N,d_1,d_2,t):
    """
    N is number of bolts 
    d_i_case is dia of case
    MEOP is  max operating pressure
    As is shear area
    d_1 is edge distance for bolts level 1
    d_2 is edge distance for bolts level 2
    """
    As=(t*(d_1 + d_2))/2
    T_shear= (MEOP*((d/2)**2)*math.pi)/(N*2*As)

    return T_shear

    