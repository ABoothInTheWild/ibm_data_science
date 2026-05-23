# Module 7: Analyzing Data with Python

**Author:** Alexander Booth
**Date:** May 2026

---

## Overview

This module focuses on **analyzing data and building predictive models in Python**: from loading and cleaning data to exploratory analysis, regression (simple, multiple, polynomial), and model evaluation and refinement. You use **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**, and **scikit-learn** to go from raw data to a model that can predict a target (e.g. car price, house price) and assess how well it generalizes.

The core takeaway:

> Data anlaytics is not only about collecting and storing data—it is about **understanding** it, **cleaning** it, **modeling** it, and **evaluating** it. This module gives you the full pipeline: **data wrangling**, **exploratory data analysis**, **model development**, and **model evaluation and refinement** so you can make predictions and decisions from real datasets.

---

## Why Analyzing Data Matters

Once data is in your hands (e.g. from files, databases, or the web), you need to:

* **Understand and clean it** — Wrong types, missing values, inconsistent formats, and different units can break analysis and models; pre-processing and data wrangling fix this.
* **Explore it** — Descriptive statistics, grouping, correlation, and visualization reveal which variables matter and how they relate to the target.
* **Model it** — Regression models (linear, multiple, polynomial) turn relationships into equations you can use to predict new outcomes (e.g. car price from features).
* **Evaluate and refine it** — Train/test splits, cross-validation, and metrics (MSE, R²) tell you whether the model generalizes; techniques like ridge regression and grid search help you avoid overfitting and choose good hyperparameters.

**The end goal** is to go from “data in a table” to “reliable predictions and better decisions”—whether that is pricing a used car or estimating the market price of a house.

---

## What This Module Covers

The module is organized as a **progressive path** from data ingestion and cleaning through EDA, model development, evaluation, and a capstone project.

### 1. Introduction and Data Acquisition

* **Getting Started Analyzing Data in Python** — Pandas methods for exploring data: `dtype`, `describe`, `info`; data types (object, float, int, datetime); why checking types and distributions matters before modeling.
* **Understanding the Data** — The used-car dataset (Schlimmer): CSV format, 26 columns, meaning of attributes (e.g. symboling, normalized losses), and identifying the **target** (price) and **predictors**.
* **Importing and Exporting Data in Python** — Data acquisition: format (CSV, JSON, XLSX) and file path; `read_csv`, handling missing headers (`header=None`), assigning column names; `head`, `tail`; exporting with `to_csv`.

### 2. Data Wrangling (Pre-processing)

* **Pre-processing Data in Python** — Data cleaning and wrangling: converting raw data into a form ready for analysis; working along columns in Pandas.
* **Dealing with Missing Values in Python** — What missing values are (e.g. `?`, N/A, blank, NaN); strategies: drop (rows/columns) vs. replace (mean, mode); `dropna` and `replace` in Pandas.
* **Data Formatting in Python** — Standardizing formats, units, and conventions; converting units (e.g. city-mpg to L/100 km); fixing incorrect dtypes with `astype`; `rename` for column names.
* **Data Normalization in Python** — Centering and scaling so different numeric ranges can be compared; standardization (e.g. StandardScaler in scikit-learn).
* **Binning in Python** — Creating broader categories from numerical values for comparison across groups.
* **Turning Categorical Variables into Quantitative Variables in Python** — Converting categorical values to numeric form for statistical modeling (e.g. one-hot or indicator variables).

### 3. Exploratory Data Analysis (EDA)

* **Exploratory Data Analysis** — EDA goals: summarize main characteristics, uncover relationships, extract important variables; main question: which characteristics have the most impact on car price?
* **Descriptive Statistics** — `describe`, quartiles, mean, std, extremes; `value_counts` for categorical data; box plots (median, quartiles, IQR, outliers); scatter plots (predictor vs. target).
* **GroupBy in Python** — Grouping by categorical variables (`groupby`); comparing groups (e.g. average price by drive wheels and body style); pivot tables and heatmaps for visualization.
* **Correlation** — Correlation as interdependence of variables; positive vs. negative correlation; correlation vs. causation; regression line and scatter plots (e.g. engine size vs. price, highway mpg vs. price); weak vs. strong correlation.
* **Correlation — Statistics** — Pearson correlation and correlation heatmaps for EDA.

### 4. Model Development

* **Model Development** — Models as mathematical equations relating independent variables (features) to a dependent variable (target); why more relevant data and more features can improve predictions; simple linear regression (SLR), multiple linear regression (MLR), and polynomial regression.
* **Linear Regression and Multiple Linear Regression** — SLR: one predictor, intercept and slope (b0, b1), fitting with training data, noise; fitting in Python (`LinearRegression`, `fit`, `predict`, intercept and coefficients); MLR: multiple predictors, visualization in 2D (height = predicted y).
* **Model Evaluation using Visualization** — Regression plots (e.g. Seaborn `regplot`); residual plots (actual − predicted) and what they tell you (linear vs. curved, variance); distribution plots (predicted vs. actual) for single and multiple features.
* **Polynomial Regression and Pipelines** — When linear fit is insufficient; polynomial regression (quadratic, cubic, higher order); `polyfit` (NumPy) and polynomial features in scikit-learn; pipelines to chain transformation (e.g. polynomial, standardization) and regression.
* **Measures for In-Sample Evaluation** — MSE (mean squared error) and R² (coefficient of determination); comparing fitted line to a baseline (mean of y); interpreting R² (e.g. share of variation explained).
* **Prediction and Decision Making** — Using the model for prediction (`predict`); sanity-checking coefficients and predictions; when predictions are unrealistic (e.g. negative price); comparing models (e.g. SLR vs. MLR, MSE and R²).

### 5. Model Evaluation and Refinement

* **Model Evaluation and Refinement** — In-sample vs. out-of-sample evaluation; need to estimate how the model performs on new data.
* **Train/Test Split** — Splitting data into training and test sets; `train_test_split` (e.g. 70% train, 30% test); using training data to build the model and test data to approximate generalization error; trade-off between accuracy and precision of the estimate.
* **Cross Validation** — k-fold cross-validation: data split into k folds, each fold used as test once; `cross_val_score` and `cross_val_predict` in scikit-learn; averaging scores for out-of-sample estimate.
* **Overfitting, Underfitting and Model Selection** — Underfitting (model too simple, e.g. linear for polynomial data); overfitting (model too flexible, fits noise); selecting polynomial order by minimizing test error; irreducible error; R² vs. polynomial order on real data.
* **Ridge Regression** — Controlling overfitting by penalizing coefficient magnitude; hyperparameter alpha; effect of alpha (too large → underfitting, zero → overfitting); selecting alpha via validation/cross-validation; using Ridge in scikit-learn.
* **Grid Search** — Automating hyperparameter selection; GridSearchCV with a grid of parameter values (e.g. alpha, normalize); scoring (e.g. R², MSE); `best_estimator_` and `cv_results_`.

### 6. Python Packages for Data Science

* **Python Packages for Data Science** — Scientific computing: Pandas (DataFrames), NumPy (arrays), SciPy (advanced math); visualization: Matplotlib, Seaborn; machine learning: scikit-learn (regression, classification, clustering), Statsmodels.

### 7. Labs and Notebooks

* **7.01 — Introduction**
    * **Introduction / Data Acquisition** (`DA0101EN-Review-Introduction.ipynb`) — Load the Automobile dataset (CSV from UCI), use Pandas to read data (including `header=None`), assign column names, and get basic insight with `head` and exploration methods. Datasets: `auto.csv`, `automobile.csv`.
* **7.03 — Data Wrangling**
    * **Review: Data Wrangling** (`DA0101EN-2-Review-Data-Wrangling-20231003-1696291200.ipynb`) — Identify and handle missing values, correct data format, standardize and normalize data, binning, and indicator variables. Practice: `practice_data_wrangling.ipynb`. Datasets: `laptops.csv`, `usedcars.csv`, `clean_df.csv`.
* **7.05 — Exploratory Data Analysis**
    * **Exploratory Data Analysis** (`Exploratory_data_analysis.ipynb`, `Exploratory_data_analysis_cars-20231003-1696291200.ipynb`) — Descriptive statistics, grouping, ANOVA, correlation, and visualizations to find which characteristics most impact car price. Datasets: `laptops.csv`, `usedcars.csv`.
* **7.06 — Model Development**
    * **Review: Model Development** (`DA0101EN-4-Review-Model-Development-20231003-1696291200.ipynb`) — Build simple and multiple linear regression models, polynomial regression, pipelines, and in-sample evaluation (MSE, R²). Practice: `practice_model_development_laptops.ipynb`. Datasets: `laptops.csv`, `usedcars.csv`.
* **7.08 — Model Evaluation and Refinement**
    * **Model Evaluation and Refinement** (`DA0101EN-5-Model-Evaluation-and-Refinement.ipynb`) — Train/test split, cross-validation, overfitting/underfitting, ridge regression, and grid search. Practice: `practice_model_evaluation.ipynb`. Datasets: `laptops.csv`, `module_5_auto.csv`.
* **7.10 — Final Project**
    * **House Sales in King County, USA** (`House_Sales_in_King_Count_USA-20231003-1696291200.jupyterlite.ipynb`) — Capstone: act as a Data Analyst for a Real Estate Investment Trust; use the King County housing dataset (`housing.csv`) to analyze and predict house prices. Work through importing data, data wrangling, EDA, model development, and model evaluation and refinement; complete the assigned questions and capture outputs for peer review.

### 8. Supporting Materials

* **Downloads** — Transcripts and notes (TXT) for all video topics above (e.g. Getting Started Analyzing Data, Understanding the Data, Importing/Exporting, Pre-processing, Missing Values, Data Formatting, Normalization, Binning, Categorical Variables, EDA, Descriptive Statistics, GroupBy, Correlation, Model Development, Linear and Multiple Linear Regression, Model Evaluation using Visualization, Polynomial Regression and Pipelines, Measures for In-Sample Evaluation, Prediction and Decision Making, Model Evaluation and Refinement, Overfitting/Underfitting, Ridge Regression, Grid Search, Python Packages).
* **7.11 — Live Session** — Placeholder for live session materials (e.g. `.gitkeep`).

---

## Key Takeaways

* **Data acquisition and types** — Use Pandas to read data (e.g. `read_csv`), set column names, and inspect with `dtype`, `describe`, and `info`; fix wrong types with `astype`.
* **Data wrangling** — Handle missing values (`dropna`, `replace`), standardize formats and units, normalize or scale when needed, use binning and convert categorical variables to quantitative form for modeling.
* **EDA** — Use descriptive statistics, `groupby`, pivot tables, heatmaps, scatter plots, and correlation (including Pearson and heatmaps) to understand distributions and relationships and to choose important variables.
* **Model development** — **Simple linear regression** (one predictor) and **multiple linear regression** (several predictors) with scikit-learn (`LinearRegression`, `fit`, `predict`); **polynomial regression** and **pipelines** when relationships are nonlinear; evaluate fit with **MSE** and **R²** (in-sample).
* **Model evaluation and refinement** — Split data into **training** and **test** sets; use **cross-validation** for a more stable estimate of generalization; avoid **overfitting** (e.g. with **ridge regression** and **grid search** for hyperparameters like alpha).
* **End-to-end workflow** — The **final project** (House Sales in King County) ties the module together: load data → wrangle → explore → develop models → evaluate and refine → predict house prices and support decisions.

---

## The Data Analyst's Modeling Toolkit

Think of this module as building your **analysis and modeling toolkit**, not just running a single script.

The goal is not to memorize every Pandas method or scikit-learn parameter.
The goal is to **take raw data, clean and explore it, build regression models, and evaluate and refine them** so you can make predictions and decisions—and carry this pipeline forward to more advanced modeling and real-world projects.
