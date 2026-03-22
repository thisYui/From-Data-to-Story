"""
vizint.annotation
=================
Annotation and labeling utilities: direct labels, inline labels,
arrows, callouts, notes, and captions.
"""

from vizint.annotation.arrows import add_callout_arrow, annotate_with_arrow
from vizint.annotation.direct_label import label_last_point, label_max, label_min
from vizint.annotation.inline_label import inline_series_labels
from vizint.annotation.notes import add_caption, add_note, add_source_note

__all__ = [
    "label_last_point",
    "label_max",
    "label_min",
    "inline_series_labels",
    "annotate_with_arrow",
    "add_callout_arrow",
    "add_note",
    "add_source_note",
    "add_caption",
]
