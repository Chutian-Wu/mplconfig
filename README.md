# mplconfig

A tiny Python package that provides a single function `plot_config()` to apply consistent, publication‑ready Matplotlib settings across all your projects.

## Features

- One‑line configuration of figure DPI, font sizes, tick directions, line widths, etc.
- Optional LaTeX text rendering (with `amsmath` and `bm` packages).
- Works on any device with Matplotlib.

## Installation

```bash
pip install git https://github.com/Chutian-Wu/mplconfig.git   # from git
```

## Usage
```Python
import matplotlib.pyplot as plt
from mplconfig import plot_config

# Apply your preferred settings
plot_config(latex=True)

# Now create plots as usual
fig,ax=plt.subplots()
x=np.linspace(0,np.pi*2,101)
y=np.exp(np.sin(x))
ax.plot(x,y)
ax.set(xlabel=r'$x$,ylabel=r'$e^{\sin x}$)
```
