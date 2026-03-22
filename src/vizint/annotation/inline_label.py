"""
vizint.annotation.inline_label
================================
Inline series labeling — label each line at a specified position along the series.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence

import numpy as np
from matplotlib.axes import Axes


def inline_series_labels(
    ax: Axes,
    x,
    series: Dict[str, np.ndarray],
    position: float = 0.85,
    fontsize: int = 9,
    color_map: Optional[Dict[str, str]] = None,
    offset: tuple = (5, 0),
    ha: str = "left",
) -> Axes:
    """Add inline labels to each named series at a given x-fraction.

    Parameters
    ----------
    ax:
        Target axes.
    x:
        Shared x-axis array.
    series:
        Dict mapping series name → y-values.
    position:
        x-position as a fraction of the axis range [0, 1] where labels
        are placed.
    fontsize:
        Label font size.
    color_map:
        Optional dict mapping series name → color.  If ``None``, label
        color matches the last plotted line for that series.
    offset:
        ``(dx, dy)`` annotation offset in display points.
    ha:
        Horizontal alignment.

    Returns
    -------
    Axes
    """
    x_arr = np.asarray(x)
    xlim = ax.get_xlim()
    x_pos = xlim[0] + position * (xlim[1] - xlim[0])

    # Map existing lines by label
    line_colors: Dict[str, str] = {}
    for line in ax.get_lines():
        if line.get_label() and not line.get_label().startswith("_"):
            line_colors[line.get_label()] = line.get_color()

    for name, y in series.items():
        y_arr = np.asarray(y, dtype=float)
        # Interpolate y at x_pos
        idx = int(np.searchsorted(x_arr, x_pos))
        idx = min(max(idx, 0), len(y_arr) - 1)
        y_val = y_arr[idx]

        color = "#333333"
        if color_map and name in color_map:
            color = color_map[name]
        elif name in line_colors:
            color = line_colors[name]

        ax.annotate(
            name,
            xy=(x_arr[idx], y_val),
            xytext=offset,
            textcoords="offset points",
            fontsize=fontsize,
            color=color,
            ha=ha,
            va="center",
            fontweight="bold",
        )
    return ax
