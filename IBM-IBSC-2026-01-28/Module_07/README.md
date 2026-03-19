# Module 7: Machine Learning — Regression & Classification

**Author:** Alexander Booth
**Date:** March 2026
**Cohort:** IBM-IBSC Jan 28, 2026

---

## Overview

This module introduces **machine learning fundamentals** and then focuses on two core supervised learning families:

* **Regression** — predicting **continuous numeric values** (e.g., CO2 emissions) using **simple**, **multiple**, and **polynomial / non-linear** regression concepts.
* **Classification** — predicting **classes / categories**, with a deep dive into **logistic regression** as a probability-based binary classifier (e.g., customer churn).

You’ll also connect the modeling work to the bigger picture: the **machine learning ecosystem (scikit-learn and friends)** and the **end-to-end ML model lifecycle** (problem definition → data collection/ETL → preparation/EDA → model development & evaluation → deployment + monitoring).

---

## Why This Module Matters

Once you can clean data and explore it, the next step is to **build models that predict**:

* **Continuous outcomes** (regression): emissions, prices, revenue, rainfall, maintenance needs.
* **Binary outcomes** (classification): churn/no churn, disease/no disease, default/no default.

This module builds the practical foundation for doing that with **scikit-learn**, while emphasizing model thinking: choosing features, training/testing, evaluating error (e.g., **MSE** for regression, **log loss** for logistic regression), and avoiding common pitfalls (overfitting, collinearity, unrealistic “what-if” scenarios).

---

## What This Module Covers

### 1. Machine Learning Fundamentals

* **What ML is (and isn’t)** — ML as a subset of AI; supervised vs unsupervised vs semi-supervised vs reinforcement learning.
* **Common ML techniques** — classification, regression, clustering, association, anomaly detection, dimensionality reduction, recommendation systems.

### 2. Regression (Supervised Learning)

* **Regression definition** — modeling the relationship between a **continuous target** and explanatory features.
* **Simple linear regression** — one feature → one target; best-fit line; residuals and **mean squared error (MSE)**; ordinary least squares (OLS).
* **Multiple linear regression** — multiple features → one target; interpreting feature impact; handling categorical variables; pitfalls like **overfitting** and **collinearity**.
* **Polynomial & non-linear regression (conceptual)** — when a straight line underfits; polynomial features; overfitting with high-degree polynomials; exponential/logarithmic/periodic relationships.

### 3. Classification with Logistic Regression

* **Logistic regression** — probability model with a **sigmoid** function; thresholding to create a decision boundary; good when target is binary and probabilities matter.
* **Training logistic regression** — minimizing **log loss** using optimization; gradient descent vs stochastic gradient descent concepts.

### 4. Tools, Ecosystem, and the ML Lifecycle

* **Tools for ML** — languages (Python, R, etc.) and tool categories: data processing, visualization, ML, deep learning, CV, NLP, generative AI.
* **Scikit-learn ecosystem** — common workflow: preprocessing → train/test split → fit → predict → evaluate → export model.
* **ML model lifecycle** — problem definition → data collection → data preparation → model development & evaluation → deployment and monitoring (iterative loop).

---

## Labs and Notebooks

### 7.03 — Regression Labs

* **Simple Linear Regression** (`7.03/Simple-Linear-Regression.ipynb`)
    * Use scikit-learn to implement simple linear regression
    * Train/test a model using the Fuel Consumption / CO2 dataset (`FuelConsumptionCo2.csv` via Skills Network URL)
* **Multiple Linear Regression** (`7.03/Mulitple-Linear-Regression.ipynb`)
    * Use scikit-learn to implement multiple linear regression
    * Train/test a model using multiple features (same Fuel Consumption / CO2 dataset)

### 7.04 — Classification Lab

* **Logistic Regression with Python** (`7.04/Logistic_Regression.ipynb`)
    * Preprocess data (scaling + train/test split)
    * Train a logistic regression classifier
    * Evaluate with **log loss**, confusion matrix, and classification report
    * Scenario: telecom customer churn (Telco Churn dataset loaded from URL)

### 7.05 — Quick Reference

* **Machine learning cheat sheet** (`7.05/ml_cheat_sheet.pdf`)
    * Quick-reference PDF (formulas/at-a-glance concepts). Note: this file did not extract cleanly to text in this environment, so the summary above is based on its intended use as a cheat sheet rather than readable PDF text.

### 7.06 — Live Session

* Placeholder for live session materials (`7.06 - Live Session/.gitkeep`)

---

## Supporting Materials

### Downloads (Lecture Transcripts / Notes)

Located in `Downloads/`:

* `An overview of machine learning.txt`
* `Introduction to regression.txt`
* `Introduction to simple linear regression.txt`
* `Multiple linear regression.txt`
* `Polynomial and non-linear regression .txt`
* `Introduction to logistic regression.txt`
* `Training a logistic regression model.txt`
* `Scikit-learn machine learning ecosystem.txt`
* `Tools for machine learning.txt`
* `Machine learning model lifecycle (Part 1).txt`
* `Machine learning model lifecycle (Part 2).txt`
* `Data scientist vs AI engineer.txt`

### Prof’s Study Guides

Located in `Prof's ML Study Guides/`:

* `Supervised ML Study Guide.pdf`
    * Supervised learning framing (features/labels; regression vs classification; train/test split; overfitting vs underfitting)
    * Linear model family + assumptions (linearity, independence / multicollinearity) and common fixes (PCA, L1/L2 regularization)
    * Tree-based models overview (decision trees, random forests, boosted trees like XGBoost/LightGBM/CatBoost) + pros/cons
    * Regression evaluation metrics (R², MSE, RMSE, MAE) + diagnostic plots (predicted vs actual, residual plots)
    * End-to-end supervised workflow checklist (preprocessing → feature selection → experiment tracking → model selection)
* `Classification ML Study Guide.pdf`
    * Classification problem types (binary, multi-class, multi-label) framed as probability prediction
    * Algorithms overview: SVM, KNN, logistic regression (incl. when/why they work, trade-offs)
    * Core evaluation building blocks: confusion matrix; Type I/II errors; TP/FP/TN/FN
    * Metrics: accuracy, precision, recall, F1; ROC curve + AUC; Brier score (probability calibration-style error)
    * Practical workflow notes (scaling, stratified splits, handling imbalanced classes, experiment comparisons)
* `Production ML Study Guide.pdf`
    * Practical preprocessing: imputation, scaling, encoding (label vs one-hot; binning high-cardinality categories), outliers, class balancing (incl. SMOTE)
    * Saving models for reuse/deployment (pickle vs joblib; common extensions) + environment consistency via containerization (Docker)
    * scikit-learn pipelines (bundle preprocessors + model; avoid data leakage; consistent transformations for inference)
    * Robust evaluation: k-fold cross-validation + stratified k-fold for classification
    * Explainability: tree feature importances, linear coefficients (with scaling caveat), plus SHAP and partial dependence plots as advanced options

---

## Key Takeaways

* **ML landscape** — ML sits within AI; learning types include supervised, unsupervised, semi-supervised, and reinforcement learning.
* **Regression vs classification** — regression predicts **continuous values**; classification predicts **classes**; logistic regression turns a linear model into probabilities via the **sigmoid** function.
* **Evaluation matters** — regression commonly uses residuals and **MSE**; logistic regression commonly uses **log loss** and classification metrics.
* **Model pitfalls** — avoid overfitting (too many variables / overly flexible models) and watch for correlated features (collinearity) that break “what-if” interpretations.
* **From notebook to product** — scikit-learn supports the full workflow, and the ML lifecycle frames how models get built, deployed, and monitored in real systems.
