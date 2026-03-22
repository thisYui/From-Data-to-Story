# Visualization Intelligence

### From Data to Perception to Insight to Story

Visualization is not just about displaying data.
Visualization controls how the viewer understands data.

This project builds a Visualization Intelligence Framework designed to:

* control attention
* reduce cognitive load
* add context
* construct narratives from data
* avoid misleading visualization

---

# Core Idea

```
Data ≠ Insight

Insight =
Data
+ Perception Control
+ Context
+ Narrative
```

---

# What This Project Provides

* Perception-driven visualization
* Narrative chart construction
* Context-aware plots
* Uncertainty visualization
* Comparison-first charts
* Storytelling pipeline
* Anti-misleading visualization tools

---

# Project Structure

```
from-data-to-story/
│
├── notebooks/
│   ├── 01_perception_control.ipynb
│   ├── 02_narrative_visualization.ipynb
│   ├── 03_context_and_comparison.ipynb
│   ├── 04_uncertainty_visualization.ipynb
│   ├── 05_cognitive_load_reduction.ipynb
│   ├── 06_process_and_journey.ipynb
│   ├── 07_framing_and_bias.ipynb
│   └── 08_visualization_storytelling.ipynb
│
├── src/vizint/
│
├── examples/
│
└── data/
```

---

# Framework

## 1. Perception Control

* Signal vs Noise
* Focus vs Distraction
* Visual hierarchy
* Saliency
* Highlight standout

Goal:
Make the viewer look where it matters.

---

## 2. Narrative Visualization

* Turning points
* Event annotation
* Story framing
* Regime change

Goal:
Show when things changed.

---

## 3. Context Injection

* Benchmark
* Target
* Reference line
* Comparison

Goal:
Make data meaningful.

---

## 4. Cognitive Load Reduction

* Direct labeling
* Remove legend
* Declutter
* Missing data handling

Goal:
Reduce thinking effort.

---

## 5. Uncertainty Visualization

* Confidence band
* Prediction interval
* Forecast shading

Goal:
Show how certain the prediction is.

---

## 6. Comparative Visualization

* A vs B
* Before vs after
* Distribution comparison
* Small multiples

Goal:
Insight comes from comparison.

---

## 7. Process Visualization

* Waterfall
* Contribution
* Decomposition

Goal:
Show the journey, not only the snapshot.

---

## 8. Framing and Bias Awareness

* Multiple stories from the same data
* Partial vs full context
* Percentage trap
* Misleading axes

Goal:
Avoid misleading visualization.

---

# Visualization Storytelling Pipeline

```
Raw Data
   ↓
Signal Extraction
   ↓
Focus / Highlight
   ↓
Add Context
   ↓
Annotate
   ↓
Narrative
   ↓
Insight
```

---

# Example

```python
from vizint.pipeline import story_chart

story_chart(
    data,
    highlight="trend",
    annotate="event",
    benchmark=target,
    confidence=True
)
```

---

# Notebooks

Each notebook introduces one visualization intelligence concept.

### 01 — Perception Control

Signal vs noise, highlight, focus

### 02 — Narrative Visualization

Turning points, event annotation

### 03 — Context and Comparison

Benchmark, relative performance

### 04 — Uncertainty Visualization

Confidence interval, forecast band

### 05 — Cognitive Load Reduction

Direct labeling, declutter

### 06 — Process and Journey

Waterfall, decomposition

### 07 — Framing and Bias

Misleading visualization examples

### 08 — Full Storytelling Pipeline

Combine all concepts

---

# Philosophy

Visualization is not:

* drawing charts
* plotting lines
* showing values

Visualization is:

Controlled cognition through graphics.

---

# Goals

This project aims to become:

* Visualization intelligence framework
* Storytelling chart library
* Research visualization toolkit
* Decision-focused plotting API

---

# Design Principles

* Highlight the signal
* Reduce cognitive load
* Provide context
* Show uncertainty
* Enable comparison
* Tell a clear story
* Avoid misleading representation

---

# License

MIT
