"""
vizint.comparison.distribution
================================
Distribution comparison: overlaid KDEs, histograms, and ridge plots.
"""

from __future__ import annotations

from typing import Dict, List, Optional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from scipy.stats import gaussian_kde

from vizint.styling.palette import categorical_colors


def compare_distributions(
    ax: Axes,
    groups: Dict[str, np.ndarray],
    palette: str = "default",
    bw_method: Optional[float] = None,
    alpha: float = 0.35,
    linewidth: float = 2.0,
    legend: bool = True,
) -> Axes:
    """Overlay KDE curves for multiple groups on the same axes.

    Parameters
    ----------
    ax:
        Target axes.
    groups:
        Dict mapping group name → 1-D data array.
    palette:
        Named vizint palette.
    bw_method:
        Bandwidth method forwarded to ``scipy.stats.gaussian_kde``.
    alpha:
        Fill opacity under the KDE curves.
    linewidth:
        Line width of KDE outlines.
    legend:
        Whether to draw a legend.

    Returns
    -------
    Axes
    """
    colors = categorical_colors(len(groups), palette=palette)
    for (name, data), color in zip(groups.items(), colors):
        arr = np.asarray(data, dtype=float)
        arr = arr[~np.isnan(arr)]
        if len(arr) < 2:
            continue
        kde = gaussian_kde(arr, bw_method=bw_method)
        xs = np.linspace(arr.min(), arr.max(), 300)
        ys = kde(xs)
        ax.plot(xs, ys, color=color, linewidth=linewidth, label=name)
        ax.fill_between(xs, ys, color=color, alpha=alpha)

    if legend:
        ax.legend(frameon=False, fontsize=9)
    return ax


def ridge_plot(
    groups: Dict[str, np.ndarray],
    overlap: float = 0.4,
    palette: str = "default",
    figsize: Optional[tuple] = None,
    bw_method: Optional[float] = None,
) -> Figure:
    """Create a ridge (joy) plot — stacked, overlapping KDE curves.

    Parameters
    ----------
    groups:
        Ordered dict of group name → array.
    overlap:
        Fraction by which adjacent rows overlap (0 = no overlap, 1 = full).
    palette:
        Named vizint palette.
    figsize:
        Figure size; defaults to ``(10, 0.9 * len(groups))``.
    bw_method:
        Bandwidth for KDE estimation.

    Returns
    -------
    Figure
    """
    n = len(groups)
    if figsize is None:
        figsize = (10, max(3, int(n * 0.9)))

    colors = categorical_colors(n, palette=palette)
    fig, axes = plt.subplots(n, 1, figsize=figsize, sharex=True)
    if n == 1:
        axes = [axes]

    for ax, (name, data), color in zip(axes, groups.items(), colors):
        arr = np.asarray(data, dtype=float)
        arr = arr[~np.isnan(arr)]
        if len(arr) >= 2:
            kde = gaussian_kde(arr, bw_method=bw_method)
            xs = np.linspace(arr.min(), arr.max(), 300)
            ys = kde(xs)
            ax.fill_between(xs, ys, color=color, alpha=0.7)
            ax.plot(xs, ys, color=color, linewidth=1.5)
        ax.set_ylabel(name, rotation=0, labelpad=50, va="center", fontsize=9)
        ax.set_yticks([])
        for spine in ["top", "right", "left"]:
            ax.spines[spine].set_visible(False)

    fig.tight_layout(h_pad=-overlap)
    return fig
