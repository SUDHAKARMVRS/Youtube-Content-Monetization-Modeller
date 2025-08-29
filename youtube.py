# -----------------------------
# YouTube Ad Revenue Prediction - Training
# -----------------------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Models
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import joblib

# -----------------------------
# 1. Load Data
# -----------------------------
df = pd.read_csv("youtube_ad_revenue_dataset.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop duplicates
df = df.drop_duplicates()

# Fill missing values with mean
df['likes'].fillna(df['likes'].mean(), inplace=True)
df['comments'].fillna(df['comments'].mean(), inplace=True)
df['watch_time_minutes'].fillna(df['watch_time_minutes'].mean(), inplace=True)

# -----------------------------
# 2. Feature Engineering
# -----------------------------
# Drop non-predictive ID
df = df.drop(columns=['video_id'])

# Extract date features
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek
df = df.drop(columns=['date'])

# Define features (X) and target (y)
X = df.drop(columns=['ad_revenue_usd'])
y = df['ad_revenue_usd']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 3. Preprocessing Pipeline
# -----------------------------
categorical_cols = ['category', 'device', 'country']
numeric_cols = [col for col in X.columns if col not in categorical_cols]

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ],
    remainder='passthrough'
)

# -----------------------------
# 4. Define Models
# -----------------------------
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(),
    "Lasso Regression": Lasso(alpha=0.001),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "XGBoost": XGBRegressor(n_estimators=100, random_state=42, verbosity=0)
}

# -----------------------------
# 5. Train & Evaluate
# -----------------------------
results = {}
best_model = None
best_score = -np.inf

for name, model in models.items():
    pipe = Pipeline(steps=[('preprocessor', preprocessor),
                           ('model', model)])
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)

    results[name] = {"R²": r2, "RMSE": rmse, "MAE": mae}
    print(f"{name}: R²={r2:.4f}, RMSE={rmse:.2f}, MAE={mae:.2f}")

    # Track best model (highest R²)
    if r2 > best_score:
        best_score = r2
        best_model = pipe

# Save results table
results_df = pd.DataFrame(results).T.sort_values(by="R²", ascending=False)
print("\nModel Comparison:\n", results_df)

# -----------------------------
# 6. Save Best Model
# -----------------------------
joblib.dump(best_model, "lasso_youtube_model.pkl")
print("✅ Best model saved as lasso_youtube_model.pkl")
