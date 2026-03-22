"""
vizint.perception.focus
=======================
Focus-and-context rendering — emphasise a data range and blur the rest.
"""

from __future__ import annotations

from typing import Optional, Tuple

import matplotlib.patches as mpatches
import numpy as np
from matplotlib.axes import Axes


def focus_on_range(
    ax: Axes,
    xmin: float,
    xmax: float,
    highlight_color: str = "#EFF6FF",
    alpha: float = 0.3,
    border_color: str = "#93C5FD",
    border_linewidth: float = 1.0,
    zorder: int = 0,
) -> Axes:
    """Shade a specific x-range to draw viewer focus.

    Parameters
    ----------
    ax:
        Target axes.
    xmin, xmax:
        Horizontal bounds of the focus region.
    highlight_color:
        Fill color for the highlighted region.
    alpha:
        Fill opacity.
    border_color:
        Color of the vertical border lines.
    border_linewidth:
        Width of border lines.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    ax.axvspan(
        xmin, xmax,
        color=highlight_color, alpha=alpha, zorder=zorder,
    )
    ax.axvline(xmin, color=border_color, linewidth=border_linewidth,
               linestyle="--", alpha=0.7, zorder=zorder + 1)
    ax.axvline(xmax, color=border_color, linewidth=border_linewidth,
               linestyle="--", alpha=0.7, zorder=zorder + 1)
    return ax


def blur_outside_range(
    ax: Axes,
    xmin: float,
    xmax: float,
    blur_color: str = "white",
    blur_alpha: float = 0.55,
    zorder: int = 4,
) -> Axes:
    """Overlay a translucent mask on regions *outside* [xmin, xmax].

    This visually dims the non-focus regions.

    Parameters
    ----------
    ax:
        Target axes.
    xmin, xmax:
        The focus window — regions *outside* will be dimmed.
    blur_color:
        Overlay color.
    blur_alpha:
        Opacity of the overlay (higher = more obscured).
    zorder:
        Draw order for the overlay patches (should be above data).

    Returns
    -------
    Axes
    """
    xlim = ax.get_xlim()
    # Left mask
    if xlim[0] < xmin:
        ax.axvspan(xlim[0], xmin, color=blur_color, alpha=blur_alpha, zorder=zorder)
    # Right mask
    if xmax < xlim[1]:
        ax.axvspan(xmax, xlim[1], color=blur_color, alpha=blur_alpha, zorder=zorder)
    return ax
