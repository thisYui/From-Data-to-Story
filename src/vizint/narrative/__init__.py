"""
vizint.narrative
================
Narrative construction: turning points, regimes, timelines, and story frames.
"""

from vizint.narrative.regime import add_regime_labels, shade_regimes
from vizint.narrative.story import StoryFrame, add_narrative_caption, build_story_sequence
from vizint.narrative.timeline import add_event_markers, add_timeline_band
from vizint.narrative.turning_point import detect_local_extrema, mark_turning_points

__all__ = [
    "StoryFrame",
    "add_narrative_caption",
    "build_story_sequence",
    "mark_turning_points",
    "detect_local_extrema",
    "shade_regimes",
    "add_regime_labels",
    "add_event_markers",
    "add_timeline_band",
]
