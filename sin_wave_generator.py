import numpy as np


freq = float(input("frequency(Hz) :"))
phase = float(input("sine-wave phase(deg.) :"))
N = float(input("number of periods :"))
size = int(input("number of time divisions :"))

p = 2*np.pi*freq
t = np.linspace(0, N/freq, size)
y = np.sin(p*t + phase/180*np.pi)*0.5+0.5

np.savetxt(f"sin_wav_{freq}Hz_{phase}deg_x{N}.csv", np.array([t, y]).T, delimiter=",")
