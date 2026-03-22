"""
vizint.uncertainty.confidence_band
===================================
Confidence band overlays for time series and regression models.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
from matplotlib.axes import Axes


def add_confidence_band(
    ax: Axes,
    x,
    y,
    lower,
    upper,
    color: str = "#93C5FD",
    alpha: float = 0.25,
    line_color: Optional[str] = None,
    line_alpha: float = 0.4,
    label: Optional[str] = "Confidence interval",
    zorder: int = 1,
) -> Axes:
    """Shade a confidence band between *lower* and *upper*.

    Parameters
    ----------
    ax:
        Target axes.
    x:
        x-coordinates (shared for all arrays).
    y:
        Central estimate series (plotted if *line_color* provided).
    lower, upper:
        Lower and upper bound arrays.
    color:
        Fill color.
    alpha:
        Fill opacity.
    line_color:
        If provided, draws boundary lines in this color.
    line_alpha:
        Opacity of boundary lines.
    label:
        Patch label for the legend.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    ax.fill_between(x, lower, upper, color=color, alpha=alpha,
                    label=label, zorder=zorder)
    if line_color is not None:
        ax.plot(x, lower, color=line_color, linewidth=0.8,
                alpha=line_alpha, zorder=zorder + 1)
        ax.plot(x, upper, color=line_color, linewidth=0.8,
                alpha=line_alpha, zorder=zorder + 1)
    return ax
