"""
vizint.annotation.direct_label
================================
Direct labeling: label line endpoints, maxima, and minima directly on the chart.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
from matplotlib.axes import Axes


def label_last_point(
    ax: Axes,
    x,
    y,
    text: Optional[str] = None,
    fmt: str = "{:.2f}",
    color: str = "#1a1a1a",
    fontsize: int = 9,
    offset_x: float = 5,
    offset_y: float = 0,
    ha: str = "left",
    va: str = "center",
) -> Axes:
    """Label the last data point of a series.

    Useful for replacing legends with direct series labels.

    Parameters
    ----------
    ax:
        Target axes.
    x, y:
        Data arrays.
    text:
        Custom label text. If ``None``, formats the last y-value using *fmt*.
    fmt:
        Format string for the automatic label value.
    color:
        Label text color.
    fontsize:
        Label font size.
    offset_x, offset_y:
        Offset in display points from the data point.
    ha, va:
        Horizontal / vertical alignment.

    Returns
    -------
    Axes
    """
    x_last = np.asarray(x)[-1]
    y_last = np.asarray(y, dtype=float)[-1]
    label_text = text if text is not None else fmt.format(y_last)
    ax.annotate(
        label_text,
        xy=(x_last, y_last),
        xytext=(offset_x, offset_y),
        textcoords="offset points",
        fontsize=fontsize,
        color=color,
        ha=ha,
        va=va,
    )
    return ax


def label_max(
    ax: Axes,
    x,
    y,
    text: Optional[str] = None,
    fmt: str = "Max: {:.2f}",
    color: str = "#16A34A",
    fontsize: int = 9,
    offset: tuple = (0, 10),
    ha: str = "center",
) -> Axes:
    """Label the maximum value of *y*.

    Parameters
    ----------
    ax:
        Target axes.
    x, y:
        Data arrays.
    text:
        Custom label.  If ``None``, formats the max value using *fmt*.
    fmt:
        Format string for the automatic label.
    color:
        Label color.
    fontsize:
        Font size.
    offset:
        ``(dx, dy)`` in display points.
    ha:
        Horizontal alignment.

    Returns
    -------
    Axes
    """
    y_arr = np.asarray(y, dtype=float)
    x_arr = np.asarray(x)
    idx = int(np.nanargmax(y_arr))
    label_text = text if text is not None else fmt.format(y_arr[idx])
    ax.annotate(
        label_text,
        xy=(x_arr[idx], y_arr[idx]),
        xytext=offset,
        textcoords="offset points",
        fontsize=fontsize,
        color=color,
        ha=ha,
        va="bottom",
    )
    return ax


def label_min(
    ax: Axes,
    x,
    y,
    text: Optional[str] = None,
    fmt: str = "Min: {:.2f}",
    color: str = "#DC2626",
    fontsize: int = 9,
    offset: tuple = (0, -10),
    ha: str = "center",
) -> Axes:
    """Label the minimum value of *y*.

    Parameters
    ----------
    ax:
        Target axes.
    x, y:
        Data arrays.
    text:
        Custom label.
    fmt:
        Format string.
    color:
        Label color.
    fontsize:
        Font size.
    offset:
        ``(dx, dy)`` in display points.
    ha:
        Horizontal alignment.

    Returns
    -------
    Axes
    """
    y_arr = np.asarray(y, dtype=float)
    x_arr = np.asarray(x)
    idx = int(np.nanargmin(y_arr))
    label_text = text if text is not None else fmt.format(y_arr[idx])
    ax.annotate(
        label_text,
        xy=(x_arr[idx], y_arr[idx]),
        xytext=offset,
        textcoords="offset points",
        fontsize=fontsize,
        color=color,
        ha=ha,
        va="top",
    )
    return ax
