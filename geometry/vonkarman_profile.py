import numpy as np
import matplotlib.pyplot as plt
import csv
import os

# ============================================================
# Von Karman (LD-Haack) Nosecone Profile Generator
# Author: Praise [Last Name]
# Description: Generates the theoretically optimal nosecone
#              profile for minimum wave drag and exports
#              coordinates for ANSYS SpaceClaim import.
# ============================================================

# --- Geometry Parameters ---
L = 0.300   # Nosecone length in meters (300 mm)
R = 0.050   # Base radius in meters (50 mm)
N = 500     # Number of points along the profile

# --- Von Karman Profile Equations ---
# theta runs from 0 to pi
theta = np.linspace(0, np.pi, N)

x = (L / np.pi) * (theta - np.sin(2 * theta) / 2)
r = R * np.sqrt(theta / np.pi)

# --- Export to CSV for ANSYS SpaceClaim ---
output_path = os.path.join(os.path.dirname(__file__), "vonkarman_profile.csv")

with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x (m)", "r (m)"])
    for xi, ri in zip(x, r):
        writer.writerow([round(xi, 6), round(ri, 6)])

print(f"Profile exported to: {output_path}")
print(f"Total points: {N}")
print(f"Nosecone length: {L*1000:.1f} mm")
print(f"Base radius: {R*1000:.1f} mm")
print(f"Fineness ratio (L/D): {L / (2*R):.2f}")

# --- Plot the Profile ---
fig, ax = plt.subplots(figsize=(10, 4))

# Plot upper and lower profile (mirrored for visual clarity)
ax.plot(x * 1000, r * 1000, color="steelblue", linewidth=2, label="Von Kármán Profile")
ax.plot(x * 1000, -r * 1000, color="steelblue", linewidth=2)
ax.fill_between(x * 1000, r * 1000, -r * 1000, alpha=0.15, color="steelblue")
ax.axhline(0, color="gray", linewidth=0.8, linestyle="--")

# Annotations
ax.annotate("", xy=(L * 1000, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="<->", color="black"))
ax.text(L * 500, 8, f"L = {L*1000:.0f} mm", ha="center", fontsize=9)

ax.set_xlabel("Axial Distance x (mm)")
ax.set_ylabel("Radius r (mm)")
ax.set_title("Von Kármán (LD-Haack) Nosecone Profile\nL = 300 mm | R = 50 mm | Fineness Ratio = 3.0")
ax.legend()
ax.set_aspect("equal")
ax.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()

# Save plot
plot_path = os.path.join(os.path.dirname(__file__), "vonkarman_profile.png")
plt.savefig(plot_path, dpi=150, bbox_inches="tight")
print(f"Plot saved to: {plot_path}")

plt.show()