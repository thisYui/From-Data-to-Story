"""
vizint.narrative.timeline
=========================
Event markers, timeline bands, and milestone annotations.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence

import matplotlib.pyplot as plt
from matplotlib.axes import Axes


def add_event_markers(
    ax: Axes,
    x_positions: Sequence,
    labels: Optional[Sequence[str]] = None,
    color: str = "#7C3AED",
    linewidth: float = 1.2,
    linestyle: str = "--",
    alpha: float = 0.7,
    label_y: float = 0.98,
    label_fontsize: int = 8,
    label_rotation: float = 90,
    zorder: int = 3,
) -> Axes:
    """Draw vertical event marker lines with optional text labels.

    Parameters
    ----------
    ax:
        Target axes.
    x_positions:
        x-axis positions of the events.
    labels:
        Optional text labels for each event (must match length of *x_positions*).
    color:
        Marker line color.
    linewidth, linestyle, alpha:
        Line visual properties.
    label_y:
        Y position for labels in axes fraction.
    label_fontsize:
        Font size of event labels.
    label_rotation:
        Rotation of label text (90 = vertical).
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    for i, pos in enumerate(x_positions):
        ax.axvline(pos, color=color, linewidth=linewidth,
                   linestyle=linestyle, alpha=alpha, zorder=zorder)
        if labels is not None and i < len(labels):
            ax.text(
                pos, label_y, f"  {labels[i]}",
                transform=ax.get_xaxis_transform(),
                fontsize=label_fontsize,
                color=color,
                rotation=label_rotation,
                va="top",
                ha="left",
                alpha=0.9,
            )
    return ax


def add_timeline_band(
    ax: Axes,
    xmin: float,
    xmax: float,
    label: Optional[str] = None,
    color: str = "#EDE9FE",
    alpha: float = 0.4,
    label_y: float = 0.98,
    label_fontsize: int = 9,
    zorder: int = 0,
) -> Axes:
    """Shade a time band (e.g. a policy period, crisis window).

    Parameters
    ----------
    ax:
        Target axes.
    xmin, xmax:
        Horizontal span.
    label:
        Optional label drawn in the center of the band.
    color:
        Fill color.
    alpha:
        Fill opacity.
    label_y:
        Label y-position in axes fraction.
    label_fontsize:
        Label font size.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    ax.axvspan(xmin, xmax, color=color, alpha=alpha, zorder=zorder)
    if label is not None:
        mid = (xmin + xmax) / 2
        ax.text(
            mid, label_y, label,
            transform=ax.get_xaxis_transform(),
            fontsize=label_fontsize,
            color="#4C1D95",
            ha="center",
            va="top",
            alpha=0.85,
        )
    return ax
