import matplotlib.pyplot as plt
from math import log10

# Calcula la cabeza de la bomba
def Hb(pressure_1, pressure_2, density_1):
    (pressure_2-pressure_1)/(density_1*9.81)

# Calcula la cabeza del sistema
def Hs(pressure_1, pressure_2, density_1, velocity_1, velocity_2,
       z_1, z_2, frictions):
    dp = pressure_2-pressure_1
    dz = z_2-z_1
    dv = velocity_2**2-velocity_1**2
    return (dp*100**2)/(density_1) + (dz) + (dv)/(2*9.81) + frictions

# Calcula el número de Reynolds
def Re(velocity, diameter, density, viscosity):
    return velocity*diameter*density/viscosity

# Calcula los factores de fricción
def factor_friction(diameter, roughness, Reynolds):
    den = 0.25/(log10(1/(3.7*diameter/roughness)) + 5.74/Reynolds**0.9)**2
    return den

# Calcula las pérdidas de cabeza
def friction(f_friction, diameter, velocity, length):
    return f_friction*length*velocity**2/(diameter*2*9.81)


def plot_data(x: list, y: list, title: str, xlabel: str, ylabel: str) -> None:
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.set_ylim(0, max(y)+max(y)*0.1)
    ax.grid()
    plt.show()


def velocity(flow, diameter):
    return flow/(3.1416*(diameter/2)**2)


def len_eq(accesorios: dict[str, int], len:dict[str, int]) -> int:
    dict = {k: accesorios[k]*len[k] for k in accesorios}
    longuitudeseq = sum(dict.values())
    return longuitudeseq 