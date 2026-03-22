"""
vizint.uncertainty.fan_chart
============================
Fan charts for visualising forecast uncertainty across multiple quantile bands.
"""

from __future__ import annotations

from typing import List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd
from matplotlib.axes import Axes


def fan_chart(
    ax: Axes,
    x,
    quantile_df: pd.DataFrame,
    center_col: Optional[str] = None,
    quantile_pairs: Optional[List[Tuple[str, str]]] = None,
    palette: Optional[List[str]] = None,
    alpha_base: float = 0.20,
    center_color: str = "#2563EB",
    center_linewidth: float = 2.0,
    label_prefix: str = "PI",
    zorder: int = 1,
) -> Axes:
    """Draw a fan chart from a DataFrame of quantile columns.

    Parameters
    ----------
    ax:
        Target axes.
    x:
        x-coordinates (length must match ``len(quantile_df)``).
    quantile_df:
        DataFrame where columns are named quantile series
        (e.g. ``"q10"``, ``"q25"``, ``"q50"``, ``"q75"``, ``"q90"``).
    center_col:
        Column name of the central forecast (e.g. ``"q50"`` or ``"mean"``).
        If ``None``, no central line is drawn.
    quantile_pairs:
        List of ``(lower_col, upper_col)`` tuples forming symmetric bands.
        Drawn from widest to narrowest (back to front).
        If ``None``, pairs are inferred by pairing first ↔ last, second ↔
        second-to-last columns (excluding *center_col*).
    palette:
        Colors for each band (outermost to innermost).
        Defaults to shades of blue.
    alpha_base:
        Base opacity for the outermost band; inner bands are slightly darker.
    center_color:
        Color of the central forecast line.
    center_linewidth:
        Line width of the central forecast line.
    label_prefix:
        Prefix for band legend labels (e.g. ``"PI 80%"``).
    zorder:
        Base draw order.

    Returns
    -------
    Axes
    """
    # --- Auto-infer pairs ---------------------------------------------------
    if quantile_pairs is None:
        cols = [c for c in quantile_df.columns if c != center_col]
        pairs: List[Tuple[str, str]] = []
        lo, hi = 0, len(cols) - 1
        while lo < hi:
            pairs.append((cols[lo], cols[hi]))
            lo += 1
            hi -= 1
    else:
        pairs = quantile_pairs

    # --- Default palette ----------------------------------------------------
    if palette is None:
        palette = ["#BFDBFE", "#93C5FD", "#60A5FA", "#3B82F6"]

    # --- Draw bands (widest first) ------------------------------------------
    for i, (lo_col, hi_col) in enumerate(pairs):
        color = palette[i % len(palette)]
        alpha = alpha_base + i * 0.05
        ax.fill_between(
            x,
            quantile_df[lo_col],
            quantile_df[hi_col],
            color=color,
            alpha=min(alpha, 0.60),
            zorder=zorder + i,
            label=f"{label_prefix} band {i + 1}",
        )

    # --- Draw central line --------------------------------------------------
    if center_col is not None and center_col in quantile_df.columns:
        ax.plot(
            x,
            quantile_df[center_col],
            color=center_color,
            linewidth=center_linewidth,
            zorder=zorder + len(pairs) + 1,
            label="Central forecast",
        )

    return ax
