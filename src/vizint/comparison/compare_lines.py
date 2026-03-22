"""
vizint.comparison.compare_lines
================================
Multi-series and before/after line comparison charts.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

from vizint.styling.palette import categorical_colors


def compare_lines(
    ax: Axes,
    x,
    series: Dict[str, np.ndarray],
    palette: str = "default",
    linewidth: float = 2.0,
    alpha: float = 0.9,
    legend: bool = True,
    legend_loc: str = "best",
) -> Axes:
    """Plot multiple named series on the same axes for direct comparison.

    Parameters
    ----------
    ax:
        Target axes.
    x:
        Shared x-axis array.
    series:
        Dict mapping series name → y values.
    palette:
        Named vizint palette to draw colors from.
    linewidth:
        Line width.
    alpha:
        Line opacity.
    legend:
        Whether to draw a legend.
    legend_loc:
        Legend location string.

    Returns
    -------
    Axes
    """
    colors = categorical_colors(len(series), palette=palette)
    for (name, y), color in zip(series.items(), colors):
        ax.plot(x, y, label=name, color=color, linewidth=linewidth, alpha=alpha)
    if legend:
        ax.legend(loc=legend_loc, frameon=False, fontsize=9)
    return ax


def before_after_lines(
    ax: Axes,
    x,
    y_before,
    y_after,
    before_color: str = "#94A3B8",
    after_color: str = "#2563EB",
    before_label: str = "Before",
    after_label: str = "After",
    linewidth: float = 2.0,
    fill: bool = True,
    fill_color: str = "#BFDBFE",
    fill_alpha: float = 0.20,
) -> Axes:
    """Overlay a 'before' and 'after' series with optional difference fill.

    Parameters
    ----------
    ax:
        Target axes.
    x:
        Shared x-coordinates.
    y_before, y_after:
        Before and after value arrays.
    before_color, after_color:
        Line colors.
    before_label, after_label:
        Legend labels.
    linewidth:
        Line width.
    fill:
        If ``True``, shade the area between the two series.
    fill_color:
        Color of the fill between the series.
    fill_alpha:
        Opacity of the fill.

    Returns
    -------
    Axes
    """
    ax.plot(x, y_before, color=before_color, linewidth=linewidth,
            linestyle="--", label=before_label, alpha=0.7)
    ax.plot(x, y_after, color=after_color, linewidth=linewidth,
            label=after_label)
    if fill:
        ax.fill_between(x, y_before, y_after, color=fill_color,
                        alpha=fill_alpha)
    ax.legend(frameon=False, fontsize=9)
    return ax
