# Module 4: Databases and SQL for Data Science

**Author:** Alexander Booth
**Date:** February 2026

---

## Overview

This module focuses on **databases and SQL in the data science workflow**: from relational concepts and SQL syntax to **accessing databases with Python** (Jupyter, SQL Magic, DB-API, SQLite) and **analyzing real-world data** in a database. You learn how to create and query tables, use DDL and DML, work with multiple tables, and combine SQL with Pandas and visualization.

The core takeaway:

> Data scientists need to read and write data in databases. This module gives you **SQL fundamentals** and **Python–database integration** so you can store, query, and analyze data in relational systems and bring results into your analysis and visualizations.

---

## Why Databases and SQL Matter

Real-world data often lives in **relational databases**:

* **Structured storage** — Tables, rows, and columns with types and constraints
* **Query power** — SQL to filter, aggregate, join, and sort without loading everything into memory
* **Integration** — Python (Jupyter, Pandas, DB-API, SQL Magic) connects your analysis to DBMSs such as SQLite, MySQL, and IBM Db2

**SQL and Python together** let you:

* Run queries from notebooks and assign results to variables or DataFrames
* Load CSV or other sources into a database, then analyze with SQL and Pandas
* Build repeatable pipelines: load once, query many times

---

## What This Module Covers

The module is organized as a **progressive path** from SQL and database concepts to Python access and a capstone project with real datasets.

### 1. SQL, Databases, and DBMS

* **Introduction to SQL, Database, and DBMS** — What SQL is; data, databases, and repositories; relational databases (tables, columns, rows); RDBMS (e.g. MySQL, Oracle, DB2); five basic operations: create table, insert, select, update, delete.
* **Relational Database Concepts** — Relational model and data independence; entity–relationship (ER) concepts; entities and attributes; mapping entities to tables and attributes to columns; data types (CHAR, VARCHAR, INTEGER, etc.); primary keys and foreign keys.

### 2. Types of SQL Statements

* **DDL vs. DML** — Data Definition Language (CREATE, ALTER, TRUNCATE, DROP) for defining or changing database objects; Data Manipulation Language (INSERT, SELECT, UPDATE, DELETE) for reading and modifying data (CRUD).

### 3. Creating and Querying Data

* **CREATE TABLE Statement** — Defining tables and columns.
* **Creating Tables, Loading Data and Querying Data** — End-to-end: create tables, load data, run queries.
* **SELECT Statement** — Retrieving data; result sets; selecting columns; WHERE clause and predicates; comparison operators.
* **COUNT, DISTINCT, LIMIT** — Aggregating and limiting result sets.
* **INSERT Statement** — Adding rows to tables.
* **UPDATE and DELETE Statements** — Modifying and removing rows.
* **ALTER, DROP, and TRUNCATE Tables** — Changing table structure and removing tables or data.

### 4. Filtering, Sorting, and Grouping

* **Using String Patterns and Ranges** — LIKE, BETWEEN, IN, and related patterns.
* **Sorting Result Sets** — ORDER BY (ASC/DESC).
* **Grouping Result Sets** — GROUP BY and aggregation.
* **Built-in Database Functions** — Common scalar and aggregate functions.
* **Date and Time Built-in Functions** — Working with dates and times in SQL.

### 5. Multiple Tables and Advanced Queries

* **Sub-Queries and Nested Selects** — Using subqueries for filtering and derived data.
* **Working with Multiple Tables** — Subqueries, implicit joins, and JOIN operators (inner join, outer join); qualifying column names and table aliases.

### 6. Accessing Databases with Python

* **How to Access Databases Using Python** — Benefits of Python for DB access; Jupyter notebooks; SQL APIs and DB-API; how application code connects to the DBMS and passes SQL.
* **Accessing Databases with SQL Magic** — Line magics (%) and cell magics (%%); `%sql` and `%%sql` in Jupyter; connecting to SQLite (e.g. `%sql sqlite:///DatabaseName`); using Python variables in SQL (`:variable`); assigning query results to variables; converting results to Pandas DataFrames.
* **Writing Code Using DB-API** — Standard DB-API pattern for connecting and executing SQL.
* **Connecting to a Database Using ibm_db API** — IBM Db2 and proprietary APIs.
* **How to create a Database instance on Cloud** — Creating a cloud database instance for labs.
* **Analyzing Data with Python** — EDA with Pandas; SQLite3 with Python for storage and retrieval; visualization (e.g. Seaborn) for insights; example with McDonald’s menu nutrition data: load CSV into SQLite, query with `read_sql`, describe statistics, and visualize (e.g. sodium content).

### 7. Working with Real-World Data

* **Working with Real-World Data Sets** — CSV as common format; header row and column names; loading data into databases (e.g. phpMyAdmin/import); querying columns with spaces (backticks); splitting long queries across lines; `read_sql` in Pandas; quoting and escaping; using LIMIT to sample rows.

### 8. Labs and Notebooks

* **4.11 — SQL Magic and SQLite**
    * **Accessing Databases with SQL Magic** (`DB0201EN-Week3-1-3-SQLmagic_SQlite.ipynb`) — Load ipython-sql, connect to SQLite, create tables, use `%%sql`, Python variables in SQL, assign results to variables, convert to DataFrames and visualize.
    * **Analyzing a real world data-set with SQL and Python** (`DB0201EN-Week3-1-4-Analyzing_SQLite.ipynb`) — Chicago socioeconomic indicators; store data in SQLite; practice SQL and basic analysis.
    * **Create & Access SQLite database using Python** (`Week4_Insert_Update_SQLite.ipynb`) — Create database and table, insert data, query, retrieve into Pandas, close connection (e.g. `INSTRUCTOR.db`).
* **4.13 — Real Data Practice**
    * **Working with a real world data-set using SQL and Python** (`DB0201EN-Week4-1-1-RealDataPractice-v5_sqlite_Learner.ipynb`) — Chicago Public Schools Progress Report Cards (2011–2012); store in SQLite (`RealWorldData.db`); metadata and mixed-case columns; built-in functions and SQL practice.

### 9. Final Project

* **4.16 — Module Assessment** (`mod5_final_project.ipynb`) — Final Module Lab:
    * Understand three Chicago datasets: **Socioeconomic Indicators**, **Chicago Public Schools**, **Chicago Crime Data**.
    * Load the three datasets into three tables in a **SQLite** database (`FinalDB.db`).
    * Execute SQL queries to answer assignment questions.

### 10. Supporting Materials

* **Downloads** — Transcripts and notes (TXT) for all video topics above (e.g. Introduction to SQL, Relational Database Concepts, SELECT, INSERT, UPDATE/DELETE, JOINs, SQL Magic, DB-API, Analyzing Data with Python, Working with Real-World Data Sets).
* **PDFs** — In sections 4.03, 4.06, 4.08, and 4.09 (e.g. 4.3.3, 4.3.5, 4.3.8, 4.6.3, 4.6.4, 4.8.3, 4.9.3, 4.9.4, 4.9.5) for slides or handouts.
* **4.07** — Placeholder (e.g. .gitkeep).
* **4.17 — Live Session** — Placeholder for live session materials.

---

## Key Takeaways

* **SQL** is the language for querying and manipulating data in relational databases; **DDL** defines structure (CREATE, ALTER, DROP, TRUNCATE), **DML** manipulates data (INSERT, SELECT, UPDATE, DELETE).
* **Relational concepts** — tables, columns, primary/foreign keys, entities and attributes — underpin how you design and query databases.
* **SELECT**, **WHERE**, **ORDER BY**, **GROUP BY**, **JOINs**, and **subqueries** are the core tools for filtering, sorting, aggregating, and combining tables.
* **Python + databases** — Use **SQL Magic** (`%sql` / `%%sql`) in Jupyter for quick queries and DataFrame conversion; use **DB-API** (e.g. `sqlite3`) for programmatic create/insert/query and **Pandas** `read_sql` for analysis.
* **Real-world workflow** — Load CSV (or other sources) into SQLite (or another RDBMS), then analyze with SQL and Python (Pandas, Seaborn) and answer questions with queries and visualizations.
* The **final project** ties the module together: load three Chicago datasets into SQLite and answer questions using SQL.

---

## The Data Scientist’s Database Toolkit

Think of this module as building your **database toolkit** for data science, not just learning SQL in isolation.

The goal is not to memorize every SQL clause or API call.
The goal is to **understand relational data, write correct SQL for querying and updating tables, and connect Python (Jupyter, Pandas, SQL Magic, DB-API) to databases**—so you can store, retrieve, and analyze real-world data and move on to modeling and decision-making.
