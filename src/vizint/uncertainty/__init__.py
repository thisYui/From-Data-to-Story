"""
vizint.uncertainty
==================
Uncertainty visualization: confidence bands, prediction intervals,
forecast regions, and fan charts.
"""

from vizint.uncertainty.confidence_band import add_confidence_band
from vizint.uncertainty.fan_chart import fan_chart
from vizint.uncertainty.forecast import add_forecast_region, shade_forecast_period
from vizint.uncertainty.prediction_interval import add_dual_interval, add_prediction_interval

__all__ = [
    "add_confidence_band",
    "add_prediction_interval",
    "add_dual_interval",
    "shade_forecast_period",
    "add_forecast_region",
    "fan_chart",
]
