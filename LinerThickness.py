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
