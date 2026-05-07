"""
Matplotlib plot configuration module
"""

import matplotlib.pyplot as plt

__version__ = "0.1.0"


def plot_config(
    latex=True,
    dpi=600,
    axeslabelsize=8,
    xtickslabelsize=8,
    ytickslabelsize=8,
    titlesize=8,
    legendfontsize=8,
    textfontsize=8,
    tickmajorsize=3,
    tickminorsize=1.5,
    lineswidth=0.5,
):
    """
    Apply common plot settings for Matplotlib.

    Parameters
    ----------
    latex : bool, default=True
        Whether to use LaTeX for text rendering.
    dpi : int, default=600
        Figure DPI.
    axeslabelsize : int, default=8
        Font size for axes labels.
    xtickslabelsize : int, default=8
        Font size for x-axis tick labels.
    ytickslabelsize : int, default=8
        Font size for y-axis tick labels.
    titlesize : int, default=8
        Font size for title.
    legendfontsize : int, default=8
        Font size for legend.
    textfontsize : int, default=8
        General font size.
    tickmajorsize : int, default=3
        Major tick length (in points).
    tickminorsize : float, default=1.5
        Minor tick length (in points).
    lineswidth : float, default=0.5
        Width of axes lines, tick lines, and grid lines.
    """
    if latex:
        plt.rcParams.update(
            {
                "text.usetex": True,
                "font.family": "serif",
                "text.latex.preamble": r"\usepackage{amsmath, bm}",
            }
        )

    plt.rcParams.update(
        {
            "figure.dpi": dpi,
            "axes.labelsize": axeslabelsize,
            "xtick.direction": "in",
            "xtick.labelsize": xtickslabelsize,
            "xtick.top": True,
            "xtick.major.width": lineswidth,
            "xtick.minor.width": lineswidth,
            "xtick.major.size": tickmajorsize,
            "xtick.minor.size": tickminorsize,
            "ytick.direction": "in",
            "ytick.labelsize": ytickslabelsize,
            "ytick.right": True,
            "ytick.major.width": lineswidth,
            "ytick.minor.width": lineswidth,
            "ytick.major.size": tickmajorsize,
            "ytick.minor.size": tickminorsize,
            "legend.fontsize": legendfontsize,
            "axes.linewidth": lineswidth,
            "axes.titlesize": titlesize,
            "grid.linewidth": lineswidth,
            "font.size": textfontsize,
        }
    )
