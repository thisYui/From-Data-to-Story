"""
vizint.styling.typography
=========================
Font size constants and style helpers for chart text elements.
"""

from __future__ import annotations

from typing import Optional

from matplotlib.axes import Axes
from matplotlib.figure import Figure

# ---------------------------------------------------------------------------
# Font size scale
# ---------------------------------------------------------------------------

TITLE_SIZE      = 16
SUBTITLE_SIZE   = 12
AXIS_LABEL_SIZE = 11
TICK_SIZE       = 10
ANNOTATION_SIZE = 9
CAPTION_SIZE    = 8
SOURCE_SIZE     = 8

_TITLE_STYLE    = dict(fontsize=TITLE_SIZE, fontweight="bold", color="#1a1a1a")
_SUBTITLE_STYLE = dict(fontsize=SUBTITLE_SIZE, color="#555555")
_LABEL_STYLE    = dict(fontsize=AXIS_LABEL_SIZE, color="#444444")
_CAPTION_STYLE  = dict(fontsize=CAPTION_SIZE, color="#888888")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def style_title(ax: Axes, title: str, **kwargs) -> Axes:
    """Set a bold, left-aligned chart title.

    Parameters
    ----------
    ax:
        Target axes.
    title:
        Title text.
    **kwargs:
        Forwarded to ``Axes.set_title``.

    Returns
    -------
    Axes
    """
    opts = {**_TITLE_STYLE, "loc": "left", "pad": 12, **kwargs}
    ax.set_title(title, **opts)
    return ax


def style_label(ax: Axes, xlabel: Optional[str] = None, ylabel: Optional[str] = None, **kwargs) -> Axes:
    """Apply consistent axis labels.

    Parameters
    ----------
    ax:
        Target axes.
    xlabel, ylabel:
        Label strings (``None`` skips).
    **kwargs:
        Forwarded to ``set_xlabel`` / ``set_ylabel``.

    Returns
    -------
    Axes
    """
    opts = {**_LABEL_STYLE, **kwargs}
    if xlabel is not None:
        ax.set_xlabel(xlabel, **opts)
    if ylabel is not None:
        ax.set_ylabel(ylabel, **opts)
    return ax


def style_caption(fig: Figure, text: str, x: float = 0.01, y: float = -0.04, **kwargs) -> Figure:
    """Add a bottom-left caption / source note to the figure.

    Parameters
    ----------
    fig:
        Target figure.
    text:
        Caption string.
    x, y:
        Figure-relative coordinates (in figure fraction).
    **kwargs:
        Forwarded to ``Figure.text``.

    Returns
    -------
    Figure
    """
    opts = {**_CAPTION_STYLE, "ha": "left", **kwargs}
    fig.text(x, y, text, **opts)
    return fig
