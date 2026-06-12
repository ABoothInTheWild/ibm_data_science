# Module 9: Capstone Project — Part 1

## Data Collection, Wrangling, and Exploratory Data Analysis

**Author:** Alexander Booth
**Date:** June 2026
**Cohort:** IBM Data Analyst (IBDA), April 2026

---

## Capstone at a Glance

Module 9 is the **IBM Data Analyst capstone**: you act as an **Associate Data Analyst** at a technology consulting firm and analyze the **Stack Overflow Developer Survey** to surface trends in languages, databases, platforms, and frameworks—what developers use today and what they want to learn next.

The capstone runs across multiple phases. **This module is Part 1.** Every lab here builds skills you will reuse in later capstone deliverables.

| Phase | Focus | Where it lives |
| ----- | ----- | -------------- |
| **Part 1** (this module) | Collect, wrangle, and explore the survey data in Jupyter | Lessons 9.01–9.15 |
| **Part 2** (upcoming) | Visualize trends; build dashboards in IBM Cognos Analytics or Google Looker Studio | Module 10 |
| **Part 3** (upcoming) | Present findings in a PowerPoint report for stakeholders | Final capstone delivery |

**Part 1 deliverable mindset:** leave Module 9 with a **cleaned, explored dataset** (e.g. `survey-data-cleaned.csv`) and a clear understanding of compensation, satisfaction, remote work, and technology patterns—ready for charts and dashboards in Part 2.

See `Downloads/IBM DA M9U1V1 Project Overview-en.txt` for the full project brief.

---

## Overview

Part 1 focuses on **getting data into Python and preparing it for analysis**: from **HTTP requests**, **APIs**, and **web scraping** through **data wrangling** (duplicates, missing values, normalization, encoding, feature engineering) to **exploratory data analysis (EDA)**—distributions, outliers, and correlations. The **Stack Overflow Developer Survey** is the capstone dataset throughout.

The core takeaway:

> Raw survey data is not dashboard-ready. Part 1 of the capstone gives you the pipeline to **collect data from the web**, **clean and transform it with Pandas**, and **explore it with statistics and visualizations**—so Part 2 visualizations and Part 3 presentations rest on data you understand and trust.

---

## Why Part 1 Matters

The capstone assumes you can move from messy source data to analysis-ready tables. In Part 1 you:

* **Collect it reliably** — Use HTTP and REST APIs to request structured data, and web scraping (`requests`, BeautifulSoup) when data lives in HTML tables or pages (as in the project overview's API + scraping workflow).
* **Understand it first** — `head()`, `info()`, `describe()`, and dtype checks reveal shape, missing values, and which columns are numeric vs. categorical before you clean or chart.
* **Wrangle it deliberately** — Duplicates, missing values, inconsistent labels, and skewed compensation can invalidate every downstream dashboard; imputation, standardization, one-hot encoding, and log transforms address these systematically.
* **Explore before you visualize** — EDA with histograms, box plots, heatmaps, and correlation matrices surfaces outliers, regional differences, and relationships (e.g. experience vs. job satisfaction) that will drive your Part 2 chart choices.

**The Part 1 end goal:** a cleaned, explored Stack Overflow dataset with documented insights—the foundation for the **Current Technology Usage**, **Future Technology Trends**, and **Demographics** dashboards described in the capstone brief.

---

## What Part 1 Covers

Lessons are organized as a **progressive capstone prep path** from data collection through wrangling to exploratory analysis.

### 1. Data Collection Foundations

* **HTTP and Requests** — How the web works (client, server, URL, request/response); using Python's `requests` library for GET/POST; reading status codes, headers, and body content.
* **Accessing APIs** — Structured data via REST endpoints; parsing JSON responses into Pandas DataFrames; storing results (e.g. Excel/CSV).
* **Web Scraping** — Downloading HTML with `requests`; parsing with BeautifulSoup; extracting links, images, and table data; writing scraped output to CSV.

### 2. Exploring a New Dataset

* **Dataset structure** — Loading CSVs with `read_csv()`; previewing rows; summarizing columns with `info()` and `describe()`.
* **Data types** — Identifying `object`, `int64`, `float64`, and mixed-type columns; understanding why dtypes matter for cleaning and analysis.

### 3. Data Wrangling

* **Duplicates** — Finding duplicate rows with `duplicated()`; analyzing duplicate patterns; removing duplicates with `drop_duplicates()` while preserving data integrity.
* **Missing values** — Detecting nulls with `isnull()`; visualizing gaps (e.g. heatmaps); imputing categorical columns with mode and numeric columns with median/mean.
* **Normalization** — Min-Max scaling and Z-score standardization on compensation fields; log transforms to reduce skew; forward-fill for sequential categorical gaps.
* **Broader wrangling** — Standardizing inconsistent labels (e.g. country names); one-hot encoding (`get_dummies`); feature engineering (e.g. `ExperienceLevel` from `YearsCodePro`); median imputation and scaling in an integrated wrangling workflow.

### 4. Exploratory Data Analysis (EDA)

* **Handling missing data in EDA** — Imputing key columns (`JobSat`, `RemoteWork`, `EdLevel`) so analysis is not blocked by nulls.
* **Key variable analysis** — Value counts and distributions for employment, satisfaction, experience, and languages.
* **Job satisfaction & experience** — Grouping `YearsCodePro` into ranges; median satisfaction by experience; KDE and count plots.
* **Remote work & demographics** — Remote work by employment type and region; cross-tabs of education vs. employment.
* **Programming languages** — Comparing `LanguageHaveWorkedWith` vs. `LanguageWantToWorkWith`; top languages by country/region.
* **Distributions** — KDE plots, grouped bar charts, and heatmaps for categorical and numeric variables.
* **Outliers** — Standard-deviation thresholds and **IQR** bounds on `ConvertedCompYearly`; box plots; building a cleaned DataFrame for further analysis.
* **Correlation** — Pearson and Spearman coefficients; correlation heatmaps and scatter plots linking compensation, `WorkExp`, and `JobSatPoints_1`.

### 5. How Part 1 Connects to the Full Capstone

Part 1 labs map directly to the first stages of the project overview:

* **Collect** (9.01–9.03) — HTTP, APIs, and web scraping mirror how capstone data is gathered before analysis.
* **Explore & wrangle** (9.04–9.09) — Prepare the Stack Overflow survey: duplicates, missing values, normalization, encoding, feature engineering.
* **EDA** (9.12–9.15) — Distributions, outliers, and correlations inform which metrics and chart types you will use in Part 2 dashboards.
* **Part 2 preview** — Visualization and three dashboards (Current Usage, Future Trends, Demographics) in Cognos or Looker Studio.
* **Part 3 preview** — Peer-graded PowerPoint presentation with clear titles, labels, and chart choices.

---

## Labs and Notebooks (Capstone Part 1)

All hands-on notebooks are configured for the **`dev`** conda kernel. Pip install cells are commented out; run labs top-to-bottom after selecting the dev kernel. Work through lessons in order where possible—they follow the capstone workflow from collection to EDA.

### 9.01 — HTTP and Requests

* **Review of Accessing APIs / HTTP** (`PY0101EN-5 3_Requests_HTTP.ipynb`) — Overview of HTTP (URL, request, response); using the `requests` module for GET requests with parameters and POST requests. Supporting file: `example1.txt`.

### 9.02 — Collecting Data with APIs

* **Collecting Job Data Using APIs** (`Collecting_job_data_using_APIs-Lab.ipynb`) — Collect job posting data via a Jobs API (Flask backend); store results in Excel/CSV. Local datasets: `job-postings.csv`, `job-postings.xlsx`, `technology-job-postings.csv`, `technology-job-postings.xlsx`.

### 9.03 — Web Scraping

* **Web Scraping Lab** (`Web-Scraping-Review-Lab.ipynb`) — Download pages with `requests`; scrape links, image URLs, and HTML tables from a live site.
* **Web Scraping Lab Solution** (`Web-Scraping-Lab-Solution.ipynb`) — Reference solution: extract table data and write to CSV. Output example: `popular-language.csv`.

### 9.04 — Exploring the Dataset

* **Lab: Exploring the Dataset** (`M1ExploreDataSet-lab_V2.ipynb`) — Load the Stack Overflow survey data; summarize characteristics; identify column data types. Dataset: `survey-data-with-duplicate.csv` (URL-hosted).

### 9.06 — Duplicates

* **Finding Duplicates Lab** (`Hands-on Lab Finding Duplicates_v2.ipynb`) — Identify duplicate rows; analyze response patterns across key columns; visualize and strategically remove duplicates.
* **Removing Duplicates** (`Hands-on Lab 7 Removing Duplicates_v2.ipynb`) — Remove duplicate rows; impute missing values in `EdLevel` and `ConvertedCompYearly`; preview cleaned data. Dataset: `survey-data-duplicates.csv`.

### 9.07 — Missing Values

* **Finding Missing Values** (`Hands-on Lab 8 Finding Missing Values.ipynb`) — Detect missing values across columns; heatmap visualization; quantify and impute `EdLevel` with the mode; plot distribution after imputation.
* **Impute Missing Values** (`Hands-on Lab 9 Imput Missing Values.ipynb`) — Remove duplicates; impute `RemoteWork`; describe compensation-related columns. Dataset: `survey-data-duplicates.csv`.

### 9.08 — Normalization

* **Data Normalization Techniques** (`Hands-on Lab 10 Normalizing Data.ipynb`) — Handle duplicates and missing `CodingActivities`; Min-Max and Z-score normalization on `ConvertedCompYearly`; visualize normalized distributions.

### 9.09 — Integrated Data Wrangling

* **Data Wrangling Lab** (`M2DataWrangling-lab-v2.ipynb`) — End-to-end wrangling on `survey-data.csv`: structure exploration, country standardization, one-hot encoding `Employment`, imputation, Min-Max/Z-score/log transforms, and `ExperienceLevel` feature engineering.

### 9.12 — Exploratory Data Analysis

* **Lab: Exploratory Data Analysis** (`Hands-on Lab Exploratory Data Analysis.ipynb`) — Impute critical columns; analyze experience vs. job satisfaction; remote work and language trends by region; education vs. employment cross-tabs; save `survey-data-cleaned.csv`.

### 9.13 — Data Distributions

* **Finding How The Data Is Distributed** (`Lab 13 Finding How The Data is Distributed.ipynb`) — Structure and missing-data handling; value counts; KDE of `JobSat`; language comparison bar chart; remote work heatmap by region; Pearson/Spearman correlation; export `survey-data-distributed.csv`.

### 9.14 — Outliers

* **Finding Outliers** (`Lab 14 Finding Outliers.ipynb`) — Industry distribution; high-compensation outliers (3σ rule); IQR detection and box plots; `df_clean` without compensation outliers; age mapping and correlation heatmap.

### 9.15 — Correlation

* **Finding Correlation** (`Lab 15 Finding Correlation.ipynb`) — Compensation histograms; median pay for full-time employees; box plots by country; IQR-cleaned data; heatmap and scatter plots for `ConvertedCompYearly`, `WorkExp`, and `JobSatPoints_1`.

### 9.16 — Live Session

* Placeholder for live session materials (`.gitkeep`).

---

## Datasets

| Dataset | Used in | Notes |
| ------- | ------- | ----- |
| `survey-data.csv` | 9.09, 9.12–9.15 | Primary cleaned survey (URL-hosted) |
| `survey-data-duplicates.csv` | 9.06 (Removing), 9.07, 9.08 | Includes duplicate rows for wrangling labs |
| `survey-data-with-duplicate.csv` | 9.04, 9.06 (Finding) | Exploration and duplicate-detection practice |
| `job-postings.csv` / `.xlsx` | 9.02 | API-collected job data |
| `technology-job-postings.csv` / `.xlsx` | 9.02 | Technology-focused job postings |
| `popular-language.csv` | 9.03 | Web-scraped language popularity |
| `survey-data-cleaned.csv` | 9.12 (output) | EDA lab export |
| `survey-data-distributed.csv` | 9.13 (output) | Distribution lab export |

---

## Supporting Materials

* **Downloads** — `IBM DA M9U1V1 Project Overview-en.txt`: full capstone brief (all parts). Part 1 aligns with data collection, wrangling, and EDA; the overview also describes Part 2 dashboards and Part 3 presentation requirements.

---

## Key Takeaways (Part 1)

* **Capstone role** — You are preparing the **Stack Overflow Developer Survey** for a technology consulting engagement; Part 1 is the analytical foundation.
* **Collection** — **HTTP** and **`requests`** for web resources; **APIs** for structured JSON/CSV data; **web scraping** when data is embedded in HTML.
* **Exploration** — Always start with **`head()`**, **`info()`**, **`describe()`**, and **dtype** review before cleaning.
* **Wrangling** — **`drop_duplicates()`**, **`isnull()` / `fillna()`**, **IQR/outlier removal**, **Min-Max / Z-score / log transforms**, **`get_dummies()`**, and **feature engineering** turn messy survey data into analysis-ready tables.
* **EDA** — **Distributions** (histograms, KDE, box plots), **cross-tabs**, **heatmaps**, and **correlation** (Pearson/Spearman) reveal satisfaction, compensation, remote work, and technology patterns for Part 2.
* **What's next** — Part 2: dashboards in **Cognos** or **Looker Studio**. Part 3: **PowerPoint** presentation and peer review.

---

## Part 1 Completion Checklist

Before moving to capstone visualization and dashboards, you should be able to:

* [ ] Load and describe the Stack Overflow survey (`info`, `describe`, dtypes)
* [ ] Collect supplementary data via HTTP, API, or scraping (9.01–9.03)
* [ ] Remove duplicates and impute missing values in key columns
* [ ] Normalize or transform skewed fields (e.g. `ConvertedCompYearly`)
* [ ] Identify outliers and produce a cleaned DataFrame for analysis
* [ ] Summarize distributions and correlations that will inform dashboard metrics
* [ ] Export a cleaned dataset (e.g. `survey-data-cleaned.csv`) for Part 2

---

## Part 1 — Laying the Capstone Groundwork

Think of this module as the **data foundation** for the capstone—not a separate set of exercises.

The goal is not to memorize every Pandas method.
The goal is to **collect data from real sources**, **clean it with defensible choices**, and **explore it thoroughly**—so Part 2 dashboards and Part 3 presentations answer real business questions about technology trends with data you understand and trust.
