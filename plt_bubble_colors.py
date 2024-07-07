import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mycolorpy import colorlist as mcp

rng = np.random.default_rng() # random number range

num_maps = len(plt.colormaps()) # 164 max
num_bubbles = 132
num_colors = 8
num_sizes = 8
size_step = 16
plot_width = 12
plot_height = 2.5

plt.style.use('dark_background')
fig, axes = plt.subplots(num_maps, 1, figsize=(plot_width, num_maps*plot_height))

for i, color_scale in enumerate(plt.colormaps()[:num_maps]):

    # Data
    x = np.random.normal(0, 3, num_bubbles).round(3)                                # +/-3 std from 0rigin
    y = np.random.normal(0, 3, num_bubbles).round(3)                                # +/-3 std from 0rigin
    sizes = (rng.integers(num_sizes, size=num_bubbles).astype('int') + 1)*size_step # size_step to size_step*num_sizes
    colors = rng.integers(num_colors, size=num_bubbles).astype('int')               # 0 to num_bubbles

    # Frame
    df = pd.DataFrame([x, y, sizes, colors]).T
    df.columns = ['Distance', 'Height', 'Size', 'Color']

    # Color
    scale_colors = dict(zip(range(num_colors), 
                            mcp.gen_color(cmap=color_scale, n=num_colors)))
    df['Color'] = df['Color'].map(scale_colors)

    # Plot
    axes[i].scatter(df.iloc[:,0], df.iloc[:,1], df.iloc[:,2], df.iloc[:,3])
    axes[i].spines[:].set_visible(False)
    axes[i].set_xticks([])
    axes[i].set_yticks([])
    axes[i].set_title(color_scale, loc='left')

#plt.savefig("colormaps.jpg",bbox_inches='tight')