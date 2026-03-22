"""
vizint.core.axes_utils
======================
Low-level utilities for formatting and cleaning matplotlib axes.
"""

from __future__ import annotations

from typing import Optional, Sequence, Union

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.axes import Axes


# ---------------------------------------------------------------------------
# Spine / frame helpers
# ---------------------------------------------------------------------------

def despine(
    ax: Axes,
    top: bool = True,
    right: bool = True,
    left: bool = False,
    bottom: bool = False,
) -> Axes:
    """Remove spines from *ax*.

    Parameters
    ----------
    ax:
        Target axes.
    top, right, left, bottom:
        Which spines to remove. Defaults remove top and right (seaborn-style).

    Returns
    -------
    Axes
        The same axes (for chaining).
    """
    spines = {"top": top, "right": right, "left": left, "bottom": bottom}
    for spine, remove in spines.items():
        ax.spines[spine].set_visible(not remove)
    return ax


def set_grid(
    ax: Axes,
    which: str = "y",
    color: str = "#e0e0e0",
    linewidth: float = 0.8,
    linestyle: str = "--",
    alpha: float = 0.7,
    zorder: int = 0,
) -> Axes:
    """Apply a clean reference grid to *ax*.

    Parameters
    ----------
    ax:
        Target axes.
    which:
        ``'x'``, ``'y'``, or ``'both'``.
    color, linewidth, linestyle, alpha:
        Grid visual properties.
    zorder:
        Draw order — keep low so grid sits behind data.

    Returns
    -------
    Axes
    """
    ax.set_axisbelow(True)
    if which in ("y", "both"):
        ax.yaxis.grid(True, color=color, linewidth=linewidth,
                      linestyle=linestyle, alpha=alpha, zorder=zorder)
    if which in ("x", "both"):
        ax.xaxis.grid(True, color=color, linewidth=linewidth,
                      linestyle=linestyle, alpha=alpha, zorder=zorder)
    return ax


# ---------------------------------------------------------------------------
# Label helpers
# ---------------------------------------------------------------------------

def set_axis_labels(
    ax: Axes,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    fontsize: int = 11,
    color: str = "#444444",
    labelpad: float = 8.0,
) -> Axes:
    """Set x- and y-axis labels with consistent styling.

    Parameters
    ----------
    ax:
        Target axes.
    xlabel, ylabel:
        Label strings. ``None`` leaves the existing label unchanged.
    fontsize:
        Font size for labels.
    color:
        Label text color.
    labelpad:
        Padding between the axis and the label.

    Returns
    -------
    Axes
    """
    if xlabel is not None:
        ax.set_xlabel(xlabel, fontsize=fontsize, color=color, labelpad=labelpad)
    if ylabel is not None:
        ax.set_ylabel(ylabel, fontsize=fontsize, color=color, labelpad=labelpad)
    return ax


def rotate_ticks(
    ax: Axes,
    axis: str = "x",
    rotation: float = 45,
    ha: str = "right",
) -> Axes:
    """Rotate tick labels on *ax* for readability.

    Parameters
    ----------
    ax:
        Target axes.
    axis:
        ``'x'`` or ``'y'``.
    rotation:
        Degrees of rotation.
    ha:
        Horizontal alignment for the labels.

    Returns
    -------
    Axes
    """
    labels = ax.get_xticklabels() if axis == "x" else ax.get_yticklabels()
    for label in labels:
        label.set_rotation(rotation)
        label.set_ha(ha)
    return ax


# ---------------------------------------------------------------------------
# Number formatters
# ---------------------------------------------------------------------------

def format_thousands(ax: Axes, axis: str = "y") -> Axes:
    """Format tick labels with comma thousands separator (e.g. 1,234,567).

    Parameters
    ----------
    ax:
        Target axes.
    axis:
        ``'x'`` or ``'y'``.

    Returns
    -------
    Axes
    """
    fmt = mticker.FuncFormatter(lambda x, _: f"{x:,.0f}")
    if axis == "y":
        ax.yaxis.set_major_formatter(fmt)
    else:
        ax.xaxis.set_major_formatter(fmt)
    return ax


def format_percent(ax: Axes, axis: str = "y", decimals: int = 1) -> Axes:
    """Format tick labels as percentages.

    Parameters
    ----------
    ax:
        Target axes.
    axis:
        ``'x'`` or ``'y'``.
    decimals:
        Number of decimal places in the percentage string.

    Returns
    -------
    Axes
    """
    fmt = mticker.FuncFormatter(lambda x, _: f"{x:.{decimals}f}%")
    if axis == "y":
        ax.yaxis.set_major_formatter(fmt)
    else:
        ax.xaxis.set_major_formatter(fmt)
    return ax


def set_tick_style(
    ax: Axes,
    color: str = "#888888",
    labelsize: int = 10,
) -> Axes:
    """Apply uniform tick color and label size.

    Parameters
    ----------
    ax:
        Target axes.
    color:
        Tick mark and label color.
    labelsize:
        Label font size.

    Returns
    -------
    Axes
    """
    ax.tick_params(colors=color, labelsize=labelsize)
    for spine in ax.spines.values():
        spine.set_edgecolor(color)
    return ax
