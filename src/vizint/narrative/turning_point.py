"""
vizint.narrative.turning_point
==============================
Detect and visualise turning points (local extrema) in time series.
"""

from __future__ import annotations

from typing import Optional, Tuple

import numpy as np
from matplotlib.axes import Axes
from scipy.signal import argrelextrema


def detect_local_extrema(
    y,
    order: int = 5,
) -> Tuple[np.ndarray, np.ndarray]:
    """Return indices of local maxima and minima in *y*.

    Parameters
    ----------
    y:
        1-D array of values.
    order:
        How many surrounding points each candidate point must surpass.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        ``(maxima_indices, minima_indices)``.
    """
    y_arr = np.asarray(y, dtype=float)
    maxima = argrelextrema(y_arr, np.greater, order=order)[0]
    minima = argrelextrema(y_arr, np.less, order=order)[0]
    return maxima, minima


def mark_turning_points(
    ax: Axes,
    x,
    y,
    order: int = 5,
    max_color: str = "#16A34A",
    min_color: str = "#DC2626",
    size: float = 80,
    alpha: float = 0.9,
    show_labels: bool = True,
    label_fontsize: int = 8,
    zorder: int = 6,
) -> Axes:
    """Detect and mark local maxima / minima on *ax*.

    Parameters
    ----------
    ax:
        Target axes.
    x, y:
        Data arrays.
    order:
        Sensitivity of extrema detection.
    max_color:
        Color for local maxima markers.
    min_color:
        Color for local minima markers.
    size:
        Marker area in points².
    alpha:
        Marker opacity.
    show_labels:
        If ``True``, annotate each turning point with its value.
    label_fontsize:
        Font size for value labels.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    x_arr = np.asarray(x)
    y_arr = np.asarray(y, dtype=float)
    maxima, minima = detect_local_extrema(y_arr, order=order)

    if len(maxima):
        ax.scatter(x_arr[maxima], y_arr[maxima], c=max_color, s=size,
                   zorder=zorder, edgecolors="white", linewidths=1.2, alpha=alpha)
        if show_labels:
            for i in maxima:
                ax.annotate(
                    f"{y_arr[i]:.2f}",
                    xy=(x_arr[i], y_arr[i]),
                    xytext=(0, 8), textcoords="offset points",
                    ha="center", fontsize=label_fontsize, color=max_color,
                )

    if len(minima):
        ax.scatter(x_arr[minima], y_arr[minima], c=min_color, s=size,
                   zorder=zorder, edgecolors="white", linewidths=1.2, alpha=alpha,
                   marker="v")
        if show_labels:
            for i in minima:
                ax.annotate(
                    f"{y_arr[i]:.2f}",
                    xy=(x_arr[i], y_arr[i]),
                    xytext=(0, -12), textcoords="offset points",
                    ha="center", fontsize=label_fontsize, color=min_color,
                )

    return ax
