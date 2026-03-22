"""
vizint.context.reference
========================
Reference lines: means, medians, and custom horizontal/vertical baselines.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
from matplotlib.axes import Axes


def add_reference_line(
    ax: Axes,
    value: float,
    orientation: str = "h",
    color: str = "#374151",
    linewidth: float = 1.2,
    linestyle: str = "--",
    alpha: float = 0.7,
    label: Optional[str] = None,
    zorder: int = 2,
) -> Axes:
    """Add a horizontal or vertical reference line.

    Parameters
    ----------
    ax:
        Target axes.
    value:
        Position of the reference line.
    orientation:
        ``'h'`` for horizontal (constant y) or ``'v'`` for vertical (constant x).
    color, linewidth, linestyle, alpha:
        Line visual properties.
    label:
        Legend label.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    kwargs = dict(color=color, linewidth=linewidth, linestyle=linestyle,
                  alpha=alpha, label=label, zorder=zorder)
    if orientation == "h":
        ax.axhline(value, **kwargs)
    else:
        ax.axvline(value, **kwargs)
    return ax


def add_mean_line(
    ax: Axes,
    y,
    color: str = "#6B7280",
    linewidth: float = 1.2,
    linestyle: str = "--",
    alpha: float = 0.8,
    show_label: bool = True,
) -> Axes:
    """Add the mean of *y* as a horizontal reference line.

    Parameters
    ----------
    ax:
        Target axes.
    y:
        Data array whose mean defines the reference.
    color, linewidth, linestyle, alpha:
        Line visual properties.
    show_label:
        If ``True``, annotate the line with "Mean = {value:.2f}".

    Returns
    -------
    Axes
    """
    mean_val = np.nanmean(y)
    ax.axhline(mean_val, color=color, linewidth=linewidth,
               linestyle=linestyle, alpha=alpha)
    if show_label:
        xlim = ax.get_xlim()
        ax.text(
            xlim[1], mean_val, f" Mean = {mean_val:.2f}",
            va="center", fontsize=9, color=color,
        )
    return ax


def add_median_line(
    ax: Axes,
    y,
    color: str = "#9CA3AF",
    linewidth: float = 1.0,
    linestyle: str = ":",
    alpha: float = 0.8,
    show_label: bool = True,
) -> Axes:
    """Add the median of *y* as a horizontal reference line.

    Parameters
    ----------
    ax:
        Target axes.
    y:
        Data array whose median defines the reference.
    color, linewidth, linestyle, alpha:
        Line visual properties.
    show_label:
        If ``True``, annotate the line with "Median = {value:.2f}".

    Returns
    -------
    Axes
    """
    med_val = np.nanmedian(y)
    ax.axhline(med_val, color=color, linewidth=linewidth,
               linestyle=linestyle, alpha=alpha)
    if show_label:
        xlim = ax.get_xlim()
        ax.text(
            xlim[1], med_val, f" Median = {med_val:.2f}",
            va="center", fontsize=9, color=color,
        )
    return ax
