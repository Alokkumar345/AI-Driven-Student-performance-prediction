
import joblib
import pandas as pd
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import Ridge

BASE = Path(__file__).resolve().parent
DATA = BASE / "data" / "student_performance.csv"
MODEL_DIR = BASE / "models"
MODEL_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA)

target = "final_score"
drop_cols = ["student_id", "performance_category"]
X = df.drop(columns=[target] + drop_cols)
y = df[target]

num_cols = X.select_dtypes(include=["number"]).columns.tolist()
cat_cols = X.select_dtypes(exclude=["number"]).columns.tolist()

preprocessor = ColumnTransformer([
    ("num", Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]), num_cols),
    ("cat", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ]), cat_cols)
])

models = {
    "Ridge": Ridge(alpha=10.0),
    "RandomForest": RandomForestRegressor(
        n_estimators=250, random_state=42, n_jobs=-1, max_depth=12
    ),
    "GradientBoosting": GradientBoostingRegressor(
        n_estimators=250, learning_rate=0.05, max_depth=3, random_state=42
    )
}

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

results = {}
best_name, best_pipe, best_rmse = None, None, float("inf")

for name, model in models.items():
    pipe = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])
    pipe.fit(X_train, y_train)
    pred = pipe.predict(X_test)
    mae = mean_absolute_error(y_test, pred)
    rmse = mean_squared_error(y_test, pred) ** 0.5
    r2 = r2_score(y_test, pred)
    results[name] = {"MAE": mae, "RMSE": rmse, "R2": r2}
    print(f"{name:16s} MAE={mae:.3f} RMSE={rmse:.3f} R2={r2:.3f}")
    if rmse < best_rmse:
        best_name, best_pipe, best_rmse = name, pipe, rmse

joblib.dump(best_pipe, MODEL_DIR / "student_performance_model.joblib")
joblib.dump({"model_name": best_name, "metrics": results}, MODEL_DIR / "model_metadata.joblib")

print("\nBest model:", best_name)
print("Saved:", MODEL_DIR / "student_performance_model.joblib")
