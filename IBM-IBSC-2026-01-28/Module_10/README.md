# Module 10: Interactive Analytics, Dashboards, Predictive Modeling & Capstone Delivery

**Author:** Alexander Booth
**Date:** April 2026
**Cohort:** IBM-IBSC Jan 28, 2026

---

## Overview

This module closes the **SpaceX project** by moving from analysis-ready data to **interactive storytelling** and **predictive models**, then to **capstone communications**: dashboards stakeholders can explore, classification models for **first-stage landing success**, and **reports, decks, and presentation** guidance aligned with professional data science practice.

The core threads:

* **Interactive visual analytics** — **Folium** for **launch-site geography** and proximities; patterns that inform site choice; exporting or embedding map outputs (for example `site_map.html`).
* **Dashboards with Plotly Dash** — Layouts, **inputs** (dropdown, range slider), and **callbacks** linking controls to **Plotly** charts so users can filter and drill into launch outcomes and payload patterns.
* **Predictive analysis** — **Preprocessing**, **train/test split**, **hyperparameter search** (for example **GridSearchCV**), comparing **multiple classifiers**, and **evaluation** (confusion matrix, classification metrics)—with the course lab extending through **model persistence** concepts (for example saving a fitted estimator for inference).
* **Capstone deliverables** — **Report structure**, **example submissions**, and templates for a **written report** and **slide deck**; supplements on **findings reports** and **presenting** results.

---

## Why This Module Matters

Stakeholders rarely live inside your notebooks:

* **Interactive maps and dashboards** make **exploration** and **what-if** views accessible without rerunning code—and they mirror how analytics products are often consumed.
* **Predictive models** turn historical patterns into **scores or labels** for new scenarios, but only when paired with **sound evaluation** and clear **limitations** (small test sets, leakage, and deployment constraints are recurring themes in real projects).
* **Communication**—structured reports and presentations—is how analysis becomes **decisions**; this module’s resources emphasize **clarity**, **structure**, and **professional standards** for capstone work.

---

## Capstone overview and deliverables

You are acting as a **data scientist** on a **realistic business problem** in the SpaceX scenario. Across **Module 9 and Module 10**, the arc looks like this:

* **Collect** data about SpaceX launches (API, scraping, and related sources as in the labs).
* **Clean and structure** the data into analysis- and model-ready tables.
* **Explore** patterns linked to **launch success** (EDA, SQL where assigned, visual analytics).
* **Build and evaluate** models that **predict first-stage landing outcomes** (classification workflow in Module 10).

**Final deliverables** typically include:

* A **GitHub repository** with your **notebooks from Week 9 and Week 10**, plus **outputs** such as **CSVs** (and other artifacts you were asked to produce), and **preferably a README** that explains what to run and where things live.
* A **slide deck** (use the **template** in `10.04 - Capstone Resources/`—rename with your name).
* A **short written summary / report** (structured write-up of the problem, data, methods, results, and limitations—not a dump of notebook cells).

---

## What This Module Covers

### 1. Interactive Maps and Launch-Site Context

* **Geo visualization** — Marking launch sites and nearby features; zoom, pan, and layer-style exploration with **Folium**.
* **Interpretation** — Relating geography and proximity to operational patterns; supporting narrative for **site comparison**.

### 2. Plotly Dash Dashboards

* **Dash application structure** — `app`, `layout`, and **components** (`dcc`, `html`); wiring **inputs** to **outputs** with **callbacks**.
* **SpaceX launch records** — Filtering by **launch site** and **payload** range; **pie** and **scatter**-style charts for success vs. failure and multivariate views.
* **Reference implementation and practice** — Compare the **unsolved** starter script, the **completed** app, and optional **bar-plot** variants as you align with the lab instructions.

### 3. Machine Learning Prediction (SpaceX)

* **End-to-end classification workflow** — **Standardization**, **splitting**, **tuning**, and **testing** on a feature matrix derived from the capstone feature-engineering path.
* **Algorithm comparison** — Exploring **logistic regression**, **support vector machines**, **tree-based models**, **k-nearest neighbors**, and **ensemble / boosting**-style estimators with systematic hyperparameter search where the lab specifies.
* **Evaluation** — **Confusion matrix**, **ROC-oriented** summaries where used, and **classification reports**; optional extension on **serializing** a trained model for **inference** (for example with **pickle**).

### 4. Capstone Reporting and Presentation

* **Report anatomy** — Chapters and flow for a **data science findings** report (see course PDF on report structure).
* **Templates and exemplars** — Placeholder **report** and **PowerPoint** naming patterns plus **example** capstone PDFs for format and depth reference.
* **Professional communication** — Briefs on **successful findings reports**, **presenting** results, and **best practices** for stakeholder-facing delivery.

---

## Labs and Notebooks

### 10.01 — Interactive Visual Analytics (Folium) and Plotly Dash

* **Launch site location lab (Folium / map workflow)** (`10.01/lab_jupyter_launch_site_location.ipynb`)
* **Plotly Dash lab instructions** (`10.01/plotly_dash_lab_instructions.pdf`)

**Supporting assets in `10.01/`:**

* `spacex_launch_dash.csv` — Tabular launch records for the Dash application.
* `spacex-dash-app_UNSOLVED.py` — Starter Dash app for learner tasks.
* `spacex-dash-app.py` — Reference completed Dash application.
* `spacex-dash-app-bar-plots.py` — Alternate or extension script using bar-plot style figures.
* `site_map.html` — Example or exported interactive map output (open in a browser).

### 10.02 — Machine Learning Prediction (SpaceX)

* **SpaceX machine learning prediction (classification capstone lab)** (`10.02/SpaceX_Machine Learning Prediction_Part_5.ipynb`)

### 10.03 — Live Session

* Placeholder for live session materials (`10.03 - Live Session/.gitkeep`)

### 10.04 — Capstone Resources

* **Report structure (course chapter excerpt)** (`10.04 - Capstone Resources/Getting Started with Data Science - Chapter 3 - The Report Structure.pdf`)
* **Example capstone submissions** (`10.04 - Capstone Resources/Example Capstone Report/`)
  * `Michelle Thys M10U4 Capstone project report.pdf`
  * `Michelle Thys M10U4 Capstone project.pdf`
* **Learner templates (rename with your name)** (`10.04 - Capstone Resources/`)
  * `First Name Last Name M10U4 Capstone project.pdf`
  * `First Name Last Name M10U4 Capstone project.pptx`

---

## Supporting Materials

### Downloads (Lecture Transcripts / Notes)

Located in `Downloads/`:

* `Data Visualization and Dashboard Overview-en.txt`
* `Predictive Analysis Overview-en.txt`
* `Elements Of A Successful Data Findings Report-en.txt`
* `Best Practices For Presenting Your Findings-en.txt`

---

## Key Takeaways

* **Interactivity** — Maps and dashboards should answer **repeatable questions** (filters, comparisons, ranges)—design controls so non-technical stakeholders can explore safely.
* **Dash fundamentals** — Master **layout → callback → figure update**; keep data loading and chart logic **deterministic** so the app behaves predictably as inputs change.
* **Modeling discipline** — **Preprocess consistently**, **tune** without peeking at the test set, and **report metrics** suited to the business question; know when a small holdout set limits how strongly you can claim generalization.
* **Persistence** — Saving a **fitted** model (or full **pipeline**, when you use one) is how notebook experiments connect to **batch scoring** or **services**—always match **training-time** preprocessing at **inference** time.
* **Delivery** — A strong capstone pairs **evidence** (notebooks, dashboards, metrics) with a **structured narrative** in the report and a **focused** deck for executive communication.

---

## From Dashboards and Models to a Finished Capstone Story

Module 10 is where **technical work becomes shareable**: geographic and dashboard views for discovery, **rigorous** predictive comparisons where the rubric requires them, and **polished** reporting—so your SpaceX storyline is **understandable**, **auditable**, and **convincing** to stakeholders.
