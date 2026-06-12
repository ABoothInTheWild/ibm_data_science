# Module 10: Capstone Project — Part 2

## Data Visualization, Dashboards, and Presenting Your Findings

**Author:** Alexander Booth
**Date:** June 2026
**Cohort:** IBM Data Analyst (IBDA), April 2026

---

## Capstone at a Glance

Module 10 is the **second half of the IBM Data Analyst capstone**. Continuing the **Associate Data Analyst** scenario from Module 9, you take the cleaned **Stack Overflow Developer Survey** data and turn it into **visualizations, dashboards, and a stakeholder presentation** about what developers use today and what they want to learn next.

| Phase | Focus | Where it lives |
| ----- | ----- | -------------- |
| **Part 1** | Collect, wrangle, and explore the survey data in Jupyter | Module 9 (Lessons 9.01–9.15) |
| **Part 2** (this module) | Visualize trends with Matplotlib/Seaborn; build dashboards in Google Looker Studio | Lessons 10.02–10.09 |
| **Part 3** (this module) | Present findings in a PowerPoint report for stakeholders | Lesson 10.10 + capstone deck |

**Part 2/3 deliverable mindset:** leave Module 10 with a **set of clear, honest charts**, a **dashboard**, and a **findings presentation**—all built on the cleaned dataset from Part 1.

See Module 9's `README.md` for Part 1 (collection, wrangling, and EDA), which this module builds directly on.

---

## Overview

Part 2 focuses on **communicating** what the data shows. You build the full range of chart types in Python—**histograms, box plots, scatter and bubble plots, pie charts, stacked charts, line charts, and bar charts**—first from data stored in an **SQLite database** (queried with SQL) and then directly from a **Pandas DataFrame**. You then move from notebooks to **Google Looker Studio** dashboards and a **PowerPoint findings report**.

The core takeaway:

> A cleaned dataset only creates value when its insights are *seen and understood*. Part 2 of the capstone gives you the toolkit to **choose the right chart for each question**, **build interactive dashboards**, and **present findings clearly**—so decision-makers can act on developer technology trends.

---

## Why Part 2 Matters

The capstone is graded on whether stakeholders can understand your conclusions. In Part 2 you:

* **Match the chart to the question** — Histograms and box plots for **distributions**, scatter and bubble plots for **relationships**, pie and stacked charts for **composition**, line and bar charts for **trends and comparisons**.
* **Work from real storage** — Several labs read the survey from an **SQLite database** via SQL queries (`pd.read_sql_query`), mirroring how analysts pull data from an RDBMS before charting it.
* **Handle messy survey fields** — Survey columns need care before plotting: `Age` is a set of text buckets (mapped to numeric midpoints), `YearsCodePro` mixes numbers with `"Less than 1 year"`/`"More than 50 years"`, and technology columns (languages, databases, tools) are **multi-select** strings that must be split and exploded before counting.
* **Go from notebook to dashboard to deck** — Looker Studio turns the cleaned data into interactive, shareable dashboards; the findings report turns charts into a narrative for stakeholders.

**The Part 2 end goal:** dashboards and a presentation covering **Current Technology Usage**, **Future Technology Trends**, and **Demographics**, as described in the capstone brief.

---

## What Part 2 Covers

Lessons progress from **plotting in Python** (SQL-sourced and DataFrame-sourced) through **dashboarding** to **presenting findings**.

### 1. Visualizing Data from a Database (SQL → Pandas → Matplotlib)

* **Working with an RDBMS** — Load the survey into **SQLite**, list tables, describe schemas, and run **`GROUP BY`** queries; pull just the columns you need into Pandas with `pd.read_sql_query` before plotting.
* **All four visualization goals** — Distribution, relationship, composition, and comparison, demonstrated end-to-end on the survey data.

### 2. Core Chart Types in Python

* **Histograms** — Distribution of a single variable (compensation, coding experience); overlay by group; bin counts and skew (compensation is capped at the 99th percentile so a few extreme values don't flatten the chart).
* **Box plots** — Median, quartiles, IQR, and outliers; converting the categorical `Age` field to numeric for a box plot.
* **Scatter plots** — Relationships between two numeric variables (age vs. job satisfaction, compensation vs. satisfaction), with a **Seaborn regression line** (`sns.regplot`) to show the trend.
* **Bubble plots** — A third dimension via bubble size (e.g., age or respondent count) layered onto a scatter plot.
* **Pie charts** — Composition of a whole; **top-5** databases, developer roles, operating systems, languages, collaboration tools, AI tools, web frameworks, and embedded technologies (splitting multi-select columns first).
* **Stacked charts** — Composition *and* comparison at once; job-satisfaction components, compensation, databases, languages, and platforms stacked across age groups and employment types.
* **Line charts** — Trends across an ordered axis; median compensation by age group and by years of experience; job satisfaction by experience level.
* **Bar charts** — Distribution, composition, and comparison; horizontal (`MainBranch`), vertical top-5 (desired languages), grouped (compensation by age), and respondent counts by country.

### 3. Dashboards in Google Looker Studio

* **Getting started with Looker Studio** — Connect data and build a first dashboard (`10.09/getting-started-looker.pdf`).
* **Word clouds in Looker Studio** — Add a community word-cloud visualization (`10.09/word-cloud-looker.pdf`).

### 4. Presenting Your Findings (Part 3)

* **Elements of a successful data findings report** — What a findings report is and why effective reporting matters (`Downloads/IBM DA M10U3V1 ...`).
* **Best practices for presenting your findings** — How to present to an audience: clear titles, labels, and chart choices (`Downloads/IBM DA M10U3V2 ...`).
* **Capstone presentation** — Fill in the provided PowerPoint template (`First Name Last Name M10U3 Capstone project.pptx`) for the peer-graded review.

---

## Labs and Notebooks (Capstone Part 2)

All hands-on notebooks are configured for the **`dev`** conda kernel. `pip install` cells are commented out, and each lab downloads its dataset at runtime via a small `urllib` helper (the large survey files are **not** committed to the repo). Run labs top-to-bottom after selecting the `dev` kernel; work through the chart types in order.

### 10.02 — Data Visualization (RDBMS)

* **Lab 16 — Data Visualization** (`Lab 16 Data Visualization.ipynb`) — Load the survey CSV, write it to an **SQLite** database, and use SQL queries to drive one of each chart type: histogram (`CompTotal`), box plot (`Age`), scatter (`Age` vs `WorkExp`), bubble (`TimeSearching` vs frustrations, size = `Age`), pie (top-5 `DatabaseWantToWorkWith`), stacked bar (median `TimeSearching`/`TimeAnswering`), line (median `CompTotal` by age), and horizontal bar (`MainBranch`).

### 10.03 — Histograms and Box Plots

* **Lab 17 — Histogram** (`Lab 17 Data Visualization - Histogram.ipynb`) — Histograms from the SQLite survey database: distribution of `CompTotal` and `YearsCodePro`, comparison of `CompTotal` and `TimeSearching` by age group, composition of top databases and `RemoteWork`, and `JobSat` by experience band.
* **Lab 18 — Box Plot** (`Lab 18 Box Plot.ipynb`) — Box plots of compensation and other fields by category, pulled from the SQLite database (worked reference lab).

### 10.04 — Scatter and Bubble Plots

* **Lab 19 — Scatter Plot** (`Lab 19 Scatter Plot.ipynb`) — Scatter relationships (age vs. satisfaction, compensation vs. satisfaction), a **Seaborn `regplot`** trend line, a bubble plot, and group comparisons by employment type and country. Dataset loaded directly from the survey URL.
* **Lab 20 — Bubble Plots** (`Lab 20 Bubble Plots.ipynb`) — Bubble plots across demographics and technology preferences: participation frequency, compensation vs. satisfaction, languages/collaboration tools by age, developer roles, web frameworks, and admired languages by country (bubble size = count or age).

### 10.05 — Pie and Stacked Charts

* **Lab 21 — Pie Charts** (`Lab 21 Pie Charts.ipynb`) — Top-5 composition pies for databases, developer roles, operating systems, languages, collaboration tools, admired languages, AI tools, web frameworks, and embedded technologies.
* **Lab 22 — Stacked Charts** (`Lab 22 Stacked Charts.ipynb`) — Stacked bars for job-satisfaction components by age group and employment status, compensation + satisfaction by age, and preferred databases / admired languages / platforms by group.

### 10.06 — Line and Bar Charts

* **Lab 23 — Line Charts** (`Lab 23 Line Charts.ipynb`) — Trend lines: median `ConvertedCompYearly` by age group and for ages 25–45, and job satisfaction across years of experience.
* **Lab 24 — Bar Charts** (`Lab 24 Bar Charts.ipynb`) — A full pass through distribution, relationship, composition, and comparison: histogram, box plot, scatter, bubble, and horizontal/vertical/grouped/stacked bars (`MainBranch`, `LanguageWantToWorkWith`, `DatabaseHaveWorkedWith`, compensation by age, respondents by country).

### 10.09 — Dashboards (Google Looker Studio)

* **Getting Started with Looker** (`10.09/getting-started-looker.pdf`) and **Word Cloud in Looker** (`10.09/word-cloud-looker.pdf`) — Build the capstone dashboards.

### 10.10 — Live Session

* Placeholder for live session materials (`.gitkeep`).

---

## Datasets

| Dataset | Used in | Notes |
| ------- | ------- | ----- |
| `survey-data.csv` | 10.02, 10.04–10.06 | Cleaned Stack Overflow survey (URL-hosted; downloaded at runtime) |
| `survey-results-public.sqlite` | 10.03 (Labs 17, 18) | Full public survey as an SQLite database (downloaded at runtime) |
| `survey-data.sqlite` | 10.02 | Created by Lab 16 from the CSV |

> The survey CSV (~160 MB) and SQLite database (~210 MB) are **downloaded at runtime** and are git-ignored, so they are not stored in the repository.

---

## Supporting Materials

* **Looker Studio guides** (`10.09/`) — Step-by-step PDFs for building dashboards and a word-cloud visualization.
* **Downloads** — Transcripts on **Elements of a Successful Data Findings Report** and **Best Practices for Presenting Your Findings**.
* **Capstone presentation template** — `First Name Last Name M10U3 Capstone project.pptx` for the Part 3 peer-graded deliverable.

---

## Key Takeaways (Part 2)

* **Chart selection** — Distribution → **histogram/box**; relationship → **scatter/bubble**; composition → **pie/stacked**; trend & comparison → **line/bar**.
* **SQL + Pandas** — Pull survey data from **SQLite** with `pd.read_sql_query`, then visualize with **Matplotlib**/**Seaborn**.
* **Prep before plotting** — Map categorical `Age` to numeric midpoints, coerce `YearsCodePro` to numbers, and **split/explode** multi-select technology columns before counting.
* **From notebook to stakeholder** — Move charts into **Looker Studio** dashboards and a **PowerPoint** findings report with clear titles, labels, and an honest story.

---

## Part 2 Completion Checklist

Before finishing the capstone, you should be able to:

* [ ] Pull survey data from an SQLite database with SQL and load it into Pandas
* [ ] Build each core chart type (histogram, box, scatter, bubble, pie, stacked, line, bar)
* [ ] Convert categorical/text survey fields to numeric and split multi-select columns
* [ ] Add a regression line to a scatter plot with Seaborn
* [ ] Build a dashboard in Google Looker Studio
* [ ] Produce a findings presentation (PowerPoint) for the peer-graded review

---

## Part 2 — Telling the Capstone Story

Think of this module as the **communication layer** of the capstone—where analysis becomes insight that others can act on.

The goal is not to memorize every Matplotlib call.
The goal is to **choose the right visualization for each question**, **build dashboards stakeholders can explore**, and **present findings clearly and honestly**—so the technology trends you uncovered in Part 1 drive real decisions.
