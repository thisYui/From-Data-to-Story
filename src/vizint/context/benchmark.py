"""
vizint.context.benchmark
========================
Benchmark bands and shading relative to a performance reference.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
from matplotlib.axes import Axes


def add_benchmark_band(
    ax: Axes,
    lower: float,
    upper: float,
    color: str = "#FEF3C7",
    alpha: float = 0.4,
    label: Optional[str] = "Benchmark range",
    zorder: int = 0,
) -> Axes:
    """Shade a horizontal band representing the benchmark range.

    Parameters
    ----------
    ax:
        Target axes.
    lower, upper:
        Vertical bounds of the band.
    color:
        Fill color.
    alpha:
        Fill opacity.
    label:
        Legend label.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    ax.axhspan(lower, upper, color=color, alpha=alpha, label=label, zorder=zorder)
    return ax


def shade_above_benchmark(
    ax: Axes,
    x,
    y,
    benchmark: float,
    color: str = "#BBF7D0",
    alpha: float = 0.35,
    zorder: int = 0,
) -> Axes:
    """Shade the region where *y* is **above** the benchmark.

    Parameters
    ----------
    ax:
        Target axes.
    x, y:
        Data arrays.
    benchmark:
        Horizontal threshold.
    color:
        Fill color (typically a positive/good color).
    alpha:
        Fill opacity.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    ax.fill_between(x, y, benchmark, where=(np.asarray(y) >= benchmark),
                    color=color, alpha=alpha, zorder=zorder)
    return ax


def shade_below_benchmark(
    ax: Axes,
    x,
    y,
    benchmark: float,
    color: str = "#FECACA",
    alpha: float = 0.35,
    zorder: int = 0,
) -> Axes:
    """Shade the region where *y* is **below** the benchmark.

    Parameters
    ----------
    ax:
        Target axes.
    x, y:
        Data arrays.
    benchmark:
        Horizontal threshold.
    color:
        Fill color (typically a negative/bad color).
    alpha:
        Fill opacity.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    ax.fill_between(x, y, benchmark, where=(np.asarray(y) <= benchmark),
                    color=color, alpha=alpha, zorder=zorder)
    return ax
