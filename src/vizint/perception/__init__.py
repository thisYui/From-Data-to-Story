"""
vizint.perception
=================
Perception and attention control — highlight signals, fade noise, emphasise
outliers, and control saliency.
"""

from vizint.perception.fade import fade_background_lines, fade_series
from vizint.perception.focus import blur_outside_range, focus_on_range
from vizint.perception.highlight import highlight_points, highlight_region, highlight_series
from vizint.perception.outlier import detect_and_mark_outliers, emphasize_outliers
from vizint.perception.saliency import saliency_map_scatter

__all__ = [
    "highlight_series",
    "highlight_region",
    "highlight_points",
    "fade_series",
    "fade_background_lines",
    "focus_on_range",
    "blur_outside_range",
    "saliency_map_scatter",
    "detect_and_mark_outliers",
    "emphasize_outliers",
]
