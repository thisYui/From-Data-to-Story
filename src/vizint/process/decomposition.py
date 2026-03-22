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
import matplotlib.dates as mdates          # FIX 1: import trực tiếp, không dùng plt.matplotlib.dates
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

    Raises
    ------
    ImportError
        If ``statsmodels`` is not installed.
    """
    # FIX 2: lazy import với error message rõ ràng
    try:
        from statsmodels.tsa.seasonal import seasonal_decompose
    except ImportError:
        raise ImportError(
            "statsmodels is required for decomposition_chart(). "
            "Install it with:  pip install statsmodels"
        )

    result = seasonal_decompose(series, model=model, period=period,
                                extrapolate_trend="freq")

    # FIX 3: extract x-axis rõ ràng — tránh DatetimeIndex-to-epoch misinterpretation
    if isinstance(series, pd.Series) and isinstance(series.index, pd.DatetimeIndex):
        x = series.index
        use_dates = True
        bar_width = pd.Timedelta(days=20)  # FIX 4: width=None → bars invisible (0.8 seconds)
    else:
        x = np.arange(len(series))
        use_dates = False
        bar_width = 0.8

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
        y_vals = comp.values if isinstance(comp, pd.Series) else np.asarray(comp)
        if label == "Residual":
            ax.bar(x, y_vals, color=color, alpha=0.6, width=bar_width)
        else:
            ax.plot(x, y_vals, color=color, linewidth=1.8)
        ax.set_ylabel(label, fontsize=9, color="#444444")
        for spine in ["top", "right"]:
            ax.spines[spine].set_visible(False)
        ax.tick_params(labelsize=8)
        ax.set_facecolor("white")
        if use_dates:
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    fig.tight_layout()
    return fig