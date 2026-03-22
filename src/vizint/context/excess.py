"""
vizint.context.excess
=====================
Shade excess (over-performance) and deficit (under-performance) regions
relative to a baseline series or scalar.
"""

from __future__ import annotations

from typing import Union

import numpy as np
from matplotlib.axes import Axes


def shade_excess(
    ax: Axes,
    x,
    y,
    baseline: Union[float, np.ndarray],
    color: str = "#BBF7D0",
    alpha: float = 0.4,
    label: str = "Excess",
    zorder: int = 0,
) -> Axes:
    """Fill between *y* and *baseline* where *y* > *baseline*.

    Parameters
    ----------
    ax:
        Target axes.
    x, y:
        Primary data arrays.
    baseline:
        Scalar or array-like reference series.
    color:
        Fill color.
    alpha:
        Fill opacity.
    label:
        Label for the fill patch.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    y_arr = np.asarray(y, dtype=float)
    b_arr = np.full_like(y_arr, baseline) if np.isscalar(baseline) else np.asarray(baseline, dtype=float)
    ax.fill_between(
        x, y_arr, b_arr,
        where=(y_arr > b_arr),
        color=color, alpha=alpha, label=label, zorder=zorder,
    )
    return ax


def shade_deficit(
    ax: Axes,
    x,
    y,
    baseline: Union[float, np.ndarray],
    color: str = "#FECACA",
    alpha: float = 0.4,
    label: str = "Deficit",
    zorder: int = 0,
) -> Axes:
    """Fill between *y* and *baseline* where *y* < *baseline*.

    Parameters
    ----------
    ax:
        Target axes.
    x, y:
        Primary data arrays.
    baseline:
        Scalar or array-like reference series.
    color:
        Fill color.
    alpha:
        Fill opacity.
    label:
        Label for the fill patch.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    y_arr = np.asarray(y, dtype=float)
    b_arr = np.full_like(y_arr, baseline) if np.isscalar(baseline) else np.asarray(baseline, dtype=float)
    ax.fill_between(
        x, y_arr, b_arr,
        where=(y_arr < b_arr),
        color=color, alpha=alpha, label=label, zorder=zorder,
    )
    return ax
