"""
vizint.styling.palette
======================
Curated color palettes designed for Visualization Intelligence charts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


# ---------------------------------------------------------------------------
# Default palette values
# ---------------------------------------------------------------------------

# Primary signal / accent colors
_SIGNAL_COLORS: List[str] = [
    "#2563EB",  # cobalt blue
    "#DC2626",  # vivid red
    "#16A34A",  # forest green
    "#D97706",  # amber
    "#7C3AED",  # violet
    "#0891B2",  # cyan
]

# Muted / background series
_MUTED_COLORS: List[str] = [
    "#94A3B8",
    "#CBD5E1",
    "#B0BEC5",
    "#CFD8DC",
    "#ECEFF1",
]

# Sequential (light → dark)
_SEQUENTIAL: List[str] = [
    "#EFF6FF", "#BFDBFE", "#93C5FD",
    "#60A5FA", "#3B82F6", "#2563EB",
    "#1D4ED8", "#1E40AF",
]

# Diverging (negative → neutral → positive)
_DIVERGING: List[str] = [
    "#DC2626", "#F87171", "#FCA5A5",
    "#E5E7EB",
    "#86EFAC", "#22C55E", "#16A34A",
]


@dataclass
class VizPalette:
    """Container for a coordinated vizint color palette.

    Attributes
    ----------
    signal : list[str]
        High-emphasis, distinct colors for key data series.
    muted : list[str]
        Low-emphasis colors for background / context series.
    accent : str
        Single accent color used for highlights and callouts.
    sequential : list[str]
        Ordered list from light to dark for sequential encoding.
    diverging : list[str]
        Colors for diverging data (e.g. negative / positive).
    """

    signal: List[str] = field(default_factory=lambda: list(_SIGNAL_COLORS))
    muted: List[str] = field(default_factory=lambda: list(_MUTED_COLORS))
    accent: str = "#FF6B35"
    sequential: List[str] = field(default_factory=lambda: list(_SEQUENTIAL))
    diverging: List[str] = field(default_factory=lambda: list(_DIVERGING))

    def get_signal(self, index: int = 0) -> str:
        """Return the signal color at *index* (wraps around)."""
        return self.signal[index % len(self.signal)]

    def get_muted(self, index: int = 0) -> str:
        """Return the muted color at *index* (wraps around)."""
        return self.muted[index % len(self.muted)]

    def as_cmap(self, palette: str = "sequential") -> mcolors.LinearSegmentedColormap:
        """Convert a palette to a matplotlib colormap.

        Parameters
        ----------
        palette:
            ``'sequential'`` or ``'diverging'``.

        Returns
        -------
        LinearSegmentedColormap
        """
        colors = self.sequential if palette == "sequential" else self.diverging
        return mcolors.LinearSegmentedColormap.from_list("vizint", colors)


# ---------------------------------------------------------------------------
# Named built-in palettes
# ---------------------------------------------------------------------------

_PALETTES: Dict[str, VizPalette] = {
    "default": VizPalette(),
    "warm": VizPalette(
        signal=["#DC2626", "#D97706", "#92400E", "#B45309", "#F59E0B"],
        muted=["#FEF3C7", "#FDE68A", "#FCD34D"],
        accent="#EF4444",
    ),
    "cool": VizPalette(
        signal=["#0891B2", "#2563EB", "#7C3AED", "#0E7490", "#1D4ED8"],
        muted=["#E0F2FE", "#BAE6FD", "#7DD3FC"],
        accent="#06B6D4",
    ),
    "mono": VizPalette(
        signal=["#111827", "#374151", "#6B7280"],
        muted=["#D1D5DB", "#E5E7EB", "#F3F4F6"],
        accent="#1F2937",
        sequential=["#F9FAFB", "#D1D5DB", "#9CA3AF", "#6B7280", "#374151", "#111827"],
    ),
}


def get_palette(name: str = "default") -> VizPalette:
    """Retrieve a named built-in :class:`VizPalette`.

    Parameters
    ----------
    name:
        Palette key: ``'default'``, ``'warm'``, ``'cool'``, or ``'mono'``.

    Returns
    -------
    VizPalette

    Raises
    ------
    KeyError
        If *name* is not a registered palette.
    """
    if name not in _PALETTES:
        raise KeyError(f"Unknown palette '{name}'. Available: {list(_PALETTES)}")
    return _PALETTES[name]


def categorical_colors(n: int, palette: str = "default") -> List[str]:
    """Return *n* categorical signal colors from the named palette.

    If *n* exceeds the palette's signal colors the list wraps around.

    Parameters
    ----------
    n:
        Number of colors required.
    palette:
        Palette name.

    Returns
    -------
    list[str]
    """
    pal = get_palette(palette)
    return [pal.get_signal(i) for i in range(n)]


def register_palette(name: str, palette: VizPalette) -> None:
    """Register a custom :class:`VizPalette` under *name*.

    Parameters
    ----------
    name:
        Key for the palette.
    palette:
        Palette to register.
    """
    _PALETTES[name] = palette
