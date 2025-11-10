import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 2))

#ТЕЛО
for i in range(10):
    ax.add_patch(plt.Circle((i * 0.4, 0), 0.25, color='green'))

# ГОЛОВА
ax.add_patch(plt.Circle((10 * 0.4, 0), 0.3, color='green'))

# ГЛАЗА
ax.add_patch(plt.Circle((10 * 0.4 + 0.1, 0.08), 0.05, color='white'))
ax.add_patch(plt.Circle((10 * 0.4 + 0.1, -0.08), 0.05, color='white'))
ax.add_patch(plt.Circle((10 * 0.4 + 0.12, 0.08), 0.02, color='black'))
ax.add_patch(plt.Circle((10 * 0.4 + 0.12, -0.08), 0.02, color='black'))

# ЯЗЫК
ax.plot([10 * 0.4 + 0.3, 10 * 0.4 + 0.45], [0, 0], color='red', linewidth=2)
ax.plot([10 * 0.4 + 0.45, 10 * 0.4 + 0.5], [0, 0.05], color='red', linewidth=2)
ax.plot([10 * 0.4 + 0.45, 10 * 0.4 + 0.5], [0, -0.05], color='red', linewidth=2)

ax.set_aspect('equal')
ax.axis('off')
plt.show()
