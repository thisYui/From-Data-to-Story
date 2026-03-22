"""
vizint.comparison.relative
===========================
Relative and indexed performance charts.
"""

from __future__ import annotations

from typing import Dict, Optional

import numpy as np
from matplotlib.axes import Axes

from vizint.styling.palette import categorical_colors


def index_to_base(
    values: np.ndarray,
    base_index: int = 0,
    scale: float = 100.0,
) -> np.ndarray:
    """Rebase *values* so the value at *base_index* equals *scale*.

    Parameters
    ----------
    values:
        1-D array of values.
    base_index:
        Integer position to use as the base (default: 0 = first element).
    scale:
        Target value at the base index (typically 100).

    Returns
    -------
    np.ndarray
        Rebased array.
    """
    arr = np.asarray(values, dtype=float)
    base = arr[base_index]
    if base == 0:
        raise ValueError("Base value is zero — cannot index to zero.")
    return arr / base * scale


def relative_performance_chart(
    ax: Axes,
    x,
    series: Dict[str, np.ndarray],
    base_index: int = 0,
    scale: float = 100.0,
    palette: str = "default",
    linewidth: float = 2.0,
    legend: bool = True,
    reference_line: bool = True,
    reference_color: str = "#9CA3AF",
) -> Axes:
    """Plot multiple series rebased to 100 at *base_index*.

    Parameters
    ----------
    ax:
        Target axes.
    x:
        Shared x-coordinates.
    series:
        Dict mapping series name → y-values (raw, not yet indexed).
    base_index:
        Position to set as 100.
    scale:
        Base value (default 100).
    palette:
        Named vizint palette.
    linewidth:
        Line width.
    legend:
        Whether to draw a legend.
    reference_line:
        If ``True``, draw a horizontal line at ``scale``.
    reference_color:
        Color of the reference line.

    Returns
    -------
    Axes
    """
    colors = categorical_colors(len(series), palette=palette)
    for (name, y), color in zip(series.items(), colors):
        indexed = index_to_base(np.asarray(y, float), base_index, scale)
        ax.plot(x, indexed, color=color, linewidth=linewidth, label=name)

    if reference_line:
        ax.axhline(scale, color=reference_color, linewidth=1.0,
                   linestyle="--", alpha=0.6, zorder=0)

    if legend:
        ax.legend(frameon=False, fontsize=9)
    return ax
