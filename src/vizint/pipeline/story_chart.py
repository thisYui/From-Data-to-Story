"""
vizint.pipeline.story_chart
============================
``StoryChart`` — high-level storytelling chart that wires together
perception, narrative, context, and annotation in a single call.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from vizint.core.chart_builder import ChartBuilder
from vizint.core.base_chart import BaseChart
from vizint.perception.highlight import highlight_series
from vizint.perception.fade import fade_series
from vizint.annotation.direct_label import label_last_point
from vizint.annotation.notes import add_caption
from vizint.narrative.story import StoryFrame, add_narrative_caption
from vizint.narrative.timeline import add_event_markers
from vizint.context.reference import add_mean_line


class StoryChart:
    """High-level storytelling chart builder.

    Combines perception (highlight / fade), narrative (events, captions),
    and context (reference lines) into a single cohesive chart.

    Parameters
    ----------
    x:
        Shared x-axis data.
    signal_series:
        Dict mapping series name → y-values for the focal (highlighted) series.
    background_series:
        Dict mapping series name → y-values for context (faded) series.
    title:
        Chart title.
    subtitle:
        Chart subtitle.
    figsize:
        ``(width, height)`` in inches.
    theme:
        Theme name passed to :class:`~vizint.core.chart_builder.ChartBuilder`.

    Examples
    --------
    >>> chart = (
    ...     StoryChart(x, signal={"Revenue": y1}, background={"Industry avg": y2})
    ...     .add_event(2020, "COVID-19")
    ...     .add_caption("Revenue recovered strongly in 2022.")
    ...     .build()
    ... )
    """

    def __init__(
        self,
        x,
        signal_series: Dict[str, np.ndarray],
        background_series: Optional[Dict[str, np.ndarray]] = None,
        title: str = "",
        subtitle: str = "",
        figsize: Tuple[float, float] = (13, 5),
    ) -> None:
        self.x = x
        self.signal_series = signal_series
        self.background_series = background_series or {}
        self.title = title
        self.subtitle = subtitle
        self.figsize = figsize

        self._events: List[Tuple[float, str]] = []
        self._caption: Optional[str] = None
        self._mean_line: bool = False
        self._mean_series: Optional[np.ndarray] = None

    def add_event(self, x_pos: float, label: str) -> "StoryChart":
        """Add an event marker at *x_pos* with *label*."""
        self._events.append((x_pos, label))
        return self

    def add_caption(self, caption: str) -> "StoryChart":
        """Add a narrative caption below the chart."""
        self._caption = caption
        return self

    def add_mean_reference(self, y: np.ndarray) -> "StoryChart":
        """Add a mean reference line computed from *y*."""
        self._mean_line = True
        self._mean_series = y
        return self

    def build(self) -> BaseChart:
        """Render and return the finished :class:`~vizint.core.base_chart.BaseChart`.

        Returns
        -------
        BaseChart
        """
        chart = (
            ChartBuilder(figsize=self.figsize)
            .set_title(self.title)
            .set_subtitle(self.subtitle)
            .build()
        )
        ax = chart.ax

        # Background series
        for name, y in self.background_series.items():
            fade_series(ax, self.x, y, label=name)

        # Signal series
        signal_colors = ["#2563EB", "#DC2626", "#16A34A", "#D97706"]
        for i, (name, y) in enumerate(self.signal_series.items()):
            color = signal_colors[i % len(signal_colors)]
            highlight_series(ax, self.x, y, color=color, label=name)
            label_last_point(ax, self.x, y, text=name, color=color)

        # Mean reference
        if self._mean_line and self._mean_series is not None:
            add_mean_line(ax, self._mean_series)

        # Event markers
        if self._events:
            x_positions, labels = zip(*self._events)
            add_event_markers(ax, x_positions, labels=list(labels))

        # Caption
        if self._caption:
            add_narrative_caption(ax, self._caption)

        return chart
