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

# Preprocessing

# Drop duplicates
df = df.drop_duplicates()

# Fill missing values with mean
df['likes'].fillna(df['likes'].mean(), inplace=True)
df['comments'].fillna(df['comments'].mean(), inplace=True)
df['watch_time_minutes'].fillna(df['watch_time_minutes'].mean(), inplace=True)

# -----------------------------
# 2. Feature Engineering
# -----------------------------

# Create new features
df['engagement_rate'] = df['likes'] / df['views']  
df['watch_time_per_view'] = df['watch_time_minutes'] / df['views']
df['views_per_subscriber'] = df['views'] / df['subscribers']
df['subscribers_per_view'] = df['subscribers'] / df['views']
df['ad_revenue_per_view'] = df['ad_revenue_usd'] / df['views'] 

# Drop non-predictive ID
df = df.drop(columns=['video_id'])


# Convert date column
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Extract date features
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek
df = df.drop(columns=['date'])

# Define features (X) and target (y)
X = df.drop(columns=['ad_revenue_usd'])
y = df['ad_revenue_usd']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)

# -----------------------------
# 3. Preprocessing Pipeline
# -----------------------------
categorical_cols = ['category', 'device', 'country']
numeric_cols = [col for col in X.columns if col not in categorical_cols] + ['year', 'month', 'day_of_week'] 

from sklearn.preprocessing import StandardScaler

preprocessor = ColumnTransformer( 
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
        ('num', StandardScaler(), numeric_cols)
    ]
)

# -----------------------------
# 4. Define Models
# -----------------------------
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(),
    "Lasso Regression": Lasso(alpha=0.001),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=50),
    "XGBoost": XGBRegressor(n_estimators=100, random_state=40, verbosity=0)
}

# -----------------------------
# 5. Train & Evaluate
# -----------------------------
results = {}                # Store results
best_model = None           # Track best model
best_score = -np.inf        # Initialize best score

for name, model in models.items():                          # Iterate over models
    pipe = Pipeline(steps=[('preprocessor', preprocessor),  # Create pipeline
                           ('model', model)])
    pipe.fit(X_train, y_train)                              # Train model                  
    y_pred = pipe.predict(X_test)                           # Predict on test set    

    r2 = r2_score(y_test, y_pred)                           # Evaluate
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))      # Root Mean Squared Error   
    mae = mean_absolute_error(y_test, y_pred)               # Mean Absolute Error

    results[name] = {"R²": r2, "RMSE": rmse, "MAE": mae}    # Store results
    print(f"{name}: R²={r2:.4f}, RMSE={rmse:.2f}, MAE={mae:.2f}")

    # Track best model (highest R²)
    if r2 > best_score:   # If current model is better
        best_score = r2   # Update best score
        best_model = pipe # Update best model

# Save results table
results_df = pd.DataFrame(results).T.sort_values(by="R²", ascending=False)
print("\nModel Comparison:\n", results_df)

# -----------------------------
# 6. Save Best Model
# -----------------------------
joblib.dump(best_model, "best_youtube_model.pkl")           # Save best model
print("✅ Best model saved as best_youtube_model.pkl")
