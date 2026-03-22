"""
vizint.core.base_chart
======================
``BaseChart`` — lightweight wrapper around a matplotlib ``(Figure, Axes)``
pair that adds save/show/copy utilities and acts as the return type for
all vizint chart builders.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Tuple

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure


class BaseChart:
    """Wrapper around a ``(Figure, Axes)`` pair.

    Parameters
    ----------
    fig:
        The matplotlib ``Figure`` object.
    ax:
        The primary matplotlib ``Axes`` object.

    Attributes
    ----------
    fig : Figure
    ax  : Axes

    Examples
    --------
    >>> chart = BaseChart(fig, ax)
    >>> chart.show()
    >>> chart.save("output.png", dpi=150)
    """

    def __init__(self, fig: Figure, ax: Axes) -> None:
        self.fig: Figure = fig
        self.ax: Axes = ax

    # ------------------------------------------------------------------
    # Output helpers
    # ------------------------------------------------------------------

    def show(self) -> "BaseChart":
        """Display the figure via ``plt.show()``.

        Returns
        -------
        BaseChart
            Self, for chaining.
        """
        plt.figure(self.fig.number)
        plt.show()
        return self

    def save(
        self,
        path: Union[str, Path],
        dpi: int = 150,
        bbox_inches: str = "tight",
        **kwargs,
    ) -> "BaseChart":
        """Save the figure to *path*.

        Parameters
        ----------
        path:
            Output file path (extension determines format).
        dpi:
            Resolution in dots-per-inch.
        bbox_inches:
            Bounding box setting; ``'tight'`` avoids clipping.
        **kwargs:
            Forwarded to ``Figure.savefig``.

        Returns
        -------
        BaseChart
            Self, for chaining.
        """
        self.fig.savefig(path, dpi=dpi, bbox_inches=bbox_inches, **kwargs)
        return self

    def close(self) -> None:
        """Close the underlying figure to free memory."""
        plt.close(self.fig)

    # ------------------------------------------------------------------
    # Convenience accessors
    # ------------------------------------------------------------------

    @property
    def size(self) -> Tuple[float, float]:
        """Return ``(width, height)`` in inches."""
        return self.fig.get_size_inches().tolist()

    def set_background(self, color: str = "white") -> "BaseChart":
        """Set figure and axes background color.

        Parameters
        ----------
        color:
            Any matplotlib color specification.

        Returns
        -------
        BaseChart
        """
        self.fig.patch.set_facecolor(color)
        self.ax.set_facecolor(color)
        return self

    def __repr__(self) -> str:  # pragma: no cover
        w, h = self.size
        return f"BaseChart(fig={w:.1f}x{h:.1f}in)"


# Type alias accepted by functions that take an existing BaseChart *or* raw axes
from typing import Union  # noqa: E402  (re-import at bottom to avoid circular)
ChartLike = Union[BaseChart, Axes]
