import math

# -------------------------VARIABLE INPUT---------------------------
# All lengths in mm
d4_base = 89.6
d9_base = 89.6
d3_base = 81.3

d1_base = 78.7
d2_base = 5.33
b_base = 7.2
# ------------------------------------------------------------------


# to find d4
def d4(base):
    # Tolerance Grade: H8
    tolerance = 54 * 0.001
    d4_lower = base
    d4_upper = base + tolerance
    return d4_lower, d4_upper


# to find d9
def d9(base):
    # Tolerance Grade: f7
    tolerance = 35 * 0.001
    deviation = -36 * 0.001
    d9_lower = base - tolerance + deviation
    d9_upper = base + deviation
    return d9_lower, d9_upper


# to find d3
def d3(base):
    # Tolerance Grade: h9
    tolerance = 87 * 0.001
    d3_lower = base - tolerance
    d3_upper = base
    return d3_lower, d3_upper


d3_lower, d3_upper = d3(d3_base)
d4_lower, d4_upper = d4(d4_base)
print(d4_lower, d4_upper, d3_lower, d3_upper)


# O-ring Stretch
def oring_stretch(d1, d3_max, d3_min):
    stretch_min = ((d3_min - d1) / d1) * 100
    stretch_max = ((d3_max - d1) / d1) * 100
    return stretch_min, stretch_max


# to find gland depth
def gland_depth(d4_min, d4_max, d3_min, d3_max):
    t_min = (d4_min - d3_max) / 2
    t_max = (d4_max - d3_min) / 2

    return t_min, t_max


# Gland Compression
def gland_compression(d2):
    t_min, t_max = gland_depth(d4_lower, d4_upper, d3_lower, d3_upper)
    compression_min = ((d2 - t_max) / d2) * 100
    compression_max = ((d2 - t_min) / d2) * 100
    return compression_min, compression_max


# Gland Fill
def gland_fill(d2, b):
    t_min, t_max = gland_depth(d4_lower, d4_upper, d3_lower, d3_upper)

    oring_csa = math.pi * (d2 / 2) ** 2
    gland_csa_min = t_min * b
    gland_csa_max = t_max * b

    fill_percentage_min = (oring_csa / gland_csa_max) * 100
    fill_percentage_max = (oring_csa / gland_csa_min) * 100

    return fill_percentage_min, fill_percentage_max


print(oring_stretch(d1_base, d3_upper, d3_lower))
print(gland_depth(d4_lower, d4_upper, d3_lower, d3_upper))
print(gland_compression(d2_base))
print(gland_fill(d2_base, b_base))
