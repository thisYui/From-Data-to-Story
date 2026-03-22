"""
vizint.perception.fade
======================
Functions for reducing the visual weight of background series.
"""

from __future__ import annotations

from typing import Optional, Sequence

import matplotlib.pyplot as plt
from matplotlib.axes import Axes


def fade_series(
    ax: Axes,
    x,
    y,
    color: str = "#94A3B8",
    linewidth: float = 1.0,
    alpha: float = 0.3,
    zorder: int = 1,
    label: Optional[str] = None,
    **kwargs,
) -> Axes:
    """Draw a faded (background) line series on *ax*.

    Parameters
    ----------
    ax:
        Target axes.
    x, y:
        Data arrays.
    color:
        Line color (typically muted grey).
    linewidth:
        Line width in points.
    alpha:
        Opacity — keep below 0.5 for background effect.
    zorder:
        Draw order — keep low so faded lines sit behind signals.
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


def fade_background_lines(
    ax: Axes,
    alpha: float = 0.2,
    color: Optional[str] = None,
) -> Axes:
    """Fade all existing lines in *ax* to background level.

    Useful after plotting all series: call this to background them all,
    then re-draw the signal series on top.

    Parameters
    ----------
    ax:
        Target axes.
    alpha:
        Target opacity for all lines.
    color:
        If provided, also recolor all lines to this color.

    Returns
    -------
    Axes
    """
    for line in ax.get_lines():
        line.set_alpha(alpha)
        line.set_zorder(1)
        if color is not None:
            line.set_color(color)
    return ax
