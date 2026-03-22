"""
vizint.context.target
=====================
Target lines and goal zones for comparing actuals to objectives.
"""

from __future__ import annotations

from typing import Optional

from matplotlib.axes import Axes


def add_target_line(
    ax: Axes,
    value: float,
    color: str = "#16A34A",
    linewidth: float = 1.5,
    linestyle: str = "-",
    alpha: float = 0.9,
    label: Optional[str] = "Target",
    zorder: int = 3,
) -> Axes:
    """Add a horizontal target / goal line.

    Parameters
    ----------
    ax:
        Target axes.
    value:
        Target value (y-position of the line).
    color:
        Line color — defaults to green (positive goal).
    linewidth, linestyle, alpha:
        Visual properties.
    label:
        Legend label.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    ax.axhline(
        value,
        color=color,
        linewidth=linewidth,
        linestyle=linestyle,
        alpha=alpha,
        label=label,
        zorder=zorder,
    )
    return ax


def add_target_zone(
    ax: Axes,
    lower: float,
    upper: float,
    color: str = "#DCFCE7",
    alpha: float = 0.4,
    border_color: str = "#16A34A",
    border_style: str = "--",
    label: Optional[str] = "Target zone",
    zorder: int = 0,
) -> Axes:
    """Shade a target zone band with optional border lines.

    Parameters
    ----------
    ax:
        Target axes.
    lower, upper:
        Vertical bounds of the target zone.
    color:
        Fill color.
    alpha:
        Fill opacity.
    border_color:
        Color for the zone boundary lines.
    border_style:
        Linestyle for boundary lines.
    label:
        Legend label.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    ax.axhspan(lower, upper, color=color, alpha=alpha, label=label, zorder=zorder)
    ax.axhline(lower, color=border_color, linewidth=1.0,
               linestyle=border_style, alpha=0.7, zorder=zorder + 1)
    ax.axhline(upper, color=border_color, linewidth=1.0,
               linestyle=border_style, alpha=0.7, zorder=zorder + 1)
    return ax
