"""
vizint.process.decomposition
=============================
Decomposition panel chart: trend / seasonal / residual components.
"""

from __future__ import annotations

from typing import Optional, Union

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def decomposition_chart(
    series: Union[pd.Series, np.ndarray],
    period: int = 12,
    model: str = "additive",
    figsize: tuple = (12, 9),
    title: str = "Time Series Decomposition",
    trend_color: str = "#2563EB",
    seasonal_color: str = "#16A34A",
    residual_color: str = "#9CA3AF",
    original_color: str = "#1a1a1a",
) -> Figure:
    """Decompose a time series and plot the four components in a panel.

    Uses ``statsmodels.tsa.seasonal.seasonal_decompose`` internally.

    Parameters
    ----------
    series:
        Time series data (``pandas.Series`` with a DatetimeIndex preferred).
    period:
        Seasonal period (e.g. 12 for monthly data with annual seasonality).
    model:
        Decomposition model: ``'additive'`` or ``'multiplicative'``.
    figsize:
        Figure size.
    title:
        Figure suptitle.
    trend_color, seasonal_color, residual_color, original_color:
        Colors for each component.

    Returns
    -------
    Figure
    """
    from statsmodels.tsa.seasonal import seasonal_decompose

    result = seasonal_decompose(series, model=model, period=period,
                                extrapolate_trend="freq")

    fig, axes = plt.subplots(4, 1, figsize=figsize, facecolor="white",
                             sharex=True)
    fig.suptitle(title, fontsize=14, fontweight="bold", color="#1a1a1a",
                 y=1.01)

    components = [
        ("Observed", result.observed, original_color),
        ("Trend",    result.trend,    trend_color),
        ("Seasonal", result.seasonal, seasonal_color),
        ("Residual", result.resid,    residual_color),
    ]

    for ax, (label, comp, color) in zip(axes, components):
        if label == "Residual":
            ax.bar(range(len(comp)), comp, color=color, alpha=0.6)
        else:
            ax.plot(comp, color=color, linewidth=1.8)
        ax.set_ylabel(label, fontsize=9, color="#444444")
        for spine in ["top", "right"]:
            ax.spines[spine].set_visible(False)
        ax.tick_params(labelsize=8)
        ax.set_facecolor("white")

    fig.tight_layout()
    return fig
