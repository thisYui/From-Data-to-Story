"""
vizint.context
==============
Contextual visualization: reference lines, benchmarks, targets, and
excess/deficit shading.
"""

from vizint.context.benchmark import (
    add_benchmark_band,
    shade_above_benchmark,
    shade_below_benchmark,
)
from vizint.context.excess import shade_deficit, shade_excess
from vizint.context.reference import add_mean_line, add_median_line, add_reference_line
from vizint.context.target import add_target_line, add_target_zone

__all__ = [
    "add_reference_line",
    "add_mean_line",
    "add_median_line",
    "add_benchmark_band",
    "shade_above_benchmark",
    "shade_below_benchmark",
    "add_target_line",
    "add_target_zone",
    "shade_excess",
    "shade_deficit",
]
