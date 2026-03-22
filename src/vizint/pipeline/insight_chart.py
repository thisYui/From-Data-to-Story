"""
vizint.pipeline.insight_chart
==============================
``InsightChart`` — highlights a key insight with context and annotation.
"""

from __future__ import annotations

from typing import Dict, Optional, Tuple

import numpy as np
from matplotlib.axes import Axes

from vizint.core.chart_builder import ChartBuilder
from vizint.core.base_chart import BaseChart
from vizint.perception.highlight import highlight_series, highlight_region
from vizint.annotation.notes import add_caption
from vizint.annotation.arrows import add_callout_arrow
from vizint.context.reference import add_reference_line


class InsightChart:
    """Chart built around a single key insight.

    Draws one primary series and optionally highlights a data region or
    adds a callout annotation at the insight location.

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
    >>> ic = (
    ...     InsightChart(x, y, title="Q3 Spike")
    ...     .set_insight_region(xmin=8, xmax=10)
    ...     .set_callout(xy=(9, 150), text="Revenue spike")
    ...     .build()
    ... )
    """

    def __init__(
        self,
        x,
        y,
        title: str = "",
        figsize: Tuple[float, float] = (12, 5),
        series_color: str = "#2563EB",
    ) -> None:
        self.x = x
        self.y = y
        self.title = title
        self.figsize = figsize
        self.series_color = series_color

        self._insight_region: Optional[Tuple[float, float]] = None
        self._callout: Optional[Dict] = None
        self._reference: Optional[float] = None
        self._caption: Optional[str] = None

    def set_insight_region(self, xmin: float, xmax: float) -> "InsightChart":
        """Highlight a horizontal region of interest."""
        self._insight_region = (xmin, xmax)
        return self

    def set_callout(
        self,
        xy: Tuple[float, float],
        text: str,
        dx: float = 0.06,
        dy: float = 0.12,
    ) -> "InsightChart":
        """Add a callout annotation at (*xy*) with the given *text*."""
        self._callout = dict(xy=xy, text=text, dx=dx, dy=dy)
        return self

    def set_reference(self, value: float) -> "InsightChart":
        """Add a horizontal reference line at *value*."""
        self._reference = value
        return self

    def set_caption(self, text: str) -> "InsightChart":
        """Add a narrative caption below the chart."""
        self._caption = text
        return self

    def build(self) -> BaseChart:
        """Render and return the :class:`~vizint.core.base_chart.BaseChart`."""
        chart = (
            ChartBuilder(figsize=self.figsize)
            .set_title(self.title)
            .build()
        )
        ax = chart.ax

        highlight_series(ax, self.x, self.y, color=self.series_color)

        if self._insight_region:
            highlight_region(ax, *self._insight_region)

        if self._reference is not None:
            add_reference_line(ax, self._reference, label="Reference")

        # Refresh limits before callout
        ax.relim()
        ax.autoscale_view()

        if self._callout:
            add_callout_arrow(
                ax, self._callout["text"], self._callout["xy"],
                dx=self._callout["dx"], dy=self._callout["dy"],
            )

        if self._caption:
            add_caption(ax, self._caption)

        return chart
