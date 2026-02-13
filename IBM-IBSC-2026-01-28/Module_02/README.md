# Module 2: Python Basics for Data Science

**Author:** Alexander Booth
**Date:** February 2026

---

## Overview

This module introduces **Python as the core programming language for data science**. Rather than focusing on methodology, Module 2 emphasizes **hands-on Python**: syntax, data structures, file I/O, and the libraries (NumPy, Pandas) and techniques (APIs, web scraping) you need to work with real data.

The core takeaway:

> Python is the most widely used language in data science; mastering its basics and key libraries is the foundation for building data pipelines and analyses.

---

## Why Python for Data Science

Python is not just one tool among many. It is the **dominant language** in the data science industry:

* Clear, readable syntax that speeds up development and collaboration
* A huge global community and extensive documentation
* Scientific computing libraries: **Pandas**, **NumPy**, **SciPy**, **Matplotlib**
* Support for AI/ML (e.g. TensorFlow, PyTorch, Scikit-learn) and automation, web scraping, and data analytics

The **question of “which language first?”** for aspiring data scientists is answered overwhelmingly: Python.

---

## What This Module Covers

The module is organized as a **progressive path** from Python basics to data extraction and processing.

### 1. Getting Started

* **Introduction to Python** — Who uses it, why it matters for data science, and the Python community (e.g. PyLadies, Python Software Foundation).
* **Jupyter** — Running, inserting, and deleting cells; working with multiple notebooks; presenting results with Markdown and shutting down sessions.
* **Types** — Built-in types and how Python represents data.

### 2. Expressions, Variables, and Strings

* **Expressions and variables** — Operators, operands, assignment, and using variables to store and reuse values.
* **Strings** — String operations and formatting for text data.

### 3. Data Structures

* **Tuples** — Ordered, immutable sequences; indexing, slicing, concatenation.
* **Lists** — Mutable sequences; indexing, slicing, and list methods.
* **Sets** — Unordered collections of unique elements.
* **Dictionaries** — Key–value pairs for structured data.

### 4. Control Flow and Reuse

* **Conditions and branching** — `if`/`else` and Boolean logic.
* **Loops** — Iterating with `for` and `while`.
* **Functions** — Built-in functions, defining your own functions, and reusing code.
* **Exception handling** — `try`/`except` and handling errors gracefully.
* **Objects and classes** — Types as objects, methods, and constructing your own classes.

### 5. Files and Data

* **Reading and writing files** — The `open` function, file modes (`'r'`, `'w'`, `'a'`), and the `with` statement.
* **Loading data** — Bringing data into your workflow (e.g. CSV).
* **Working with and saving data** — Filtering, selecting, and exporting with Pandas (e.g. `to_csv`, unique values, Boolean indexing).

### 6. NumPy

* **One-dimensional NumPy** — Array creation, indexing, slicing, and universal functions.
* **Two-dimensional NumPy** — 2D arrays and operations that underpin tabular and numerical work.

### 7. APIs and Web Scraping

* **Application program interface (API)** — What APIs are and how they expose data.
* **REST APIs and HTTP** — URLs, requests, responses, status codes, and the HTTP protocol.
* **Requests** — Using the `requests` library to call APIs and get data.
* **Working with different formats** — Handling JSON and other common data formats.
* **Web scraping** — Extracting information from web pages using **Requests** and **BeautifulSoup** (e.g. `find_all`, navigating the HTML tree).

### 8. Practice Project

The module culminates in a **Practice Project: GDP Data extraction and processing**:

* Extract the top 10 largest economies (by GDP) from a Wikipedia page using **web scraping**.
* Process the data with **Pandas** and **NumPy**.
* Save the result to a **CSV** file.

This ties together APIs/web scraping, data manipulation, and file I/O in one end-to-end task.

---

## Key Takeaways

* Python’s **readability and ecosystem** make it the default choice for data science.
* **Data structures** (tuples, lists, sets, dictionaries) are the building blocks for organizing and accessing data.
* **Functions and classes** help you write reusable, maintainable code.
* **Files and Pandas** are how you load, transform, and save real datasets.
* **NumPy** provides fast, array-based operations that Pandas and many other libraries rely on.
* **APIs and web scraping** let you **gather** data from the web; Python is the tool to automate that pipeline.
* The **practice project** shows how one script can combine scraping, APIs, Pandas, NumPy, and CSV export.

---

## The Data Scientist’s Toolkit

Think of this module as building your **first toolkit**, not just learning syntax.

The goal is not to memorize every function.
The goal is to **read data from the world (files, APIs, web), shape it with Python and Pandas/NumPy, and save or use the results**—so you can focus on the next step: analysis and modeling.
