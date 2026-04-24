# Module 2: Python Basics for Data Science

**Author:** Alexander Booth  
**Cohort:** April 2026 (IBM Data Science / IBSC)

---

## Overview

Module 2 is a **practical Python track** for data work. You will move from language fundamentals—syntax, types, and collections—through control flow, files, and **Pandas** / **NumPy**, and into **HTTP APIs** and **web scraping** so you can pull and shape real-world data. Methodology and statistics come later; here the focus is on **using Python confidently as a data tool**.

**Central idea:** Most data science workflows in industry are built in Python. Building fluency in its core features and a few key libraries is what lets you connect raw sources to analysis and modeling.

---

## Why Python shows up everywhere in data

Python is widely adopted in data science for good reasons: readable syntax, strong community and docs, and a deep stack for data and ML (**Pandas**, **NumPy**, **SciPy**, **Matplotlib**, and frameworks like scikit-learn, with paths into deep learning as you advance). For this program, the practical answer to “where do I start?” is: **start with Python and these building blocks**.

---

## How the materials are organized

The numbered subfolders (`2.01`, `2.02`, …) follow the course order. **Notebook filenames** are mostly IBM **PY0101** lab titles, plus a few extras (Pandas practice, a web-scraping review lab, a simple API notebook). **Supporting data** (CSV, XLSX, text, images, JSON, XML) sit alongside the notebooks that use them. Use the list below to find a topic quickly.

| Folder | Notebooks and focus |
|--------|---------------------|
| **2.01** | `PY0101EN-1-1-Getting_Started_With_Python.ipynb`, `PY0101EN-1-1-Types.ipynb` — context for Python in data work, Jupyter basics, built-in types. |
| **2.02** | `PY0101EN-1-1-Expressions_Variables.ipynb`, `PY0101EN-1-2-Strings.ipynb` — operators, variables, string operations. |
| **2.04** | `PY0101EN-2-1-Tuples.ipynb`, `PY0101EN-2-2-Lists.ipynb` — tuples and lists, indexing and methods. |
| **2.05** | `PY0101EN-2-3-Sets.ipynb`, `PY0101EN-2-4-Dictionaries.ipynb` — sets and dictionaries. |
| **2.06** | `PY0101EN-3-1-Conditions.ipynb`, `PY0101EN-3-2-Loops.ipynb`, `PY0101EN-3-3-Functions-jupyterlite.ipynb` — conditionals, loops, defining functions. |
| **2.07** | `3-1.2ExcecptionHandling.ipynb` (exception handling; filename uses the course spelling), `PY0101EN-3-4-Classes.ipynb`, `PY0101EN-3-5-Practice_lab.ipynb` — `try`/`except`, classes and objects, short practice lab. |
| **2.08** | `PY0101EN-4-1-ReadFile.ipynb`, `PY0101EN-4-2-WriteFile.ipynb`, `PY0101EN-4-3-LoadData.ipynb`, `Pandas_Practice.ipynb` — `open` / `with`, CSV and related loading, extra Pandas exercises with bundled sample files. |
| **2.09** | `PY0101EN-5-1-Numpy1D.ipynb`, `PY0101EN-5-2-Numpy2D.ipynb` — 1D/2D arrays, ufuncs, operations that underpin numerical and tabular work. |
| **2.10** | `PY0101EN-5 2_API_2 v2.ipynb`, `Simple_API_2__v2.ipynb`, `PY0101EN-5 3_Requests_HTTP.ipynb`, `PY0101EN-5 4_WorkingWithDifferent.ipynb`, `PY0101EN-5.4_WorkingWithDifferentFileTypes.ipynb`, `labs_module 1_Web Scraping_Web-Scraping-Review.ipynb` — APIs, HTTP/`requests`, JSON and other file types, **BeautifulSoup**-style web scraping; sample assets included (e.g. CSV, JSON, XML, XLSX, images) as referenced in the labs. |
| **2.11** | `practice_project.ipynb` — capstone-style exercise (GDP data from a Wikipedia snapshot via scraping, Pandas/NumPy processing, CSV output). `Largest_economies.csv` is a reference or output artifact in this folder. |
| **2.13-live-session** | Placeholder for live session materials; content may be added by your instructor. |

If you are searching the repo, note that some notebook names include spaces (e.g. `PY0101EN-5 2_API_2 v2.ipynb`).

---

## Topic map (what you are learning, in order)

1. **Getting started** — Why Python in data science, Jupyter workflows, and types.  
2. **Expressions, variables, strings** — Core syntax and text handling.  
3. **Collections** — Tuples, lists, sets, and dictionaries.  
4. **Control flow and reuse** — Conditions, loops, functions, exception handling, and an introduction to classes.  
5. **Files and tables** — Reading and writing text files, loading data, and Pandas for filtering, selection, and export.  
6. **NumPy** — One- and two-dimensional arrays for fast numeric work.  
7. **Data from the web** — APIs, HTTP and `requests`, working with JSON and other formats, and HTML parsing for scraping.  
8. **Practice project** — One integrated task: scrape IMF GDP data from a provided Wikipedia (archive) URL, transform with Pandas/NumPy, and write **CSV** results.

---

## `Downloads` folder

The **`Downloads`** directory holds **text companion notes** (topic-by-topic) aligned with the videos or readings—useful for review without re-running a notebook. There is also **`Python Cheat Sheet - The Basics.pdf`**. Topics covered in those `.txt` files include: getting started with Jupyter, introduction to Python, types, expressions and variables, string operations, lists and tuples, sets, dictionaries, conditions, loops, functions, exception handling, objects and classes, reading/writing with `open`, loading data, working with and saving data, one- and two-dimensional NumPy, application program interfaces, REST/HTTP (parts 1 and 2), working with different file formats, and web scraping (plus **HTML for web scraping**). Match the filename to the section you are studying.

---

## Key takeaways

* Python’s **clarity and library ecosystem** make it the default environment for many data teams.  
* **Tuples, lists, sets, and dictionaries** are the usual way to hold and access structured and semi-structured data in memory.  
* **Functions, modules, and classes** keep scripts organized as tasks grow.  
* **File I/O and Pandas** are how you move between disk, notebooks, and tabular analysis.  
* **NumPy** is the array layer Pandas and much of the numeric stack build on.  
* **APIs and scraping** extend your reach to live and published data on the web.  
* The **practice project** lines up those skills: acquire → clean → transform → save.

---

## After this module

Aim to be able to **open a dataset or endpoint, turn it into a table you understand, and save or summarize it**—not to memorize every API. That working comfort is what unlocks the projects and modules that follow, where you lean more heavily on analysis and modeling.
