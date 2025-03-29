import pandas as pd
import joblib
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

# CombinedAttributesAdder class definition (copy from your original code)
rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]


def predict_housing_prices(new_data):
    """Predicts housing prices for new data."""

    print("New Data (predict_housing.py):", new_data) # Check input

    # Load the model
    model = joblib.load("housing_price_predictor.pkl")

    # Load and apply the preprocessing pipeline
    full_pipeline = joblib.load("full_pipeline.pkl")
    prepared_data = full_pipeline.transform(new_data)

    print("Prepared Data:", prepared_data) # Check transformed data

    # Make predictions
    predictions = model.predict(prepared_data)

    print("Predictions:", predictions) # Check prediction

    return predictions
if __name__ == "__main__":
    # Sample new housing data (replace with your own data)
    new_data = pd.DataFrame({
        "longitude": [-118.2, -122.3],
        "latitude": [34.0, 37.8],
        "housing_median_age": [30, 45],
        "total_rooms": [2000, 3500],
        "total_bedrooms": [400, 600],
        "population": [1500, 2500],
        "households": [350, 500],
        "median_income": [5.0, 7.0],
        "ocean_proximity": ["NEAR BAY", "NEAR BAY"]
    })

    # Make predictions
    predictions = predict_housing_prices(new_data)
    print("Predictions:", predictions)