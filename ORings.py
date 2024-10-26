
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
# d4_base = float(input("input value of d4 base"))
# d9_base = float(input("input value of d9 base"))
# d3_base = float(input("iput value for d3 base"))
# d1_base = float(input("input d1 value"))
# d2_base = float(input("input d2 value"))
b = 0.0048
