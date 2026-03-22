"""
vizint.core.figure_layout
=========================
Utilities for creating and laying out matplotlib figures.
"""

from __future__ import annotations

from typing import Any, Optional, Sequence, Tuple

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from vizint.core.base_chart import BaseChart


def make_fig(
    figsize: Tuple[float, float] = (12, 5),
    facecolor: str = "white",
    dpi: int = 100,
) -> BaseChart:
    """Create a single-panel ``BaseChart``.

    Parameters
    ----------
    figsize:
        ``(width, height)`` in inches.
    facecolor:
        Figure background color.
    dpi:
        Screen resolution.

    Returns
    -------
    BaseChart
    """
    fig, ax = plt.subplots(figsize=figsize, facecolor=facecolor, dpi=dpi)
    ax.set_facecolor(facecolor)
    return BaseChart(fig, ax)


def make_grid(
    nrows: int = 1,
    ncols: int = 2,
    figsize: Optional[Tuple[float, float]] = None,
    facecolor: str = "white",
    dpi: int = 100,
    **gridspec_kw: Any,
) -> Tuple[Figure, np.ndarray]:
    """Create a figure with a grid of axes.

    Parameters
    ----------
    nrows, ncols:
        Grid dimensions.
    figsize:
        ``(width, height)`` in inches.  Defaults to ``(6*ncols, 4*nrows)``.
    facecolor:
        Background color.
    dpi:
        Screen resolution.
    **gridspec_kw:
        Extra keyword arguments forwarded to ``plt.subplots``.

    Returns
    -------
    tuple[Figure, np.ndarray]
        The figure and a 2-D array of ``Axes``.
    """
    if figsize is None:
        figsize = (6 * ncols, 4 * nrows)
    fig, axes = plt.subplots(
        nrows=nrows,
        ncols=ncols,
        figsize=figsize,
        facecolor=facecolor,
        dpi=dpi,
        **gridspec_kw,
    )
    fig.patch.set_facecolor(facecolor)
    # Normalise to 2-D array
    if nrows == 1 and ncols == 1:
        axes = np.array([[axes]])
    elif nrows == 1:
        axes = axes[np.newaxis, :]
    elif ncols == 1:
        axes = axes[:, np.newaxis]
    return fig, axes


def tight_layout_safe(
    fig: Figure,
    pad: float = 1.5,
    h_pad: Optional[float] = None,
    w_pad: Optional[float] = None,
) -> Figure:
    """Call ``fig.tight_layout`` without raising on single-axes figures.

    A thin wrapper that suppresses the occasional ``UserWarning`` raised when
    ``tight_layout`` cannot fit all elements perfectly.

    Parameters
    ----------
    fig:
        Target figure.
    pad:
        Padding around the edges.
    h_pad, w_pad:
        Optional per-axis height / width padding.

    Returns
    -------
    Figure
    """
    import warnings

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        kwargs: dict = {"pad": pad}
        if h_pad is not None:
            kwargs["h_pad"] = h_pad
        if w_pad is not None:
            kwargs["w_pad"] = w_pad
        fig.tight_layout(**kwargs)
    return fig


def add_watermark(
    ax: Axes,
    text: str,
    fontsize: int = 28,
    color: str = "#cccccc",
    alpha: float = 0.3,
    rotation: float = 30,
) -> Axes:
    """Add a diagonal watermark text to *ax*.

    Parameters
    ----------
    ax:
        Target axes.
    text:
        Watermark string.
    fontsize:
        Font size of the watermark text.
    color:
        Text color.
    alpha:
        Transparency (0 = invisible, 1 = opaque).
    rotation:
        Angle in degrees (counter-clockwise).

    Returns
    -------
    Axes
    """
    ax.text(
        0.5, 0.5, text,
        transform=ax.transAxes,
        fontsize=fontsize,
        color=color,
        alpha=alpha,
        ha="center",
        va="center",
        rotation=rotation,
        fontweight="bold",
        zorder=0,
    )
    return ax
