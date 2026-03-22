"""
vizint.perception.outlier
=========================
Outlier detection and visual emphasis utilities.
"""

from __future__ import annotations

from typing import Optional, Tuple

import numpy as np
from matplotlib.axes import Axes
from scipy import stats


def detect_and_mark_outliers(
    ax: Axes,
    x,
    y,
    method: str = "iqr",
    threshold: float = 1.5,
    marker_color: str = "#DC2626",
    marker: str = "X",
    size: float = 100,
    edgecolor: str = "white",
    linewidths: float = 1.0,
    zorder: int = 7,
    label: Optional[str] = None,
) -> Axes:
    """Detect and visually mark outliers in a series.

    Parameters
    ----------
    ax:
        Target axes.
    x:
        x-coordinates.
    y:
        y-values used for outlier detection.
    method:
        Detection method: ``'iqr'`` (Tukey) or ``'zscore'``.
    threshold:
        IQR multiplier (default 1.5) or z-score threshold (e.g. 3.0).
    marker_color:
        Color for outlier markers.
    marker:
        Marker style.
    size:
        Marker area in points².
    edgecolor:
        Marker edge color.
    linewidths:
        Marker edge linewidth.
    zorder:
        Draw order.
    label:
        Legend label for outlier markers.

    Returns
    -------
    Axes
    """
    y_arr = np.asarray(y, dtype=float)
    x_arr = np.asarray(x)
    mask = _outlier_mask(y_arr, method, threshold)

    if mask.any():
        ax.scatter(
            x_arr[mask], y_arr[mask],
            c=marker_color,
            s=size,
            marker=marker,
            edgecolors=edgecolor,
            linewidths=linewidths,
            zorder=zorder,
            label=label,
        )
    return ax


def emphasize_outliers(
    ax: Axes,
    x,
    y,
    method: str = "iqr",
    threshold: float = 1.5,
    ring_color: str = "#FCA5A5",
    ring_size: float = 250,
    zorder: int = 6,
) -> Axes:
    """Add faint rings around outliers to attract attention.

    Parameters
    ----------
    ax:
        Target axes.
    x, y:
        Data arrays.
    method:
        Detection method: ``'iqr'`` or ``'zscore'``.
    threshold:
        Threshold for outlier detection.
    ring_color:
        Ring fill color.
    ring_size:
        Ring marker area.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    y_arr = np.asarray(y, dtype=float)
    x_arr = np.asarray(x)
    mask = _outlier_mask(y_arr, method, threshold)

    if mask.any():
        ax.scatter(
            x_arr[mask], y_arr[mask],
            c=ring_color,
            s=ring_size,
            alpha=0.4,
            edgecolors="none",
            zorder=zorder,
        )
    return ax


# ---------------------------------------------------------------------------
# Internals
# ---------------------------------------------------------------------------

def _outlier_mask(y: np.ndarray, method: str, threshold: float) -> np.ndarray:
    """Return a boolean mask where ``True`` indicates an outlier."""
    if method == "iqr":
        q1, q3 = np.nanpercentile(y, [25, 75])
        iqr = q3 - q1
        lower = q1 - threshold * iqr
        upper = q3 + threshold * iqr
        return (y < lower) | (y > upper)
    elif method == "zscore":
        z = np.abs(stats.zscore(y, nan_policy="omit"))
        return z > threshold
    else:
        raise ValueError(f"Unknown method '{method}'. Use 'iqr' or 'zscore'.")
