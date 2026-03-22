"""
vizint.narrative.story
======================
StoryFrame dataclass and narrative caption utilities.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Sequence

from matplotlib.axes import Axes
from matplotlib.figure import Figure


@dataclass
class StoryFrame:
    """Container for a single narrative frame.

    A narrative chart typically consists of one or more *frames*, each
    describing a phase, event, or insight within the data.

    Attributes
    ----------
    title : str
        Short headline describing this narrative frame.
    body : str
        Longer explanatory text (1–3 sentences).
    xmin, xmax : float or None
        Optional x-axis range this frame refers to.
    highlights : list[str]
        Key data series names relevant to this frame.
    """

    title: str
    body: str = ""
    xmin: Optional[float] = None
    xmax: Optional[float] = None
    highlights: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        return f"[{self.title}] {self.body}"


def add_narrative_caption(
    ax: Axes,
    text: str,
    x: float = 0.0,
    y: float = -0.14,
    fontsize: int = 10,
    color: str = "#374151",
    style: str = "italic",
    ha: str = "left",
    wrap: bool = True,
) -> Axes:
    """Add a narrative caption below the plot area.

    Parameters
    ----------
    ax:
        Target axes.
    text:
        Caption / takeaway text.
    x, y:
        Position in axes fraction.
    fontsize:
        Caption font size.
    color:
        Text color.
    style:
        Font style (e.g. ``'italic'``).
    ha:
        Horizontal alignment.
    wrap:
        If ``True``, enable automatic text wrapping.

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
        wrap=wrap,
        annotation_clip=False,
    )
    return ax


def build_story_sequence(
    frames: Sequence[StoryFrame],
) -> List[str]:
    """Return a list of formatted narrative strings from a sequence of frames.

    Useful for generating a text summary alongside a chart sequence.

    Parameters
    ----------
    frames:
        Ordered list of :class:`StoryFrame` objects.

    Returns
    -------
    list[str]
        Formatted strings, one per frame.
    """
    return [
        f"{i + 1}. {frame.title}: {frame.body}"
        for i, frame in enumerate(frames)
    ]
