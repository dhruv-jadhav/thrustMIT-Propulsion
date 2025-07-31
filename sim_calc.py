import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.optimize import brentq
import pandas as pd

dt=23*10**-3
dc=90.120*10**-3
dd=72.5*10**-3
Lc=45.644*10**-3
Lt=2*10**-3
Ld=115.078*10**-3
To=1600
Po=6.1*10**6
At=np.pi * (dt**2)/4
k=1.042
R=208.4
cp = 1682
L_c= []
c_star = 876
Ma1 = []
P2 = []
T2= []
m_dot = []
pr = []
mu = []
Tr= []
h = []
x=0
g = 9.8
rc = 2*dt
def heat_transfer_coefficient(C, cp, mu, dt, pr, m_dot, At, rc, A2, Tr, To, k, Ma1):
    # Compute sigma
    sigma = 1 / (
        ((Tr / (2 * To)) * (1 + (k - 1) / 2 * Ma1**2) + 1/2) ** 0.65 * 
        (1 + (k - 1) / 2 * Ma1**2) ** 0.15
    )
    term1 = C / (dt ** 0.2)                     # Diameter scaling
    term2 = (mu ** 0.2 * cp) / (pr ** 0.4)      # Viscosity/heat capacity
    term3 = (Po / c_star) ** 0.8                 # Pressure/velocity term
    term4 = (dt / rc) ** 0.1                     # Curvature effect
    h = term1 * term2 * term3 * term4 * sigma
    return h



def temp_wall(To,Pr,k,Ma1):
    # Compute recovery temperature Tr
    Tr = To * (1 + (Pr ** (1/3)) * ((k - 1) / 2) * Ma1**2)
    return Tr
def prandtl_number(k):
    Pr = (4*k)/((9*k)-5)
    return Pr
def viscosity(Ma1,To):
    mu = (11.83*(10**(-8)))*(Ma1**0.5)*(To**0.6)
    return mu

def nozzle_profile_plot(dt,dc,Lc,Lt,Ld,dd):
    # Define key points for the profile
    x_converge = np.linspace(0, Lc, 59)
    y_converge = np.linspace(dc / 2, dt / 2, 59)
    
    x_throat = np.array([Lc, Lc + Lt])
    y_throat = np.array([dt / 2, dt / 2])
    
    x_diverge = np.linspace(Lc + Lt, Lc + Lt + Ld, 125)
    y_diverge = np.linspace(dt / 2, dd / 2, 125)
    
    # Combine all sections
    x_profile = np.concatenate([x_converge, x_throat, x_diverge])
    y_profile = np.concatenate([y_converge, y_throat, y_diverge])
    
    # Plot the nozzle profile
    plt.figure(figsize=(8, 4))
    plt.plot(x_profile, y_profile, label='Nozzle Upper Profile')
    plt.plot(x_profile, -y_profile, label='Nozzle Lower Profile')
    plt.xlabel('Length (m)')
    plt.ylabel('Radius (m)')
    plt.legend()
    plt.title('Nozzle Profile')
    plt.axis('equal')
    plt.grid()
    plt.show()
def solve_M(At,A2, k, M_guess):
    def mach_area_ratio(M_guess):
        return (1/M_guess**2) * ((2/(k+1)) * (1 + ((k-1)/2) * M_guess**2))**((k+1)/((k-1))) - (A2/At)**2

    if M_guess < 1:  # This case is for a converging section (subsonic)
        lower, upper = 0.00001, 0.999999  # Subsonic Mach number range
    else:  # This case is for a diverging section (supersonic)
        lower, upper = 1, 5.0  # Supersonic Mach number range

    # Use Brent's method to find the Mach number based on area ratio
    try:
        M_solution = brentq(mach_area_ratio, lower, upper)
        return M_solution
    except ValueError:
        print(f"Error: No solution found for A2 = {A2}, At = {At}. Returning initial guess.")
        return M_guess  # Return the initial guess in case of failure

    
    #return np.abs(M_solution[0])

def pressure(Ma1,Po,k):
    P_2 = Po * (1 + ((k - 1) / 2 )* Ma1**2) ** (-((k) / (k-1)))
    return P_2
def temperature(To, Ma1, k):

    T_2 = To * (1 + ((k - 1) / 2) * Ma1**2)**(-1)
    return T_2
def mass_flow_rate(Ma1,P2,T2,R,k,A2):
    term1 = (A2 * P2) / np.sqrt(T2)
    term2 = np.sqrt(k / R)
    term3 = Ma1 * (1 + (k - 1) / 2 * Ma1**2) ** (-(k + 1) / (2 * (k- 1)))
    return term1 * term2 * term3
def full_plots():
    Ma1_value=0
    x_converge = np.linspace(0, Lc, 100)
    y_converge = np.linspace(dc / 2, dt / 2, 100)
    
    x_throat = np.array([Lc, Lc + Lt])
    y_throat = np.array([dt / 2, dt / 2])
    
    x_diverge = np.linspace(Lc + Lt, Lc + Lt + Ld, 100)
    y_diverge = np.linspace(dt / 2, dd / 2, 100)

    x_profile = np.concatenate([x_converge, x_throat, x_diverge])
    y_profile = np.concatenate([y_converge, y_throat, y_diverge])

    for i in y_converge:
        A2 = (np.pi * i**2) 
        Ma1_value = solve_M(At,A2, k, Ma1_value)
        Ma1.append(Ma1_value)
        #print(Ma1_value,"conv")

        C =0.026

        P2_value = pressure(Ma1_value, Po, k)
        P2.append(P2_value)
        T2_value = temperature(To, Ma1_value, k)
        T2.append(T2_value)
        m_dot_value = mass_flow_rate(Ma1_value, P2_value, T2_value, R, k, A2)
        m_dot.append(m_dot_value)

        pr_value = prandtl_number(k)
        pr.append(pr_value)

        mu_value = viscosity(Ma1_value, To)
        mu.append(mu_value)

        Tr_value = temp_wall(To, pr_value, k, Ma1_value)
        Tr.append(Tr_value)
        #print(Tr_value,mu_value,Ma1_value,'conv')
        h_value = heat_transfer_coefficient(C, cp, mu_value, dt, pr_value, m_dot_value, At, rc, A2, Tr_value, To, k, Ma1_value)
        h.append(h_value)
        #print(h_value,i,'conv')

        
    j=0
    for i in y_throat:

        A2 = (np.pi * i**2) 

        Ma1_value=1
        Ma1_value = solve_M(At,A2, k, Ma1_value)
        Ma1.append(Ma1_value)
        C =0.026
        #print(Ma1_value,"thrt")
        P2_value = pressure(Ma1_value, Po, k)
        P2.append(P2_value)

        T2_value = temperature(To, Ma1_value, k)
        T2.append(T2_value)

        m_dot_value = mass_flow_rate(Ma1_value, P2_value, T2_value, R, k, A2)
        m_dot.append(m_dot_value)

        pr_value = prandtl_number(k)
        pr.append(pr_value)

        mu_value = viscosity(Ma1_value, To)
        mu.append(mu_value)

        Tr_value = temp_wall(To, pr_value, k, Ma1_value)
        Tr.append(Tr_value)
        #print(Tr_value,mu_value,Ma1_value,i,'thrt')
        
        h_value = heat_transfer_coefficient(C, cp, mu_value, dt, pr_value, m_dot_value, At, rc, A2, Tr_value, To, k, Ma1_value)
        h.append(h_value)
        #print(h_value,i,'thrt')

    j=0
    for i in y_diverge:
        A2 = (np.pi * i**2) 

        Ma1_value=Ma1_value+0.016
        Ma1_value = solve_M(At,A2, k, Ma1_value)
        Ma1.append(Ma1_value)
        C =0.026
        #print(Ma1_value,"div")
        P2_value = pressure(Ma1_value, Po, k)
        P2.append(P2_value)

        T2_value = temperature(To, Ma1_value, k)
        T2.append(T2_value)

        m_dot_value = mass_flow_rate(Ma1_value, P2_value, T2_value, R, k, A2)
        m_dot.append(m_dot_value)

        pr_value = prandtl_number(k)
        pr.append(pr_value)

        mu_value = viscosity(Ma1_value, To)
        mu.append(mu_value)

        Tr_value = temp_wall(To, pr_value, k, Ma1_value)
        Tr.append(Tr_value)

        h_value = heat_transfer_coefficient(C, cp, mu_value, dt, pr_value, m_dot_value, At, rc, A2, Tr_value, To, k, Ma1_value)
        h.append(h_value)
        #print(h_value,i,'div')

    fig, plots = plt.subplots(2, 3, figsize=(9, 9))
    # Plot each dataset in appropriate subplot
    plots[0, 0].plot(x_profile, y_profile, label='upper nozzle')
    plots[0, 0].plot(x_profile, -y_profile, label='lower nozzle')
    plots[1, 1].plot(x_profile, h, label='film coef value')
    plots[1, 2].plot(x_profile, P2, label='pressure')
    plots[0, 1].plot(x_profile, T2, label='temp')
    plots[0, 2].plot(x_profile, Ma1, label='mach number')

    # Add labels to all plots
    for ax in plots.flat:
        ax.grid(True)
        ax.legend()

    # Adjust layout
    fig.tight_layout()

    # Show the figure
    plt.show()
    return h,T2,P2,x_profile,y_profile
#nozzle_profile_plot(dt,dc,Lc,Lt,Ld,dd)
h,T2,P2,x_profile,y_profile = full_plots()
nozzle_data = {'film coefficient':h,'temp':T2, 'pressure':P2,'x coordinate':x_profile,'y coordinates':y_profile}
motor_data = pd.DataFrame(nozzle_data)
file_name = 'motor_sim_data_prac_1.xlsx'
motor_data.to_excel(file_name)
# Plot the results