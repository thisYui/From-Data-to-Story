"""
vizint.uncertainty.prediction_interval
=======================================
Prediction interval overlays (typically wider than confidence bands).
"""

from __future__ import annotations

from typing import Optional

import numpy as np
from matplotlib.axes import Axes


def add_prediction_interval(
    ax: Axes,
    x,
    lower,
    upper,
    color: str = "#C4B5FD",
    alpha: float = 0.20,
    label: Optional[str] = "Prediction interval",
    zorder: int = 0,
) -> Axes:
    """Shade a prediction interval band.

    Prediction intervals are typically wider than confidence intervals
    as they account for individual observation variability.

    Parameters
    ----------
    ax:
        Target axes.
    x:
        x-coordinates.
    lower, upper:
        Lower and upper prediction bounds.
    color:
        Fill color.
    alpha:
        Fill opacity.
    label:
        Legend label.
    zorder:
        Draw order.

    Returns
    -------
    Axes
    """
    ax.fill_between(x, lower, upper, color=color, alpha=alpha,
                    label=label, zorder=zorder)
    return ax


def add_dual_interval(
    ax: Axes,
    x,
    ci_lower,
    ci_upper,
    pi_lower,
    pi_upper,
    ci_color: str = "#93C5FD",
    pi_color: str = "#C4B5FD",
    ci_alpha: float = 0.30,
    pi_alpha: float = 0.15,
) -> Axes:
    """Plot both a confidence interval and a wider prediction interval.

    The CI is plotted on top of the PI, creating a nested band effect.

    Parameters
    ----------
    ax:
        Target axes.
    x:
        x-coordinates.
    ci_lower, ci_upper:
        Confidence interval bounds.
    pi_lower, pi_upper:
        Prediction interval bounds (wider).
    ci_color:
        Color for the confidence interval fill.
    pi_color:
        Color for the prediction interval fill.
    ci_alpha, pi_alpha:
        Fill opacities.

    Returns
    -------
    Axes
    """
    ax.fill_between(x, pi_lower, pi_upper, color=pi_color, alpha=pi_alpha,
                    label="Prediction interval", zorder=0)
    ax.fill_between(x, ci_lower, ci_upper, color=ci_color, alpha=ci_alpha,
                    label="Confidence interval", zorder=1)
    return ax
