"""
vizint — Visualization Intelligence
=====================================
A modular, matplotlib-based library for perception-driven,
narrative-aware storytelling charts.

Quick start
-----------
>>> import matplotlib
>>> matplotlib.use("Agg")  # use non-interactive backend in scripts
>>> import numpy as np
>>> from vizint.pipeline import StoryChart, NarrativePipeline
>>> from vizint.core import ChartBuilder
>>> from vizint.process import waterfall_chart
>>> from vizint.uncertainty import fan_chart

Submodules
----------
vizint.core          — Base chart, figure layout, axes utilities
vizint.styling       — Palettes, themes, typography, hierarchy
vizint.perception    — Highlight, fade, focus, outlier, saliency
vizint.context       — Reference lines, benchmarks, targets, excess
vizint.narrative     — Turning points, regimes, timelines, story frames
vizint.uncertainty   — Confidence bands, PI, forecast, fan charts
vizint.comparison    — Multi-series, before/after, distributions, small multiples
vizint.annotation    — Direct labels, inline labels, arrows, notes
vizint.process       — Waterfall, contribution, decomposition
vizint.pipeline      — StoryChart, InsightChart, PipelineBuilder, NarrativePipeline
"""

# ---------------------------------------------------------------------------
# Core
# ---------------------------------------------------------------------------
from vizint.core import (
    BaseChart,
    ChartBuilder,
    make_fig,
    make_grid,
    despine,
    set_grid,
    format_thousands,
    format_percent,
)

# ---------------------------------------------------------------------------
# Styling
# ---------------------------------------------------------------------------
from vizint.styling import (
    VizPalette,
    get_palette,
    categorical_colors,
    apply_theme,
    set_global_theme,
    set_emphasis,
    emphasize_series,
    style_title,
    style_label,
)

# ---------------------------------------------------------------------------
# Perception
# ---------------------------------------------------------------------------
from vizint.perception import (
    highlight_series,
    highlight_region,
    highlight_points,
    fade_series,
    fade_background_lines,
    focus_on_range,
    detect_and_mark_outliers,
    saliency_map_scatter,
)

# ---------------------------------------------------------------------------
# Context
# ---------------------------------------------------------------------------
from vizint.context import (
    add_reference_line,
    add_mean_line,
    add_median_line,
    add_benchmark_band,
    add_target_line,
    add_target_zone,
    shade_excess,
    shade_deficit,
)

# ---------------------------------------------------------------------------
# Narrative
# ---------------------------------------------------------------------------
from vizint.narrative import (
    StoryFrame,
    mark_turning_points,
    shade_regimes,
    add_regime_labels,
    add_event_markers,
    add_timeline_band,
    add_narrative_caption,
)

# ---------------------------------------------------------------------------
# Uncertainty
# ---------------------------------------------------------------------------
from vizint.uncertainty import (
    add_confidence_band,
    add_prediction_interval,
    add_dual_interval,
    shade_forecast_period,
    add_forecast_region,
    fan_chart,
)

# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------
from vizint.comparison import (
    compare_lines,
    before_after_lines,
    compare_distributions,
    ridge_plot,
    relative_performance_chart,
    small_multiples,
)

# ---------------------------------------------------------------------------
# Annotation
# ---------------------------------------------------------------------------
from vizint.annotation import (
    label_last_point,
    label_max,
    label_min,
    inline_series_labels,
    annotate_with_arrow,
    add_callout_arrow,
    add_note,
    add_source_note,
    add_caption,
)

# ---------------------------------------------------------------------------
# Process
# ---------------------------------------------------------------------------
from vizint.process import (
    waterfall_chart,
    contribution_chart,
    stacked_contribution,
    decomposition_chart,
)

# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------
from vizint.pipeline import (
    StoryChart,
    InsightChart,
    PipelineBuilder,
    NarrativePipeline,
)

__version__ = "0.1.0"

__all__ = [
    # core
    "BaseChart", "ChartBuilder", "make_fig", "make_grid",
    "despine", "set_grid", "format_thousands", "format_percent",
    # styling
    "VizPalette", "get_palette", "categorical_colors",
    "apply_theme", "set_global_theme", "set_emphasis", "emphasize_series",
    "style_title", "style_label",
    # perception
    "highlight_series", "highlight_region", "highlight_points",
    "fade_series", "fade_background_lines", "focus_on_range",
    "detect_and_mark_outliers", "saliency_map_scatter",
    # context
    "add_reference_line", "add_mean_line", "add_median_line",
    "add_benchmark_band", "add_target_line", "add_target_zone",
    "shade_excess", "shade_deficit",
    # narrative
    "StoryFrame", "mark_turning_points", "shade_regimes", "add_regime_labels",
    "add_event_markers", "add_timeline_band", "add_narrative_caption",
    # uncertainty
    "add_confidence_band", "add_prediction_interval", "add_dual_interval",
    "shade_forecast_period", "add_forecast_region", "fan_chart",
    # comparison
    "compare_lines", "before_after_lines", "compare_distributions",
    "ridge_plot", "relative_performance_chart", "small_multiples",
    # annotation
    "label_last_point", "label_max", "label_min", "inline_series_labels",
    "annotate_with_arrow", "add_callout_arrow",
    "add_note", "add_source_note", "add_caption",
    # process
    "waterfall_chart", "contribution_chart", "stacked_contribution",
    "decomposition_chart",
    # pipeline
    "StoryChart", "InsightChart", "PipelineBuilder", "NarrativePipeline",
]
