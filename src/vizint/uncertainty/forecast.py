"""
vizint.uncertainty.forecast
============================
Utilities for shading forecast periods and distinguishing actuals from
projected values.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
from matplotlib.axes import Axes


def shade_forecast_period(
    ax: Axes,
    x_start: float,
    color: str = "#F5F3FF",
    alpha: float = 0.5,
    label: Optional[str] = "Forecast",
    linecolor: str = "#7C3AED",
    linestyle: str = "--",
    linewidth: float = 1.0,
    zorder: int = 0,
) -> Axes:
    """Shade the forecast region from *x_start* to the right axis limit.

    Parameters
    ----------
    ax:
        Target axes.
    x_start:
        x-coordinate where the forecast begins.
    color:
        Shading fill color.
    alpha:
        Fill opacity.
    label:
        Legend label displayed by the shaded patch.
    linecolor:
        Color of the vertical dividing line at *x_start*.
    linestyle, linewidth:
        Properties of the dividing line.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    xlim = ax.get_xlim()
    ax.axvspan(x_start, xlim[1], color=color, alpha=alpha,
               label=label, zorder=zorder)
    ax.axvline(x_start, color=linecolor, linewidth=linewidth,
               linestyle=linestyle, alpha=0.85, zorder=zorder + 1)
    return ax


def add_forecast_region(
    ax: Axes,
    x,
    y_central,
    lower,
    upper,
    central_color: str = "#7C3AED",
    band_color: str = "#C4B5FD",
    central_linewidth: float = 2.0,
    band_alpha: float = 0.20,
    linestyle: str = "--",
    label: Optional[str] = "Forecast",
    zorder: int = 3,
) -> Axes:
    """Plot a forecast central line and uncertainty band together.

    Parameters
    ----------
    ax:
        Target axes.
    x:
        x-coordinates for the forecast period.
    y_central:
        Central forecast values.
    lower, upper:
        Uncertainty band bounds.
    central_color:
        Color of the central forecast line.
    band_color:
        Color of the uncertainty fill.
    central_linewidth:
        Width of the central line.
    band_alpha:
        Opacity of the uncertainty fill.
    linestyle:
        Line style for the forecast line.
    label:
        Legend label.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    ax.fill_between(x, lower, upper, color=band_color, alpha=band_alpha, zorder=zorder)
    ax.plot(x, y_central, color=central_color, linewidth=central_linewidth,
            linestyle=linestyle, label=label, zorder=zorder + 1)
    return ax
