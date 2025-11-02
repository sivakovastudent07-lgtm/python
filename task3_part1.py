import matplotlib.pyplot as plt
import matplotlib.patches as patches #для геометрических фигур

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.set_aspect('equal')
ax.axis('off')

# ГОЛОВА
head = patches.Circle((5, 4), radius=1.2)
ax.add_patch(head)
# ТЕЛО
body_parts = [
    patches.Ellipse((5, 2.5), width=1.5, height=1.0, angle=0, fill=False),
    patches.Ellipse((5, 1.5), width=1.5, height=1.0, angle=0, fill=False),
    patches.Ellipse((5, 0.5), width=1.5, height=1.0, angle=0, fill=False),
]

for part in body_parts:
    ax.add_patch(part)
# ХВОСТ
tail = patches.Polygon([[5, 0.2], [5.2, 0.0], [4.8, 0.0]], fill=False)
ax.add_patch(tail)


plt.show()