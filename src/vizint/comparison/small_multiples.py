"""
vizint.comparison.small_multiples
===================================
Small multiples (faceted grid) charts.
"""

from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure

from vizint.core.axes_utils import despine, set_grid
from vizint.styling.palette import categorical_colors


def small_multiples(
    groups: Dict[str, Tuple[Any, Any]],
    plot_fn: Callable,
    ncols: int = 3,
    figsize_per_panel: Tuple[float, float] = (4.5, 3.0),
    shared_y: bool = False,
    title_fontsize: int = 11,
    palette: str = "default",
    suptitle: Optional[str] = None,
    despine_panels: bool = True,
    grid_panels: bool = True,
) -> Figure:
    """Create a faceted small-multiples grid.

    Parameters
    ----------
    groups:
        Ordered dict mapping panel title → ``(x, y)`` data tuple
        (or any tuple your *plot_fn* accepts).
    plot_fn:
        Callable ``(ax, x, y, color)`` that draws a single panel.
    ncols:
        Number of columns in the grid.
    figsize_per_panel:
        ``(width, height)`` per panel in inches.
    shared_y:
        If ``True``, all panels share the same y-axis limits.
    title_fontsize:
        Font size for panel titles.
    palette:
        Named vizint palette.
    suptitle:
        Overall figure title (rendered above all panels).
    despine_panels:
        If ``True``, remove top/right spines from each panel.
    grid_panels:
        If ``True``, add a reference grid to each panel.

    Returns
    -------
    Figure
    """
    n = len(groups)
    nrows = int(np.ceil(n / ncols))
    fig_w = figsize_per_panel[0] * ncols
    fig_h = figsize_per_panel[1] * nrows

    sharey: Any = "all" if shared_y else False
    fig, axes = plt.subplots(
        nrows, ncols,
        figsize=(fig_w, fig_h),
        sharey=sharey,
        facecolor="white",
    )
    axes_flat = np.array(axes).flatten() if n > 1 else [axes]

    colors = categorical_colors(n, palette=palette)

    for ax, (label, data), color in zip(axes_flat, groups.items(), colors):
        if isinstance(data, tuple):
            plot_fn(ax, *data, color)
        else:
            plot_fn(ax, data, color)
        ax.set_title(label, fontsize=title_fontsize, fontweight="bold",
                     loc="left", color="#1a1a1a")
        if despine_panels:
            despine(ax)
        if grid_panels:
            set_grid(ax)

    # Hide unused panels
    for ax in axes_flat[n:]:
        ax.set_visible(False)

    if suptitle:
        fig.suptitle(suptitle, fontsize=14, fontweight="bold",
                     color="#1a1a1a", y=1.01)

    fig.tight_layout()
    return fig
