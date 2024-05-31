# Spatial Analysis Project

This project performs spatial econometric analysis using Spatial Lag Model (SLM) and Spatial Error Model (SEM) on the provided datasets.

## Project Structure

```
spatial_analysis_proj/
│
├── data/
│   ├── max_min_norm.csv
│   └── new_geography.xlsx
│
├── src/
│   ├── spatial_lag_model.py
│   └── spatial_error_model.py
│
├── test/
│   └── test_models.py
│
├── main.py
└── README.md
```

## Installation

To run this project, you need to have Python installed along with the following packages:
- pandas
- numpy
- statsmodels
- scipy

You can install the required packages using pip:
```
pip install -r requirements.txt
```

## Usage

To run the project, execute the following command in the project root directory:
```
python main.py
```

## Testing

To run the tests, execute the following command in the project root directory:
```
python test/test_models.py
```

## Data

Place the provided `max_min_norm.csv` and `new_geography.xlsx` files in the `data/` folder.

## Description

- `src/spatial_lag_model.py`: Contains the code for running the Spatial Lag Model.
- `src/spatial_error_model.py`: Contains the code for running the Spatial Error Model.
- `test/test_models.py`: Contains test functions to validate the models.
- `main.py`: Entry point for running both models and printing the summaries.
