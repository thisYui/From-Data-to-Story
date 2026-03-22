"""
vizint.styling.theme
====================
Theme presets and application utilities for vizint charts.
"""

from __future__ import annotations

from typing import Any, Dict

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from vizint.core.axes_utils import despine, set_grid, set_tick_style


# ---------------------------------------------------------------------------
# Theme definitions
# ---------------------------------------------------------------------------

_THEMES: Dict[str, Dict[str, Any]] = {
    "clean": {
        "facecolor": "white",
        "grid": True,
        "grid_color": "#e8e8e8",
        "spine_color": "#cccccc",
        "tick_color": "#888888",
        "labelsize": 10,
    },
    "dark": {
        "facecolor": "#1a1a2e",
        "grid": True,
        "grid_color": "#2d2d4a",
        "spine_color": "#3d3d5c",
        "tick_color": "#aaaacc",
        "labelsize": 10,
    },
    "minimal": {
        "facecolor": "white",
        "grid": False,
        "grid_color": "#f0f0f0",
        "spine_color": "#e0e0e0",
        "tick_color": "#999999",
        "labelsize": 9,
    },
    "research": {
        "facecolor": "#fafafa",
        "grid": True,
        "grid_color": "#dddddd",
        "spine_color": "#333333",
        "tick_color": "#444444",
        "labelsize": 11,
    },
}


def apply_theme(ax: Axes, theme: str = "clean") -> Axes:
    """Apply a named theme to *ax*.

    Parameters
    ----------
    ax:
        Target axes.
    theme:
        Theme name: ``'clean'``, ``'dark'``, ``'minimal'``, or ``'research'``.

    Returns
    -------
    Axes

    Raises
    ------
    KeyError
        If *theme* is not registered.
    """
    if theme not in _THEMES:
        raise KeyError(f"Unknown theme '{theme}'. Available: {list(_THEMES)}")

    cfg = _THEMES[theme]

    ax.set_facecolor(cfg["facecolor"])
    if ax.figure is not None:
        ax.figure.patch.set_facecolor(cfg["facecolor"])

    despine(ax)
    for spine in ax.spines.values():
        spine.set_edgecolor(cfg["spine_color"])

    set_tick_style(ax, color=cfg["tick_color"], labelsize=cfg["labelsize"])

    if cfg["grid"]:
        set_grid(ax, color=cfg["grid_color"])
    else:
        ax.grid(False)

    return ax


def set_global_theme(theme: str = "clean") -> None:
    """Apply vizint theme settings globally via ``rcParams``.

    Parameters
    ----------
    theme:
        Theme name.

    Notes
    -----
    This modifies ``matplotlib.rcParams`` globally and affects all
    subsequently created plots in the session.
    """
    if theme not in _THEMES:
        raise KeyError(f"Unknown theme '{theme}'. Available: {list(_THEMES)}")

    cfg = _THEMES[theme]
    bg = cfg["facecolor"]

    mpl.rcParams.update({
        "figure.facecolor": bg,
        "axes.facecolor": bg,
        "axes.edgecolor": cfg["spine_color"],
        "axes.grid": cfg["grid"],
        "grid.color": cfg["grid_color"],
        "grid.linestyle": "--",
        "grid.linewidth": 0.8,
        "grid.alpha": 0.7,
        "xtick.color": cfg["tick_color"],
        "ytick.color": cfg["tick_color"],
        "xtick.labelsize": cfg["labelsize"],
        "ytick.labelsize": cfg["labelsize"],
        "axes.spines.top": False,
        "axes.spines.right": False,
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans"],
    })


def register_theme(name: str, config: Dict[str, Any]) -> None:
    """Register a custom theme.

    Parameters
    ----------
    name:
        Theme key.
    config:
        Dictionary with keys: ``facecolor``, ``grid``, ``grid_color``,
        ``spine_color``, ``tick_color``, ``labelsize``.
    """
    _THEMES[name] = config
