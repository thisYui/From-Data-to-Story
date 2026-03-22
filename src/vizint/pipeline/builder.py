"""
vizint.pipeline.builder
========================
``PipelineBuilder`` — generic fluent pipeline chaining arbitrary rendering steps.
"""

from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np
from matplotlib.axes import Axes

from vizint.core.chart_builder import ChartBuilder
from vizint.core.base_chart import BaseChart


# A step is any callable(ax, **kwargs) -> None
StepFn = Callable[[Axes], None]


class PipelineBuilder:
    """Generic fluent chart pipeline.

    Allows composing arbitrary rendering steps in sequence.

    Parameters
    ----------
    figsize:
        Figure size.
    title:
        Chart title.

    Examples
    --------
    >>> from vizint.pipeline import PipelineBuilder
    >>> from vizint.perception import highlight_series
    >>> from vizint.context import add_mean_line
    >>>
    >>> chart = (
    ...     PipelineBuilder(title="My Chart")
    ...     .step(lambda ax: highlight_series(ax, x, y, color="#2563EB"))
    ...     .step(lambda ax: add_mean_line(ax, y))
    ...     .build()
    ... )
    """

    def __init__(
        self,
        figsize: Tuple[float, float] = (12, 5),
        title: str = "",
        subtitle: str = "",
        source: str = "",
    ) -> None:
        self._figsize = figsize
        self._title = title
        self._subtitle = subtitle
        self._source = source
        self._steps: List[StepFn] = []

    def step(self, fn: StepFn) -> "PipelineBuilder":
        """Append a rendering step.

        Parameters
        ----------
        fn:
            Callable that accepts a single ``Axes`` argument and renders
            something on it.

        Returns
        -------
        PipelineBuilder
            Self, for chaining.
        """
        self._steps.append(fn)
        return self

    def build(self) -> BaseChart:
        """Execute all steps and return the completed :class:`BaseChart`.

        Returns
        -------
        BaseChart
        """
        builder = (
            ChartBuilder(figsize=self._figsize)
            .set_title(self._title)
        )
        if self._subtitle:
            builder.set_subtitle(self._subtitle)
        if self._source:
            builder.set_source(self._source)

        chart = builder.build()

        for fn in self._steps:
            fn(chart.ax)

        return chart
