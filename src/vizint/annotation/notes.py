"""
vizint.annotation.notes
========================
Notes, captions, and source attribution annotations.
"""

from __future__ import annotations

from typing import Optional, Union

from matplotlib.axes import Axes
from matplotlib.figure import Figure


def add_note(
    ax: Axes,
    text: str,
    x: float = 0.02,
    y: float = 0.97,
    fontsize: int = 9,
    color: str = "#6B7280",
    ha: str = "left",
    va: str = "top",
    style: str = "normal",
    transform=None,
) -> Axes:
    """Add a text note inside the axes area.

    Parameters
    ----------
    ax:
        Target axes.
    text:
        Note text.
    x, y:
        Position in axes fraction.
    fontsize:
        Font size.
    color:
        Text color.
    ha, va:
        Alignment.
    style:
        Font style (``'normal'``, ``'italic'``, etc.).
    transform:
        Coordinate transform; defaults to ``ax.transAxes``.

    Returns
    -------
    Axes
    """
    t = transform if transform is not None else ax.transAxes
    ax.text(
        x, y, text,
        transform=t,
        fontsize=fontsize,
        color=color,
        ha=ha,
        va=va,
        fontstyle=style,
    )
    return ax


def add_source_note(
    fig: Figure,
    source: str,
    x: float = 0.01,
    y: float = -0.03,
    fontsize: int = 8,
    color: str = "#9CA3AF",
    ha: str = "left",
) -> Figure:
    """Add a data-source attribution note to the figure.

    Parameters
    ----------
    fig:
        Target figure.
    source:
        Source attribution string.
    x, y:
        Figure-relative position (in figure fraction).
    fontsize:
        Font size.
    color:
        Text color.
    ha:
        Horizontal alignment.

    Returns
    -------
    Figure
    """
    fig.text(
        x, y, f"Source: {source}",
        fontsize=fontsize,
        color=color,
        ha=ha,
    )
    return fig


def add_caption(
    ax: Axes,
    text: str,
    x: float = 0.0,
    y: float = -0.12,
    fontsize: int = 10,
    color: str = "#374151",
    style: str = "italic",
    ha: str = "left",
) -> Axes:
    """Add a caption / takeaway line below the axes.

    Parameters
    ----------
    ax:
        Target axes.
    text:
        Caption text.
    x, y:
        Position in axes fraction (y < 0 places it below the axes).
    fontsize:
        Font size.
    color:
        Text color.
    style:
        Font style.
    ha:
        Horizontal alignment.

    Returns
    -------
    Axes
    """
    ax.annotate(
        text,
        xy=(x, y),
        xycoords="axes fraction",
        fontsize=fontsize,
        color=color,
        fontstyle=style,
        ha=ha,
        va="top",
        annotation_clip=False,
    )
    return ax
