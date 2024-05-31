import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.sparse import csr_matrix


def run_spatial_error_model(max_min_norm_path, new_geography_path):
    # Load data
    max_min_norm = pd.read_csv(max_min_norm_path)
    new_geography = pd.read_excel(new_geography_path)

    # Merge data
    merged_data = pd.merge(
        max_min_norm, new_geography, left_on="ID", right_on="cityseries"
    )

    # Filter the merged_data for the year 2011
    filtered_data = merged_data[merged_data["year"] == 2011]

    # Extract y and X
    y = filtered_data["Y"].values
    X = filtered_data[["X1", "X2", "X3", "X4", "X5", "X6"]].values

    # Extract spatial weights matrix
    spatial_weights = new_geography.drop(columns=["cityseries"])
    weights_array = spatial_weights.to_numpy()

    # Ensure the weights array matches the filtered data
    weights_filtered = weights_array[: len(y), : len(y)]

    # Create a sparse matrix for the spatial weights
    weights_sparse = csr_matrix(weights_filtered)

    # Compute the spatially lagged errors term (W * e)
    model_initial = sm.OLS(y, sm.add_constant(X)).fit()
    residuals = model_initial.resid
    We = weights_sparse.dot(residuals)

    # Add the spatially lagged errors term to the independent variables
    X_with_We = np.hstack([X, We.reshape(-1, 1)])

    # Fit a linear regression model with the spatially lagged errors term
    X_with_const_We = sm.add_constant(X_with_We)
    model = sm.OLS(y, X_with_const_We).fit()

    return model.summary()


if __name__ == "__main__":
    summary = run_spatial_error_model(
        "../data/max_min_norm.csv", "../data/new_geography.xlsx"
    )
    print(summary)
