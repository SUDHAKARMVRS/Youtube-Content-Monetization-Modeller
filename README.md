# 📺 YouTube Ad Revenue Prediction
## 🌐 Domain

Social Media Analytics & Content Monetization
Analyzing YouTube video performance data to predict ad revenue and help creators optimize their content strategy.

## 📝 Project Introduction

This project builds a machine learning model to predict YouTube ad revenue using video performance and contextual features.
It also includes an interactive Streamlit app where users can input video details and get revenue predictions in real-time.

## 🎯 Objective

Predict YouTube Ad Revenue accurately using regression models.

Provide a tool for creators & media companies to estimate potential earnings.

## ⚙️ ELT Approach

Extract: Data from the provided YouTube dataset (CSV).

Load: Processed into Pandas DataFrame.

Transform: Cleaned (missing values, duplicates), engineered features, and prepared for ML models.

## 📂 Data Migration

Not required (CSV-based dataset), but data preprocessing & feature engineering was performed before model training.

## 🔍 Exploratory Data Analysis (EDA)

Distribution of views, likes, comments, and revenue.

Detected outliers & missing values.

Identified correlations between engagement metrics and revenue.

## 🛠️ Feature Engineering

Derived engagement features (e.g., likes-to-views ratio).

Extracted date-based features → year, month, weekday.

Encoded categorical variables (category, device, country).

## 🤖 Machine Learning Models

Trained and compared 5 regression models:

🔹 Linear Regression

🔹 Ridge Regression

🔹 Lasso Regression

🔹 Random Forest

🔹 XGBoost

✅ Best model selected based on highest R² score and saved as best_youtube_model.pkl.

## 📊 Statistical Techniques

R² Score → Goodness of fit

RMSE (Root Mean Squared Error) → Prediction error size

MAE (Mean Absolute Error) → Average error
These metrics were chosen to evaluate accuracy and reliability of revenue predictions.

## 📌 Results

Lasso Regression achieved the best balance of accuracy and generalization.

Model evaluation showed high R² (~0.94) and low error values.

Insights revealed views, watch time, and subscribers as top revenue drivers.

## 💡 Business Use Cases

📊 Revenue Forecasting → Estimate ad revenue before uploading.

🎯 Content Strategy → Identify what drives earnings.

💼 Ad Campaign Planning → Help advertisers forecast ROI.

## 🖥️ Streamlit App

Run the app to test predictions interactively:

streamlit run stream.py


Input video stats (views, likes, comments, etc.)

## Get 💰 revenue prediction instantly

Visual, user-friendly dashboard

## 🛠️ Tech Stack

🔹 Python | 🔹 Pandas | 🔹 NumPy | 🔹 Scikit-learn | 🔹 XGBoost | 🔹 Streamlit | 🔹 Joblib

## ✨ Author: Sudhakar M
📧 For queries: [sudhakar.mvrs@gmail.com]
