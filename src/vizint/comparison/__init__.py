"""
vizint.comparison
=================
Comparative visualization: multi-series lines, before/after, distribution,
relative performance, and small multiples.
"""

from vizint.comparison.compare_lines import before_after_lines, compare_lines
from vizint.comparison.distribution import compare_distributions, ridge_plot
from vizint.comparison.relative import index_to_base, relative_performance_chart
from vizint.comparison.small_multiples import small_multiples

__all__ = [
    "compare_lines",
    "before_after_lines",
    "compare_distributions",
    "ridge_plot",
    "index_to_base",
    "relative_performance_chart",
    "small_multiples",
]
