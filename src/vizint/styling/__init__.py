"""
vizint.styling
==============
Visual hierarchy, color palettes, themes, and typography for vizint charts.
"""

from vizint.styling.hierarchy import emphasize_series, reset_emphasis, set_emphasis
from vizint.styling.palette import (
    VizPalette,
    categorical_colors,
    get_palette,
    register_palette,
)
from vizint.styling.theme import apply_theme, register_theme, set_global_theme
from vizint.styling.typography import (
    ANNOTATION_SIZE,
    AXIS_LABEL_SIZE,
    CAPTION_SIZE,
    SOURCE_SIZE,
    SUBTITLE_SIZE,
    TICK_SIZE,
    TITLE_SIZE,
    style_caption,
    style_label,
    style_title,
)

__all__ = [
    "VizPalette",
    "get_palette",
    "categorical_colors",
    "register_palette",
    "apply_theme",
    "set_global_theme",
    "register_theme",
    "set_emphasis",
    "emphasize_series",
    "reset_emphasis",
    "style_title",
    "style_label",
    "style_caption",
    "TITLE_SIZE",
    "SUBTITLE_SIZE",
    "AXIS_LABEL_SIZE",
    "TICK_SIZE",
    "ANNOTATION_SIZE",
    "CAPTION_SIZE",
    "SOURCE_SIZE",
]
