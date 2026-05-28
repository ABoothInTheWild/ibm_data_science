# Module 8: Data Visualization

**Author:** Alexander Booth
**Date:** May 2026

---

## Overview

This module focuses on **data visualization in Python**: from foundational plotting with **Matplotlib** and **Pandas** through specialized charts (line, bar, area, histogram, pie, box, scatter, bubble), to **Seaborn** regression and categorical plots, **Folium** maps (markers, choropleths), and **Plotly**/ **Dash** for interactive dashboards. You learn to choose the right plot for the question, avoid misleading visuals, and build reactive web applications that answer business questions with data.

The core takeaway:

> Data visualization is the graphical representation of data and information. It helps us understand complex datasets, highlight patterns and trends, communicate insights to stakeholders, and make informed decisions. This module gives you the full toolkit: **plot libraries and types**, **static and interactive charts**, **geospatial maps**, and **dashboarding** so you can tell a story with data.

---

## Why Data Visualization Matters

Once you have data, you need to:

* **Understand and communicate it** — Raw tables are hard to grasp; charts and graphs make patterns, trends, and relationships visible and easier to explain.
* **Choose the right visual** — Line plots for trends over time, bar charts for comparing categories, scatter plots for relationships, histograms for distributions, maps for geospatial data; each type has appropriate use cases and pitfalls (e.g. axis scales that mislead).
* **Go from static to interactive** — Plotly and Dash let you build web-based dashboards where users can filter, drill down, and explore; callbacks connect inputs (e.g. year, region) to updated charts in real time.
* **Visualize geography** — Folium creates interactive maps with markers and choropleths (e.g. immigration to Canada by country) so location-based insights are clear and explorable.

**The end goal** is to go from “data in a table” to “clear, honest, and actionable visuals”—whether that is a simple line chart, a regression plot, a choropleth map, or a multi-panel dashboard for stakeholders.

---

## What This Module Covers

The module is organized as a **progressive path** from plot libraries and fundamentals through chart types, geospatial visualization, and interactive dashboarding.

### 1. Overview and Foundations

* **Overview of Data Visualization** — What data visualization is and why it matters; uses (understanding complexity, highlighting patterns, communicating insights, telling a story); best practices; examples (e.g. COVID-19 dashboards, Airbnb pricing, Spotify Pie, Netflix dashboards).
* **Plot Libraries** — Popular Python libraries: **Matplotlib** (general-purpose, wide customization), **Pandas** (plotting on DataFrames, built on Matplotlib), **Seaborn** (statistical plots, themes, color palettes), **Folium** (geospatial maps), **Plotly** (interactive, web-based), **PyWaffle** (waffle charts); strengths and when to use each.
* **Types of Plots** — Line, bar, scatter, box, histogram: characteristics, use cases (e.g. trends over time, comparing categories, relationships, distributions), and how misleading axis scales or bar choices can distort the message.
* **Understanding the Lab Environment** — How to run labs and use the datasets (e.g. immigration to Canada).
* **Dataset on Immigration to Canada** — The course’s recurring dataset: immigration from 1980 to 2013 by country; structure and typical uses in exercises.

### 2. Exploring Data with Pandas (Pre-requisite for Visualization)

* **Exploring and Pre-processing with Pandas** — Pandas as the foundation for wrangling and exploring data before plotting; indexing, selection, filtering, sorting; preparing the immigration dataset for visualization.

### 3. Matplotlib and Basic Plotting

* **Introduction to Matplotlib** — What Matplotlib is (created by John Hunter for scientific visualization); architecture (backend, artist, scripting layers); FigureCanvas, Renderer, Artist objects; when to use scripting vs. artist layer.
* **Basic Plotting with Matplotlib** — Creating figures and axes; simple line and scatter plots; customizing colors, markers, labels, titles, legends.
* **Line Plots** — Data points connected by lines; trends over time (e.g. immigration, stock prices); continuous independent variables; cause-and-effect visualization; avoiding misleading scales.
* **Introduction to Matplotlib and Line Plots (Lab)** — Hands-on line plots with the immigration dataset.

### 4. More Chart Types: Area, Histogram, Bar, Pie, Box, Scatter, Bubble

* **Area Plots** — Stacked or overlapping areas to show composition or cumulative change over time.
* **Histograms** — Distributions of a single variable; bins and frequency; when to use histograms vs. bar charts.
* **Bar Charts** — Rectangular bars for magnitude; vertical vs. horizontal; comparing categories, rankings, contributions; axis scale best practices.
* **Pie Charts** — Proportions of a whole; when they work and when they can be hard to read.
* **Box Plots** — Quartiles, median, IQR, outliers; comparing distributions across groups.
* **Scatter Plots** — Two variables on Cartesian axes; relationships, correlation, outliers, clusters.
* **Bubble Plots** — Scatter plots with a third dimension encoded by bubble size.
* **Plotting Directly with Matplotlib** — Using the Matplotlib API directly (e.g. subplots, fine-grained control) for custom layouts.

### 5. Seaborn and Specialized Plots

* **Seaborn and Regression Plots** — Seaborn as a higher-level layer on Matplotlib; built-in themes and palettes; **regression plots** (scatter + regression line + confidence interval); categorical and distribution plots; integration with Pandas and NumPy.

### 6. Waffle Charts, Word Clouds, and Regression Plots

* **Waffle Charts** — Grid-based representation of proportions (e.g. PyWaffle); useful for categorical composition.
* **Word Clouds** — Visualizing text frequency; word size proportional to frequency.
* **Regression Plots (Seaborn)** — Reinforcing regplot and related tools for trend visualization.

### 7. Geospatial Visualization with Folium

* **Introduction to Folium** — Folium for visualizing geospatial data; creating maps from latitude/longitude; interactive zoom; map styles (OpenStreetMap, Stamen Toner, Stamen Terrain); centering and zoom_start.
* **Maps with Markers** — Adding markers to maps; `folium.Marker` and popups; FeatureGroup and layers for organizing markers (e.g. provinces, points of interest).
* **Choropleth Maps** — Thematic maps where regions are shaded by a statistical variable (e.g. population, immigration); GeoJSON for boundaries; Folium choropleth with a DataFrame and key columns; example: world map of immigration to Canada.

### 8. Plotly and Interactive Charts

* **Introduction to Plotly** — Plotly as an interactive, open-source library; Plotly Graph Objects (low-level: figures, traces, layout) vs. Plotly Express (high-level, concise); line, scatter, bar, pie, 3D, choropleths; display in Jupyter, HTML, or Dash apps.

### 9. Dash and Dashboarding

* **Dashboarding Overview** — Benefits of interactive dashboards (real-time visuals, central view, stakeholder understanding, informed decisions); comparison of report-as-tables vs. dashboard; answering critical business questions with charts and drill-down.
* **Introduction to Dash** — Dash as an open-source Python UI library for reactive web apps; Flask backend, React front end; layout (structure and placement of charts) vs. interactivity (callbacks); **dash_core_components** (sliders, dropdowns, date pickers, graphs) and **dash_html_components** (HTML tags as Python components).
* **Make Dashboards Interactive** — **Callback functions**: Python functions decorated with `@app.callback`; Input (component + property) and Output (component + property); when an input changes, the callback runs and updates the output (e.g. graph); examples: single input (year → bar chart), multiple inputs; connecting core and HTML components.

### 10. Labs and Notebooks

* **8.02 — Dataset and Pandas**
    * **Exploring and Pre-processing with Pandas** (`DV0101EN-Exercise-Dataset-Preprocessing-Exploring-with-Pandas.ipynb`) — Explore and pre-process the Immigration to Canada dataset (1980–2013) using Pandas: indexing, selection, filtering, sorting. Prepares data for later visualization labs.
* **8.03 — Matplotlib and Line Plots**
    * **Introduction to Matplotlib and Line Plots** (`DV0101EN-Exercise-Introduction-to-Matplotlib-and-Line-Plots_.ipynb`) — Create line plots with Matplotlib using the immigration dataset; practice basic customization and trend visualization.
* **8.05 — Area, Histogram, Bar**
    * **Area Plots, Histograms, and Bar Charts** (`DV0101EN-Exercise-Area-Plots-Histograms-and-Bar-Charts_.ipynb`) — Build area plots, histograms, and bar charts; compare distributions and compositions over time or by category.
* **8.06 — Pie, Box, Scatter, Bubble**
    * **Pie Charts, Box Plots, Scatter Plots, and Bubble Plots** (`DV0101EN-Exercise-Pie-Charts-Box-Plots-Scatter-Plots-and-Bubble-Plots.ipynb`) — Create pie, box, scatter, and bubble plots; explore relationships and distributions with multiple chart types.
* **8.07 — Plotting with Matplotlib**
    * **Plotting Directly with Matplotlib** (`DV0101EN-Exercise-Plotting-directly-with-Matplotlib.jupyterlite.ipynb`) — Use Matplotlib’s API directly for subplots and custom figure layout.
* **8.10 — Waffle, Word Cloud, Seaborn**
    * **Waffle Charts, Word Clouds, and Regression Plots** (`DV0101EN-Exercise-Waffle-Charts-Word-Clouds-and-Regression-Plots.ipynb`) — Build waffle charts and word clouds; create regression plots with Seaborn (e.g. trend lines and confidence intervals).
* **8.11 — Maps and Geospatial**
    * **Creating Maps and Visualizing Geospatial Data** (`DV0101EN-Exercise-Creating-maps-visualizing-geospat.ipynb`) — Use Folium to create interactive maps; add markers and build choropleth maps (e.g. world map of immigration to Canada). Dataset/asset: `world_countries.json`.
* **8.12 — Plotly and Dash**
    * **Basic Plotly Charts** (`4 3_Plotly_Basics.ipynb`) — Use Plotly Graph Objects and Plotly Express to create interactive charts (line, scatter, etc.) on the Airline Reporting Carrier On-Time Performance dataset.
    * **Dash Basics** (`4 4_Dash_Basics.py`) — Build a simple Dash app: layout with title, description, and a Plotly pie chart (e.g. distance group proportion by flights); run the app in the browser.
    * **Dash Interactivity** (`dash_interactivity.py`, `dash_interactivity_barplot.py`) — Add callbacks to Dash: connect an input (e.g. year) to an output (e.g. bar plot of top carriers); demonstrate reactive updates.
    * **Flight Delay Dashboard** (`flight_delay.py`) — Multi-panel Dash dashboard for flight delay statistics; input year; multiple graphs (carrier, weather, NAS, security, late aircraft delay) updated via callback.
* **8.13 — Practice and Wildfire Dashboard**
    * **Australia Wildfire Dashboard** (`Dash_wildfire.py`) — Full Dash app: region selector (e.g. RadioItems for Australian regions), dropdowns, and callbacks to visualize historical wildfire data (e.g. by month, year); uses Plotly and Dash dependencies (Input, Output).
    * **Practice Assignment Part 1** (`Practice_Assignment_Part1.ipynb`) — Practice assignment: analyze wildfire activities in Australia using Matplotlib, Pandas, Seaborn, and Folium; create informative plots and maps.
* **8.14 — Live Session**
    * Placeholder for live session materials (e.g. `.gitkeep`).

### 11. Supporting Materials

* **Downloads** — Transcripts and notes (TXT) for all video topics: Overview of Data Visualization, Types of Plots, Plot libraries, Introduction to Matplotlib, Basic Plotting with Matplotlib, Line plots, Area plots, Histograms, Bar charts, Box plots, Pie charts, Scatter plots, Plotting Directly with Matplotlib, Waffle charts Word cloud, Seaborn and regression plots, Introduction to Folium, Choropleth Maps, Maps with Markers, Introduction to Plotly, Introduction to Dash, Dashboarding Overview, Make dashboards interactive, Dataset on immigration to Canada, Understanding the Lab Environment.

---

## Key Takeaways

* **Visualization purpose** — Use charts to understand data, reveal patterns, and communicate insights; choose plot type and axis scales to avoid misleading the audience.
* **Plot libraries** — **Matplotlib** for general-purpose and direct control; **Pandas** for quick DataFrame plots; **Seaborn** for statistical and regression plots; **Folium** for interactive maps; **Plotly** for interactive web-ready charts; **PyWaffle** for waffle charts.
* **Chart types** — **Line** for trends over time; **bar** for comparing categories; **scatter** for relationships; **histogram** for distributions; **box** for quartiles and outliers; **pie** for proportions; **area** for composition over time; **bubble** for a third dimension.
* **Geospatial** — **Folium** builds interactive maps; add **markers** and **choropleths** with GeoJSON and DataFrames to show spatial patterns (e.g. immigration by country).
* **Interactive dashboards** — **Dash** layout (HTML + core components) plus **callbacks** (Input → function → Output) create reactive apps; **Plotly** figures embed in Dash for hover, zoom, and drill-down; multi-panel dashboards (e.g. flight delay, wildfire) tie the module together.

---

## The Data Scientist’s Visualization Toolkit

Think of this module as building your **visualization toolkit**, not just copying one chart.

The goal is not to memorize every Matplotlib or Plotly option.
The goal is to **choose the right plot for the question**, **build clear and honest visuals**, and **deliver interactive dashboards** when stakeholders need to explore data—so you can tell a story with data from static plots to maps to live dashboards.
