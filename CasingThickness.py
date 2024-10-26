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
    else:
        return "Equations Invalid"
