"""
vizint.styling.hierarchy
========================
Utilities for setting visual emphasis/weight on artists in a chart.
"""

from __future__ import annotations

from typing import Optional, Sequence, Union

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from matplotlib.patches import Patch


# Emphasis level → (alpha, linewidth_scale, zorder)
_EMPHASIS: dict = {
    "primary":    {"alpha": 1.0, "lw_scale": 1.5, "zorder": 5},
    "secondary":  {"alpha": 0.65, "lw_scale": 1.0, "zorder": 3},
    "background": {"alpha": 0.25, "lw_scale": 0.7, "zorder": 1},
}


def set_emphasis(
    artists: Union[Sequence, "mpl.artist.Artist"],
    level: str = "primary",
) -> None:
    """Apply a visual emphasis level to one or more matplotlib artists.

    Parameters
    ----------
    artists:
        A single artist or list of artists (``Line2D``, ``Patch``, etc.).
    level:
        Emphasis tier: ``'primary'``, ``'secondary'``, or ``'background'``.

    Raises
    ------
    KeyError
        If *level* is not a recognised emphasis tier.
    """
    if level not in _EMPHASIS:
        raise KeyError(f"Unknown emphasis level '{level}'. "
                       f"Available: {list(_EMPHASIS)}")

    cfg = _EMPHASIS[level]
    items = artists if isinstance(artists, (list, tuple)) else [artists]

    for artist in items:
        artist.set_alpha(cfg["alpha"])
        artist.set_zorder(cfg["zorder"])
        if isinstance(artist, Line2D):
            lw = artist.get_linewidth() * cfg["lw_scale"]
            artist.set_linewidth(lw)


def emphasize_series(
    ax: Axes,
    keep_index: int,
    level_keep: str = "primary",
    level_rest: str = "background",
) -> Axes:
    """Emphasise one line in *ax* and fade all others.

    Parameters
    ----------
    ax:
        Target axes.
    keep_index:
        Zero-based index of the line to emphasise.
    level_keep:
        Emphasis for the selected line.
    level_rest:
        Emphasis for all other lines.

    Returns
    -------
    Axes
    """
    lines = ax.get_lines()
    for i, line in enumerate(lines):
        set_emphasis(line, level=level_keep if i == keep_index else level_rest)
    return ax


def reset_emphasis(ax: Axes) -> Axes:
    """Reset all lines in *ax* to full opacity and default zorder.

    Parameters
    ----------
    ax:
        Target axes.

    Returns
    -------
    Axes
    """
    for line in ax.get_lines():
        line.set_alpha(1.0)
        line.set_zorder(2)
    return ax
