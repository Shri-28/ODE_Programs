import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# RADIOACTIVE DECAY : y' = -a*y
def decay(y, t, a):
    return -a * y

print("RADIOACTIVE DECAY : y' = -a * y")
a = float(input("Enter the decay constant :"))           # decay constant
y0 = int(input("Enter the initial amount :"))            # initial value
t = np.linspace(0, 10, 200)

# Numerical Solution
decay_num = odeint(decay, y0, t, args=(a,)).flatten()
# Analytical Solution
decay_analytical = y0 * np.exp(-a * t)

plt.figure(figsize=(6, 4))
#Plot 1: Radioactive Decay
plt.subplot(1, 2, 1)
plt.plot(t, decay_num, label="Numerical (odeint)")
plt.plot(t, decay_analytical, "--", label="Analytical")
plt.title("Radioactive Decay: y' = -a*y")
plt.xlabel("Time (t)")
plt.ylabel("y(t)")
plt.legend()
plt.grid(True)
plt.show()
print()
# LEAKY TANK (WITH INFLOW): y' = b - a*y
def leaky_tank(y, t, a, b):
    return b - a * y

print("LEAKY TANK (WITH INFLOW): y' = b - a * y")
y0_2 = float(input("Enter the initial amount :")) 
a2 = float(input("Enter the decay constant :"))        # outflow rate
b = float(input("Enter the addition constant :"))      # constant inflow
t2 = np.linspace(0, 20, 400)

# Numerical Solution
leaky_num = odeint(leaky_tank, y0_2, t2, args=(a2, b)).flatten()

# Analytical Solution
y_eq = b / a2
leaky_analytical = y_eq + (y0_2 - y_eq) * np.exp(-a2 * t2)

plt.figure(figsize=(6, 4))

#Plot 2: Leaky Tank
plt.subplot(1, 2, 2)
plt.plot(t2, leaky_num, label="Numerical (odeint)")
plt.plot(t2, leaky_analytical, "--", label="Analytical")
plt.axhline(y_eq, color='k', lw=0.6, linestyle=':', label=f"Equilibrium y*={y_eq:.2f}")
plt.title("Leaky Tank: y' = b - a*y")
plt.xlabel("Time (t)")
plt.ylabel("y(t)")
plt.legend()
plt.grid(True)
plt.show()
