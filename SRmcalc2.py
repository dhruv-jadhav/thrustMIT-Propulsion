import matplotlib.pyplot as plt
import numpy as np


# to find some key motor parameters
def constant(k, R, To, a, n, pb):
    C = ((a * pb) / np.sqrt((k / (R * To)) * ((2 / (k + 1)) ** ((k + 1) / (k - 1))))) ** (1 / (1 - n))
    return C


def chamber_pressure(C, Kn, n):
    Pc = C * (Kn) ** (1 / (1 - n))
    return Pc


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


def burn_area(L, Dp, Dg, N):
    Ab = (np.pi * Dp * L) + (N * (((np.pi) * (Dg - Dp) ** 2) / 4))
    return Ab


def burn_rate(Po, a, n):
    r = a * (Po) ** n
    return r


def length_max(Dg):
    Lmax = 12 * Dg
    return Lmax


def port_area(Dp):
    Ap = ((np.pi) * (Dp) ** 2) / 4
    return Ap


def min_Dp(At):
    Apmin = 2 * At
    Dpmin = np.sqrt((4 * Apmin) / (np.pi))
    return Dpmin


def max_Dp(At):
    Apmax = 4 * At
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
Dg = 0.0365

F_values = []
time_list = []

# Calculate constant C
C = constant(k, R, To, a, n, pb)

Favg_user = float(input("Input the average thrust: "))
l = (length_max(Dg) - 0.1) / 100

# Main loops
for N in np.arange(2, 5):
    for L in np.arange(0.1, length_max(Dg), l):
        for E in np.arange(7, 13, 0.5):
            for Ae in np.arange(0.0425 / 100, 0.0425, 0.0425 / 100):
                At = throat_area(Ae, E)
                print(f"At (throat area): {At}")
                Dp = min_Dp(At)
                inc = (max_Dp(At) - min_Dp(At)) / 100
                for Dp in np.arange(min_Dp(At), max_Dp(At), inc):
                    Favg = 0
                    for t in np.arange(0, 2, 0.001):
                        Ab = burn_area(L, Dp, Dg, N)
                        Kn_value = Kn(Ab, At)
                        Po = chamber_pressure(C, Kn_value, n)
                        F = thrust(k, Po, Pe, Ae, At)
                        F_in = F / 12
                        Favg += F_in
                        F_values.append(F)
                        time_list.append(t)

                        if np.isclose(Favg, Favg_user, atol=50):
                            print(f"Average thrust is {Favg}")
                            print(f"Length is {L}")
                            print(f"Core diameter is {Dp}")
                            print(f"Number of segments are {N}")
                            print(f"Expansion ratio is {E}")
                            break
                        Dp = Dp + (0.01 * burn_rate(Po, a, n))

# Plot results
plt.plot(time_list, F_values, marker='o', linestyle='-', color='b')
plt.title('Thrust vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Thrust (N)')
plt.grid(True)
plt.show()
