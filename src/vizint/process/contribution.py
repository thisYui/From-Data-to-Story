"""
vizint.process.contribution
===========================
Contribution charts: who contributed how much to the total.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from vizint.styling.palette import categorical_colors


def contribution_chart(
    ax: Axes,
    categories: Sequence[str],
    contributions: Sequence[float],
    palette: str = "default",
    bar_height: float = 0.6,
    show_values: bool = True,
    value_fmt: str = "{:.1f}%",
    sort: bool = True,
    edgecolor: str = "white",
) -> Axes:
    """Horizontal bar chart showing each category's share of a total.

    Parameters
    ----------
    ax:
        Target axes.
    categories:
        Category labels.
    contributions:
        Contribution values (will be normalised to percentages if they
        don't sum to 100).
    palette:
        Named vizint palette.
    bar_height:
        Fractional bar height.
    show_values:
        If ``True``, display percentage values inside/beside bars.
    value_fmt:
        Format string for bar-end labels.
    sort:
        If ``True``, sort bars by contribution (descending).
    edgecolor:
        Bar edge color.

    Returns
    -------
    Axes
    """
    cats = list(categories)
    vals = np.array(contributions, dtype=float)
    total = vals.sum()
    if total != 0 and not np.isclose(total, 100.0):
        vals = vals / total * 100.0

    if sort:
        order = np.argsort(vals)
        cats = [cats[i] for i in order]
        vals = vals[order]

    colors = categorical_colors(len(cats), palette=palette)
    y = np.arange(len(cats))

    ax.barh(y, vals, height=bar_height, color=colors, edgecolor=edgecolor)
    ax.set_yticks(y)
    ax.set_yticklabels(cats, fontsize=9)
    ax.set_xlabel("Contribution (%)")

    if show_values:
        for i, v in enumerate(vals):
            ax.text(
                v + 0.5, i, value_fmt.format(v),
                va="center", fontsize=8, color="#1a1a1a",
            )
    return ax


def stacked_contribution(
    ax: Axes,
    x,
    series: Dict[str, np.ndarray],
    palette: str = "default",
    alpha: float = 0.85,
    legend: bool = True,
    legend_loc: str = "upper left",
) -> Axes:
    """Stacked area chart showing each series' contribution to the total.

    Parameters
    ----------
    ax:
        Target axes.
    x:
        Shared x-axis array.
    series:
        Dict mapping series name → y-values (same length as *x*).
    palette:
        Named vizint palette.
    alpha:
        Fill opacity.
    legend:
        Whether to draw a legend.
    legend_loc:
        Legend location.

    Returns
    -------
    Axes
    """
    colors = categorical_colors(len(series), palette=palette)
    names = list(series.keys())
    arrays = [np.asarray(v, dtype=float) for v in series.values()]

    baseline = np.zeros(len(arrays[0]))
    for name, arr, color in zip(names, arrays, colors):
        ax.fill_between(x, baseline, baseline + arr, color=color,
                        alpha=alpha, label=name)
        baseline = baseline + arr

    if legend:
        ax.legend(loc=legend_loc, frameon=False, fontsize=9)
    return ax
