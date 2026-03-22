"""
vizint.pipeline.narrative_pipeline
====================================
``NarrativePipeline`` — orchestrates the full storytelling workflow for
a time series: regime shading → event marking → signal highlighting →
turning-point detection → annotation → caption.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np

from vizint.core.chart_builder import ChartBuilder
from vizint.core.base_chart import BaseChart
from vizint.perception.highlight import highlight_series
from vizint.perception.fade import fade_series
from vizint.narrative.regime import shade_regimes, add_regime_labels
from vizint.narrative.timeline import add_event_markers
from vizint.narrative.turning_point import mark_turning_points
from vizint.narrative.story import StoryFrame, add_narrative_caption
from vizint.context.reference import add_mean_line
from vizint.annotation.direct_label import label_last_point


class NarrativePipeline:
    """Full storytelling chart pipeline.

    Combines regime shading, event markers, signal highlighting, turning
    point detection, and narrative caption into a single cohesive figure.

    Parameters
    ----------
    x:
        Shared x-axis data.
    y:
        Primary data series.
    title:
        Chart title.
    figsize:
        Figure size.

    Examples
    --------
    >>> chart = (
    ...     NarrativePipeline(x, y, title="Growth Story")
    ...     .add_regimes(breakpoints=[2015, 2020], labels=["Pre", "Crisis", "Recovery"])
    ...     .add_events([(2020, "COVID"), (2022, "Recovery")])
    ...     .add_caption("Strong recovery driven by policy stimulus.")
    ...     .run()
    ... )
    """

    def __init__(
        self,
        x,
        y,
        title: str = "",
        subtitle: str = "",
        figsize: Tuple[float, float] = (14, 5.5),
        signal_color: str = "#2563EB",
    ) -> None:
        self.x = x
        self.y = y
        self.title = title
        self.subtitle = subtitle
        self.figsize = figsize
        self.signal_color = signal_color

        self._regimes: Optional[Tuple[Sequence, Sequence[str]]] = None
        self._events: Optional[List[Tuple[float, str]]] = None
        self._turning_points: bool = False
        self._mean_ref: bool = False
        self._caption: Optional[str] = None
        self._background: Optional[Dict[str, np.ndarray]] = None

    def add_regimes(
        self,
        breakpoints: Sequence[float],
        labels: Optional[Sequence[str]] = None,
    ) -> "NarrativePipeline":
        """Configure regime shading."""
        self._regimes = (breakpoints, labels or [])
        return self

    def add_events(self, events: Sequence[Tuple[float, str]]) -> "NarrativePipeline":
        """Add event markers as ``[(x_pos, label), ...]``."""
        self._events = list(events)
        return self

    def add_turning_points(self) -> "NarrativePipeline":
        """Enable automatic turning-point detection and annotation."""
        self._turning_points = True
        return self

    def add_mean_reference(self) -> "NarrativePipeline":
        """Add a mean reference line."""
        self._mean_ref = True
        return self

    def add_caption(self, caption: str) -> "NarrativePipeline":
        """Add a narrative caption."""
        self._caption = caption
        return self

    def add_background(self, series: Dict[str, np.ndarray]) -> "NarrativePipeline":
        """Add faded background series for context."""
        self._background = series
        return self

    def run(self) -> BaseChart:
        """Execute the pipeline and return the finished chart.

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

        # 1. Regime shading (bottom layer)
        if self._regimes:
            bp, labels = self._regimes
            shade_regimes(ax, bp)
            if labels:
                add_regime_labels(ax, bp, labels)

        # 2. Background series
        if self._background:
            for name, yb in self._background.items():
                fade_series(ax, self.x, yb, label=name)

        # 3. Signal series
        highlight_series(ax, self.x, self.y, color=self.signal_color)
        label_last_point(ax, self.x, self.y, color=self.signal_color)

        # 4. Reference
        if self._mean_ref:
            add_mean_line(ax, self.y)

        # 5. Turning points
        if self._turning_points:
            mark_turning_points(ax, self.x, self.y, order=max(3, len(self.x) // 20))

        # 6. Event markers
        if self._events:
            positions, event_labels = zip(*self._events)
            add_event_markers(ax, positions, labels=list(event_labels))

        # 7. Caption
        if self._caption:
            add_narrative_caption(ax, self._caption)

        return chart
