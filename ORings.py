import math
# to find d4
def dia_4(d4_base):
    Tg_d4 = 54 * 10 ** (-3)
    d4_lower = d4_base
    d4_upper = d4_base + Tg_d4
    return d4_lower, d4_upper


# to find d9
def dia_9(d9_base):
    Tg_d9 = 35 * 10 ** (-3)
    dev_d9 = -36 * 10 ** (-3)
    d9_lower = d9_base - Tg_d9 + dev_d9
    d9_upper = d9_base + dev_d9
    return d9_lower, d9_upper


# to find d3
def dia_3(d3__base):
    Tg_d3 = 87 * 10 ** (-3)
    d3_lower = d3__base
    d3_upper = d4_base + Tg_d3
    return d3_lower, d3_upper


# O-ring Stretch
def oring_stretch(d1__base):
    d3_lower, d3_upper = dia_3(d3__base)
    stretch_min = ((d3_lower - d1__base) / d1__base) * 100
    stretch_max = ((d3_upper - d1__base) / d1__base) * 100
    return stretch_min, stretch_max


# to find gland depth
def gland_depth():
    d4_lower, d4_upper = dia_4(d4_base)
    d3_lower, d3_upper = dia_3(d3__base)
    t_min = (d4_lower - d3_upper) / 2
    t_max = (d4_upper - d3_lower) / 2
    return t_min, t_max


# Gland Compression
def gland_compression(d2_lower,d2_upper):
    t_min, t_max = gland_depth()
    compression_min = ((d2_upper - t_max) / d2_upper) * 100
    compression_max = ((d2_upper - t_min) / d2_upper) * 100
    return compression_min, compression_max


# Gland Fill
def gland_fill(d2_lower,d2_upper, b):
    t_min, t_max = gland_depth()
    oring_csa_lower = math.pi * (d2_lower / 2) ** 2
    oring_csa_upper = math.pi * (d2_upper / 2) ** 2
    gland_csa_min = t_min * b 
    gland_csa_max = t_max * b
    fill_percentage_min = (oring_csa / gland_csa_max) * 100
    fill_percentage_max = (oring_csa / gland_csa_min) * 100
    return fill_percentage_min, fill_percentage_max
n=0
d4_base = 95.86
d9_base = 95.86
#d4_base = float(input("input value of d4 base"))
#d9_base = float(input("input value of d9 base"))
d3_base = [90.8,89.4,86.3]
d1_base = [88.57,88.47,85]
d2_base = [2.62,3.53,5.33]
d2_error = [0.09,0.1,0.13,0.15]
b = [3.6,4.8,7.2]
b1 = [4.7,5.8,8.7]
while n < len(d2_base):
    d2_lower=d2_base[n]-d2_error[n]
    d2_upper=d2_base[n]+d2_error[n]
    d3__base=d3_base[n]
    d1__base=d1_base[n]
    stretch_min, stretch_max = oring_stretch(d1__base)
    compression_min, compression_max = gland_compression(d2_lower,d2_upper)
    fill_percentage_min, fill_percentage_max = gland_fill(d2_lower,d2_upper, b):
    if stretch_max<6 and compression_min>11 and compression_max<23 and 



