"""
vizint.core
===========
Core plotting infrastructure: figure setup, axes utilities, and a fluent
chart builder that serves as the foundation for all vizint modules.
"""

from vizint.core.axes_utils import (
    despine,
    format_percent,
    format_thousands,
    rotate_ticks,
    set_axis_labels,
    set_grid,
    set_tick_style,
)
from vizint.core.base_chart import BaseChart
from vizint.core.chart_builder import ChartBuilder
from vizint.core.figure_layout import (
    add_watermark,
    make_fig,
    make_grid,
    tight_layout_safe,
)

__all__ = [
    "BaseChart",
    "ChartBuilder",
    "make_fig",
    "make_grid",
    "tight_layout_safe",
    "add_watermark",
    "despine",
    "set_grid",
    "set_axis_labels",
    "format_thousands",
    "format_percent",
    "rotate_ticks",
    "set_tick_style",
]
