"""
vizint.perception.highlight
===========================
Functions for visually emphasising signals within a chart.
"""

from __future__ import annotations

from typing import Optional, Sequence, Tuple, Union

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes


def highlight_series(
    ax: Axes,
    x,
    y,
    color: str = "#2563EB",
    linewidth: float = 2.5,
    alpha: float = 1.0,
    zorder: int = 5,
    label: Optional[str] = None,
    **kwargs,
) -> Axes:
    """Draw a highlighted (primary) line series on *ax*.

    Parameters
    ----------
    ax:
        Target axes.
    x, y:
        Data arrays.
    color:
        Line color.
    linewidth:
        Line width in points.
    alpha:
        Opacity.
    zorder:
        Draw order.
    label:
        Legend label.
    **kwargs:
        Forwarded to ``ax.plot``.

    Returns
    -------
    Axes
    """
    ax.plot(
        x, y,
        color=color,
        linewidth=linewidth,
        alpha=alpha,
        zorder=zorder,
        label=label,
        **kwargs,
    )
    return ax


def highlight_region(
    ax: Axes,
    xmin: float,
    xmax: float,
    color: str = "#FEF9C3",
    alpha: float = 0.4,
    zorder: int = 0,
    label: Optional[str] = None,
) -> Axes:
    """Shade a vertical region on the x-axis to draw attention.

    Parameters
    ----------
    ax:
        Target axes.
    xmin, xmax:
        Horizontal span bounds.
    color:
        Fill color.
    alpha:
        Opacity.
    zorder:
        Draw order.
    label:
        Patch label for the legend.

    Returns
    -------
    Axes
    """
    ax.axvspan(xmin, xmax, color=color, alpha=alpha, zorder=zorder, label=label)
    return ax


def highlight_points(
    ax: Axes,
    x,
    y,
    color: str = "#DC2626",
    size: float = 60,
    marker: str = "o",
    zorder: int = 6,
    edgecolor: str = "white",
    linewidths: float = 1.5,
    label: Optional[str] = None,
    **kwargs,
) -> Axes:
    """Plot a scatter of highlighted points (e.g. peaks, events).

    Parameters
    ----------
    ax:
        Target axes.
    x, y:
        Data coordinates.
    color:
        Marker face color.
    size:
        Marker area in points².
    marker:
        Marker style string.
    zorder:
        Draw order.
    edgecolor:
        Marker edge color.
    linewidths:
        Marker edge linewidth.
    label:
        Legend label.

    Returns
    -------
    Axes
    """
    ax.scatter(
        x, y,
        c=color,
        s=size,
        marker=marker,
        zorder=zorder,
        edgecolors=edgecolor,
        linewidths=linewidths,
        label=label,
        **kwargs,
    )
    return ax
