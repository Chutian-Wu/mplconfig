# mplconfig

A tiny Python package that provides a single function `plot_config()` to apply consistent, publication‑ready Matplotlib settings across all your projects.

## Features

- One‑line configuration of figure DPI, font sizes, tick directions, line widths, etc.
- Optional LaTeX text rendering (with `amsmath` and `bm` packages).
- Works on any device with Matplotlib and Tex

## Requirements

- Python ≥ 3.6
- Matplotlib ≥ 3.0.0
- **LaTeX** (if you use `latex=True`) – e.g., TeX Live, MiKTeX, or MacTeX.  
  *If LaTeX is not installed, set `latex=False` to avoid errors.*

## Installation

You can install directly from GitHub (recommended):
```bash
pip install git+https://github.com/Chutian-Wu/mplconfig.git
```

Or clone and install locally:
```bash
git clone https://github.com/Chutian-Wu/mplconfig.git
cd mplconfig
pip install .
```

## Usage
```Python
import numpy as np
import matplotlib.pyplot as plt
from mplconfig import plot_config

# Apply your preferred settings
plot_config(latex=True)

# Now create plots as usual
fig, ax = plt.subplots(figsize=(3, 2))
x = np.linspace(0, np.pi * 2, 101)
y = np.exp(np.sin(x))
ax.plot(x / np.pi, y)
ax.set(
    xlabel=r"$x/\pi$",
    ylabel=r"$e^{\sin x}$",
    xlim=(0, 2),
    ylim=(0, 3),
    xticks=np.linspace(0, 2, 3),
    yticks=np.linspace(0, 3, 4),
);
```
