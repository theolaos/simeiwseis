import numpy as np
import matplotlib.pyplot as plt

def addPointCharge2D(V, Ex, Ey, X, Y, q):
    eps = 1e-9  
    r2 = (X - q[0])**2 + (Y - q[1])**2 + eps
    
    Ex += q[2] * (X - q[0]) / (r2**(3/2))
    Ey += q[2] * (Y - q[1]) / (r2**(3/2))
    V  += q[2] / (r2**0.5)
    
    return V, Ex, Ey

# Define spatial domain
xrange = [-1.0, 1.0]
step = 150

xlist = np.linspace(xrange[0], xrange[1], step)
ylist = np.linspace(xrange[0], xrange[1], step)
X, Y = np.meshgrid(xlist, ylist)

# Initialize grid arrays
Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)
V  = np.zeros_like(X)

# Define two charges (Dipole: +5 and -5)
q1 = [-0.4, 0.0,  5.0]  # Positive charge
q2 = [ 0.4, 0.0, -5.0]  # Negative charge

# Add charges to the grid
V, Ex, Ey = addPointCharge2D(V, Ex, Ey, X, Y, q1)
V, Ex, Ey = addPointCharge2D(V, Ex, Ey, X, Y, q2)

# Calculate log magnitude of the electric field strength
E_mag = np.sqrt(Ex**2 + Ey**2)
E_log = np.log(E_mag + 1e-9)

# --- Generate Symmetric Levels for Positive & Negative Potential ---
v_max_abs = np.percentile(np.abs(V), 97)  # Cap extreme values near charges

# Create log-spaced levels for positive and negative values, plus zero
pos_levels = np.geomspace(0.1, v_max_abs, 12)
neg_levels = -pos_levels[::-1]
custom_levels = np.concatenate([neg_levels, [0], pos_levels])

# Create Plots
fig = plt.figure(figsize=(12, 5))

# Plot 1: Electric Field Lines & Intensity
ax1 = fig.add_subplot(121)
ax1.set_title("Electric Field Intensity, ln(E)")
ax1.streamplot(X, Y, Ex, Ey, color='black', linewidth=0.6,
               density=0.8, arrowstyle='->', arrowsize=1.0)
cp1 = ax1.contourf(X, Y, E_log, levels=50, cmap='jet')
fig.colorbar(cp1, ax=ax1)
ax1.set_aspect('equal')

# Plot 2: Dipole Equipotential Lines (Scalar Field V)
ax2 = fig.add_subplot(122)
ax2.set_title("Equipotential Lines (Scalar Field V)")

# Continuous background gradient using symmetric limits
v_bound = np.percentile(np.abs(V), 98)
cp2 = ax2.contourf(X, Y, V, levels=100, cmap='seismic')
# cp2 = ax2.contourf(X, Y, V, levels=200, cmap='seismic', vmin=-v_bound, vmax=v_bound)
fig.colorbar(cp2, ax=ax2)

# Equipotential lines spread symmetrically across positive and negative zones
contour_lines = ax2.contour(X, Y, V, levels=custom_levels, colors='black', linewidths=0.8)
ax2.clabel(contour_lines, inline=True, fontsize=8, fmt='%.1f')

ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_aspect('equal')

plt.tight_layout()
plt.show()