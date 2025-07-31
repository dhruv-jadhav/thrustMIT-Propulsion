import matplotlib.pyplot as plt
import numpy as np


# to find some key motor parameters
def constant(k, R, To, a, n, pb):
    C = ((a * pb) / np.sqrt((k / (R * To)) * ((2 / (k + 1)) ** ((k + 1) / (k - 1))))) ** (1 / (1 - n))
    return C


def chamber_pressure(C, Kn, n):
    Po = C * (Kn) ** (1 / (1 - n))
    return Po


def expansion_ratio(k, Po, Pe):
    e = ((k + 1) / 2) ** (1 / (k - 1)) * (Pe / Po) ** (1 / k) * (
                ((k + 1) / (k - 1)) * (1 - (Pe / Po) ** ((k - 1) / k))) ** (1 / 2)
    E = 1 / e
    return E


def throat_area(Ae, E):
    At = Ae / E
    return At


def thrust(k, Po, Pe, Ae, At):
    F = At * Po * np.sqrt(
        ((2 * k ** 2) / (k - 1)) * (2 / (k + 1)) ** ((k + 1) / (k - 1)) * (1 - (Pe / Po) ** ((k - 1) / k))) + (
                    Pe - Po) * Ae
    return F


def Kn(Ab, At):
    Kn_value = Ab / At
    return Kn_value


def burn_area(L, Dp, Dc, N):
    Ab = (np.pi * Dp * L) + (N * (((np.pi) * (Dc - Dp) ** 2) / 4))
    return Ab


def burn_rate(Po, a, n):
    r = a * (Po) ** n
    return r


def length_max_full(Dc):
    Lmax = 12 * Dc
    return Lmax


def length_grain(Dp):
    L_grain_max = 6*Dp
    L_grain_min = 2*Dp
    return L_grain_max,L_grain_min


def min_Dp(At):
    Apmin = 2 * At
    Dpmin = np.sqrt((4 * Apmin) / (np.pi))
    return Dpmin


def max_Dp(At):
    Apmax = 3 * At
    Dpmax = np.sqrt((4 * Apmax) / (np.pi))
    return Dpmax


# Constants
k = 1.1361
R = 208.4
To = 1488
a = 1
n = 0.22
pb = 1767
Pe = 0.0006
Dc = 0.099
F_values = []
time_list = []


