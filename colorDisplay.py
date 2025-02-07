import matplotlib.pyplot as plt
from palette import rgb_list

#normalize the RGB values to be between 0 and 1 for matplotlib
colors_normalized = [(r/255, g/255, b/255) for r, g, b in rgb_list]

plt.figure(figsize=(5, 1))

for i, color in enumerate(colors_normalized):
    plt.fill_between([i, i+1], 0, 1, color=color)

plt.axis('off')

plt.show()
