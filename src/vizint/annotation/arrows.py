"""
vizint.annotation.arrows
=========================
Arrow annotations and callout connectors.
"""

from __future__ import annotations

from typing import Optional, Tuple

from matplotlib.axes import Axes


def annotate_with_arrow(
    ax: Axes,
    text: str,
    xy: Tuple[float, float],
    xytext: Tuple[float, float],
    fontsize: int = 9,
    color: str = "#1a1a1a",
    arrowcolor: str = "#374151",
    arrowstyle: str = "->",
    connectionstyle: str = "arc3,rad=0.2",
    wrap: bool = True,
    ha: str = "left",
    va: str = "center",
) -> Axes:
    """Add a text annotation with an arrow connecting text to a data point.

    Parameters
    ----------
    ax:
        Target axes.
    text:
        Annotation text.
    xy:
        Data coordinates of the point being annotated.
    xytext:
        Position of the text box in data coordinates.
    fontsize:
        Text font size.
    color:
        Text color.
    arrowcolor:
        Arrow color.
    arrowstyle:
        Arrow style string (e.g. ``'->'``, ``'fancy'``).
    connectionstyle:
        Bezier connection style for the arrow.
    wrap:
        Whether to wrap long text.
    ha, va:
        Horizontal / vertical alignment.

    Returns
    -------
    Axes
    """
    ax.annotate(
        text,
        xy=xy,
        xytext=xytext,
        fontsize=fontsize,
        color=color,
        ha=ha,
        va=va,
        wrap=wrap,
        arrowprops=dict(
            arrowstyle=arrowstyle,
            color=arrowcolor,
            connectionstyle=connectionstyle,
            lw=1.2,
        ),
    )
    return ax


def add_callout_arrow(
    ax: Axes,
    text: str,
    xy: Tuple[float, float],
    dx: float = 0.05,
    dy: float = 0.10,
    fontsize: int = 9,
    color: str = "#2563EB",
    boxstyle: str = "round,pad=0.3",
    facecolor: str = "#EFF6FF",
    edgecolor: str = "#93C5FD",
    alpha: float = 0.9,
) -> Axes:
    """Add a color-boxed callout with an arrow to data point *xy*.

    Parameters
    ----------
    ax:
        Target axes.
    text:
        Callout text.
    xy:
        Data coordinates of the target point.
    dx, dy:
        Text offset relative to *xy* in axis fraction.
    fontsize:
        Text font size.
    color:
        Text color.
    boxstyle:
        Box shape for the text bounding box.
    facecolor:
        Fill color of the text box.
    edgecolor:
        Border color of the text box.
    alpha:
        Opacity of the text box.

    Returns
    -------
    Axes
    """
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    x_text = xy[0] + dx * (xlim[1] - xlim[0])
    y_text = xy[1] + dy * (ylim[1] - ylim[0])

    ax.annotate(
        text,
        xy=xy,
        xytext=(x_text, y_text),
        fontsize=fontsize,
        color=color,
        ha="center",
        va="center",
        bbox=dict(boxstyle=boxstyle, facecolor=facecolor,
                  edgecolor=edgecolor, alpha=alpha),
        arrowprops=dict(arrowstyle="->", color=edgecolor, lw=1.2),
    )
    return ax
