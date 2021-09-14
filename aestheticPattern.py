"""

When you have a very specific need in mind, the figures offered by matplotlib might not be of much help to you. All the graphics made by matplotlib consist of basic primitives. When demonstrating how to change the color of a boxplot, most matplotlib plotting functions return collections of lines and shapes.

"""

import matplotlib.pyplot as plt

plt.style.use("dark_background")



N = 20

for i in range(N):

 plt.gca().add_line(plt.Line2D((0, i), (N - i, 0), color = 'r'))

plt.xticks([])

plt.yticks([])

plt.grid(False)

plt.box(False)

plt.axis('scaled')

# Title & Subtitle

plt.title('Aesthetic Patterns', fontsize=15)

plt.figtext(0.84, 0.01, "© Mǟɖ↻ôɖɆⱤ™", color='w', fontsize=9)

plt.show()

plt.savefig('plot.png')
