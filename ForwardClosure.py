# Forward Closure Thickness
import math


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
