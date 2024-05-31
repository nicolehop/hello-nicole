from src.spatial_lag_model import run_spatial_lag_model
from src.spatial_error_model import run_spatial_error_model


def test_spatial_lag_model():
    summary = run_spatial_lag_model(
        "../data/max_min_norm.csv", "../data/new_geography.xlsx"
    )
    print(summary)


def test_spatial_error_model():
    summary = run_spatial_error_model(
        "../data/max_min_norm.csv", "../data/new_geography.xlsx"
    )
    print(summary)


if __name__ == "__main__":
    test_spatial_lag_model()
    test_spatial_error_model()
