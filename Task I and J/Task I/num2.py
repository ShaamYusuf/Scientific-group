'''A thermal system is designed to maintain a stable equilibrium temperature. The relationship between the temperature of the system and its heat balance is represented by the nonlinear equation:

[
T-22-8e^{-T/20}=0
]

Where:
(T) represents the equilibrium temperature in degrees Celsius (°C).
22 represents the surrounding temperature.
8 is the heat-transfer constant.
20 is the temperature scaling constant.'''


import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# Modified heat-balance model
def heat_balance(T):
    return T - 22 - 8*np.exp(-T/20)

# Bisection method
solution = root_scalar(
    heat_balance,
    bracket=[20, 40],
    method="bisect",
    xtol=1e-10
)

# Fixed-point method
def g(T):
    return 22 + 8*np.exp(-T/20)

T = 30.0
history = [T]

for _ in range(100):
    T_new = g(T)
    history.append(T_new)

    if abs(T_new - T) < 1e-10:
        break

    T = T_new

print(f"Bisection equilibrium temperature: {solution.root:.6f} C")
print(f"Fixed-point equilibrium temperature: {history[-1]:.6f} C")
print("Fixed-point iterations:", len(history) - 1)

# Plot the graph
temps = np.linspace(20, 40, 300)
plt.plot(temps, heat_balance(temps))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--")
plt.xlabel("Temperature (C)")
plt.ylabel("Heat-balance function")
plt.title("Modified Equilibrium Temperature")
plt.grid(True)
plt.show()