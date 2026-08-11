import numpy as np
import matplotlib.pyplot as plt

def addPointCharge2D(V, Ex, Ey, X, Y, q):
    eps = 1e-9  # Avoid division by zero
    r2 = (X - q[0])**2 + (Y - q[1])**2 + eps
    
    Ex += q[2] * (X - q[0]) / (r2**(3/2))
    Ey += q[2] * (Y - q[1]) / (r2**(3/2))
    V  += q[2] / (r2**0.5)
    
    return V, Ex, Ey

# Define spatial domain
xrange = [-2.0, 2.0]
step = 150

xlist = np.linspace(xrange[0], xrange[1], step)
ylist = np.linspace(xrange[0], xrange[1], step)
X, Y = np.meshgrid(xlist, ylist)

# Initialize grid arrays
Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)
V  = np.zeros_like(X)

# --- Ring / Torus Parameters ---
N_charges = 20        # Number of point charges along the ring
radius = 0.8          # Radius of the ring
charge_value = 1.0    # Magnitude of each charge

angles = np.linspace(0, 2 * np.pi, N_charges, endpoint=False)

for theta in angles:
    x_pos = radius * np.cos(theta)
    y_pos = radius * np.sin(theta)
    q = [x_pos, y_pos, charge_value]
    V, Ex, Ey = addPointCharge2D(V, Ex, Ey, X, Y, q)

# Plotting
fig, ax = plt.subplots(figsize=(7, 6))

# Filled contour plot for potential V
cp = ax.contourf(X, Y, V, levels=50, cmap='seismic')
fig.colorbar(cp, ax=ax, label="Potential V")

# Equipotential lines (Equal potential energy lines)
contour_lines = ax.contour(X, Y, V, levels=20, colors='black', linewidths=0.8)
ax.clabel(contour_lines, inline=True, fontsize=8, fmt='%.1f')  # Label line values

ax.set_title("Equipotential Lines (Scalar Field V)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_aspect('equal')

plt.tight_layout()
plt.show()