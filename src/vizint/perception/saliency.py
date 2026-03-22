"""
vizint.perception.saliency
==========================
Saliency-weighted scatter and visual attention maps.
"""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
from matplotlib.axes import Axes
from matplotlib.collections import PathCollection


def saliency_map_scatter(
    ax: Axes,
    x,
    y,
    saliency,
    cmap: str = "YlOrRd",
    size_range: tuple = (20, 300),
    alpha: float = 0.8,
    edgecolor: str = "none",
    zorder: int = 4,
    colorbar: bool = False,
    label: Optional[str] = None,
) -> PathCollection:
    """Scatter plot where marker size and color encode saliency.

    High-saliency points appear large and brightly colored.

    Parameters
    ----------
    ax:
        Target axes.
    x, y:
        Data coordinates.
    saliency:
        Array of non-negative saliency values (higher = more important).
    cmap:
        Colormap name.
    size_range:
        ``(min_size, max_size)`` in points² mapped to saliency range.
    alpha:
        Marker opacity.
    edgecolor:
        Marker edge color.
    zorder:
        Draw order.
    colorbar:
        If ``True``, attach a colorbar to the axes' figure.
    label:
        Scatter label for legend.

    Returns
    -------
    PathCollection
        The scatter artist.
    """
    s = np.asarray(saliency, dtype=float)
    s_min, s_max = s.min(), s.max()
    if s_max > s_min:
        s_norm = (s - s_min) / (s_max - s_min)
    else:
        s_norm = np.ones_like(s)

    sizes = size_range[0] + s_norm * (size_range[1] - size_range[0])

    scatter = ax.scatter(
        x, y,
        c=s_norm,
        s=sizes,
        cmap=cmap,
        alpha=alpha,
        edgecolors=edgecolor,
        zorder=zorder,
        label=label,
    )

    if colorbar and ax.figure is not None:
        ax.figure.colorbar(scatter, ax=ax, label="Saliency")

    return scatter
