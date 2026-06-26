import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Von Karman Nosecone CFD Results — Drag Coefficient vs Mach
# ============================================================

mach = [0.3, 0.8, 1.5]

cd_pressure = [0.617, 0.698, 0.729]
cd_viscous  = [0.027, 0.022, 0.019]
cd_total    = [0.644, 0.720, 0.749]

fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(mach, cd_total,    'o-',  color='steelblue',  linewidth=2.5, markersize=8, label='Total $C_d$')
ax.plot(mach, cd_pressure, 's--', color='firebrick',  linewidth=2,   markersize=7, label='Pressure $C_d$')
ax.plot(mach, cd_viscous,  '^:',  color='seagreen',   linewidth=2,   markersize=7, label='Viscous $C_d$')

# Annotate each total Cd point
for m, cd in zip(mach, cd_total):
    ax.annotate(f'{cd:.3f}', xy=(m, cd), xytext=(0, 12),
                textcoords='offset points', ha='center', fontsize=9)

# Transonic region shading
ax.axvspan(0.8, 1.2, alpha=0.08, color='orange', label='Transonic region')
ax.axvline(x=1.0, color='gray', linestyle='--', linewidth=1, alpha=0.6)
ax.text(1.01, 0.73, 'M = 1.0', fontsize=8, color='gray')

ax.set_xlabel('Mach Number', fontsize=12)
ax.set_ylabel('Drag Coefficient $C_d$', fontsize=12)
ax.set_title('Von Kármán Nosecone — Drag Coefficient vs Mach Number\n'
             'L = 300 mm | R = 50 mm | Fineness Ratio = 3.0 | 2D Axisymmetric RANS',
             fontsize=11)
ax.legend(fontsize=10)
ax.set_xlim(0.1, 1.7)
ax.set_ylim(0.0, 0.85)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()

plt.savefig('plots/cd_vs_mach.png', dpi=150, bbox_inches='tight')
print("Plot saved to results/plots/cd_vs_mach.png")
plt.show()