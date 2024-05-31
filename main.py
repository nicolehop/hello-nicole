from src.spatial_lag_model import run_spatial_lag_model
from src.spatial_error_model import run_spatial_error_model

if __name__ == "__main__":
    print("Running Spatial Lag Model...")
    lag_model_summary = run_spatial_lag_model(
        "data/max_min_norm.csv", "data/new_geography.xlsx"
    )
    print(lag_model_summary)

    print("\nRunning Spatial Error Model...")
    error_model_summary = run_spatial_error_model(
        "data/max_min_norm.csv", "data/new_geography.xlsx"
    )
    print(error_model_summary)
