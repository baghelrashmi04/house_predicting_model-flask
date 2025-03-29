from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from predict_housing import predict_housing_prices 
from sklearn.base import BaseEstimator, TransformerMixin
# Import your prediction function

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

from predict_housing import predict_housing_prices  # Import your prediction function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Get input data from the form
            longitude = float(request.form["longitude"])
            latitude = float(request.form["latitude"])
            housing_median_age = float(request.form["housing_median_age"])
            total_rooms = float(request.form["total_rooms"])
            total_bedrooms = float(request.form["total_bedrooms"])
            population = float(request.form["population"])
            households = float(request.form["households"])
            median_income = float(request.form["median_income"])
            ocean_proximity = request.form["ocean_proximity"]

            # Create a DataFrame from the input data
            new_data = pd.DataFrame({
                "longitude": [longitude],
                "latitude": [latitude],
                "housing_median_age": [housing_median_age],
                "total_rooms": [total_rooms],
                "total_bedrooms": [total_bedrooms],
                "population": [population],
                "households": [households],
                "median_income": [median_income],
                "ocean_proximity": [ocean_proximity],
            })

            print("Input Data:", new_data)  # Debugging print statement

            # Make predictions
            prediction = predict_housing_prices(new_data)[0]

            print("Prediction:", prediction)  # Debugging print statement

            return render_template("index.html", prediction=prediction)

        except ValueError as e:
            print("ValueError:", e)  # Debugging print statement
            return render_template("index.html", error="Invalid input. Please enter valid numerical values.")

        except Exception as e:
            print("Exception:", e)  # Debugging print statement
            return render_template("index.html", error="An error occurred.")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)