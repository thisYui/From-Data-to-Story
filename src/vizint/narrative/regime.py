"""
vizint.narrative.regime
=======================
Shade and label distinct regimes (phases) in a time series chart.
"""

from __future__ import annotations

from typing import List, Optional, Sequence, Tuple

import numpy as np
from matplotlib.axes import Axes


def shade_regimes(
    ax: Axes,
    breakpoints: Sequence[float],
    colors: Optional[Sequence[str]] = None,
    alpha: float = 0.12,
    zorder: int = 0,
) -> Axes:
    """Shade alternating regime bands defined by *breakpoints*.

    Parameters
    ----------
    ax:
        Target axes.
    breakpoints:
        Sorted x-axis breakpoints that delimit regime boundaries.
        The x-axis limits define the first and last edges.
    colors:
        List of fill colors cycling across regimes.
        Defaults to alternating light blue / light grey.
    alpha:
        Fill opacity.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    if colors is None:
        colors = ["#EFF6FF", "#F1F5F9"]

    xlim = ax.get_xlim()
    edges = [xlim[0]] + list(breakpoints) + [xlim[1]]

    for i in range(len(edges) - 1):
        ax.axvspan(
            edges[i], edges[i + 1],
            color=colors[i % len(colors)],
            alpha=alpha,
            zorder=zorder,
        )
    return ax


def add_regime_labels(
    ax: Axes,
    breakpoints: Sequence[float],
    labels: Sequence[str],
    y_position: float = 0.97,
    fontsize: int = 9,
    color: str = "#6B7280",
    va: str = "top",
    ha: str = "center",
) -> Axes:
    """Add text labels to regime bands.

    Parameters
    ----------
    ax:
        Target axes.
    breakpoints:
        Sorted x-axis breakpoints (same as those passed to
        :func:`shade_regimes`).
    labels:
        Text label for each regime.  Should have
        ``len(labels) == len(breakpoints) + 1``.
    y_position:
        Vertical position in *axes fraction* (0 = bottom, 1 = top).
    fontsize:
        Label font size.
    color:
        Label text color.
    va, ha:
        Vertical / horizontal alignment.

    Returns
    -------
    Axes
    """
    xlim = ax.get_xlim()
    edges = [xlim[0]] + list(breakpoints) + [xlim[1]]

    for i, label in enumerate(labels):
        mid = (edges[i] + edges[i + 1]) / 2
        ax.text(
            mid, y_position, label,
            transform=ax.get_xaxis_transform(),
            fontsize=fontsize,
            color=color,
            va=va,
            ha=ha,
            alpha=0.8,
        )
    return ax
