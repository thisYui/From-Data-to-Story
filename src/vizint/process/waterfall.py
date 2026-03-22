"""
vizint.process.waterfall
========================
Waterfall (bridge) chart for cumulative contribution analysis.
"""

from __future__ import annotations

from typing import List, Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import Patch


def waterfall_chart(
    ax: Axes,
    labels: Sequence[str],
    values: Sequence[float],
    positive_color: str = "#16A34A",
    negative_color: str = "#DC2626",
    total_color: str = "#2563EB",
    total_indices: Optional[Sequence[int]] = None,
    bar_width: float = 0.6,
    show_values: bool = True,
    value_fontsize: int = 9,
    connector_color: str = "#9CA3AF",
    edgecolor: str = "white",
    linewidth: float = 0.8,
) -> Axes:
    """Draw a waterfall (bridge) chart.

    Parameters
    ----------
    ax:
        Target axes.
    labels:
        Category labels for each bar.
    values:
        Signed values for each step.  Positive values extend upward,
        negative values downward.
    positive_color:
        Color for positive-change bars.
    negative_color:
        Color for negative-change bars.
    total_color:
        Color for total / subtotal bars.
    total_indices:
        Indices of bars that represent totals (plotted from 0, not stacked).
        The last bar is automatically treated as a total.
    bar_width:
        Bar width (fraction of available space).
    show_values:
        If ``True``, display the signed value above/below each bar.
    value_fontsize:
        Font size of value labels.
    connector_color:
        Color of horizontal connector lines between bars.
    edgecolor:
        Bar edge color.
    linewidth:
        Bar edge line width.

    Returns
    -------
    Axes
    """
    n = len(values)
    vals = np.array(values, dtype=float)

    if total_indices is None:
        total_indices = [n - 1]
    total_set = set(total_indices)

    running = 0.0
    bottoms = []
    heights = []
    colors = []

    for i, v in enumerate(vals):
        if i in total_set:
            bottoms.append(0.0)
            heights.append(float(np.sum(vals[:i]) if i == n - 1 else v))
            colors.append(total_color)
        else:
            bottoms.append(running)
            heights.append(v)
            colors.append(positive_color if v >= 0 else negative_color)
            running += v

    x = np.arange(n)
    bars = ax.bar(
        x, heights, bottom=bottoms,
        color=colors, width=bar_width,
        edgecolor=edgecolor, linewidth=linewidth,
    )

    # Draw connectors
    for i in range(n - 1):
        if i in total_set:
            continue
        top = bottoms[i] + heights[i]
        ax.plot(
            [i + bar_width / 2, i + 1 - bar_width / 2],
            [top, top],
            color=connector_color, linewidth=0.8, linestyle="--",
        )

    # Tick labels
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=9)

    # Value labels
    if show_values:
        for i, (b, h) in enumerate(zip(bottoms, heights)):
            va = "bottom" if h >= 0 else "top"
            offset = 2 if h >= 0 else -2
            ax.text(
                x[i], b + h + offset / 100 * (ax.get_ylim()[1] - ax.get_ylim()[0] + 1),
                f"{h:+.1f}",
                ha="center", va=va,
                fontsize=value_fontsize, color="#1a1a1a",
            )

    # Legend
    legend_elements = [
        Patch(facecolor=positive_color, label="Increase"),
        Patch(facecolor=negative_color, label="Decrease"),
        Patch(facecolor=total_color, label="Total"),
    ]
    ax.legend(handles=legend_elements, frameon=False, fontsize=8,
              loc="upper right")

    return ax
