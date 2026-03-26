# Module 8: Machine Learning — Trees, Ensembles, Clustering & Model Evaluation

**Author:** Alexander Booth  
**Date:** March 2026  
**Cohort:** IBM-IBSC Jan 28, 2026

---

## Overview

This module extends **supervised learning** into **non-linear models** (decision trees, ensembles, KNN, SVM-style workflows), introduces **unsupervised learning** (clustering and dimension reduction), and ties everything together with **evaluation**, **regularization**, **cross-validation**, **pipelines**, and a **capstone-style lab**.

The core threads:

* **Trees and ensembles** — From interpretable **decision trees** to **random forests**, **boosting** (e.g., XGBoost), and intuition around **bias–variance** and **ensembling**.
* **More supervised tools** — **K-nearest neighbors**, **SVMs** in practice (with fraud-detection style examples), and **multi-class** settings.
* **Unsupervised learning** — **K-means**, **DBSCAN / HDBSCAN**, and **PCA**, plus **t-SNE** and **UMAP** for visualization-oriented embedding.
* **Doing it right** — **Classification and regression metrics**, evaluating clustering without labels, **regularization**, **data leakage**, **GridSearchCV**, and **ML pipelines** in scikit-learn.

---

## Why This Module Matters

After linear and logistic models, many real problems need **flexible predictors** and **segmentation / structure discovery** without labels:

* **Trees and ensembles** often win on tabular data; they also surface **feature importance** and handle non-linearity—but they need careful **validation** and tuning.
* **Clustering and dimension reduction** help with **customer segmentation**, **anomaly patterns**, and **visualizing** high-dimensional data.
* **Pipelines, grid search, and leakage-aware workflows** are what separate notebook experiments from **reproducible** model development.

---

## What This Module Covers

### 1. Decision Trees and Tree-Based Prediction

* **Decision trees** — Splitting rules, interpretability, overfitting, and when trees help vs. hurt.
* **Regression trees** — Predicting continuous targets with piecewise-constant fits.
* **Multi-class classification** — Extending tree and ensemble ideas beyond binary problems.

### 2. Ensembles, KNN, and SVM-Style Supervised Learning

* **Bias, variance, and ensembles** — Why averaging or boosting diverse models improves stability and generalization.
* **Random forests and boosting** — Bagging vs. boosting; practical use of libraries such as XGBoost alongside scikit-learn.
* **KNN** — Instance-based classification; distance metrics and scaling.
* **SVMs** — Margins, kernels (conceptually), and workflow examples (e.g., credit-card fraud scenarios in labs).

### 3. Clustering

* **K-means** — Centroids, choosing *k*, limitations on shape/scale.
* **DBSCAN and HDBSCAN** — Density-based clusters, noise points, and parameters vs. K-means.

### 4. Dimension Reduction and Manifold Visualization

* **PCA** — Variance directions, compression, and visualization in 2D/3D.
* **t-SNE and UMAP** — Non-linear embeddings for exploring structure (interpret as visualization-first, not always for distance preservation).

### 5. Evaluation, Regularization, and Production-Style Workflows

* **Classification and regression metrics** — Accuracy, precision/recall, F1, ROC/AUC, and regression error measures in context.
* **Unsupervised evaluation** — Heuristics when there is no single “ground truth” label.
* **Regularization** — L1/L2 in linear models; connection to overfitting control.
* **Cross-validation and GridSearchCV** — Systematic tuning without leaking test information.
* **Pipelines** — Chaining preprocessing and models; avoiding **data leakage** and inconsistent transforms between train and inference.

### 6. Integrative Project

* **End-to-end practice** — A consolidated notebook pulls together ML workflow themes on a real-style dataset (Australian weather scenario in the final project notebook).

---

## Labs and Notebooks

### 8.01 — Decision Trees and Related Tasks

* **Decision trees** (`8.01/Decision_trees.ipynb`)
* **Multi-class classification** (`8.01/Multi-class_Classification.ipynb`)
* **Regression trees (taxi tips)** (`8.01/Regression_Trees_Taxi_Tip.ipynb`)

### 8.03 — KNN, Ensembles, Trees + SVM

* **KNN classification** (`8.03/KNN_Classification.ipynb`)
* **Random forests and XGBoost** (`8.03/Random_ Forests _XGBoost.ipynb`)
* **Decision tree and SVM (credit card fraud)** (`8.03/decision_tree_svm_ccFraud.ipynb`)

### 8.04 — Clustering

* **K-means customer segmentation** (`8.04/K-Means-Customer-Seg.ipynb`)
* **DBSCAN vs. HDBSCAN** (`8.04/Comparing_DBScan_HDBScan.ipynb`)
* **Geospatial asset** — `8.04/Canada.tif` (supporting raster for mapping / spatial examples as used in the lab)

### 8.05 — Dimension Reduction

* **PCA** (`8.05/PCA.ipynb`)
* **t-SNE and UMAP** (`8.05/tSNE_UMAP.ipynb`)

### 8.06 — Evaluation Labs

* **Evaluating classification models** (`8.06/Evaluating Classification Models.ipynb`)
* **Evaluating K-means clustering** (`8.06/Evaluating_k-means_clustering.ipynb`)
* **Evaluating random forest** (`8.06/Evaluating_random_forest.ipynb`)

### 8.07 — Pipelines, Tuning, and Regularization

* **ML pipelines and GridSearchCV** (`8.07/ML_Pipelines_and_GridSearchCV.ipynb`)
* **Regularization in linear regression** (`8.07/Regularization_in_LinearRegression.ipynb`)

### 8.08 — Final Project

* **Australian weather ML project** (`8.08/FinalProject_AUSWeather.ipynb`)

### 8.09 — Live Session

* Placeholder for live session materials (`8.09 - Live Session/.gitkeep`)

---

## Supporting Materials

### Downloads (Lecture Transcripts / Notes)

Located in `Downloads/`:

* `Bias, variance and ensemble models.txt`
* `Classification metrics and evaluation techniques.txt`
* `Classification.txt`
* `Clustering strategies and real-world applications.txt`
* `Clustering, dimension reduction and feature engineering.txt`
* `Cross-validation and advanced model validation techniques.txt`
* `Data leakage and other pitfalls.txt`
* `DBSCAN and HDBSCAN.txt`
* `Decision trees.txt`
* `Dimension reduction algorithms.txt`
* `Evaluating unsupervised learning models - Heuristics and techniques.txt`
* `K-means and more on k-means.txt`
* `Module wrap-up.txt`
* `Regression metrics and evaluation techniques.txt`
* `Regression trees.txt`
* `Regularization in regression and classification.txt`
* `Supervised learning with KNN.txt`
* `Supervised learning with SVMs.txt`

### Prof’s Study Guides

Located in `Prof's ML Study Guides/`:

* `Supervised ML Study Guide.pdf`
    * Supervised learning framing (features/labels; regression vs classification; train/test split; overfitting vs underfitting)
    * Linear model family + assumptions and regularization (L1/L2; complements Module 8 regularization lab)
    * Tree-based models (decision trees, random forests, boosted trees) + pros/cons—direct support for tree and ensemble weeks
    * Regression metrics (R², MSE, RMSE, MAE) + diagnostic plots
    * End-to-end supervised workflow checklist
* `Classification ML Study Guide.pdf`
    * Binary, multi-class, and multi-label classification as probability prediction
    * Algorithms overview: SVM, KNN, logistic regression and trade-offs
    * Confusion matrix; Type I/II errors; TP/FP/TN/FN
    * Metrics: accuracy, precision, recall, F1; ROC/AUC; Brier score
    * Practical notes: scaling, stratified splits, imbalanced classes
* `Production ML Study Guide.pdf`
    * Preprocessing: imputation, scaling, encoding, outliers, class balancing (e.g., SMOTE)
    * Model persistence (pickle vs joblib) and deployment considerations (e.g., containers)
    * **scikit-learn pipelines** (avoid leakage; consistent inference transforms)—pairs with `ML_Pipelines_and_GridSearchCV.ipynb`
    * k-fold and stratified cross-validation—pairs with grid search and evaluation topics
    * Explainability: feature importances, coefficients, SHAP, partial dependence

---

## Key Takeaways

* **Trees and ensembles** — Decision trees are interpretable but prone to overfitting; **random forests** and **boosting** reduce variance or bias through ensembling—understand the trade-offs and tuning knobs.
* **Clustering** — **K-means** assumes blob-like, comparable-scale groups; **DBSCAN/HDBSCAN** find density-based structure and **noise**—choose the method to match the geometry of the problem.
* **Dimension reduction** — **PCA** explains variance linearly; **t-SNE/UMAP** help **visualize** complex structure but require careful interpretation.
* **Evaluation** — Use the right **classification** or **regression** metrics for the business question; for clustering, rely on **heuristics** and domain sense when labels are absent.
* **Reliable workflows** — **Pipelines**, **cross-validation**, and **GridSearchCV** reduce leakage and make comparisons fair; **regularization** and awareness of **pitfalls** (leakage, over-tuning) scale notebook work toward practice-ready ML.

---

## The Data Scientist’s ML Toolkit (Beyond Linear Models)

This module is about **expanding the toolkit**: non-linear supervised learners, unsupervised discovery, and **evaluation plus workflow hygiene** so experiments translate to trustworthy decisions—not just higher leaderboard scores in a single split.
