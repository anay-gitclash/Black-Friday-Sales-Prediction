🛍️ Black Friday Sales Prediction
📌 Project Overview

This project predicts customer purchase amount during Black Friday sales using machine learning.
It follows a progressive modeling approach, starting from simple baselines and moving toward advanced gradient boosting models, with CatBoost selected as the final model due to its superior performance on categorical-heavy data.

🎯 Problem Statement

Given customer demographics and product information, predict the purchase amount (Purchase).

Type: Supervised Learning

Task: Regression

📂 Dataset Description

The dataset contains customer and product-level data collected during Black Friday sales.

Key Features

Gender

Age

Occupation

City_Category

Stay_In_Current_City_Years

Product_Category_1/2/3

Purchase (target)

Identifier columns (User_ID, Product_ID) were removed as they do not contribute predictive value.

🧹 Data Preprocessing

Removed identifier columns to prevent noise and leakage

Handled missing values using appropriate imputation strategies

Separated target variable before preprocessing

Used train–test split prior to scaling and modeling

📊 Exploratory Data Analysis (EDA)

EDA was performed to:

Analyze purchase distribution

Study the impact of demographics and product categories

Identify skewness and spending patterns

Key insights:

Purchase values are right-skewed

Product categories strongly influence spending

Customer attributes show clear behavioral trends

⚙️ Feature Engineering

One-Hot Encoding for categorical features

Proper handling of numerical features

Ensured no target leakage during preprocessing

🧠 Modeling Strategy (Progressive Approach)

The project followed an iterative model improvement pipeline:

1️⃣ Baseline Model

Mean purchase predictor

MAE ≈ 4000

2️⃣ Linear Regression

Simple interpretable model

Struggled with non-linear relationships

MAE ≈ 3500

3️⃣ Random Forest Regressor

Captured non-linear interactions

Significant improvement

MAE ≈ 2200

4️⃣ XGBoost Regressor

Gradient boosting for better bias–variance tradeoff

Improved handling of complex patterns

Further reduced error compared to Random Forest

5️⃣ CatBoost Regressor (Final Model) ✅

Why CatBoost?

Handles categorical features efficiently

Reduces need for heavy preprocessing

Strong performance on tabular data

Robust against overfitting

MAE ≈ 2100

👉 Best overall performance achieved with CatBoost

🔗 Pipeline Architecture

A full scikit-learn pipeline was used to ensure:

Clean preprocessing

Consistent transformations

No data leakage

Reproducibility

Pipeline Flow
Raw Data
 → Imputation
 → Encoding
 → Model Training
 → Prediction

📈 Model Evaluation
Metrics Used

Mean Absolute Error (MAE)

R² Score

Actual vs Predicted visualization

Performance Summary
Model	MAE
Baseline	~4000
Linear Regression	~3500
Random Forest	~2200
XGBoost	↓ improved
CatBoost	Best ✅(2100)

The final model achieves a ~45% reduction in error compared to the baseline.

📊 Visualization

An Actual vs Predicted scatter plot was used to validate:

Strong positive correlation

Reasonable dispersion around the diagonal

No signs of data leakage or overfitting

🧠 Key Learnings

Model performance improves significantly with non-linear and boosting models

Feature preprocessing and leakage prevention are critical

MAE must always be interpreted relative to target scale

Extremely high R² values can indicate leakage and must be validated carefully

CatBoost is highly effective for categorical-heavy retail datasets

🚀 Future Enhancements

Advanced feature engineering (user-level aggregates)

Hyperparameter tuning using GridSearchCV

Model deployment using FastAPI

Real-time prediction API

🛠️ Tech Stack

Python

Pandas, NumPy

Matplotlib, Seaborn

scikit-learn

XGBoost

CatBoost

📌 Conclusion

This project demonstrates an end-to-end, industry-style machine learning workflow, progressing from simple baselines to advanced boosting models.
The final CatBoost model delivers strong and realistic performance, making this project interview-ready and portfolio-worthy.
