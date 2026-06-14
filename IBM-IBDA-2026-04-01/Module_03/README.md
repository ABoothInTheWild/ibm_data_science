# Module 3: Data Visualization and Dashboards

**Author:** Alexander Booth
**Cohort:** April 2026 (IBM Data Analyst / IBDA)

---

## Overview

This module is about **turning analysis into insight**—taking prepared data and making it understandable through charts, dashboards, and data stories. You start in **Excel** (basic charts, advanced charts, and a simple dashboard), then move to two dedicated business intelligence tools: **IBM Cognos Analytics** and **Google Looker Studio**. The emphasis is less on memorizing menus and more on **choosing the right chart, building a coherent dashboard, and telling a clear data story**.

The core takeaway:

> Analysis only matters if people can understand it. This module teaches you how to **visualize** results and assemble them into **dashboards**—in Excel and in BI tools—so your findings drive decisions.

---

## Why Visualization and Dashboards Matter

A correct number buried in a spreadsheet rarely changes anyone's mind. Stakeholders respond to **visuals**:

* **Charts** — Surface trends, comparisons, distributions, and outliers far faster than a table
* **Dashboards** — Bring related charts together into a single, monitored view
* **Data stories** — Frame the visuals so the audience knows what to take away and what to do next

Building this skill lets you:

* Pick the chart type that actually fits the question (trend vs. comparison vs. composition vs. relationship vs. distribution)
* Assemble interactive dashboards instead of static screenshots
* Communicate insights to non-technical audiences without losing the message

At its core, this module answers a key question: *Now that I have the analysis, how do I make people see it?*

---

## What This Module Covers

The content is a **progression**: chart fundamentals in Excel, then dashboards in Excel, then the same ideas in two BI platforms, and finally a capstone assignment that brings it together. The hands-on labs run in **Excel for the web** (free), the **IBM Cognos Analytics** trial, and the free **Google Looker Studio**.

### 1. Charts in Excel

* **Introduction to charts** — Matching a chart to a question
* **Creating basic charts** — Column, area, bar, and line charts (including line/bar charts built from a **PivotTable**)
* **Advanced chart types** — Treemaps and **sunburst** charts, **scatter** charts, **histograms**, **filled maps**, **sparklines**, and **PivotCharts**

### 2. Dashboards in Excel

* **Introduction to dashboarding** — What a dashboard is and what makes a good one
* **Creating a simple dashboard in Excel** — Combining charts and adding **slicers** to filter interactively
* **Using dashboards to present data results** — Layout, focus, and interactivity
* **Using visualizations to tell a data story** — Framing visuals so the audience reaches the right conclusion

### 3. IBM Cognos Analytics

* **Getting started** — Signing up for the Cognos Analytics trial, navigating the UI, uploading data, and starting a dashboard from templates
* **Creating dashboard visualizations** — Different methods for building visuals on a dashboard
* **Advanced dashboard capabilities** — Calculations, keeping/excluding data points, top/bottom, navigation paths, and filtering

### 4. Google Looker Studio

* **Getting started** — Signing up, navigating the UI, creating a data source via a connector, and applying themes/layouts
* **Creating and configuring visualizations** — Page settings, blending data from multiple tables, and charts (bar, bubble, heatmap)
* **Advanced charts (optional)** — Community visualizations (Vega/Vega-Lite), including a **word cloud** and a scattered bubble chart

### 5. Final Assignment (Capstone)

The module closes with a **peer-graded final assignment**, offered in **two equivalent versions**—one in **Cognos**, one in **Looker**. The scenario: you are a **regional manager for a chain of car dealerships** and must build dashboards to understand the sales and service departments. You create:

* A **Sales** dashboard (tabbed, four small panels + one large): Profit, Quantity sold, Quantity sold by model (bar chart), Average quantity sold, and Profit by Dealer ID (column chart, sorted)
* A **Service** dashboard (2×2): recalls per model (column chart), customer sentiment (treemap), cars sold per month vs. profit (line + column combo), and recalls by model and affected system (heatmap)

You then export the dashboard to **PDF** for submission. Doing the same brief in two tools highlights what's universal about dashboarding versus what's tool-specific.

---

## How the Materials Are Organized

The numbered subfolders follow the course order. **PDFs** are the step-by-step lab and exercise guides; **XLSX/CSV** files are the datasets they use. Use the table below to find a topic quickly.

| Folder / File | Contents and focus |
|---------------|--------------------|
| **3.00** | `ibda-3.0-spreadsheet-basics.pdf`, `ibda-3.0-excel-for-web.pdf` — prerequisite refreshers (the same *Intro to Excel for the web* and *Spreadsheet Basics* labs from Module 2). Dataset: `indian_startup_funding_Lab2.xlsx`. |
| **3.02** | `3.2-creating-basic-charts.pdf` — **Lab: Creating Basic Charts** (column, area, bar, line). Dataset: `Car_Sales_Kaggle_DV0130EN_Lab1_Start.xlsx`. |
| **3.04** | `3.4-advanced-charts.pdf` (**Creating Advanced Charts** — sunburst, scatter, histogram) and `3.4-excel-dashboard.pdf` (**Creating a Simple Dashboard**, with slicers). Datasets: `..._Lab2_Start.xlsx`, `..._Lab3_Start.xlsx`, `..._Lab3_Ex2Start.xlsx`. |
| **3.07** | `3.7-getting-started-cognos.pdf`, `3.7-dashboard-cognos.pdf`, `3.7-advanced-dashboard-cognos.pdf` — IBM Cognos Analytics: setup/navigation, building dashboard visualizations, and advanced capabilities. Dataset: `CustomerLoyaltyProgram.csv`. |
| **3.08** | `3.8-getting-started-looker.pdf`, `3.8-visualizations-looker.pdf`, `3.8-advanced-charts-looker.pdf` — Google Looker Studio: setup, configuring visualizations, and (optional) advanced community charts. Dataset: `CustomerLoyaltyProgram.csv`. |
| **3.09** | `3.9-cognos-lab.pdf`, `3.9-looker-lab.pdf` — the **final assignment** (car-dealership Sales + Service dashboards) in Cognos and Looker. Datasets in `Automotive_Industry/` (XLSX) and `Looker_Dataset/` (CSV), plus `CarSalesByModelStart.xlsx`. |
| **`IBM Data Analyst M3U3 Live session presentation.pdf`** | Slide deck for the Module 3 live session—a guided demo of Excel PivotChart visuals and Cognos/Looker dashboards on the car-dealership dataset. |
| **3.10 - Live Session** | Placeholder folder for live session materials (the deck above lives at the module root). |
| **Downloads** | Text transcripts/notes (`.txt`) for the video topics—useful for review without opening a PDF. |

> Sections `3.01`, `3.03`, `3.05`, and `3.06` are video/reading topics in the course with no separate lab files, so they have no folder here.

---

## `Downloads` folder

The **`Downloads`** directory holds **text companion notes** aligned with the course videos—handy for quick review. Topics include: introduction to charts, creating basic charts in Excel, creating treemaps/scatter charts/histograms, creating filled map charts and sparklines, using the Excel PivotChart feature, introduction to dashboarding, creating a simple dashboard in Excel, using dashboards to present data results, using visualizations to tell a data story, and the Cognos Analytics set (introduction and sign-up, navigating the interface, creating a simple dashboard, and advanced dashboard capabilities). Match the filename to the section you are studying.

---

## Key Takeaways

* **Chart choice is the first decision** — match the visual to the question (trend, comparison, composition, relationship, distribution).
* **Excel** covers a lot of ground: basic charts, advanced types (sunburst/treemap, scatter, histogram, filled maps, sparklines), **PivotCharts**, and a slicer-driven dashboard.
* **Dashboards** combine related visuals into one monitored view; good ones have focus and a clear takeaway.
* **Data storytelling** is what turns a dashboard into a decision—frame the visuals for your audience.
* **BI tools** — **IBM Cognos Analytics** and **Google Looker Studio** scale visualization beyond a single spreadsheet with connected data sources, calculations, and interactivity.
* The **final assignment** proves the point by building the same Sales and Service dashboards in two different tools.

---

## The Data Analyst's Visualization Toolkit

Think of this module as building your **visualization and communication toolkit**, not as learning one chart wizard.

The goal is not to memorize every menu in Excel, Cognos, or Looker. The goal is to **choose the right visual, assemble a coherent dashboard, and tell a clear data story**—so the analysis you do in the rest of the course actually lands with the people who need it. The tool is temporary; the thinking is permanent.
