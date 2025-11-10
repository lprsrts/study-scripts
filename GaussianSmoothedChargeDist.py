# Gradient vector fields overlaid on the two previously discussed scalar fields:
# (1) Impulse-like Dirac-delta visualization of 10 point charges
# (2) Gaussian-smoothed charge density

import numpy as np
import matplotlib.pyplot as plt

# Recreate domain and random charges (same seed for reproducibility)
rng = np.random.default_rng(42)
xmin, xmax, ymin, ymax = -5.0, 5.0, -5.0, 5.0
nx, ny = 300, 300
x = np.linspace(xmin, xmax, nx)
y = np.linspace(ymin, ymax, ny)
X, Y = np.meshgrid(x, y, indexing="xy")
dx = (xmax - xmin) / (nx - 1)
dy = (ymax - ymin) / (ny - 1)

N = 10
px = rng.uniform(xmin+0.5, xmax-0.5, size=N)
py = rng.uniform(ymin+0.5, ymax-0.5, size=N)
q = rng.choice([-1.0, 1.0], size=N)

# --- (1) Dirac-delta-like image on grid ---
delta_img = np.zeros((ny, nx), dtype=float)
ix = np.clip(((px - xmin) / (xmax - xmin) * (nx - 1)).astype(int), 0, nx - 1)
iy = np.clip(((py - ymin) / (ymax - ymin) * (ny - 1)).astype(int), 0, ny - 1)
for k in range(N):
    delta_img[iy[k], ix[k]] += q[k] * (nx * ny)

# Gradient of the delta image
Gy_delta, Gx_delta = np.gradient(delta_img, dy, dx)

# Downsample for quiver so it's readable
step = 12
Xq = X[::step, ::step]
Yq = Y[::step, ::step]

Ux = Gx_delta[::step, ::step]
Uy = Gy_delta[::step, ::step]
mag = np.hypot(Ux, Uy)
# Normalize to show directions clearly; avoid division by zero
eps = 1e-12
Ux_n = np.where(mag > eps, Ux / (mag + eps), 0.0)
Uy_n = np.where(mag > eps, Uy / (mag + eps), 0.0)

plt.figure(figsize=(7,7))
plt.imshow(delta_img, extent=[xmin, xmax, ymin, ymax], origin="lower", aspect="equal")
plt.quiver(Xq, Yq, Ux_n, Uy_n, angles="xy", scale_units="xy", scale=0.35, width=0.002)
plt.scatter(px, py, s=30, marker='o')
plt.title("Dirac-Delta Görselleştirmesi + ∇(delta-img) Yönleri")
plt.xlabel("x"); plt.ylabel("y")
plt.tight_layout()
plt.show()

# --- (2) Gaussian-smoothed density ---
sigma = 0.9
norm = 1.0 / (2.0 * np.pi * sigma**2)
rho = np.zeros_like(X)
for k in range(N):
    dxk = X - px[k]
    dyk = Y - py[k]
    rho += q[k] * norm * np.exp(-(dxk*dxk + dyk*dyk) / (2.0 * sigma**2))

# Gradient of smoothed density
Gy_rho, Gx_rho = np.gradient(rho, dy, dx)

# Downsample and normalize for quiver
Ux2 = Gx_rho[::step, ::step]
Uy2 = Gy_rho[::step, ::step]
mag2 = np.hypot(Ux2, Uy2)
Ux2_n = np.where(mag2 > eps, Ux2 / (mag2 + eps), 0.0)
Uy2_n = np.where(mag2 > eps, Uy2 / (mag2 + eps), 0.0)

plt.figure(figsize=(7,7))
plt.imshow(rho, extent=[xmin, xmax, ymin, ymax], origin="lower", aspect="equal")
plt.quiver(Xq, Yq, Ux2_n, Uy2_n, angles="xy", scale_units="xy", scale=0.35, width=0.002)
plt.title("Gauss Pürüzsüzleştirilmiş ρ(x,y) + ∇ρ Vektör Alanı (Yönler)")
plt.xlabel("x"); plt.ylabel("y")
plt.colorbar(label="ρ(x,y)")
plt.tight_layout()
plt.show()
