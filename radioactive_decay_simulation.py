import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# y' = -a*y
def decay(y, t, a):
    return -a * y

a = float(input("Enter the decay constant :"))        
y0 = int(input("Enter the initial amount :")) 
t = np.linspace(0, 10, 100)  # time from 0 to 10

solution = odeint(decay, y0, t, args=(a,))

plt.plot(t, solution, label=f'Decay (a={a})')
plt.xlabel('Time')
plt.ylabel('Amount y(t)')
plt.title('Radioactive Decay y\' = -a*y')
plt.legend()
plt.grid(True)
plt.show()
