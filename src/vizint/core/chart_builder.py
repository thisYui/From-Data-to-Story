"""
vizint.core.chart_builder
=========================
Fluent ``ChartBuilder`` for constructing styled charts step-by-step.
"""

from __future__ import annotations

from typing import Optional, Tuple

import matplotlib.pyplot as plt

from vizint.core.base_chart import BaseChart
from vizint.core.axes_utils import despine, set_grid, set_tick_style


class ChartBuilder:
    """Fluent builder that produces a :class:`~vizint.core.base_chart.BaseChart`.

    Parameters
    ----------
    figsize:
        ``(width, height)`` in inches.
    dpi:
        Screen resolution.

    Examples
    --------
    >>> chart = (
    ...     ChartBuilder(figsize=(12, 5))
    ...     .set_title("Revenue over Time")
    ...     .set_subtitle("Q1–Q4 2024")
    ...     .set_source("Company BI")
    ...     .build()
    ... )
    """

    def __init__(
        self,
        figsize: Tuple[float, float] = (12, 5),
        dpi: int = 100,
        facecolor: str = "white",
    ) -> None:
        self._figsize = figsize
        self._dpi = dpi
        self._facecolor = facecolor
        self._title: Optional[str] = None
        self._subtitle: Optional[str] = None
        self._source: Optional[str] = None
        self._grid: bool = True
        self._despine: bool = True
        self._xlabel: Optional[str] = None
        self._ylabel: Optional[str] = None

    # ------------------------------------------------------------------
    # Chainable setters
    # ------------------------------------------------------------------

    def set_title(self, title: str) -> "ChartBuilder":
        """Set the main chart title."""
        self._title = title
        return self

    def set_subtitle(self, subtitle: str) -> "ChartBuilder":
        """Set a subtitle rendered below the main title."""
        self._subtitle = subtitle
        return self

    def set_source(self, source: str) -> "ChartBuilder":
        """Set a data-source note rendered at the bottom of the figure."""
        self._source = source
        return self

    def set_figsize(self, width: float, height: float) -> "ChartBuilder":
        """Override the figure size."""
        self._figsize = (width, height)
        return self

    def set_labels(self, xlabel: str = "", ylabel: str = "") -> "ChartBuilder":
        """Set axis labels."""
        self._xlabel = xlabel
        self._ylabel = ylabel
        return self

    def no_grid(self) -> "ChartBuilder":
        """Disable the default y-axis reference grid."""
        self._grid = False
        return self

    def no_despine(self) -> "ChartBuilder":
        """Keep all four spines (disable default despine)."""
        self._despine = False
        return self

    # ------------------------------------------------------------------
    # Build
    # ------------------------------------------------------------------

    def build(self) -> BaseChart:
        """Construct and return the :class:`BaseChart`.

        Returns
        -------
        BaseChart
        """
        fig, ax = plt.subplots(
            figsize=self._figsize,
            dpi=self._dpi,
            facecolor=self._facecolor,
        )
        ax.set_facecolor(self._facecolor)

        if self._despine:
            despine(ax)
        if self._grid:
            set_grid(ax)

        set_tick_style(ax)

        if self._xlabel:
            ax.set_xlabel(self._xlabel, fontsize=11, color="#444444")
        if self._ylabel:
            ax.set_ylabel(self._ylabel, fontsize=11, color="#444444")

        if self._title:
            ax.set_title(
                self._title,
                fontsize=15,
                fontweight="bold",
                color="#1a1a1a",
                loc="left",
                pad=12,
            )

        if self._subtitle:
            ax.annotate(
                self._subtitle,
                xy=(0, 1),
                xycoords="axes fraction",
                xytext=(0, 14 + 12),
                textcoords="offset points",
                fontsize=11,
                color="#666666",
                va="bottom",
            )

        if self._source:
            fig.text(
                0.01, -0.02,
                f"Source: {self._source}",
                fontsize=8,
                color="#999999",
                ha="left",
            )

        return BaseChart(fig, ax)
